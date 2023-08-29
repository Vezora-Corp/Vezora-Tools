
# LoraTools

This folder is part of the `vezora-tools` GitHub repository and contains utilities for working with LoRA (Low Power, Long Range) models. Here you'll find scripts to merge models, combine weights, and perform other experimental tasks.

## Table of Contents

- [Franken Llama](#franken-llama)
- [Merge-CLI](#merge-cli)
- [Simple Merge with Args](#simple-merge-with-args)
- [Requirements](#requirements)

## Franken Llama

### Purpose

The `frankenllama_22b.py` script is designed to combine two models and their weights to create an experimental merged model.

### How to Run

This script doesn't use command-line arguments and may require manual configuration within the script.

### Requirements

- copy
- torch
- transformers

### Credits

This script was entirely written by [chargoddard](https://huggingface.co/chargoddard).

## Merge-CLI

### Purpose

The `merge-cli.py` script merges the weights of two models but keeps the size of the model the same.

### How to Run

```bash
python merge-cli.py --first_model_path [Path to the first model] --second_model_path [Path to the second model] --merged_model_path [Path to save the merged model] --merge_ratios [Merge ratios]
```

### Requirements

- os
- shutil
- transformers
- torch
- argparse
- json

### Credits

This script was made by [zarakiquemparte](https://github.com/zarakiquemparte/zaraki-tools).

## Simple Merge with Args

### Purpose

The `simplemerge_with_args.py` script allows the user to merge LoRA to the model and merge to every layer of the model.

### How to Run

This script doesn't use command-line arguments and may require manual configuration within the script.

### Requirements

- torch
- peft
- json
- shutil
- os
- bitsandbytes
- argparse
- gc
- copy
- transformers

### Credits

This script was written by [jinyongyoo](https://github.com/jinyongyoo) and [eugene-yh](https://gist.github.com/eugene-yh).

## General Requirements

- Python 3.x

Feel free to contribute or report issues!
