#!/usr/bin/env python3
# Charles O. Goddard
# 7/20/2023
"""Script used to generate the base frankenmerge. Output will need fine-tuning to be useful."""

import copy
import torch
from torch import Tensor, nn
import transformers

from transformers.models.llama.modeling_llama import (
    LlamaForCausalLM,
    LlamaDecoderLayer,
)
from transformers import LlamaForCausalLM, LlamaConfig

import torch
import transformers
import numpy as np


MODEL_NAME_13B = "meta-llama/Llama-2-13b-hf"  # primary model
MODEL_NAME_33B = "huggyllama/llama-30b"  # donor
BLOCK_DIAGONAL = True
# If BLOCK_DIAGONAL is set to True, each tensor in the resultant model will form a
# block diagonal matrix, as illustrated below:

# a a a 0 0
# a a a 0 0
# a a a 0 0
# 0 0 0 b b
# 0 0 0 b b

# In this configuration, the states (hidden and intermediate) from the original 
# and donor models are completely decoupled. That is, the hidden states
# corresponding to the original model remain unchanged, and the new dimensions 
# added from the donor model do not depend on the hidden states of the original model.

# If BLOCK_DIAGONAL is set to False, the tensors will instead have the following form:

# a a a 0 0
# a a a 0 0
# a a a 0 0
# b b b b b
# b b b b b

# In this case, the output of the newly added attention heads depends on the hidden 
# state values as if they were part of the donor model. Although the original model's
# hidden states remain unchanged in either case, interaction between the new and old
# features will result in features of varying usefulness.


class NoInit:
    def __enter__(self):
        def noop(*args, **kwargs):
            pass

        (k, u, n) = (
            torch.nn.init.kaiming_uniform_,
            torch.nn.init.uniform_,
            torch.nn.init.normal_,
        )
        torch.nn.init.kaiming_uniform_ = noop
        torch.nn.init.uniform_ = noop
        torch.nn.init.normal_ = noop

        transformers.modeling_utils._init_weights = False
        self.funcs = (k, u, n)

    def __exit__(self, *args):
        (k, u, n) = self.funcs
        (
            torch.nn.init.kaiming_uniform_,
            torch.nn.init.uniform_,
            torch.nn.init.normal_,
        ) = (
            k,
            u,
            n,
        )
        transformers.modeling_utils._init_weights = True


def format_kmb(n, digits=None):
    n = int(n)
    if n < 1000:
        return str(n)
    elif n < 1000_000:
        return f"{round(n/1000, digits)}k"
    elif n < 1000 * 1000 * 1000:
        return f"{round(n/(1000*1000), digits)}m"
    else:
        return f"{round(n/(1000*1000*1000), digits)}b"


def count_params(model):
    model_parameters = filter(lambda p: p.requires_grad, model.parameters())
    params = sum([np.prod(p.size()) for p in model_parameters])
    return int(params)


torch.set_default_dtype(torch.float16)

config_13b: LlamaConfig = LlamaConfig.from_pretrained(MODEL_NAME_13B)
config_33b: LlamaConfig = LlamaConfig.from_pretrained(MODEL_NAME_33B)
config_more = copy.deepcopy(config_13b)
config_more.intermediate_size = config_33b.intermediate_size
config_more.hidden_size = config_33b.hidden_size
config_more.num_key_value_heads = config_33b.num_key_value_heads
config_more.num_attention_heads = config_33b.num_key_value_heads

print(config_more)

with NoInit():
    model = LlamaForCausalLM(config_more)

print(f"{format_kmb(count_params(model), 3)} parameters")


def merge_tensors_inplace(dest: Tensor, s0: Tensor, s1: Tensor, block_diagonal: bool):
    dest.zero_()
    if block_diagonal:
        dest[s0.shape[0] :, s0.shape[1] :] = s1[
            s0.shape[0] : dest.shape[0],
            s0.shape[1] : dest.shape[1],
        ]
    else:
        dest[s0.shape[0] :, :] = s1[
            s0.shape[0] : dest.shape[0],
            : dest.shape[1],
        ]
    dest[: s0.shape[0], : s0.shape[1]] = s0


with NoInit():
    donor_13b = (
        LlamaForCausalLM.from_pretrained(MODEL_NAME_13B).to(torch.float16).eval()
    )
    donor_33b = (
        LlamaForCausalLM.from_pretrained(MODEL_NAME_33B).to(torch.float16).eval()
    )

with torch.no_grad():
    for layer_idx in range(len(model.model.layers)):
        layer: LlamaDecoderLayer = model.model.layers[layer_idx]
        l13: LlamaDecoderLayer = donor_13b.model.layers[layer_idx]
        l33: LlamaDecoderLayer = donor_33b.model.layers[layer_idx]

        for name in ("q_proj", "k_proj", "v_proj", "o_proj"):
            dest: nn.Linear = getattr(layer.self_attn, name)
            s13: nn.Linear = getattr(l13.self_attn, name)
            s33: nn.Linear = getattr(l33.self_attn, name)
            merge_tensors_inplace(dest.weight, s13.weight, s33.weight, BLOCK_DIAGONAL)

        for name in ("up_proj", "gate_proj", "down_proj"):
            dest: nn.Linear = getattr(layer.mlp, name)
            s13: nn.Linear = getattr(l13.mlp, name)
            s33: nn.Linear = getattr(l33.mlp, name)
            merge_tensors_inplace(dest.weight, s13.weight, s33.weight, BLOCK_DIAGONAL)

        layer.input_layernorm.weight[:] = l33.input_layernorm.weight[
            : layer.input_layernorm.weight.shape[0]
        ]
        layer.input_layernorm.weight[
            : l13.input_layernorm.weight.shape[0]
        ] = l13.input_layernorm.weight
        layer.post_attention_layernorm.weight[:] = l33.post_attention_layernorm.weight[
            : layer.post_attention_layernorm.weight.shape[0]
        ]
        layer.post_attention_layernorm.weight[
            : l13.post_attention_layernorm.weight.shape[0]
        ] = l13.post_attention_layernorm.weight

    # have initial output depend on only original llama2-13b features, so model
    # starts unimpaired and can learn to incorporate the new features as well
    model.lm_head.weight.zero_()
    model.lm_head.weight[
        : donor_13b.lm_head.weight.shape[0], : donor_13b.lm_head.weight.shape[1]
    ] = donor_13b.lm_head.weight

    merge_tensors_inplace(
        model.model.embed_tokens.weight,
        donor_13b.model.embed_tokens.weight,
        donor_33b.model.embed_tokens.weight,
        BLOCK_DIAGONAL,
    )

model.save_pretrained("./llama2-22b/", safe_serialization=True)
