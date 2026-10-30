from tests.utils import Checker
import sys, os

# Add project root to path
sys.path.append(r"d:\Users\BuiTrongNguyen\[HK252] PPL\BTL-PPL-HK252")

source = """
void main() {
    int x = 1;
    switch (x) {
        case 1:
            auto unused;
            break;
    }
}
"""
result = Checker(source).check_from_source()
print(f"Result: '{result}'")
if result.startswith("TypeCannotBeInferred"):
    print("PASS: Got TypeCannotBeInferred")
else:
    print("FAIL: Expected TypeCannotBeInferred")
