import sys
import os

# Add src to python path
sys.path.append(r"d:\Users\BuiTrongNguyen\[HK252] PPL\BTL-PPL-HK252\src")

from semantics.static_checker import StaticChecker
from utils.nodes import *

class Checker:
    def __init__(self, source):
        self.source = source
    def check_from_source(self):
        # We need a proper way to run the checker from source.
        # Since I don't have the parser here, I'll mock the AST for the specific cases.
        pass

def test_043():
    # void main() { auto v; v = 3; { auto v; } }
    # Mocking AST
    v1_decl = VarDecl("v", None, None) # auto v
    v1_assign = ExprStmt(AssignExpr(Identifier("v"), IntLiteral(3)))
    v2_decl = VarDecl("v", None, None) # auto v (inner)
    inner_block = BlockStmt([v2_decl])
    main_body = BlockStmt([v1_decl, v1_assign, inner_block])
    main_func = FuncDecl("main", VoidType(), [], main_body)
    program = Program([], [main_func])
    
    checker = StaticChecker(program)
    try:
        checker.check()
        return "Static checking passed"
    except Exception as e:
        return str(e)

def test_057():
    # void main() { auto a1; int b1 = 5; int c1 = a1 + b1; }
    # Mocking AST
    a1_decl = VarDecl("a1", None, None)
    b1_decl = VarDecl("b1", IntType(), IntLiteral(5))
    c1_expr = BinaryOp(Identifier("a1"), "+", Identifier("b1"))
    c1_decl = VarDecl("c1", IntType(), c1_expr)
    main_body = BlockStmt([a1_decl, b1_decl, c1_decl])
    main_func = FuncDecl("main", VoidType(), [], main_body)
    program = Program([], [main_func])
    
    checker = StaticChecker(program)
    try:
        checker.check()
        return "Static checking passed"
    except Exception as e:
        return str(e)

print("Test 043 Result:", test_043())
print("Test 057 Result:", test_057())
