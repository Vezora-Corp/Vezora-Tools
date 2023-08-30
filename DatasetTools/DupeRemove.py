import json
import os
from tkinter import filedialog
from tkinter import Tk

def get_file_paths():
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    file_paths = filedialog.askopenfilenames(title="Select the input files", filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
    return file_paths

def read_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def main():
    input_files = get_file_paths()
    if not input_files:
        print("No input files selected. Exiting.")
        return

    output_file_name = input("Enter the output JSON file name (without extension): ")
    output_file_path = os.path.join(os.path.dirname(input_files[0]), f"{output_file_name}.json")

    all_examples = []
    for input_file in input_files:
        examples = read_json_file(input_file)
        all_examples.extend(examples)

    # Remove duplicates and count them
    unique_examples = []
    duplicate_count = 0
    for example in all_examples:
        if example not in unique_examples:
            unique_examples.append(example)
        else:
            duplicate_count += 1

    print(f"Total number of examples: {len(all_examples)}")
    print(f"Number of unique examples: {len(unique_examples)}")
    print(f"Number of duplicate examples: {duplicate_count}")

    with open(output_file_path, 'w') as f:
        json.dump(unique_examples, f, indent=2)

    print(f"Converted data has been saved to {output_file_path}")

if __name__ == "__main__":
    main()
