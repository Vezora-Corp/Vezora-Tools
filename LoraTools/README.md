
# LoraTools

Welcome to the `LoraTools` directory inside the `vezora tools` repository! This folder contains utility scripts to work with models related to the "llama" architecture from Hugging Face's Transformers library.

## Contents

1. `frankenllama_22b.py` - A script used to generate the base frankenmerge. The output from this script may need fine-tuning to be usable.
2. `simplemerge_with_args.py` - A utility to merge a given model with a LoRA adapter using command-line arguments.

## How to Run

### `frankenllama_22b.py`

Simply run:
```bash
python frankenllama_22b.py
```

### `simplemerge_with_args.py`

Use the following command:
```bash
python simplemerge_with_args.py --model_path <PATH_TO_MODEL> --lora_adapter_path <PATH_TO_LORA_ADAPTER> --output_path <OUTPUT_PATH>
```
Replace `<PATH_TO_MODEL>`, `<PATH_TO_LORA_ADAPTER>`, and `<OUTPUT_PATH>` with the appropriate paths.

## Requirements

1. Python 3
2. PyTorch
3. Transformers library from Hugging Face
4. peft
5. json
6. shutil
7. bitsandbytes

## Credits

- `frankenllama_22b.py` is entirely written by Charles O. Goddard. More about his work can be found [here](https://huggingface.co/chargoddard).
- `simplemerge_with_args.py` was written by combining approaches published by @eugene-yh and @jinyongyoo. Their contributions can be found on [GitHub](https://github.com/jinyongyoo) and [Gist](https://gist.github.com/eugene-yh) respectively.

