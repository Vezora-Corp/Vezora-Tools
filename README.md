# Vezora-Tools
Tools for Peft lora training 
Simple Merge With Args Merges lora adapter with peft, to every layer to achieve optimum preformance, nearly equal to a full finetune.


# SimpleMerge with Command-Line Arguments

This script is an updated version of a model and LoRA adapter merging utility. It now supports command-line arguments, making it easier to specify input and output paths directly from the command line.

## Credits

This script combines approaches published by:

- [Eugene YH](https://gist.github.com/eugene-yh)
- [JinYong Yoo](https://github.com/jinyongyoo)

Thanks for their contributions!

## Requirements

To run this script, you'll need the following Python packages:

- `torch`
- `peft`
- `bitsandbytes`
- `transformers`

You can install them using pip:

\`\`\`bash
pip install torch peft bitsandbytes transformers
\`\`\`

## Usage

You can run this script from the command line, specifying the model path, LoRA adapter path, and output path as arguments:

\`\`\`bash
python simplemerge_with_args.py --model_path /path/to/model --lora_adapter_path /path/to/lora_adapter --output_path /path/to/output
\`\`\`

### Arguments

- `--model_path`: Specifies the path to the model. This argument is required.
- `--lora_adapter_path`: Specifies the path to the LoRA adapter. This argument is required.
- `--output_path`: Specifies the path to save the output. This argument is required.
