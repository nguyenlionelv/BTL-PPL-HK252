"""Quick script to check specific test cases against the grammar."""
import os, sys
project_root = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(project_root, "build")
sys.path.insert(0, project_root)
sys.path.insert(0, build_dir)

from build.TyCLexer import TyCLexer
from build.TyCParser import TyCParser
from antlr4 import InputStream, CommonTokenStream
from src.utils.error_listener import NewErrorListener
from src.astgen.ast_generation import ASTGeneration

def test_source(label, source):
    try:
        inp = InputStream(source)
        lexer = TyCLexer(inp)
        tokens = CommonTokenStream(lexer)
        parser = TyCParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(NewErrorListener.INSTANCE)
        tree = parser.program()
        ast = ASTGeneration().visit(tree)
        print(f"{label}: {ast}")
    except Exception as e:
        print(f"{label}: ERROR: {e}")

# Test 030: nested block stmts
test_source("T030", """void main() { { { { { int x; } } } } }""")

# Test 036: case with block stmt  
test_source("T036", """void main() { switch(x) { case 1: { int y; } break; } }""")

# Test 057: method-like call on member
test_source("T057", """void main() { x = s.foo(1); }""")

# Test 062: chained member assign via expr rule
test_source("T062", """void main() { p.x = p.y = 0; }""")

# Test 083: auto as function return type
test_source("T083", """auto foo() { return 1; }""")

# Test 011: chained assignment
test_source("T011", """void main() { x = a = b = c = d = 5; }""")
