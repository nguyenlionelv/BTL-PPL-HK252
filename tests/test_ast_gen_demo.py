"""
Generated Advanced AST Test Cases
"""

import pytest
from tests.utils import ASTGenerator

def test_adv_000():
    """Test Case 0: Advanced"""
    source = """void main() { x = a * b + c * d - e / f; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(BinaryOp(Identifier(a), *, Identifier(b)), +, BinaryOp(Identifier(c), *, Identifier(d))), -, BinaryOp(Identifier(e), /, Identifier(f)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_001():
    """Test Case 1: Advanced"""
    source = """void main() { x = a * (b + c) * (d - e) / f; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(BinaryOp(Identifier(a), *, BinaryOp(Identifier(b), +, Identifier(c))), *, BinaryOp(Identifier(d), -, Identifier(e))), /, Identifier(f))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_002():
    """Test Case 2: Advanced"""
    source = """void main() { x = -a + --b * ++c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(PrefixOp(-Identifier(a)), +, BinaryOp(PrefixOp(--Identifier(b)), *, PrefixOp(++Identifier(c))))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_003():
    """Test Case 3: Advanced"""
    source = """void main() { x = a || b && c || d && e; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), ||, BinaryOp(Identifier(b), &&, Identifier(c))), ||, BinaryOp(Identifier(d), &&, Identifier(e)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_004():
    """Test Case 4: Advanced"""
    source = """void main() { x = (a || b) && (c || d) && e; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(BinaryOp(Identifier(a), ||, Identifier(b)), &&, BinaryOp(Identifier(c), ||, Identifier(d))), &&, Identifier(e))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_005():
    """Test Case 5: Advanced"""
    source = """void main() { x = a > b == c < d; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), >, Identifier(b)), ==, BinaryOp(Identifier(c), <, Identifier(d)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_006():
    """Test Case 6: Advanced"""
    source = """void main() { x = a >= b != c <= d; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), >=, Identifier(b)), !=, BinaryOp(Identifier(c), <=, Identifier(d)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_007():
    """Test Case 7: Advanced"""
    source = """void main() { x = !a && !b || !c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(PrefixOp(!Identifier(a)), &&, PrefixOp(!Identifier(b))), ||, PrefixOp(!Identifier(c)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_008():
    """Test Case 8: Advanced"""
    source = """void main() { x = !(a && b) || !(c && d); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(PrefixOp(!BinaryOp(Identifier(a), &&, Identifier(b))), ||, PrefixOp(!BinaryOp(Identifier(c), &&, Identifier(d))))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_009():
    """Test Case 9: Advanced"""
    source = """void main() { x = a + b + c + d + e + f; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(BinaryOp(BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), +, Identifier(c)), +, Identifier(d)), +, Identifier(e)), +, Identifier(f))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_010():
    """Test Case 10: Advanced"""
    source = """void main() { x = a * b * c * d * e * f; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(BinaryOp(BinaryOp(BinaryOp(Identifier(a), *, Identifier(b)), *, Identifier(c)), *, Identifier(d)), *, Identifier(e)), *, Identifier(f))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_011():
    """Test Case 11: Advanced"""
    source = """void main() { x = a = b = c = d = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = AssignExpr(Identifier(c) = AssignExpr(Identifier(d) = IntLiteral(5)))))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_012():
    """Test Case 12: Advanced"""
    source = """void main() { x = a.b.c.d.e; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = MemberAccess(MemberAccess(MemberAccess(MemberAccess(Identifier(a).b).c).d).e)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_013():
    """Test Case 13: Advanced"""
    source = """void main() { x = foo(1, 2, 3) + bar(4, 5, 6); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(FuncCall(foo, [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), +, FuncCall(bar, [IntLiteral(4), IntLiteral(5), IntLiteral(6)]))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_014():
    """Test Case 14: Advanced"""
    source = """void main() { x = foo(a + b, c * d, e / f); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = FuncCall(foo, [BinaryOp(Identifier(a), +, Identifier(b)), BinaryOp(Identifier(c), *, Identifier(d)), BinaryOp(Identifier(e), /, Identifier(f))])))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_015():
    """Test Case 15: Advanced"""
    source = """void main() { x = a[i] + b[j]; }"""
    expected = "AST Generation Error: Error Token ["
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_016():
    """Test Case 16: Advanced"""
    source = """void main() { x = {1, 2, 3}; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = StructLiteral({IntLiteral(1), IntLiteral(2), IntLiteral(3)})))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_017():
    """Test Case 17: Advanced"""
    source = """void main() { x = {a + 1, b * 2, c / 3}; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = StructLiteral({BinaryOp(Identifier(a), +, IntLiteral(1)), BinaryOp(Identifier(b), *, IntLiteral(2)), BinaryOp(Identifier(c), /, IntLiteral(3))})))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_018():
    """Test Case 18: Advanced"""
    source = """void main() { x = (a > b) ? c : d; }"""
    expected = "AST Generation Error: Error Token ?"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_019():
    """Test Case 19: Advanced"""
    source = """void main() { if (a > b) { x = c; } else { x = d; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if BinaryOp(Identifier(a), >, Identifier(b)) then BlockStmt([ExprStmt(AssignExpr(Identifier(x) = Identifier(c)))]), else BlockStmt([ExprStmt(AssignExpr(Identifier(x) = Identifier(d)))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_020():
    """Test Case 20: Advanced"""
    source = """void main() { x = (a + b) % (c - d); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), %, BinaryOp(Identifier(c), -, Identifier(d)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_021():
    """Test Case 21: Advanced"""
    source = """void main() { x = a + b * c / d % e - f; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), +, BinaryOp(BinaryOp(BinaryOp(Identifier(b), *, Identifier(c)), /, Identifier(d)), %, Identifier(e))), -, Identifier(f))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_022():
    """Test Case 22: Advanced"""
    source = """void main() { if (a) { if (b) { if (c) { return; } } } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(a) then BlockStmt([IfStmt(if Identifier(b) then BlockStmt([IfStmt(if Identifier(c) then BlockStmt([ReturnStmt(return)]))]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_023():
    """Test Case 23: Advanced"""
    source = """void main() { while (a) { while (b) { while (c) { break; } } } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while Identifier(a) do BlockStmt([WhileStmt(while Identifier(b) do BlockStmt([WhileStmt(while Identifier(c) do BlockStmt([BreakStmt()]))]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_024():
    """Test Case 24: Advanced"""
    source = """void main() { for(i=0;i<10;i++) { for(j=0;j<10;j++) { return; } } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for AssignExpr(Identifier(i) = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ForStmt(for AssignExpr(Identifier(j) = IntLiteral(0)); BinaryOp(Identifier(j), <, IntLiteral(10)); PostfixOp(Identifier(j)++) do BlockStmt([ReturnStmt(return)]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_025():
    """Test Case 25: Advanced"""
    source = """void main() { if(a) { while(b) { if(c) { break; } } } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(a) then BlockStmt([WhileStmt(while Identifier(b) do BlockStmt([IfStmt(if Identifier(c) then BlockStmt([BreakStmt()]))]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_026():
    """Test Case 26: Advanced"""
    source = """void main() { switch(x) { case 1: if(y) break; case 2: while(z) continue; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [IfStmt(if Identifier(y) then BreakStmt())]), CaseStmt(case IntLiteral(2): [WhileStmt(while Identifier(z) do ContinueStmt())])])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_027():
    """Test Case 27: Advanced"""
    source = """void main() { do { x = x + 1; } while (x < 10); }"""
    expected = "AST Generation Error: Error on line 1 col 17: {"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_028():
    """Test Case 28: Advanced"""
    source = """void main() { while (x < 10) { x = x + 1; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while BinaryOp(Identifier(x), <, IntLiteral(10)) do BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1))))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_029():
    """Test Case 29: Advanced"""
    source = """void main() { if (x) { return; } else { if (y) { return; } else { return; } } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(x) then BlockStmt([ReturnStmt(return)]), else BlockStmt([IfStmt(if Identifier(y) then BlockStmt([ReturnStmt(return)]), else BlockStmt([ReturnStmt(return)]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_030():
    """Test Case 30: Advanced"""
    source = """void main() { { { { { int x; } } } } }"""
    expected = "AST Generation Error: Error on line 1 col 22: int"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_031():
    """Test Case 31: Advanced"""
    source = """void main() { if(1){ if(1){ if(1){ int x; } } } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if IntLiteral(1) then BlockStmt([IfStmt(if IntLiteral(1) then BlockStmt([IfStmt(if IntLiteral(1) then BlockStmt([VarDecl(IntType(), x)]))]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_032():
    """Test Case 32: Advanced"""
    source = """void main() { for(;;){ if(x) break; else continue; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for None; None; None do BlockStmt([IfStmt(if Identifier(x) then BreakStmt(), else ContinueStmt())]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_033():
    """Test Case 33: Advanced"""
    source = """void main() { while(true) { if(x) return; x=x+1; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while Identifier(true) do BlockStmt([IfStmt(if Identifier(x) then ReturnStmt(return)), ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1))))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_034():
    """Test Case 34: Advanced"""
    source = """void main() { if(x) x=1; else if(y) y=2; else z=3; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(x) then ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))), else IfStmt(if Identifier(y) then ExprStmt(AssignExpr(Identifier(y) = IntLiteral(2))), else ExprStmt(AssignExpr(Identifier(z) = IntLiteral(3)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_035():
    """Test Case 35: Advanced"""
    source = """void main() { switch(x) { default: break; case 1: return; } }"""
    expected = "AST Generation Error: Error on line 1 col 42: case"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_036():
    """Test Case 36: Advanced"""
    source = """void main() { switch(x) { case 1: { int y; } break; } }"""
    expected = "AST Generation Error: Error on line 1 col 36: int"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_037():
    """Test Case 37: Advanced"""
    source = """void main() { if(x) { int y = 1; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(x) then BlockStmt([VarDecl(IntType(), y = IntLiteral(1))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_038():
    """Test Case 38: Advanced"""
    source = """void main() { for(int i=0; i<10; i++) { if(i%2==0) continue; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)) then ContinueStmt())]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_039():
    """Test Case 39: Advanced"""
    source = """void main() { while(x>0) { x--; if(x==5) break; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while BinaryOp(Identifier(x), >, IntLiteral(0)) do BlockStmt([ExprStmt(PostfixOp(Identifier(x)--)), IfStmt(if BinaryOp(Identifier(x), ==, IntLiteral(5)) then BreakStmt())]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_040():
    """Test Case 40: Advanced"""
    source = """void main() { if(a && b || c) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(a), &&, Identifier(b)), ||, Identifier(c)) then BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_041():
    """Test Case 41: Advanced"""
    source = """void main() { if((a+b) > (c-d)) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), >, BinaryOp(Identifier(c), -, Identifier(d))) then BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_042():
    """Test Case 42: Advanced"""
    source = """void main() { for(i=0, j=0; i<10; i++, j++) { return; } }"""
    expected = "AST Generation Error: Error on line 1 col 37: ,"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_043():
    """Test Case 43: Advanced"""
    source = """struct A { int x; }; struct B { A a; }; void main() { B b; }"""
    expected = "Program([StructDecl(A, [MemberDecl(IntType(), x)]), StructDecl(B, [MemberDecl(StructType(A), a)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(B), b)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_044():
    """Test Case 44: Advanced"""
    source = """struct Node { int val; Node next; }; void main() { return; }"""
    expected = "Program([StructDecl(Node, [MemberDecl(IntType(), val), MemberDecl(StructType(Node), next)]), FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_045():
    """Test Case 45: Advanced"""
    source = """struct Rect { int w; int h; }; void main() { Rect r = {10, 20}; }"""
    expected = "Program([StructDecl(Rect, [MemberDecl(IntType(), w), MemberDecl(IntType(), h)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Rect), r = StructLiteral({IntLiteral(10), IntLiteral(20)}))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_046():
    """Test Case 46: Advanced"""
    source = """struct Point { float x; float y; }; void main() { Point p = {1.5, 2.5}; }"""
    expected = "Program([StructDecl(Point, [MemberDecl(FloatType(), x), MemberDecl(FloatType(), y)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p = StructLiteral({FloatLiteral(1.5), FloatLiteral(2.5)}))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_047():
    """Test Case 47: Advanced"""
    source = """struct Data { int id; string name; float val; }; void main() { return; }"""
    expected = "Program([StructDecl(Data, [MemberDecl(IntType(), id), MemberDecl(StringType(), name), MemberDecl(FloatType(), val)]), FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_048():
    """Test Case 48: Advanced"""
    source = """struct Empty {}; void main() { Empty e; }"""
    expected = "Program([StructDecl(Empty, []), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Empty), e)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_049():
    """Test Case 49: Advanced"""
    source = """struct Nested { struct Inner { int x; }; Inner i; }; void main() { return; }"""
    expected = "AST Generation Error: Error on line 1 col 16: struct"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_050():
    """Test Case 50: Advanced"""
    source = """struct A { int x; }; struct B { int y; }; void main() { A a; B b; }"""
    expected = "Program([StructDecl(A, [MemberDecl(IntType(), x)]), StructDecl(B, [MemberDecl(IntType(), y)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(A), a), VarDecl(StructType(B), b)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_051():
    """Test Case 51: Advanced"""
    source = """struct Vec3 { float x; float y; float z; }; void main() { Vec3 v = {1.0, 2.0, 3.0}; }"""
    expected = "Program([StructDecl(Vec3, [MemberDecl(FloatType(), x), MemberDecl(FloatType(), y), MemberDecl(FloatType(), z)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Vec3), v = StructLiteral({FloatLiteral(1.0), FloatLiteral(2.0), FloatLiteral(3.0)}))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_052():
    """Test Case 52: Advanced"""
    source = """struct Complex { float real; float imag; }; void main() { Complex c = {1.0, -1.0}; }"""
    expected = "Program([StructDecl(Complex, [MemberDecl(FloatType(), real), MemberDecl(FloatType(), imag)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Complex), c = StructLiteral({FloatLiteral(1.0), PrefixOp(-FloatLiteral(1.0))}))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_053():
    """Test Case 53: Advanced"""
    source = """void main() { Point p; p.x = 10; p.y = 20; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p), ExprStmt(AssignExpr(MemberAccess(Identifier(p).x) = IntLiteral(10))), ExprStmt(AssignExpr(MemberAccess(Identifier(p).y) = IntLiteral(20)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_054():
    """Test Case 54: Advanced"""
    source = """void main() { Rect r; r.w = 100; r.h = 200; area = r.w * r.h; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Rect), r), ExprStmt(AssignExpr(MemberAccess(Identifier(r).w) = IntLiteral(100))), ExprStmt(AssignExpr(MemberAccess(Identifier(r).h) = IntLiteral(200))), ExprStmt(AssignExpr(Identifier(area) = BinaryOp(MemberAccess(Identifier(r).w), *, MemberAccess(Identifier(r).h))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_055():
    """Test Case 55: Advanced"""
    source = """void main() { Node n; n.next.val = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Node), n), ExprStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(n).next).val) = IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_056():
    """Test Case 56: Advanced"""
    source = """void main() { a.b.c.d = 10; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(MemberAccess(MemberAccess(Identifier(a).b).c).d) = IntLiteral(10)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_057():
    """Test Case 57: Advanced"""
    source = """void main() { x = s.foo(1); }"""
    expected = "AST Generation Error: Error on line 1 col 23: ("
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_058():
    """Test Case 58: Advanced"""
    source = """void main() { foo(s.x); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, [MemberAccess(Identifier(s).x)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_059():
    """Test Case 59: Advanced"""
    source = """void main() { foo(s.a.b); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, [MemberAccess(MemberAccess(Identifier(s).a).b)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_060():
    """Test Case 60: Advanced"""
    source = """void main() { Point p = {1, 2}; Point q = p; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p = StructLiteral({IntLiteral(1), IntLiteral(2)})), VarDecl(StructType(Point), q = Identifier(p))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_061():
    """Test Case 61: Advanced"""
    source = """void main() { x = p.x + p.y; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(MemberAccess(Identifier(p).x), +, MemberAccess(Identifier(p).y))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_062():
    """Test Case 62: Advanced"""
    source = """void main() { p.x = p.y = 0; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(p).x) = AssignExpr(MemberAccess(Identifier(p).y) = IntLiteral(0))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_063():
    """Test Case 63: Advanced"""
    source = """void main() { return p.x; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return MemberAccess(Identifier(p).x))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_064():
    """Test Case 64: Advanced"""
    source = """int fib(int n) { if(n<=1) return n; return fib(n-1) + fib(n-2); }"""
    expected = "Program([FuncDecl(IntType(), fib, [Param(IntType(), n)], BlockStmt([IfStmt(if BinaryOp(Identifier(n), <=, IntLiteral(1)) then ReturnStmt(return Identifier(n))), ReturnStmt(return BinaryOp(FuncCall(fib, [BinaryOp(Identifier(n), -, IntLiteral(1))]), +, FuncCall(fib, [BinaryOp(Identifier(n), -, IntLiteral(2))])))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_065():
    """Test Case 65: Advanced"""
    source = """int fact(int n) { if(n==0) return 1; return n * fact(n-1); }"""
    expected = "Program([FuncDecl(IntType(), fact, [Param(IntType(), n)], BlockStmt([IfStmt(if BinaryOp(Identifier(n), ==, IntLiteral(0)) then ReturnStmt(return IntLiteral(1))), ReturnStmt(return BinaryOp(Identifier(n), *, FuncCall(fact, [BinaryOp(Identifier(n), -, IntLiteral(1))])))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_066():
    """Test Case 66: Advanced"""
    source = """void swap(int a, int b) { int t=a; a=b; b=t; }"""
    expected = "Program([FuncDecl(VoidType(), swap, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([VarDecl(IntType(), t = Identifier(a)), ExprStmt(AssignExpr(Identifier(a) = Identifier(b))), ExprStmt(AssignExpr(Identifier(b) = Identifier(t)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_067():
    """Test Case 67: Advanced"""
    source = """int max(int a, int b) { if(a>b) return a; return b; }"""
    expected = "Program([FuncDecl(IntType(), max, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([IfStmt(if BinaryOp(Identifier(a), >, Identifier(b)) then ReturnStmt(return Identifier(a))), ReturnStmt(return Identifier(b))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_068():
    """Test Case 68: Advanced"""
    source = """int min(int a, int b) { return (a<b) ? a : b; }"""
    expected = "AST Generation Error: Error Token ?"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_069():
    """Test Case 69: Advanced"""
    source = """int min(int a, int b) { if(a<b) return a; return b; }"""
    expected = "Program([FuncDecl(IntType(), min, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([IfStmt(if BinaryOp(Identifier(a), <, Identifier(b)) then ReturnStmt(return Identifier(a))), ReturnStmt(return Identifier(b))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_070():
    """Test Case 70: Advanced"""
    source = """void foo(int a, float b, string c) { return; }"""
    expected = "Program([FuncDecl(VoidType(), foo, [Param(IntType(), a), Param(FloatType(), b), Param(StringType(), c)], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_071():
    """Test Case 71: Advanced"""
    source = """int add3(int a, int b, int c) { return a+b+c; }"""
    expected = "Program([FuncDecl(IntType(), add3, [Param(IntType(), a), Param(IntType(), b), Param(IntType(), c)], BlockStmt([ReturnStmt(return BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), +, Identifier(c)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_072():
    """Test Case 72: Advanced"""
    source = """float circleArea(float r) { return 3.14 * r * r; }"""
    expected = "Program([FuncDecl(FloatType(), circleArea, [Param(FloatType(), r)], BlockStmt([ReturnStmt(return BinaryOp(BinaryOp(FloatLiteral(3.14), *, Identifier(r)), *, Identifier(r)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_073():
    """Test Case 73: Advanced"""
    source = """void doNothing() { return; }"""
    expected = "Program([FuncDecl(VoidType(), doNothing, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_074():
    """Test Case 74: Advanced"""
    source = """int callMe() { return callMe(); }"""
    expected = "Program([FuncDecl(IntType(), callMe, [], BlockStmt([ReturnStmt(return FuncCall(callMe, []))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_075():
    """Test Case 75: Advanced"""
    source = """void f1() { f2(); } void f2() { f1(); }"""
    expected = "Program([FuncDecl(VoidType(), f1, [], BlockStmt([ExprStmt(FuncCall(f2, []))])), FuncDecl(VoidType(), f2, [], BlockStmt([ExprStmt(FuncCall(f1, []))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_076():
    """Test Case 76: Advanced"""
    source = """int complexCalc(int x) { int y = x*2; int z = y+1; return z*z; }"""
    expected = "Program([FuncDecl(IntType(), complexCalc, [Param(IntType(), x)], BlockStmt([VarDecl(IntType(), y = BinaryOp(Identifier(x), *, IntLiteral(2))), VarDecl(IntType(), z = BinaryOp(Identifier(y), +, IntLiteral(1))), ReturnStmt(return BinaryOp(Identifier(z), *, Identifier(z)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_077():
    """Test Case 77: Advanced"""
    source = """string greet(string name) { return "Hello " + name; }"""
    expected = "Program([FuncDecl(StringType(), greet, [Param(StringType(), name)], BlockStmt([ReturnStmt(return BinaryOp(StringLiteral('Hello '), +, Identifier(name)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_078():
    """Test Case 78: Advanced"""
    source = """void main() { print(fact(5)); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(print, [FuncCall(fact, [IntLiteral(5)])]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_079():
    """Test Case 79: Advanced"""
    source = """void main() { init(); update(); draw(); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(init, [])), ExprStmt(FuncCall(update, [])), ExprStmt(FuncCall(draw, []))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_080():
    """Test Case 80: Advanced"""
    source = """void main() { x = f1(f2(f3(5))); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = FuncCall(f1, [FuncCall(f2, [FuncCall(f3, [IntLiteral(5)])])])))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_081():
    """Test Case 81: Advanced"""
    source = """void main() { return f(a, b, g(c)); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return FuncCall(f, [Identifier(a), Identifier(b), FuncCall(g, [Identifier(c)])]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_082():
    """Test Case 82: Advanced"""
    source = """int main() { return 0; }"""
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return IntLiteral(0))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_083():
    """Test Case 83: Advanced"""
    source = """auto foo() { return 1; }"""
    expected = "AST Generation Error: Error on line 1 col 0: auto"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_084():
    """Test Case 84: Advanced"""
    source = """struct Point { int x; int y; };
    int distSq(Point p) { return p.x*p.x + p.y*p.y; }
    void main() { Point p = {3, 4}; int d = distSq(p); }"""
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), FuncDecl(IntType(), distSq, [Param(StructType(Point), p)], BlockStmt([ReturnStmt(return BinaryOp(BinaryOp(MemberAccess(Identifier(p).x), *, MemberAccess(Identifier(p).x)), +, BinaryOp(MemberAccess(Identifier(p).y), *, MemberAccess(Identifier(p).y))))])), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p = StructLiteral({IntLiteral(3), IntLiteral(4)})), VarDecl(IntType(), d = FuncCall(distSq, [Identifier(p)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_085():
    """Test Case 85: Advanced"""
    source = """void main() {
        int sum = 0;
        for(int i=0; i<10; i++) {
            if (i % 2 == 0) sum = sum + i;
        }
    }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), sum = IntLiteral(0)), ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)) then ExprStmt(AssignExpr(Identifier(sum) = BinaryOp(Identifier(sum), +, Identifier(i)))))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_086():
    """Test Case 86: Advanced"""
    source = """void main() {
        int i = 0;
        while(i < 100) {
            i = i * 2 + 1;
            if (i > 50) break;
        }
    }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), i = IntLiteral(0)), WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(100)) do BlockStmt([ExprStmt(AssignExpr(Identifier(i) = BinaryOp(BinaryOp(Identifier(i), *, IntLiteral(2)), +, IntLiteral(1)))), IfStmt(if BinaryOp(Identifier(i), >, IntLiteral(50)) then BreakStmt())]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_087():
    """Test Case 87: Advanced"""
    source = """void main() {
        switch(state) {
            case 0: init(); break;
            case 1: run(); break;
            case 2: cleanup(); break;
            default: error(); break;
        }
    }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(state) cases [CaseStmt(case IntLiteral(0): [ExprStmt(FuncCall(init, [])), BreakStmt()]), CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(run, [])), BreakStmt()]), CaseStmt(case IntLiteral(2): [ExprStmt(FuncCall(cleanup, [])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(error, [])), BreakStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_088():
    """Test Case 88: Advanced"""
    source = """void main() {
        int x = 10;
        if (x > 0) {
            int y = 20;
            if (y > 10) {
                int z = 30;
                x = x + y + z;
            }
        }
    }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x = IntLiteral(10)), IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStmt([VarDecl(IntType(), y = IntLiteral(20)), IfStmt(if BinaryOp(Identifier(y), >, IntLiteral(10)) then BlockStmt([VarDecl(IntType(), z = IntLiteral(30)), ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(x), +, Identifier(y)), +, Identifier(z))))]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_089():
    """Test Case 89: Advanced"""
    source = """struct Rect { int w; int h; };
    int area(Rect r) { return r.w * r.h; }
    void main() { Rect r = {10, 5}; int a = area(r); }"""
    expected = "Program([StructDecl(Rect, [MemberDecl(IntType(), w), MemberDecl(IntType(), h)]), FuncDecl(IntType(), area, [Param(StructType(Rect), r)], BlockStmt([ReturnStmt(return BinaryOp(MemberAccess(Identifier(r).w), *, MemberAccess(Identifier(r).h)))])), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Rect), r = StructLiteral({IntLiteral(10), IntLiteral(5)})), VarDecl(IntType(), a = FuncCall(area, [Identifier(r)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_090():
    """Test Case 90: Advanced"""
    source = """void main() { int x = 1, y = 2, z = 3; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x = IntLiteral(1)), VarDecl(IntType(), y = IntLiteral(2)), VarDecl(IntType(), z = IntLiteral(3))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_091():
    """Test Case 91: Advanced"""
    source = """void main() { x = (a+b) * (c-d) / (e%f); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, BinaryOp(Identifier(c), -, Identifier(d))), /, BinaryOp(Identifier(e), %, Identifier(f)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_092():
    """Test Case 92: Advanced"""
    source = """void main() { if (x && y || z && !w) return; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(x), &&, Identifier(y)), ||, BinaryOp(Identifier(z), &&, PrefixOp(!Identifier(w)))) then ReturnStmt(return))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_093():
    """Test Case 93: Advanced"""
    source = """void main() { return a.x + b.y * c.z; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return BinaryOp(MemberAccess(Identifier(a).x), +, BinaryOp(MemberAccess(Identifier(b).y), *, MemberAccess(Identifier(c).z))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_094():
    """Test Case 94: Advanced"""
    source = """void main() { for(i=0; i<n; i++) { for(j=0; j<m; j++) { sum = sum + i*j; } } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for AssignExpr(Identifier(i) = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(n)); PostfixOp(Identifier(i)++) do BlockStmt([ForStmt(for AssignExpr(Identifier(j) = IntLiteral(0)); BinaryOp(Identifier(j), <, Identifier(m)); PostfixOp(Identifier(j)++) do BlockStmt([ExprStmt(AssignExpr(Identifier(sum) = BinaryOp(Identifier(sum), +, BinaryOp(Identifier(i), *, Identifier(j)))))]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_095():
    """Test Case 95: Advanced"""
    source = """void main() { if(check()) process(); else skip(); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if FuncCall(check, []) then ExprStmt(FuncCall(process, [])), else ExprStmt(FuncCall(skip, [])))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_096():
    """Test Case 96: Advanced"""
    source = """void main() { while(valid()) { data = read(); process(data); } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while FuncCall(valid, []) do BlockStmt([ExprStmt(AssignExpr(Identifier(data) = FuncCall(read, []))), ExprStmt(FuncCall(process, [Identifier(data)]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_097():
    """Test Case 97: Advanced"""
    source = """void main() { float f = 1.2e-3; float g = .5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(FloatType(), f = FloatLiteral(0.0012)), VarDecl(FloatType(), g = FloatLiteral(0.5))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_098():
    """Test Case 98: Advanced"""
    source = """void main() { string s = "Hello \n World"; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StringType(), s = StringLiteral('Hello \\n World'))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_099():
    """Test Case 99: Advanced"""
    source = """void main() { int hex = 0; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), hex = IntLiteral(0))]))])"
    assert str(ASTGenerator(source).generate()) == expected

