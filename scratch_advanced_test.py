"""Advanced type-checking tests - auto inference, structs, edge cases"""
from tests.utils import Checker

tests = [
    # --- auto type inference (valid) ---
    ("002_auto_init",
     "void main() { auto x = 10; auto y = 3.14; auto z = x + y; }",
     "Static checking passed"),

    ("006_auto_str",
     'void main() { auto x = "hello"; printString(x); }',
     "Static checking passed"),

    ("008_auto_no_init_then_assign",
     "void main() { auto x; x = 1; auto y; y = 2.0; auto z = x + y; }",
     "Static checking passed"),

    ("009_auto_from_func",
     "void main() { auto x = readInt(); printInt(x); }",
     "Static checking passed"),

    ("012_for_auto",
     "void main() { for (auto i = 0; i < 10; i++) printInt(i); }",
     "Static checking passed"),

    ("015_inferred_return",
     "add(int x, int y) { return x + y; } void main() { auto x = add(1, 2); printInt(x); }",
     "Static checking passed"),

    # --- TypeCannotBeInferred ---
    ("034_auto_binop_two_unknown",
     "void main() { auto x; auto y; auto z = x + y; }",
     "TypeCannotBeInferred(BinaryOp(Identifier(x), +, Identifier(y)))"),

    ("035_auto_assign_two_unknown",
     "void main() { auto x; auto y; x = y; }",
     "TypeCannotBeInferred(AssignExpr(Identifier(x) = Identifier(y)))"),

    ("036_auto_binop_two_unknown2",
     "void mixed() { auto a; auto b; int c = a * b; }",
     "TypeCannotBeInferred(BinaryOp(Identifier(a), *, Identifier(b)))"),

    ("037_auto_unused",
     "void unused() { auto x; }",
     "TypeCannotBeInferred(BlockStmt([VarDecl(auto, x)]))"),

    ("039_auto_cmp_two_unknown",
     "void main() { auto x; auto y; int c = x < y; }",
     "TypeCannotBeInferred(BinaryOp(Identifier(x), <, Identifier(y)))"),

    ("040_auto_member_access",
     "void struct_auto() { auto x; x.y = 1; }",
     "TypeCannotBeInferred(MemberAccess(Identifier(x).y))"),

    ("041_for_auto_no_init",
     "void main() { for(auto i; i < 10; i++) {} }",
     "TypeCannotBeInferred(BinaryOp(Identifier(i), <, IntLiteral(10)))"),

    ("038_auto_return",
     "func() { auto x; return x; } void main() {}",
     "TypeCannotBeInferred(ReturnStmt(return Identifier(x)))"),

    # --- Struct literal ---
    ("004_struct_member_access",
     "struct Point { int x; int y; }; void main() { Point p; p.x = 10; p.y = 20; }",
     "Static checking passed"),

    ("046_struct_assign_mismatch",
     "struct P { int x; }; struct Q { int x; }; void main() { P p; Q q; p = q; }",
     "TypeMismatchInStatement(ExprStmt(AssignExpr(Identifier(p) = Identifier(q))))"),

    ("062_struct_literal_wrong_count",
     "struct P { int x; }; void main() { P p = {1, 2}; }",
     "TypeMismatchInExpression(StructLiteral({IntLiteral(1), IntLiteral(2)}))"),

    # --- Assignment expression in expression context ---
    ("060_assign_as_expr_type_mismatch",
     "void main() { int x; string t; int y = (x = t) + 1; }",
     "TypeMismatchInExpression(AssignExpr(Identifier(x) = Identifier(t)))"),

    # --- valid: inferred function return ---
    ("003_add_func_call",
     "int add(int x, int y) { return x + y; } void main() { int sum = add(5, 3); }",
     "Static checking passed"),

    # --- valid: for loop ---
    ("014_for_break_continue",
     "void main() { for (int i=0; i<10; i++) { if (i == 5) break; else continue; } }",
     "Static checking passed"),

    # --- valid: struct literal init ---
    ("076_struct_literal_valid",
     "struct S75 { int x; }; void main() { S75 s = {10}; }",
     "Static checking passed"),

    # --- valid: printInt with auto arg ---
    ("valid_auto_func_arg",
     "void main() { auto x; printInt(x); }",
     "Static checking passed"),

    # --- struct member access valid ---
    ("valid_member_access",
     "struct Point { int x; int y; }; void main() { Point p; int v = p.x; }",
     "Static checking passed"),

    # --- MustInLoop: break in switch (valid) ---
    ("013_switch_break",
     "void main() { int x = 1; switch (x) { case 1: printInt(1); break; default: printInt(0); } }",
     "Static checking passed"),

    # --- for loop with valid condition ---
    ("010_if_valid",
     "void main() { int x = 1; if (x > 0) x = 2; else x = 3; }",
     "Static checking passed"),

    # --- while valid  ---
    ("011_while_valid",
     "void main() { int x = 1; while (x < 10) x++; }",
     "Static checking passed"),

    # --- function that uses inferred return for auto ---
    ("valid_auto_add",
     "add(int x, int y) { return x + y; } void main() {}",
     "Static checking passed"),

    # --- string literal comparison ---
    ("053_relational_str",
     'void main() { int x; int y = x < "a"; }',
     'TypeMismatchInExpression(BinaryOp(Identifier(x), <, StringLiteral(\'a\')))'),

    # --- postfix/prefix on non-lvalue ---
    ("valid_postfix_inc",
     "void main() { int x = 1; x++; }",
     "Static checking passed"),

    ("valid_prefix_inc",
     "void main() { int x = 1; ++x; }",
     "Static checking passed"),

    # break in nested loop
    ("valid_nested_break",
     "void main() { for(int i=0; i<5; i++) { for(int j=0; j<5; j++) { break; } } }",
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
