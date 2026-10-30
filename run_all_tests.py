import sys
import os

sys.path.append(os.path.dirname(__file__))

import inspect
import tests.test_checker as tc

tests_run = 0
tests_passed = 0
tests_failed = 0

for name, obj in inspect.getmembers(tc):
    if inspect.isfunction(obj) and name.startswith("test_checker_"):
        tests_run += 1
        try:
            obj()
            tests_passed += 1
        except AssertionError as e:
            print(f"FAILED {name}")
            tests_failed += 1
        except Exception as e:
            print(f"ERROR {name}: {e}")
            tests_failed += 1

print(f"Ran {tests_run} tests. Passed: {tests_passed}. Failed: {tests_failed}.")
