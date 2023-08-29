import pandas as pd
import os

# Initial prompt
file_name = input('Enter the name of the file (with extension): ')

# Check if file exists in the directory
if not os.path.isfile(file_name):
    print(f"File '{file_name}' does not exist in the current directory.")
else:
    # Determine file extension
    _, file_extension = os.path.splitext(file_name)

    # Load file into pandas dataframe
    try:
        if file_extension.lower() == '.csv':
            df = pd.read_csv(file_name)
        elif file_extension.lower() == '.parquet':
            df = pd.read_parquet(file_name)
        else:
            print(f"File format '{file_extension}' is not supported. Only '.csv' and '.parquet' are accepted.")
            exit()
    except Exception as e:
        print(f"Error occurred while loading the file: {str(e)}")
        exit()

    # Ask for output format
    output_format = input('Enter the format you would like the file in (csv, html, json): ')

    # Check if output format is valid
    if output_format not in ['csv', 'html', 'json']:
        print(f"Invalid format. Only 'csv', 'html', and 'json' are accepted.")
    else:
        # Create output file name
        base_name = os.path.splitext(file_name)[0]  # get file name without extension
        output_file_name = f'{base_name}.{output_format}'

        # Save file in the chosen format
        try:
            if output_format == 'csv':
                df.to_csv(output_file_name, index=False)
            elif output_format == 'html':
                df.to_html(output_file_name, index=False)
            elif output_format == 'json':
                df.to_json(output_file_name, orient='records')
            print(f'File successfully saved as {output_file_name}')
        except Exception as e:
            print(f"Error occurred while saving the file: {str(e)}")
