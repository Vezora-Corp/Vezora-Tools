
# Vezora Tools

## Description

Vezora Tools is a collection of utility scripts to make your life easier. Currently, the repository contains:

- `Uncensor_alpaca.py`: A tool to uncensor Alpaca Formated Datasets to remove "Alignment".
- `Parquet-Converter-Main.py`: A tool to convert files to the Parquet format.
- `randomizer.py`: A tool for randomizing elements in a list.
- `ConvertGPTconvo.py`: A tool for filtering alpaca datasets input instruction and output from a txt chatgpt conversation. (not the conversation must already be in the alpaca format, for example prompting chatgpt like i have a dataset that looks like this "alpaca dataset example" recreate it and continue giving me examples increase the difficuly. Then you can use a macro to repeat the process. to get the text file use this [chrome extension](https://chrome.google.com/webstore/detail/save-chatgpt/iccmddoieihalmghkeocgmlpilhgnnfn)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/vezora-tools.git
    ```
2. Navigate into the directory:
    ```bash
    cd vezora-tools
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

> **Note**: You need to create a `requirements.txt` file listing all your Python dependencies.

## Usage

### Uncensor Alpaca

To use `Uncensor_alpaca.py`, run the following command:

```bash
python Uncensor_alpaca.py
```

### Parquet Converter

To use `Parquet-Converter-Main.py`, run the following command:

```bash
python Parquet-Converter-Main.py 
```

### Randomizer

To use `randomizer.py`, run the following command:

```bash
python randomizer.py
```
### Randomizer

To use `ConvertGPTconvo.py`, run the following command:

```bash
python ConvertGPTconvo.py
```

## Contributing

Feel free to fork the project, make changes, and submit Pull Requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
