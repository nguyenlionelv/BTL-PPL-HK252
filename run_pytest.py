import pytest
import sys
import os

os.chdir(r"d:\Users\BuiTrongNguyen\[HK252] PPL\BTL-PPL-HK252")
sys.path.append(r"d:\Users\BuiTrongNguyen\[HK252] PPL\BTL-PPL-HK252")

pytest.main(["-v", "tests/test_checker.py"])
