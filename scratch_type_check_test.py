"""Quick type-checking validation tests"""
from tests.utils import Checker

tests = [
    # (test_name, source, expected)
    # --- Name checking (should still pass) ---
    ("001_basic_valid",
     "void main() { int x = 5; int y = x + 1; } int A() { int a = A(); int y; }",
     "Static checking passed"),

    ("016_redecl_func",
     "int foo() {} int foo() {} void main() {}",
     "Redeclared(Function, foo)"),

    ("017_redecl_struct",
     "struct Point { int x; }; struct Point { int y; }; void main() {}",
     "Redeclared(Struct, Point)"),

    ("018_redecl_member",
     "struct Point { int x; int x; }; void main() {}",
     "Redeclared(Member, x)"),

    ("019_redecl_param",
     "void foo(int x, int x) {} void main() {}",
     "Redeclared(Parameter, x)"),

    ("020_redecl_var",
     "void main() { int x; int x; }",
     "Redeclared(Variable, x)"),

    ("021_redecl_var_shadows_param",
     "void foo(int x) { int x; } void main() {}",
     "Redeclared(Variable, x)"),

    ("022_redecl_var_nested_shadows_param",
     "void foo(int x) { { int x; } } void main() {}",
     "Redeclared(Variable, x)"),

    ("023_valid_shadowing",
     "void foo() { int x; { int x; } } void main() {}",
     "Static checking passed"),

    ("024_struct_func_same_name",
     "struct foo { int x; }; int foo() {} void main() {}",
     "Static checking passed"),

    ("025_undecl_id",
     "void main() { int x = y; }",
     "UndeclaredIdentifier(y)"),

    ("026_undecl_id_assign",
     "void main() { x = 1; }",
     "UndeclaredIdentifier(x)"),

    ("029_undecl_func",
     "void main() { foo(); }",
     "UndeclaredFunction(foo)"),

    ("031_undecl_struct_var",
     "void main() { Point p; }",
     "UndeclaredStruct(Point)"),

    ("032_undecl_struct_member",
     "struct A { B b; }; void main() {}",
     "UndeclaredStruct(B)"),

    # --- Type checking: TypeMismatchInStatement ---
    ("043_if_float",
     "void main() { float x; if (x) {} }",
     "TypeMismatchInStatement(IfStmt(if Identifier(x) then BlockStmt([])))"),

    ("044_while_float",
     "void main() { float f; while (f) {} }",
     "TypeMismatchInStatement(WhileStmt(while Identifier(f) do BlockStmt([])))"),

    ("045_assign_type_mismatch",
     "void main() { int x; string y; x = y; }",
     "TypeMismatchInStatement(ExprStmt(AssignExpr(Identifier(x) = Identifier(y))))"),

    ("047_ret_str_in_int_func",
     'int func() { return "hi"; } void main() {}',
     "TypeMismatchInStatement(ReturnStmt(return StringLiteral('hi')))"),

    ("048_ret_val_in_void",
     "void func() { return 1; } void main() {}",
     "TypeMismatchInStatement(ReturnStmt(return IntLiteral(1)))"),

    ("049_ret_empty_in_int",
     "int func() { return; } void main() {}",
     "TypeMismatchInStatement(ReturnStmt(return))"),

    ("050_switch_float",
     "void main() { switch(3.14) { case 1: break; } }",
     "TypeMismatchInStatement(SwitchStmt(switch FloatLiteral(3.14) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])]))"),

    # --- TypeMismatchInExpression ---
    ("051_binop_int_str",
     'void main() { int x = 1 + "a"; }',
     "TypeMismatchInExpression(BinaryOp(IntLiteral(1), +, StringLiteral('a')))"),

    ("052_mod_float",
     "void main() { int x; int y = x % 3.14; }",
     "TypeMismatchInExpression(BinaryOp(Identifier(x), %, FloatLiteral(3.14)))"),

    ("054_logical_float",
     "void main() { int x; int y = x && 3.14; }",
     "TypeMismatchInExpression(BinaryOp(Identifier(x), &&, FloatLiteral(3.14)))"),

    ("055_prefix_inc_float",
     "void main() { float x; ++x; }",
     "TypeMismatchInExpression(PrefixOp(++Identifier(x)))"),

    ("056_prefix_inc_literal",
     "void main() { ++5; }",
     "TypeMismatchInExpression(PrefixOp(++IntLiteral(5)))"),

    ("057_member_nonstructb",
     "void main() { int x; int y = x.z; }",
     "TypeMismatchInExpression(MemberAccess(Identifier(x).z))"),

    ("058_func_call_wrong_arg_type",
     'void foo(int x) {} void main() { foo("a"); }',
     "TypeMismatchInExpression(FuncCall(foo, [StringLiteral('a')]))"),

    ("059_func_call_wrong_arg_count",
     "void foo(int x) {} void main() { foo(1, 2); }",
     "TypeMismatchInExpression(FuncCall(foo, [IntLiteral(1), IntLiteral(2)]))"),

    ("061_assign_literal_lhs",
     "void main() { int x; int y = (5 = x); }",
     "TypeMismatchInExpression(AssignExpr(IntLiteral(5) = Identifier(x)))"),

    # --- MustInLoop ---
    ("063_break_outside",
     "void main() { break; }",
     "MustInLoop(BreakStmt())"),

    ("064_continue_outside",
     "void main() { continue; }",
     "MustInLoop(ContinueStmt())"),

    ("065_break_in_if",
     "void main() { if (1) break; }",
     "MustInLoop(BreakStmt())"),

    ("066_continue_in_switch",
     "void main() { switch(1) { case 1: continue; } }",
     "MustInLoop(ContinueStmt())"),

    # --- auto type inference ---
    ("074_auto_int_literal",
     "void main() { auto x = 73; }",
     "Static checking passed"),

    ("075_func_return",
     "int f74() { return 74; } void main() {}",
     "Static checking passed"),

    # --- valid loops ---
    ("068_for_valid",
     "void main() { for(int i=0; i<67; i++) {} }",
     "Static checking passed"),

    ("069_if_valid",
     "void main() { int x = 68; if (x > 0) {} }",
     "Static checking passed"),

    ("071_basic_valid",
     "void main() { int x70 = 70; }",
     "Static checking passed"),
]

pass_count = 0
fail_count = 0
for name, src, expected in tests:
    result = Checker(src).check_from_source()
    if result == expected:
        print(f"  PASS test_{name}")
        pass_count += 1
    else:
        print(f"  FAIL test_{name}:")
        print(f"    expected: {expected!r}")
        print(f"    got:      {result!r}")
        fail_count += 1

print(f"\n{pass_count} passed, {fail_count} failed out of {len(tests)} tests.")
