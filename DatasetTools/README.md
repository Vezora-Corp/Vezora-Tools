
# Vezora Tools

## Description

Vezora Tools is a collection of utility scripts to make your life easier. Currently, the repository contains:

- `Uncensor_alpaca.py`: A tool to uncensor alpaca images (example purpose).
- `Parquet-Converter-Main.py`: A tool to convert files to the Parquet format.

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
python Uncensor_alpaca.py [options]
```

#### Options:

- `-i, --input`: Path to the input image
- `-o, --output`: Path to the output image

### Parquet Converter

To use `Parquet-Converter-Main.py`, run the following command:

```bash
python Parquet-Converter-Main.py [options]
```

#### Options:

- `-i, --input`: Path to the input file
- `-o, --output`: Path to the output Parquet file

## Contributing

Feel free to fork the project, make changes, and submit Pull Requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
