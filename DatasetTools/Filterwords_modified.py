import json

# Ask user for the input file path
input_file_path = input("Please enter the location of the input JSON file: ")

# Ask user for the output file path
output_file_path = input("Please enter the location of the output JSON file: ")

# Read the input JSON file and load its content into a Python list
with open(input_file_path, 'r', encoding='utf-8') as f:
    dataset = json.load(f)

# Ask user for keywords to filter by
keywords = input("Please enter the keywords to filter by, separated by commas: ").split(',')

# Filter the dataset
filtered_dataset = []
for entry in dataset:
    if any(keyword.lower() in entry['instruction'].lower() or 
           keyword.lower() in entry['input'].lower() or 
           keyword.lower() in entry['output'].lower() 
           for keyword in keywords):
        filtered_dataset.append(entry)

# Write the filtered dataset to the output JSON file
with open(output_file_path, 'w') as f:
    json.dump(filtered_dataset, f, indent=2)

# Confirm that the filtered dataset has been saved
print("Filtered dataset has been saved.")
