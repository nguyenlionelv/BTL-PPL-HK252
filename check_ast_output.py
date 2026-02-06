"""Quick test to see actual AST output"""
import sys
sys.path.insert(0, r'c:\Users\Bui Trong Nguyen\OneDrive\Desktop\[HK252] PPL\BTL-PPL-HK252')
sys.path.insert(0, r'c:\Users\Bui Trong Nguyen\OneDrive\Desktop\[HK252] PPL\BTL-PPL-HK252\build')

from tests.utils import ASTGenerator

# Test cases
tests = [
    "void main() {}",
    "int add() {}",
    "struct A{};",
    "void foo(int x) {}",
    "void main() { int x; }",
    "void main() { int x = 5; }",
    "void main() { if (x) { } }",
    "void main() { while (i < 10) { } }",
    "void main() { x = a + b; }",
]

for i, source in enumerate(tests, 1):
    print(f"\n=== Test {i} ===")
    print(f"Source: {source}")
    ast = ASTGenerator(source).generate()
    print(f"Output: {str(ast)}")
