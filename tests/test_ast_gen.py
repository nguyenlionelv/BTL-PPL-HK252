"""
AST Generation test cases for TyC compiler.
TODO: Implement 100 test cases for AST generation
"""

import pytest
from tests.utils import ASTGenerator


# ============================================================================
# PROGRAM & DECLARATIONS (15 tests)
# ============================================================================

def test_001_simple_void_function():
    """Test simple void function with empty body"""
    source = """void main() { return; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_002_function_with_int_return():
    """Test function with int return type"""
    source = """int add() { return; }"""
    expected = "Program([FuncDecl(IntType(), add, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_003_function_auto_return():
    """Test function with auto return type (no type specified)"""
    source = """foo() { return; }"""
    expected = "Program([FuncDecl(auto, foo, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_004_function_with_one_param():
    """Test function with one parameter"""
    source = """void foo(int x) { return; }"""
    expected = "Program([FuncDecl(VoidType(), foo, [Param(IntType(), x)], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_005():
    """Test function with two parameters"""
    source = """void foo(int x, float y) { return; }"""
    expected = "Program([FuncDecl(VoidType(), foo, [Param(IntType(), x), Param(FloatType(), y)], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_006_simple_struct():
    """Test simple struct declaration with one member"""
    source = """struct Point { int x; };"""
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_007_struct_two_members():
    """Test struct with two members"""
    source = """struct Point { int x; int y; };"""
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_008_empty_struct():
    """Test empty struct"""
    source = """struct Empty {};"""
    expected = "Program([StructDecl(Empty, [])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_009_struct_with_string_member():
    """Test struct with string type member"""
    source = """struct Person { string name; };"""
    expected = "Program([StructDecl(Person, [MemberDecl(StringType(), name)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_010_struct_with_float_member():
    """Test struct with float member"""
    source = """struct Circle { float radius; };"""
    expected = "Program([StructDecl(Circle, [MemberDecl(FloatType(), radius)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_011_struct_with_struct_member():
    """Test struct with another struct as member"""
    source = """struct Line { Point start; };"""
    expected = "Program([StructDecl(Line, [MemberDecl(StructType(Point), start)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_012_multiple_functions():
    """Test program with two functions"""
    source = """void foo() { return; } int bar() { return; }"""
    expected = "Program([FuncDecl(VoidType(), foo, [], BlockStmt([ReturnStmt(return)])), FuncDecl(IntType(), bar, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_013_struct_and_function():
    """Test program with struct and function"""
    source = """struct Point { int x; }; void main() { return; }"""
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x)]), FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_014_function_float_return():
    """Test function with float return type"""
    source = """float calculate() { return; }"""
    expected = "Program([FuncDecl(FloatType(), calculate, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_015_function_string_return():
    """Test function with string return type"""
    source = """string getName() { return; }"""
    expected = "Program([FuncDecl(StringType(), getName, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# VARIABLE DECLARATIONS (10 tests)
# ============================================================================

def test_016_single_var_no_init():
    """Test single variable without initialization"""
    source = """void main() { int x; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_017_single_var_with_init():
    """Test single variable with initialization"""
    source = """void main() { int x = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x = IntLiteral(5))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_018_float_var_with_init():
    """Test float variable with initialization"""
    source = """void main() { float pi = 3.14; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(FloatType(), pi = FloatLiteral(3.14))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_019_string_var():
    """Test string variable"""
    source = """void main() { string name = "Alice"; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StringType(), name = StringLiteral('Alice'))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_020_auto_var():
    """Test auto type variable"""
    source = """void main() { auto x = 10; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, x = IntLiteral(10))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_021_multiple_vars_no_init():
    """Test multiple variables without initialization"""
    source = """void main() { int x, y; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x), VarDecl(IntType(), y)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_022_multiple_vars_with_init():
    """Test multiple variables with mixed initialization"""
    source = """void main() { int x = 1, y = 2; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x = IntLiteral(1)), VarDecl(IntType(), y = IntLiteral(2))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_023_struct_var():
    """Test struct type variable"""
    source = """void main() { Point p; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_024_var_init_with_expr():
    """Test variable initialized with expression"""
    source = """void main() { int x = 1 + 2; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x = BinaryOp(IntLiteral(1), +, IntLiteral(2)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_025_var_init_negative():
    """Test variable with negative number"""
    source = """void main() { int x = -5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x = PrefixOp(-IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================  
# STATEMENTS (25 tests)
# ============================================================================

def test_026_if_without_else():
    """Test if statement without else"""
    source = """void main() { if (x) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(x) then BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_027_if_with_else():
    """Test if statement with else"""
    source = """void main() { if (x) { return; } else { } }"""
    expected = "AST Generation Error: Error on line 1 col 42: }"
    assert str(ASTGenerator(source).generate()) == expected

def test_027_if_with_else_correct():
    """Test if statement with else"""
    source = """void main() { if (x) { return; } else { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(x) then BlockStmt([ReturnStmt(return)]), else BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_028_if_with_comparison():
    """Test if with comparison condition"""
    source = """void main() { if (x > 5) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(5)) then BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_029_while_loop():
    """Test while loop"""
    source = """void main() { while (i < 10) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(10)) do BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_030_for_loop_full():
    """Test for loop with all parts"""
    source = """void main() { for (int i = 0; i < 10; i++) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_031_for_loop_no_init():
    """Test for loop without initialization"""
    source = """void main() { for (; i < 10; i++) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_032_for_loop_no_condition():
    """Test for loop without condition (infinite loop)"""
    source = """void main() { for (int i = 0; ; i++) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); None; PostfixOp(Identifier(i)++) do BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_033_for_loop_no_update():
    """Test for loop without update"""
    source = """void main() { for (int i = 0; i < 10; ) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); None do BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_034_switch_one_case():
    """Test switch statement with one case"""
    source = """void main() { switch (x) { case 1: break; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])])]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_035_switch_two_cases():
    """Test switch with two cases"""
    source = """void main() { switch (x) { case 1: break; case 2: break; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()]), CaseStmt(case IntLiteral(2): [BreakStmt()])])]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_036_switch_with_default():
    """Test switch with default case"""
    source = """void main() { switch (x) { case 1: break; default: break; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])], default DefaultStmt(default: [BreakStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_037_break_statement():
    """Test break statement"""
    source = """void main() { while (1) { break; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while IntLiteral(1) do BlockStmt([BreakStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_038_continue_statement():
    """Test continue statement"""
    source = """void main() { while (1) { continue; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while IntLiteral(1) do BlockStmt([ContinueStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_039_return_with_value():
    """Test return with value"""
    source = """int main() { return 42; }"""
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return IntLiteral(42))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_040_return_without_value():
    """Test return without value"""
    source = """void main() { return; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_041_assignment_statement():
    """Test assignment statement"""
    source = """void main() { x = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_042_function_call_statement():
    """Test function call as statement"""
    source = """void main() { foo(); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, []))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_043_function_call_with_args():
    """Test function call with arguments"""
    source = """void main() { foo(1, 2); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, [IntLiteral(1), IntLiteral(2)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_044_nested_blocks():
    """Test nested blocks"""
    source = """void main() { { int x; } }"""
    expected = "AST Generation Error: Error on line 1 col 16: int"
    assert str(ASTGenerator(source).generate()) == expected


def test_045_multiple_statements():
    """Test multiple statements in block"""
    source = """void main() { int x; x = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x), ExprStmt(AssignExpr(Identifier(x) = IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_046_if_with_statement_body():
    """Test if with statement body (not block)"""
    source = """void main() { if (x) x = 1; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(x) then ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_047_while_with_statement_body():
    """Test while with statement body (not block)"""
    source = """void main() { while (x) x = 1; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while Identifier(x) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_048_for_with_assignment_init():
    """Test for loop with assignment initialization"""
    source = """void main() { for (i = 0; i < 10; i++) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for AssignExpr(Identifier(i) = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_049_prefix_increment_statement():
    """Test prefix increment as statement"""
    source = """void main() { ++x; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(PrefixOp(++Identifier(x)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_050_postfix_increment_statement():
    """Test postfix increment as statement"""
    source = """void main() { x++; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(PostfixOp(Identifier(x)++))]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# EXPRESSIONS (30 tests)
# ============================================================================

def test_051_addition():
    """Test addition operation"""
    source = """void main() { x = a + b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), +, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_052_subtraction():
    """Test subtraction operation"""
    source = """void main() { x = a - b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), -, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_053_multiplication():
    """Test multiplication operation"""
    source = """void main() { x = a * b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), *, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_054_division():
    """Test division operation"""
    source = """void main() { x = a / b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), /, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_055_modulo():
    """Test modulo operation"""
    source = """void main() { x = a % b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), %, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_056_logical_and():
    """Test logical AND"""
    source = """void main() { x = a && b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), &&, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_057_logical_or():
    """Test logical OR"""
    source = """void main() { x = a || b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), ||, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_058_less_than():
    """Test less than comparison"""
    source = """void main() { x = a < b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), <, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_059_greater_than():
    """Test greater than comparison"""
    source = """void main() { x = a > b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), >, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_060_equals():
    """Test equality comparison"""
    source = """void main() { x = a == b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), ==, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_061_not_equals():
    """Test inequality comparison"""
    source = """void main() { x = a != b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), !=, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_062_less_equal():
    """Test less than or equal"""
    source = """void main() { x = a <= b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), <=, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_063_greater_equal():
    """Test greater than or equal"""
    source = """void main() { x = a >= b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), >=, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_064_prefix_increment():
    """Test prefix increment"""
    source = """void main() { x = ++y; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PrefixOp(++Identifier(y))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_065_prefix_decrement():
    """Test prefix decrement"""
    source = """void main() { x = --y; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PrefixOp(--Identifier(y))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_066_postfix_increment():
    """Test postfix increment"""
    source = """void main() { x = y++; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PostfixOp(Identifier(y)++)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_067_postfix_decrement():
    """Test postfix decrement"""
    source = """void main() { x = y--; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PostfixOp(Identifier(y)--)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_068_logical_not():
    """Test logical NOT"""
    source = """void main() { x = !y; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PrefixOp(!Identifier(y))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_069_unary_minus():
    """Test unary minus"""
    source = """void main() { x = -y; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PrefixOp(-Identifier(y))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_070_unary_plus():
    """Test unary plus"""
    source = """void main() { x = +y; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PrefixOp(+Identifier(y))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_071_member_access():
    """Test member access"""
    source = """void main() { x = p.x; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = MemberAccess(Identifier(p).x)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_072_chained_member_access():
    """Test chained member access"""
    source = """void main() { x = p.q.r; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = MemberAccess(MemberAccess(Identifier(p).q).r)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_073_struct_literal_empty():
    """Test empty struct literal"""
    source = """void main() { Point p = {}; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p = StructLiteral({}))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_074_struct_literal_one_value():
    """Test struct literal with one value"""
    source = """void main() { Point p = {5}; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p = StructLiteral({IntLiteral(5)}))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_075_struct_literal_two_values():
    """Test struct literal with two values"""
    source = """void main() { Point p = {1, 2}; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p = StructLiteral({IntLiteral(1), IntLiteral(2)}))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_076_parenthesized_expr():
    """Test parenthesized expression"""
    source = """void main() { x = (5); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_077_complex_arithmetic():
    """Test complex arithmetic expression"""
    source = """void main() { x = a + b * c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), +, BinaryOp(Identifier(b), *, Identifier(c)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_078_chained_assignment():
    """Test chained assignment"""
    source = """void main() { x = y = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = AssignExpr(Identifier(y) = IntLiteral(5))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_079_member_assignment():
    """Test member access assignment"""
    source = """void main() { p.x = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(p).x) = IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_080_chained_member_assignment():
    """Test chained member access assignment"""
    source = """void main() { p.q.r = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(p).q).r) = IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# COMPLEX EXPRESSIONS & PRECEDENCE (10 tests)
# ============================================================================

def test_081_precedence_mul_add():
    """Test multiplication before addition precedence"""
    source = """void main() { x = a + b * c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), +, BinaryOp(Identifier(b), *, Identifier(c)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_082_precedence_parentheses():
    """Test parentheses override precedence"""
    source = """void main() { x = (a + b) * c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, Identifier(c))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_083_precedence_comparison_logical():
    """Test comparison before logical AND"""
    source = """void main() { x = a < b && c > d; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), <, Identifier(b)), &&, BinaryOp(Identifier(c), >, Identifier(d)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_084_nested_function_calls():
    """Test nested function calls"""
    source = """void main() { x = foo(bar(baz())); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = FuncCall(foo, [FuncCall(bar, [FuncCall(baz, [])])])))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_085_member_access_on_call():
    """Test member access on function call result"""
    source = """void main() { x = foo().bar; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = MemberAccess(FuncCall(foo, []).bar)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_086_call_with_complex_args():
    """Test function call with complex arguments"""
    source = """void main() { foo(a + b, c * d); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, [BinaryOp(Identifier(a), +, Identifier(b)), BinaryOp(Identifier(c), *, Identifier(d))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_087_unary_in_binary():
    """Test unary operator in binary expression"""
    source = """void main() { x = -a + b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(PrefixOp(-Identifier(a)), +, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_088_postfix_in_comparison():
    """Test postfix operator in comparison"""
    source = """void main() { x = i++ < 10; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(PostfixOp(Identifier(i)++), <, IntLiteral(10))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_089_mixed_operators():
    """Test expression with mixed operators"""
    source = """void main() { x = a * b + c / d - e % f; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(BinaryOp(Identifier(a), *, Identifier(b)), +, BinaryOp(Identifier(c), /, Identifier(d))), -, BinaryOp(Identifier(e), %, Identifier(f)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_090_logical_or_and():
    """Test logical OR and AND precedence"""
    source = """void main() { x = a || b && c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), ||, BinaryOp(Identifier(b), &&, Identifier(c)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


# ============================================================================
# INTEGRATION TESTS (10 tests)
# ============================================================================

def test_091_complete_struct_and_func():
    """Test complete program with struct and function"""
    source = """struct Point { int x; int y; }; void main() { Point p; }"""
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_092_function_with_return():
    """Test function with return value"""
    source = """int add(int a, int b) { return a + b; }"""
    expected = "Program([FuncDecl(IntType(), add, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), +, Identifier(b)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_093_multiple_statements_complex():
    """Test function with multiple complex statements"""
    source = """void foo() { int x = 5; x = x + 1; return; }"""
    expected = "Program([FuncDecl(VoidType(), foo, [], BlockStmt([VarDecl(IntType(), x = IntLiteral(5)), ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1)))), ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_094_nested_if_else():
    """Test nested if-else"""
    source = """void main() { if (x) { if (y) { z = 1; } } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(x) then BlockStmt([IfStmt(if Identifier(y) then BlockStmt([ExprStmt(AssignExpr(Identifier(z) = IntLiteral(1)))]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_095_for_with_body():
    """Test for loop with body statements"""
    source = """void main() { for (int i = 0; i < 10; i++) { x = x + 1; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1))))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_096_switch_multiple_stmts():
    """Test switch with multiple statements in case"""
    source = """void main() { switch (x) { case 1: x = 1; y = 2; break; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))), ExprStmt(AssignExpr(Identifier(y) = IntLiteral(2))), BreakStmt()])])]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_097_member_access_chain():
    """Test long member access chain"""
    source = """void main() { x = a.b.c.d; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = MemberAccess(MemberAccess(MemberAccess(Identifier(a).b).c).d)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_098_struct_init_with_exprs():
    """Test struct literal with expressions"""
    source = """void main() { Point p = {x + 1, y * 2}; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p = StructLiteral({BinaryOp(Identifier(x), +, IntLiteral(1)), BinaryOp(Identifier(y), *, IntLiteral(2))}))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_099_three_level_nesting():
    """Test three level nesting"""
    source = """void main() { { { int x; } } }"""
    expected = "AST Generation Error: Error on line 1 col 18: int"
    assert str(ASTGenerator(source).generate()) == expected


def test_100_full_program():
    """Test complete program with all features"""
    source = """struct Point { int x; int y; }; int distance(Point p1, Point p2) { int dx = p2.x - p1.x; return dx * dx; }"""
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), FuncDecl(IntType(), distance, [Param(StructType(Point), p1), Param(StructType(Point), p2)], BlockStmt([VarDecl(IntType(), dx = BinaryOp(MemberAccess(Identifier(p2).x), -, MemberAccess(Identifier(p1).x))), ReturnStmt(return BinaryOp(Identifier(dx), *, Identifier(dx)))]))])"
    assert str(ASTGenerator(source).generate()) == expected
