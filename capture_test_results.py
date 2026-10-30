import sys
import os
import re

# Add current directory to path
sys.path.append(r'd:\Users\BuiTrongNguyen\[HK252] PPL\BTL-PPL-HK252')

from tests.utils import Checker

def gather_results():
    path = r'd:\Users\BuiTrongNguyen\[HK252] PPL\BTL-PPL-HK252\tests\test_checker.py'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by test functions
    tests = re.split(r'(def test_\d+\(\):)', content)
    results = {}
    for i in range(1, len(tests), 2):
        header = tests[i]
        body = tests[i+1]
        m = re.search(r'test_(\d+)', header)
        if not m: continue
        num = int(m.group(1))
        
        # Capture source code
        s_m = re.search(r'source = """(.*?)"""', body, re.DOTALL)
        if s_m:
            src = s_m.group(1).strip()
            try:
                res = Checker(src).check_from_source()
                results[num] = res
            except Exception as e:
                results[num] = f"ERROR: {str(e)}"
    
    # Print results for tests 66-100
    for k in sorted(results.keys()):
        if k >= 66:
            print(f"T{k:03}: {results[k]}")

if __name__ == "__main__":
    gather_results()
