import json
import re
import tkinter as tk
from tkinter import filedialog
from collections import OrderedDict

def open_file_dialog(title, filetypes):
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(title=title, filetypes=filetypes)

def save_file_dialog(title, filetypes):
    root = tk.Tk()
    root.withdraw()
    return filedialog.asksaveasfilename(title=title, filetypes=filetypes, defaultextension=filetypes)

def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)

def extract_json_from_text(text_content):
    json_like_strs = re.findall(r'\[\s*{.*?}\s*\]', text_content, re.DOTALL)
    extracted_json_objects = []
    for json_like_str in json_like_strs:
        try:
            json_object = json.loads(json_like_str)
            extracted_json_objects.extend(json_object)
        except json.JSONDecodeError:
            continue
    return extracted_json_objects

def filter_and_deduplicate(dataset):
    filtered_dataset = [item for item in dataset if ',' in json.dumps(item)]
    unique_dataset = [dict(s) for s in set(frozenset(d.items()) for d in filtered_dataset)]
    return unique_dataset

def main():
    input_files = []
    while True:
        input_file = open_file_dialog("Select an input file", [("Text files", "*.txt")])
        if not input_file:
            break
        input_files.append(input_file)

    output_file = save_file_dialog("Save the output file", [("JSON files", "*.json")])
    
    if not output_file:
        print("Operation cancelled.")
        return

    combined_dataset = []
    for input_file in input_files:
        content = read_txt_file(input_file)
        extracted_dataset = extract_json_from_text(content)
        combined_dataset.extend(extracted_dataset)

    filtered_and_unique_dataset = filter_and_deduplicate(combined_dataset)

    # Reorder the keys in the dictionaries
    ordered_dataset = [OrderedDict(sorted(item.items(), key=lambda x: ['instruction', 'input', 'output'].index(x[0]))) for item in filtered_and_unique_dataset]

    write_json_file(output_file, ordered_dataset)

    print(f"Dataset has been saved to {output_file}")

if __name__ == '__main__':
    main()
