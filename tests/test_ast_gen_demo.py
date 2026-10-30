"""
AST Generation Test Cases - Verified against TyC.g4 spec
"""

import pytest
from tests.utils import ASTGenerator

# ============================================================================
# Variable Declarations
# ============================================================================

def test_adv_000():
    """Test 0"""
    source = """void launch() { int count = 7; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([VarDecl(IntType(), count = IntLiteral(7))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_001():
    """Test 1"""
    source = """void launch() { float ratio = 2.71; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([VarDecl(FloatType(), ratio = FloatLiteral(2.71))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_002():
    """Test 2"""
    source = """void launch() { string msg = "world"; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([VarDecl(StringType(), msg = StringLiteral('world'))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_003():
    """Test 3"""
    source = """void launch() { auto val = 15; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([VarDecl(auto, val = IntLiteral(15))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_004():
    """Test 4"""
    source = """void launch() { int num; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([VarDecl(IntType(), num)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_005():
    """Test 5"""
    source = """void launch() { Coord pos; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([VarDecl(StructType(Coord), pos)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_006():
    """Test 6"""
    source = """void launch() { Coord pos = {3, 7}; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([VarDecl(StructType(Coord), pos = StructLiteral({IntLiteral(3), IntLiteral(7)}))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_007():
    """Test 7"""
    source = """void launch() { int alpha; float beta; string gamma; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([VarDecl(IntType(), alpha), VarDecl(FloatType(), beta), VarDecl(StringType(), gamma)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_008():
    """Test 8"""
    source = """void launch() { auto res = 4 + 9; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([VarDecl(auto, res = BinaryOp(IntLiteral(4), +, IntLiteral(9)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_009():
    """Test 9"""
    source = """void launch() { int val = compute(8); }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([VarDecl(IntType(), val = FuncCall(compute, [IntLiteral(8)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

# ============================================================================
# Arithmetic & Operator Precedence
# ============================================================================

def test_adv_010():
    """Test 10"""
    source = """void launch() { res = 3 + 8; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(IntLiteral(3), +, IntLiteral(8))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_011():
    """Test 11"""
    source = """void launch() { res = 5 + 3 * 4; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(IntLiteral(5), +, BinaryOp(IntLiteral(3), *, IntLiteral(4)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_012():
    """Test 12"""
    source = """void launch() { res = (5 + 3) * 4; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(BinaryOp(IntLiteral(5), +, IntLiteral(3)), *, IntLiteral(4))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_013():
    """Test 13"""
    source = """void launch() { res = 20 - 6 / 3; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(IntLiteral(20), -, BinaryOp(IntLiteral(6), /, IntLiteral(3)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_014():
    """Test 14"""
    source = """void launch() { res = 17 % 5; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(IntLiteral(17), %, IntLiteral(5))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_015():
    """Test 15"""
    source = """void launch() { res = p + q + r; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(BinaryOp(Identifier(p), +, Identifier(q)), +, Identifier(r))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_016():
    """Test 16"""
    source = """void launch() { res = p * q * r; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(BinaryOp(Identifier(p), *, Identifier(q)), *, Identifier(r))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_017():
    """Test 17"""
    source = """void launch() { res = m * n + o / p - q; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(BinaryOp(BinaryOp(Identifier(m), *, Identifier(n)), +, BinaryOp(Identifier(o), /, Identifier(p))), -, Identifier(q))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_018():
    """Test 18"""
    source = """void launch() { res = (m + n) * (o - p); }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(BinaryOp(Identifier(m), +, Identifier(n)), *, BinaryOp(Identifier(o), -, Identifier(p)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_019():
    """Test 19"""
    source = """void launch() { res = ((m + n)); }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(Identifier(m), +, Identifier(n))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

# ============================================================================
# Unary / Prefix / Postfix Operators
# ============================================================================

def test_adv_020():
    """Test 20"""
    source = """void launch() { cnt++; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(PostfixOp(Identifier(cnt)++))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_021():
    """Test 21"""
    source = """void launch() { cnt--; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(PostfixOp(Identifier(cnt)--))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_022():
    """Test 22"""
    source = """void launch() { ++cnt; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(PrefixOp(++Identifier(cnt)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_023():
    """Test 23"""
    source = """void launch() { --cnt; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(PrefixOp(--Identifier(cnt)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_024():
    """Test 24"""
    source = """void launch() { res = -val; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = PrefixOp(-Identifier(val))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_025():
    """Test 25"""
    source = """void launch() { res = !flag; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = PrefixOp(!Identifier(flag))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_026():
    """Test 26"""
    source = """void launch() { res = +val; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = PrefixOp(+Identifier(val))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_027():
    """Test 27"""
    source = """void launch() { res = ++left + right--; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(PrefixOp(++Identifier(left)), +, PostfixOp(Identifier(right)--))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_028():
    """Test 28"""
    source = """void launch() { res = -(-val); }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = PrefixOp(-PrefixOp(-Identifier(val)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_029():
    """Test 29"""
    source = """void launch() { res = !!flag; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = PrefixOp(!PrefixOp(!Identifier(flag)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

# ============================================================================
# Logical & Comparison Operators
# ============================================================================

def test_adv_030():
    """Test 30"""
    source = """void launch() { res = p && q; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(Identifier(p), &&, Identifier(q))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_031():
    """Test 31"""
    source = """void launch() { res = p || q; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(Identifier(p), ||, Identifier(q))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_032():
    """Test 32"""
    source = """void launch() { res = p == q; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(Identifier(p), ==, Identifier(q))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_033():
    """Test 33"""
    source = """void launch() { res = p < q; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(Identifier(p), <, Identifier(q))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_034():
    """Test 34"""
    source = """void launch() { res = p >= q; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(Identifier(p), >=, Identifier(q))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_035():
    """Test 35"""
    source = """void launch() { res = p || q && r; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(Identifier(p), ||, BinaryOp(Identifier(q), &&, Identifier(r)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_036():
    """Test 36"""
    source = """void launch() { res = m > n && o < p; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(BinaryOp(Identifier(m), >, Identifier(n)), &&, BinaryOp(Identifier(o), <, Identifier(p)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_037():
    """Test 37"""
    source = """void launch() { res = m > n == o < p; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(BinaryOp(Identifier(m), >, Identifier(n)), ==, BinaryOp(Identifier(o), <, Identifier(p)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_038():
    """Test 38"""
    source = """void launch() { res = !p && !q || !r; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(BinaryOp(PrefixOp(!Identifier(p)), &&, PrefixOp(!Identifier(q))), ||, PrefixOp(!Identifier(r)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_039():
    """Test 39"""
    source = """void launch() { res = (p || q) && r; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(BinaryOp(Identifier(p), ||, Identifier(q)), &&, Identifier(r))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

# ============================================================================
# Assignments
# ============================================================================

def test_adv_040():
    """Test 40"""
    source = """void launch() { score = 99; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(score) = IntLiteral(99)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_041():
    """Test 41"""
    source = """void launch() { obj.field = 42; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(obj).field) = IntLiteral(42)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_042():
    """Test 42"""
    source = """void launch() { obj.inner.field = 77; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(obj).inner).field) = IntLiteral(77)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_043():
    """Test 43"""
    source = """void launch() { alpha = beta = gamma = 0; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(alpha) = AssignExpr(Identifier(beta) = AssignExpr(Identifier(gamma) = IntLiteral(0)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_044():
    """Test 44"""
    source = """void launch() { node.left = node.right = 0; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(node).left) = AssignExpr(MemberAccess(Identifier(node).right) = IntLiteral(0))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

# ============================================================================
# Function Calls
# ============================================================================

def test_adv_045():
    """Test 45"""
    source = """void launch() { render(); }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(FuncCall(render, []))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_046():
    """Test 46"""
    source = """void launch() { draw(10, 20, 30); }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(FuncCall(draw, [IntLiteral(10), IntLiteral(20), IntLiteral(30)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_047():
    """Test 47"""
    source = """void launch() { calc(m + n, o * p); }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(FuncCall(calc, [BinaryOp(Identifier(m), +, Identifier(n)), BinaryOp(Identifier(o), *, Identifier(p))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_048():
    """Test 48"""
    source = """void launch() { outer(inner(5)); }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(FuncCall(outer, [FuncCall(inner, [IntLiteral(5)])]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_049():
    """Test 49"""
    source = """void launch() { res = encode(7) + decode(3); }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(FuncCall(encode, [IntLiteral(7)]), +, FuncCall(decode, [IntLiteral(3)]))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

# ============================================================================
# If Statements
# ============================================================================

def test_adv_050():
    """Test 50"""
    source = """void launch() { if (flag) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([IfStmt(if Identifier(flag) then BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_051():
    """Test 51"""
    source = """void launch() { if (flag) return; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([IfStmt(if Identifier(flag) then ReturnStmt(return))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_052():
    """Test 52"""
    source = """void launch() { if (val > 0) { out = 1; } else { out = 2; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([IfStmt(if BinaryOp(Identifier(val), >, IntLiteral(0)) then BlockStmt([ExprStmt(AssignExpr(Identifier(out) = IntLiteral(1)))]), else BlockStmt([ExprStmt(AssignExpr(Identifier(out) = IntLiteral(2)))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_053():
    """Test 53"""
    source = """void launch() { if (flag) out = 10; else out = 20; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([IfStmt(if Identifier(flag) then ExprStmt(AssignExpr(Identifier(out) = IntLiteral(10))), else ExprStmt(AssignExpr(Identifier(out) = IntLiteral(20))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_054():
    """Test 54"""
    source = """void launch() { if (cond1) out = 1; else if (cond2) out = 2; else out = 3; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([IfStmt(if Identifier(cond1) then ExprStmt(AssignExpr(Identifier(out) = IntLiteral(1))), else IfStmt(if Identifier(cond2) then ExprStmt(AssignExpr(Identifier(out) = IntLiteral(2))), else ExprStmt(AssignExpr(Identifier(out) = IntLiteral(3)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_055():
    """Test 55"""
    source = """void launch() { if (cond1) { if (cond2) { return 1; } } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([IfStmt(if Identifier(cond1) then BlockStmt([IfStmt(if Identifier(cond2) then BlockStmt([ReturnStmt(return IntLiteral(1))]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_056():
    """Test 56"""
    source = """void launch() { if (cond1) { } else { } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([IfStmt(if Identifier(cond1) then BlockStmt([]), else BlockStmt([]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_057():
    """Test 57"""
    source = """void launch() { if (p && q || r) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(p), &&, Identifier(q)), ||, Identifier(r)) then BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_058():
    """Test 58"""
    source = """void launch() { if (flag) { int local = 9; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([IfStmt(if Identifier(flag) then BlockStmt([VarDecl(IntType(), local = IntLiteral(9))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

# ============================================================================
# While Loops
# ============================================================================

def test_adv_060():
    """Test 60"""
    source = """void launch() { while (cnt > 0) { cnt--; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([WhileStmt(while BinaryOp(Identifier(cnt), >, IntLiteral(0)) do BlockStmt([ExprStmt(PostfixOp(Identifier(cnt)--))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_061():
    """Test 61"""
    source = """void launch() { while (cnt) cnt = cnt - 1; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([WhileStmt(while Identifier(cnt) do ExprStmt(AssignExpr(Identifier(cnt) = BinaryOp(Identifier(cnt), -, IntLiteral(1)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_062():
    """Test 62"""
    source = """void launch() { while (outer) { while (inner) { break; } } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([WhileStmt(while Identifier(outer) do BlockStmt([WhileStmt(while Identifier(inner) do BlockStmt([BreakStmt()]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_063():
    """Test 63"""
    source = """void launch() { while (cnt > 0) { if (cnt == 3) break; cnt--; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([WhileStmt(while BinaryOp(Identifier(cnt), >, IntLiteral(0)) do BlockStmt([IfStmt(if BinaryOp(Identifier(cnt), ==, IntLiteral(3)) then BreakStmt()), ExprStmt(PostfixOp(Identifier(cnt)--))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_064():
    """Test 64"""
    source = """void launch() { while (hasNext()) { handle(); } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([WhileStmt(while FuncCall(hasNext, []) do BlockStmt([ExprStmt(FuncCall(handle, []))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

# ============================================================================
# For Loops
# ============================================================================

def test_adv_065():
    """Test 65"""
    source = """void launch() { for (int idx = 0; idx < 8; idx++) { break; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ForStmt(for VarDecl(IntType(), idx = IntLiteral(0)); BinaryOp(Identifier(idx), <, IntLiteral(8)); PostfixOp(Identifier(idx)++) do BlockStmt([BreakStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_066():
    """Test 66"""
    source = """void launch() { for (;;) { break; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ForStmt(for None; None; None do BlockStmt([BreakStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_067():
    """Test 67"""
    source = """void launch() { for (idx = 0; idx < limit; idx++) total = total + 1; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ForStmt(for ExprStmt(AssignExpr(Identifier(idx) = IntLiteral(0))); BinaryOp(Identifier(idx), <, Identifier(limit)); PostfixOp(Identifier(idx)++) do ExprStmt(AssignExpr(Identifier(total) = BinaryOp(Identifier(total), +, IntLiteral(1)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_068():
    """Test 68"""
    source = """void launch() { for (int idx = 0; idx < 8; ++idx) { continue; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ForStmt(for VarDecl(IntType(), idx = IntLiteral(0)); BinaryOp(Identifier(idx), <, IntLiteral(8)); PrefixOp(++Identifier(idx)) do BlockStmt([ContinueStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_069():
    """Test 69"""
    source = """void launch() { for (idx = 0; idx < 8; idx = idx + 1) { return; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ForStmt(for ExprStmt(AssignExpr(Identifier(idx) = IntLiteral(0))); BinaryOp(Identifier(idx), <, IntLiteral(8)); AssignExpr(Identifier(idx) = BinaryOp(Identifier(idx), +, IntLiteral(1))) do BlockStmt([ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_070():
    """Test 70"""
    source = """void launch() { for (row = 0; row < 5; row++) { for (col = 0; col < 5; col++) { return; } } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ForStmt(for ExprStmt(AssignExpr(Identifier(row) = IntLiteral(0))); BinaryOp(Identifier(row), <, IntLiteral(5)); PostfixOp(Identifier(row)++) do BlockStmt([ForStmt(for ExprStmt(AssignExpr(Identifier(col) = IntLiteral(0))); BinaryOp(Identifier(col), <, IntLiteral(5)); PostfixOp(Identifier(col)++) do BlockStmt([ReturnStmt(return)]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_071():
    """Test 71"""
    source = """void launch() { for (;;) { if (done) break; else continue; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ForStmt(for None; None; None do BlockStmt([IfStmt(if Identifier(done) then BreakStmt(), else ContinueStmt())]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_072():
    """Test 72"""
    source = """void launch() { for (int idx = 15; idx > 0; --idx) { break; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ForStmt(for VarDecl(IntType(), idx = IntLiteral(15)); BinaryOp(Identifier(idx), >, IntLiteral(0)); PrefixOp(--Identifier(idx)) do BlockStmt([BreakStmt()]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

# ============================================================================
# Switch Statements
# ============================================================================

def test_adv_073():
    """Test 73"""
    source = """void launch() { switch (mode) { case 1: break; case 2: break; default: return; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([SwitchStmt(switch Identifier(mode) cases [CaseStmt(case IntLiteral(1): [BreakStmt()]), CaseStmt(case IntLiteral(2): [BreakStmt()])], default DefaultStmt(default: [ReturnStmt(return)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_074():
    """Test 74"""
    source = """void launch() { switch (mode) { case 1: out = 10; break; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([SwitchStmt(switch Identifier(mode) cases [CaseStmt(case IntLiteral(1): [ExprStmt(AssignExpr(Identifier(out) = IntLiteral(10))), BreakStmt()])])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_075():
    """Test 75"""
    source = """void launch() { switch (state) { case 0: setup(); break; case 1: execute(); break; default: teardown(); } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([SwitchStmt(switch Identifier(state) cases [CaseStmt(case IntLiteral(0): [ExprStmt(FuncCall(setup, [])), BreakStmt()]), CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(execute, [])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(teardown, []))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_076():
    """Test 76"""
    source = """void launch() { switch (lvl) { case 1: case 2: out = 1; break; default: out = 0; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([SwitchStmt(switch Identifier(lvl) cases [CaseStmt(case IntLiteral(1): []), CaseStmt(case IntLiteral(2): [ExprStmt(AssignExpr(Identifier(out) = IntLiteral(1))), BreakStmt()])], default DefaultStmt(default: [ExprStmt(AssignExpr(Identifier(out) = IntLiteral(0)))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

# ============================================================================
# Function Declarations
# ============================================================================

def test_adv_077():
    """Test 77"""
    source = """void noop() { return; }"""
    expected = "Program([FuncDecl(VoidType(), noop, [], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_078():
    """Test 78"""
    source = """int combine(int lhs, int rhs) { return lhs + rhs; }"""
    expected = "Program([FuncDecl(IntType(), combine, [Param(IntType(), lhs), Param(IntType(), rhs)], BlockStmt([ReturnStmt(return BinaryOp(Identifier(lhs), +, Identifier(rhs)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_079():
    """Test 79"""
    source = """float circleArea(float rad) { return 3.14 * rad * rad; }"""
    expected = "Program([FuncDecl(FloatType(), circleArea, [Param(FloatType(), rad)], BlockStmt([ReturnStmt(return BinaryOp(BinaryOp(FloatLiteral(3.14), *, Identifier(rad)), *, Identifier(rad)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_080():
    """Test 80"""
    source = """string welcome(string user) { return "Hey"; }"""
    expected = "Program([FuncDecl(StringType(), welcome, [Param(StringType(), user)], BlockStmt([ReturnStmt(return StringLiteral('Hey'))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_081():
    """Test 81"""
    source = """int fetchX(Coord pt) { return pt.x; }"""
    expected = "Program([FuncDecl(IntType(), fetchX, [Param(StructType(Coord), pt)], BlockStmt([ReturnStmt(return MemberAccess(Identifier(pt).x))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_082():
    """Test 82"""
    source = """int factorial(int num) { if (num == 0) return 1; return num * factorial(num - 1); }"""
    expected = "Program([FuncDecl(IntType(), factorial, [Param(IntType(), num)], BlockStmt([IfStmt(if BinaryOp(Identifier(num), ==, IntLiteral(0)) then ReturnStmt(return IntLiteral(1))), ReturnStmt(return BinaryOp(Identifier(num), *, FuncCall(factorial, [BinaryOp(Identifier(num), -, IntLiteral(1))])))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_083():
    """Test 83"""
    source = """void alpha() { beta(); } void beta() { alpha(); }"""
    expected = "Program([FuncDecl(VoidType(), alpha, [], BlockStmt([ExprStmt(FuncCall(beta, []))])), FuncDecl(VoidType(), beta, [], BlockStmt([ExprStmt(FuncCall(alpha, []))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_084():
    """Test 84"""
    source = """void mixed(int num, float ratio, string label) { return; }"""
    expected = "Program([FuncDecl(VoidType(), mixed, [Param(IntType(), num), Param(FloatType(), ratio), Param(StringType(), label)], BlockStmt([ReturnStmt(return)]))])"
    assert str(ASTGenerator(source).generate()) == expected

# ============================================================================
# Struct Declarations
# ============================================================================

def test_adv_085():
    """Test 85"""
    source = """struct Vec2 { int dx; int dy; };"""
    expected = "Program([StructDecl(Vec2, [MemberDecl(IntType(), dx), MemberDecl(IntType(), dy)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_086():
    """Test 86"""
    source = """struct Record { int key; string desc; float weight; };"""
    expected = "Program([StructDecl(Record, [MemberDecl(IntType(), key), MemberDecl(StringType(), desc), MemberDecl(FloatType(), weight)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_087():
    """Test 87"""
    source = """struct Blank {};"""
    expected = "Program([StructDecl(Blank, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_088():
    """Test 88"""
    source = """struct Inner { int val; }; struct Outer { Inner child; };"""
    expected = "Program([StructDecl(Inner, [MemberDecl(IntType(), val)]), StructDecl(Outer, [MemberDecl(StructType(Inner), child)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_089():
    """Test 89"""
    source = """struct Box { int width; int height; }; int surface(Box bx) { return bx.width * bx.height; }"""
    expected = "Program([StructDecl(Box, [MemberDecl(IntType(), width), MemberDecl(IntType(), height)]), FuncDecl(IntType(), surface, [Param(StructType(Box), bx)], BlockStmt([ReturnStmt(return BinaryOp(MemberAccess(Identifier(bx).width), *, MemberAccess(Identifier(bx).height)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

# ============================================================================
# Member Access & Postfix Chains
# ============================================================================

def test_adv_090():
    """Test 90"""
    source = """void launch() { res = obj.field; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = MemberAccess(Identifier(obj).field)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_091():
    """Test 91"""
    source = """void launch() { res = root.mid.leaf.val; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = MemberAccess(MemberAccess(MemberAccess(Identifier(root).mid).leaf).val)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_092():
    """Test 92"""
    source = """void launch() { res = pt.dx + pt.dy; }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = BinaryOp(MemberAccess(Identifier(pt).dx), +, MemberAccess(Identifier(pt).dy))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_093():
    """Test 93"""
    source = """void launch() { render(obj.color); }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(FuncCall(render, [MemberAccess(Identifier(obj).color)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_094():
    """Test 94"""
    source = """void launch() { res = entity.getVal(5); }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([ExprStmt(AssignExpr(Identifier(res) = FuncCall(MemberAccess(Identifier(entity).getVal), [IntLiteral(5)])))]))])"
    assert str(ASTGenerator(source).generate()) == expected

# ============================================================================
# Control Flow & Block Stmts
# ============================================================================

def test_adv_095():
    """Test 95"""
    source = """int entry() { return 0; }"""
    expected = "Program([FuncDecl(IntType(), entry, [], BlockStmt([ReturnStmt(return IntLiteral(0))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_096():
    """Test 96"""
    source = """void launch() { { { int local = 7; } } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([BlockStmt([BlockStmt([VarDecl(IntType(), local = IntLiteral(7))])])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_097():
    """Test 97"""
    source = """void launch() { }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected

# ============================================================================
# Complex / Integration
# ============================================================================

def test_adv_098():
    """Test 98"""
    source = """struct Vec2 { int dx; int dy; }; int magSq(Vec2 v) { return v.dx * v.dx + v.dy * v.dy; } void launch() { Vec2 v = {5, 12}; int ms = magSq(v); }"""
    expected = "Program([StructDecl(Vec2, [MemberDecl(IntType(), dx), MemberDecl(IntType(), dy)]), FuncDecl(IntType(), magSq, [Param(StructType(Vec2), v)], BlockStmt([ReturnStmt(return BinaryOp(BinaryOp(MemberAccess(Identifier(v).dx), *, MemberAccess(Identifier(v).dx)), +, BinaryOp(MemberAccess(Identifier(v).dy), *, MemberAccess(Identifier(v).dy))))])), FuncDecl(VoidType(), launch, [], BlockStmt([VarDecl(StructType(Vec2), v = StructLiteral({IntLiteral(5), IntLiteral(12)})), VarDecl(IntType(), ms = FuncCall(magSq, [Identifier(v)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_adv_099():
    """Test 99"""
    source = """void launch() { int total = 0; for (int idx = 0; idx < 8; idx++) { if (idx % 2 == 0) total = total + idx; } }"""
    expected = "Program([FuncDecl(VoidType(), launch, [], BlockStmt([VarDecl(IntType(), total = IntLiteral(0)), ForStmt(for VarDecl(IntType(), idx = IntLiteral(0)); BinaryOp(Identifier(idx), <, IntLiteral(8)); PostfixOp(Identifier(idx)++) do BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(idx), %, IntLiteral(2)), ==, IntLiteral(0)) then ExprStmt(AssignExpr(Identifier(total) = BinaryOp(Identifier(total), +, Identifier(idx)))))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected
