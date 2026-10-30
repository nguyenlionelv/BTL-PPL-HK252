import pytest
from tests.utils import ASTGenerator


def test_001():
    """Test 1"""
    source = """void main() { return; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_002():
    """Test 2"""
    source = """int add() { return; }"""
    expected = "Program([FuncDecl(IntType(), add, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_003():
    """Test 3"""
    source = """foo() { return; }"""
    expected = "Program([FuncDecl(auto, foo, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_004():
    """Test 4"""
    source = """void foo(int x) { return; }"""
    expected = "Program([FuncDecl(VoidType(), foo, [Param(IntType(), x)], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_005():
    """Test 5"""
    source = """void foo(int x, float y) { return; }"""
    expected = "Program([FuncDecl(VoidType(), foo, [Param(IntType(), x), Param(FloatType(), y)], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_006():
    """Test 6"""
    source = """struct Point { int x; };"""
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_007():
    """Test 7"""
    source = """struct Point { int x; int y; };"""
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_008():
    """Test 8"""
    source = """struct Empty {};"""
    expected = "Program([StructDecl(Empty, [])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_009():
    """Test 9"""
    source = """struct Person { string name; };"""
    expected = "Program([StructDecl(Person, [MemberDecl(StringType(), name)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_010():
    """Test 10"""
    source = """struct Circle { float radius; };"""
    expected = "Program([StructDecl(Circle, [MemberDecl(FloatType(), radius)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_011():
    """Test 11"""
    source = """struct Line { Point start; };"""
    expected = "Program([StructDecl(Line, [MemberDecl(StructType(Point), start)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_012():
    """Test 12"""
    source = """void foo() { return; } int bar() { return; }"""
    expected = "Program([FuncDecl(VoidType(), foo, [], BlockStmt([ReturnStmt(return)])), FuncDecl(IntType(), bar, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_013():
    """Test 13"""
    source = """struct Point { int x; }; void main() { return; }"""
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x)]), FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_014():
    """Test 14"""
    source = """float calculate() { return; }"""
    expected = "Program([FuncDecl(FloatType(), calculate, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_015():
    """Test 15"""
    source = """string getName() { return; }"""
    expected = "Program([FuncDecl(StringType(), getName, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_016():
    """Test 16"""
    source = """void main() { int x; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_017():
    """Test 17"""
    source = """void main() { int x = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x = IntLiteral(5))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_018():
    """Test 18"""
    source = """void main() { float pi = 3.14; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(FloatType(), pi = FloatLiteral(3.14))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_019():
    """Test 19"""
    source = """void main() { string name = "Alice"; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StringType(), name = StringLiteral('Alice'))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_020():
    """Test 20"""
    source = """void main() { auto x = 10; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, x = IntLiteral(10))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_021():
    """Test 21"""
    source = """void main() { int x; int y; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x), VarDecl(IntType(), y)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_022():
    """Test 22"""
    source = """void main() { int x = 1; int y = 2; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x = IntLiteral(1)), VarDecl(IntType(), y = IntLiteral(2))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_023():
    """Test 23"""
    source = """void main() { Point p; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_024():
    """Test 24"""
    source = """void main() { int x = 1 + 2; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x = BinaryOp(IntLiteral(1), +, IntLiteral(2)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_025():
    """Test 25"""
    source = """void main() { int x = -5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x = PrefixOp(-IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_026():
    """Test 26"""
    source = """void main() { if (x) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(x) then BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_027():
    """Test 27"""
    source = """void main() { if (x) { return; } else { } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(x) then BlockStmt([ReturnStmt(return)]), else BlockStmt([]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_027b():
    """Test 27b"""
    source = """void main() { if (x) { return; } else { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(x) then BlockStmt([ReturnStmt(return)]), else BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_028():
    """Test 28"""
    source = """void main() { if (x > 5) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(5)) then BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_029():
    """Test 29"""
    source = """void main() { while (i < 10) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(10)) do BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_030():
    """Test 30"""
    source = """void main() { for (int i = 0; i < 10; i++) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_031():
    """Test 31"""
    source = """void main() { for (; i < 10; i++) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_032():
    """Test 32"""
    source = """void main() { for (int i = 0; ; i++) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); None; PostfixOp(Identifier(i)++) do BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_033():
    """Test 33"""
    source = """void main() { for (int i = 0; i < 10; ) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); None do BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_034():
    """Test 34"""
    source = """void main() { switch (x) { case 1: break; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])])]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_035():
    """Test 35"""
    source = """void main() { switch (x) { case 1: break; case 2: break; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()]), CaseStmt(case IntLiteral(2): [BreakStmt()])])]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_036():
    """Test 36"""
    source = """void main() { switch (x) { case 1: break; default: break; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])], default DefaultStmt(default: [BreakStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_037():
    """Test 37"""
    source = """void main() { while (1) { break; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while IntLiteral(1) do BlockStmt([BreakStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_038():
    """Test 38"""
    source = """void main() { while (1) { continue; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while IntLiteral(1) do BlockStmt([ContinueStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_039():
    """Test 39"""
    source = """int main() { return 42; }"""
    expected = "Program([FuncDecl(IntType(), main, [], BlockStmt([ReturnStmt(return IntLiteral(42))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_040():
    """Test 40"""
    source = """void main() { return; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_041():
    """Test 41"""
    source = """void main() { x = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_042():
    """Test 42"""
    source = """void main() { foo(); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, []))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_043():
    """Test 43"""
    source = """void main() { foo(1, 2); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, [IntLiteral(1), IntLiteral(2)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_044():
    """Test 44"""
    source = """void main() { { int x; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([BlockStmt([VarDecl(IntType(), x)])]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_045():
    """Test 45"""
    source = """void main() { int x; x = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x), ExprStmt(AssignExpr(Identifier(x) = IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_046():
    """Test 46"""
    source = """void main() { if (x) x = 1; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(x) then ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_047():
    """Test 47"""
    source = """void main() { while (x) x = 1; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(while Identifier(x) do ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_048():
    """Test 48"""
    source = """void main() { for (i = 0; i < 10; i++) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_049():
    """Test 49"""
    source = """void main() { ++x; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(PrefixOp(++Identifier(x)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_050():
    """Test 50"""
    source = """void main() { x++; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(PostfixOp(Identifier(x)++))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_051():
    """Test 51"""
    source = """void main() { x = a + b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), +, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_052():
    """Test 52"""
    source = """void main() { x = a - b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), -, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_053():
    """Test 53"""
    source = """void main() { x = a * b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), *, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_054():
    """Test 54"""
    source = """void main() { x = a / b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), /, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_055():
    """Test 55"""
    source = """void main() { x = a % b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), %, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_056():
    """Test 56"""
    source = """void main() { x = a && b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), &&, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_057():
    """Test 57"""
    source = """void main() { x = a || b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), ||, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_058():
    """Test 58"""
    source = """void main() { x = a < b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), <, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_059():
    """Test 59"""
    source = """void main() { x = a > b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), >, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_060():
    """Test 60"""
    source = """void main() { x = a == b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), ==, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_061():
    """Test 61"""
    source = """void main() { x = a != b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), !=, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_062():
    """Test 62"""
    source = """void main() { x = a <= b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), <=, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_063():
    """Test 63"""
    source = """void main() { x = a >= b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), >=, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_064():
    """Test 64"""
    source = """void main() { x = ++y; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PrefixOp(++Identifier(y))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_065():
    """Test 65"""
    source = """void main() { x = --y; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PrefixOp(--Identifier(y))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_066():
    """Test 66"""
    source = """void main() { x = y++; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PostfixOp(Identifier(y)++)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_067():
    """Test 67"""
    source = """void main() { x = y--; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PostfixOp(Identifier(y)--)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_068():
    """Test 68"""
    source = """void main() { x = !y; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PrefixOp(!Identifier(y))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_069():
    """Test 69"""
    source = """void main() { x = -y; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PrefixOp(-Identifier(y))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_070():
    """Test 70"""
    source = """void main() { x = +y; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PrefixOp(+Identifier(y))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_071():
    """Test 71"""
    source = """void main() { x = p.x; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = MemberAccess(Identifier(p).x)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_072():
    """Test 72"""
    source = """void main() { x = p.q.r; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = MemberAccess(MemberAccess(Identifier(p).q).r)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_073():
    """Test 73"""
    source = """void main() { Point p = {}; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p = StructLiteral({}))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_074():
    """Test 74"""
    source = """void main() { Point p = {5}; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p = StructLiteral({IntLiteral(5)}))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_075():
    """Test 75"""
    source = """void main() { Point p = {1, 2}; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p = StructLiteral({IntLiteral(1), IntLiteral(2)}))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_076():
    """Test 76"""
    source = """void main() { x = (5); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_077():
    """Test 77"""
    source = """void main() { x = a + b * c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), +, BinaryOp(Identifier(b), *, Identifier(c)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_078():
    """Test 78"""
    source = """void main() { x = y = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = AssignExpr(Identifier(y) = IntLiteral(5))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_079():
    """Test 79"""
    source = """void main() { p.x = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(p).x) = IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_080():
    """Test 80"""
    source = """void main() { p.q.r = 5; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(p).q).r) = IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_081():
    """Test 81"""
    source = """void main() { x = a + b * c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), +, BinaryOp(Identifier(b), *, Identifier(c)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_082():
    """Test 82"""
    source = """void main() { x = (a + b) * c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, Identifier(c))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_083():
    """Test 83"""
    source = """void main() { x = a < b && c > d; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(Identifier(a), <, Identifier(b)), &&, BinaryOp(Identifier(c), >, Identifier(d)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_084():
    """Test 84"""
    source = """void main() { x = foo(bar(baz())); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = FuncCall(foo, [FuncCall(bar, [FuncCall(baz, [])])])))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_085():
    """Test 85"""
    source = """void main() { x = foo().bar; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = MemberAccess(FuncCall(foo, []).bar)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_086():
    """Test 86"""
    source = """void main() { foo(a + b, c * d); }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(FuncCall(foo, [BinaryOp(Identifier(a), +, Identifier(b)), BinaryOp(Identifier(c), *, Identifier(d))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_087():
    """Test 87"""
    source = """void main() { x = -a + b; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(PrefixOp(-Identifier(a)), +, Identifier(b))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_088():
    """Test 88"""
    source = """void main() { x = i++ < 10; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(PostfixOp(Identifier(i)++), <, IntLiteral(10))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_089():
    """Test 89"""
    source = """void main() { x = a * b + c / d - e % f; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(BinaryOp(BinaryOp(Identifier(a), *, Identifier(b)), +, BinaryOp(Identifier(c), /, Identifier(d))), -, BinaryOp(Identifier(e), %, Identifier(f)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_090():
    """Test 90"""
    source = """void main() { x = a || b && c; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(a), ||, BinaryOp(Identifier(b), &&, Identifier(c)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_091():
    """Test 91"""
    source = """struct Point { int x; int y; }; void main() { Point p; }"""
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_092():
    """Test 92"""
    source = """int add(int a, int b) { return a + b; }"""
    expected = "Program([FuncDecl(IntType(), add, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), +, Identifier(b)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_093():
    """Test 93"""
    source = """void foo() { int x = 5; x = x + 1; return; }"""
    expected = "Program([FuncDecl(VoidType(), foo, [], BlockStmt([VarDecl(IntType(), x = IntLiteral(5)), ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1)))), ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_094():
    """Test 94"""
    source = """void main() { if (x) { if (y) { z = 1; } } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([IfStmt(if Identifier(x) then BlockStmt([IfStmt(if Identifier(y) then BlockStmt([ExprStmt(AssignExpr(Identifier(z) = IntLiteral(1)))]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_095():
    """Test 95"""
    source = """void main() { for (int i = 0; i < 10; i++) { x = x + 1; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1))))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_096():
    """Test 96"""
    source = """void main() { switch (x) { case 1: x = 1; y = 2; break; } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1))), ExprStmt(AssignExpr(Identifier(y) = IntLiteral(2))), BreakStmt()])])]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_097():
    """Test 97"""
    source = """void main() { x = a.b.c.d; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ExprStmt(AssignExpr(Identifier(x) = MemberAccess(MemberAccess(MemberAccess(Identifier(a).b).c).d)))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_098():
    """Test 98"""
    source = """void main() { Point p = {x + 1, y * 2}; }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p = StructLiteral({BinaryOp(Identifier(x), +, IntLiteral(1)), BinaryOp(Identifier(y), *, IntLiteral(2))}))]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_099():
    """Test 99"""
    source = """void main() { { { int x; } } }"""
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([BlockStmt([BlockStmt([VarDecl(IntType(), x)])])]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_100():
    """Test 100"""
    source = """struct Point { int x; int y; }; int distance(Point p1, Point p2) { int dx = p2.x - p1.x; return dx * dx; }"""
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), FuncDecl(IntType(), distance, [Param(StructType(Point), p1), Param(StructType(Point), p2)], BlockStmt([VarDecl(IntType(), dx = BinaryOp(MemberAccess(Identifier(p2).x), -, MemberAccess(Identifier(p1).x))), ReturnStmt(return BinaryOp(Identifier(dx), *, Identifier(dx)))]))])"
    assert str(ASTGenerator(source).generate()) == expected
