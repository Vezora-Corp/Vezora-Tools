import json
import random

# Asking user for the input file path
input_file_path = input("Please enter the file path for the input JSON file: ")
with open(input_file_path, 'r') as infile:
    data = json.load(infile)

# Shuffling the entries
random.shuffle(data)

# Asking user for the output file path
output_file_path = input("Please enter the file path for the output JSON file: ")
with open(output_file_path, 'w') as outfile:
    json.dump(data, outfile, indent=2)

print("The randomized JSON data has been saved to", output_file_path)
