import sys
sys.path.append(".")
from tests.utils import Checker
print("Starting...")
print(Checker("void main() { int x = 5; int y = x + 1; }").check_from_source())
print("Done.")
