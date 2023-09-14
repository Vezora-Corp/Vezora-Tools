import json
import subprocess
import re
import os
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

def run_python_code(code):
    try:
        os.makedirs('cache', exist_ok=True)
        os.chdir('cache')
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        result = subprocess.run(['python', '-c', code], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, timeout=1, startupinfo=startupinfo)
        os.chdir('..')
    except Exception as e:
        os.chdir('..')
        return False
    return True

def extract_python_code(output):
    pattern = r'```python(.*?)```'
    match = re.search(pattern, output, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def test_python_code(example):
    output = example['output']
    code = extract_python_code(output)
    if code and run_python_code(code):
        return example
    return None

def test_python_codes(dataset):
    with Pool(cpu_count()) as p:
        working_codes = list(tqdm(p.imap(test_python_code, dataset), total=len(dataset)))
    working_codes = [code for code in working_codes if code]
    
    print(f"Number of examples that worked: {len(working_codes)}")
    print(f"Number of examples removed: {len(dataset) - len(working_codes)}")
    
    return working_codes

if __name__ == '__main__':
    dataset_path = input("Enter the path to your dataset: ")
    output_filename = input("Enter the filename for your new JSON file: ")

    with open(dataset_path) as f:
        dataset = json.load(f)

    working_codes = test_python_codes(dataset)

    with open(output_filename, 'w') as f:
        json.dump(working_codes, f, indent=2)
