import json
import subprocess
import re
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

def run_python_code(code):
    try:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        result = subprocess.run(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=10, startupinfo=startupinfo)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
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
    print(f"Number of examples that did not work: {len(dataset) - len(working_codes)}")
    print(f"Number of examples removed: {len(dataset) - len(working_codes)}")
    return working_codes

if __name__ == '__main__':
    dataset_path = input("Enter the path to your dataset: ")
    output_filename = input("Enter the filename for your new JSON file: ")

    with open(dataset_path) as f:
        dataset = json.load(f)

    print("Testing Python codes in the dataset...")
    working_codes = test_python_codes(dataset)

    with open(output_filename, 'w') as f:
        json.dump(working_codes, f, indent=2)
