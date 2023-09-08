import json

def main():
    try:
        # Ask user for the maximum number of tokens allowed in the output
        max_tokens = int(input("Enter the maximum number of tokens allowed in the output: "))

        # Ask user for the input file path
        input_file_path = input("Enter the file path for the input .json file: ")

        # Ask user for the output file path
        output_file_path = input("Enter the file path for the output .json file: ")

        # Read the original dataset from the input file
        with open(input_file_path, 'r') as infile:
            original_data = json.load(infile)

        # Filter examples based on the specified token limit
        filtered_data = [example for example in original_data if len(example["output"].split()) <= max_tokens]

        # Write the filtered data to the output file
        with open(output_file_path, 'w') as outfile:
            json.dump(filtered_data, outfile, indent=2)

        print(f"Filtered dataset saved to {output_file_path}. {len(filtered_data)} examples retained.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
