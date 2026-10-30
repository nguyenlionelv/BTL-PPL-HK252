"""
Test cases for TyC code generation.
All tests construct the AST manually — no dependency on the parser/ASTGenerator.
"""

from src.utils.nodes import *
from tests.utils import CodeGenerator


def _run(ast: Program, expected: str, input_data: str = "") -> None:
    result = CodeGenerator().generate_and_run(ast, input_data)
    assert result == expected, f"Expected '{expected}', got '{result}'"


# ---------------------------------------------------------------------------
# Helper: wrap statements in a void main() function
# ---------------------------------------------------------------------------
def _main(*stmts) -> Program:
    return Program([FuncDecl(VoidType(), "main", [], BlockStmt(list(stmts)))])


# ===========================================================================
# Tests 001 – 010  (unchanged — kept as originally written)
# ===========================================================================

def test_001():
    """Test 1: Hello World - print string"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printString", [StringLiteral("Hello World")]))
        ]))
    ])
    _run(ast, "Hello World")


def test_002():
    """Test 2: Print integer"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [IntLiteral(42)]))
        ]))
    ])
    _run(ast, "42")


def test_003():
    """Test 3: Print float"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printFloat", [FloatLiteral(3.14)]))
        ]))
    ])
    _run(ast, "3.14")


def test_004():
    """Test 4: Variable declaration and assignment"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "x", IntLiteral(10)),
            ExprStmt(FuncCall("printInt", [Identifier("x")]))
        ]))
    ])
    _run(ast, "10")


def test_005():
    """Test 5: Binary operation - addition"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [
                BinaryOp(IntLiteral(5), "+", IntLiteral(3))
            ]))
        ]))
    ])
    _run(ast, "8")


def test_006():
    """Test 6: Binary operation - multiplication"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [
                BinaryOp(IntLiteral(6), "*", IntLiteral(7))
            ]))
        ]))
    ])
    _run(ast, "42")


def test_007():
    """Test 7: If statement"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            IfStmt(
                BinaryOp(IntLiteral(1), "<", IntLiteral(2)),
                ExprStmt(FuncCall("printString", [StringLiteral("yes")])),
                ExprStmt(FuncCall("printString", [StringLiteral("no")]))
            )
        ]))
    ])
    _run(ast, "yes")


def test_008():
    """Test 8: While loop"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "i", IntLiteral(0)),
            WhileStmt(
                BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                BlockStmt([
                    ExprStmt(FuncCall("printInt", [Identifier("i")])),
                    ExprStmt(AssignExpr(
                        Identifier("i"),
                        BinaryOp(Identifier("i"), "+", IntLiteral(1))
                    ))
                ])
            )
        ]))
    ])
    _run(ast, "012")


def test_009():
    """Test 9: Function call with return value"""
    ast = Program([
        FuncDecl(
            IntType(), "add",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [
                FuncCall("add", [IntLiteral(20), IntLiteral(22)])
            ]))
        ]))
    ])
    _run(ast, "42")


def test_010():
    """Test 10: Multiple statements - arithmetic operations"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "x", IntLiteral(10)),
            VarDecl(IntType(), "y", IntLiteral(20)),
            ExprStmt(FuncCall("printInt", [
                BinaryOp(Identifier("x"), "+", Identifier("y"))
            ]))
        ]))
    ])
    _run(ast, "30")


# ===========================================================================
# Batch 1: Expressions & Control Flow (011 – 060)
# ===========================================================================

def test_011_operator_precedence():
    # 2 + 3 * 4  →  2 + (3*4)  →  14
    ast = _main(
        ExprStmt(FuncCall("printInt", [
            BinaryOp(IntLiteral(2), "+", BinaryOp(IntLiteral(3), "*", IntLiteral(4)))
        ]))
    )
    _run(ast, "14")


def test_012_operator_precedence_complex():
    # (2+3) * (10/2) % 7  →  5 * 5 % 7  →  25 % 7  →  4
    ast = _main(
        ExprStmt(FuncCall("printInt", [
            BinaryOp(
                BinaryOp(
                    BinaryOp(IntLiteral(2), "+", IntLiteral(3)),
                    "*",
                    BinaryOp(IntLiteral(10), "/", IntLiteral(2))
                ),
                "%",
                IntLiteral(7)
            )
        ]))
    )
    _run(ast, "4")


def test_013_float_promotion_add():
    # 2 + 3.5  →  5.5  (int promoted to float)
    ast = _main(
        ExprStmt(FuncCall("printFloat", [
            BinaryOp(IntLiteral(2), "+", FloatLiteral(3.5))
        ]))
    )
    _run(ast, "5.5")


def test_014_float_promotion_mul():
    # 10 * 0.5  →  5.0
    ast = _main(
        ExprStmt(FuncCall("printFloat", [
            BinaryOp(IntLiteral(10), "*", FloatLiteral(0.5))
        ]))
    )
    _run(ast, "5.0")


def test_015_logical_short_circuit_and():
    # 0 && side()  →  short-circuits, side() is never called → prints "no"
    ast = Program([
        FuncDecl(
            IntType(), "side", [],
            BlockStmt([
                ExprStmt(FuncCall("printString", [StringLiteral("side")])),
                ReturnStmt(IntLiteral(1))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            IfStmt(
                BinaryOp(IntLiteral(0), "&&", FuncCall("side", [])),
                BlockStmt([]),
                ExprStmt(FuncCall("printString", [StringLiteral("no")]))
            )
        ]))
    ])
    _run(ast, "no")


def test_016_logical_short_circuit_or():
    # 1 || side()  →  short-circuits, side() never called → prints "yes"
    ast = Program([
        FuncDecl(
            IntType(), "side", [],
            BlockStmt([
                ExprStmt(FuncCall("printString", [StringLiteral("side")])),
                ReturnStmt(IntLiteral(1))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            IfStmt(
                BinaryOp(IntLiteral(1), "||", FuncCall("side", [])),
                ExprStmt(FuncCall("printString", [StringLiteral("yes")])),
                None
            )
        ]))
    ])
    _run(ast, "yes")


def test_017_unary_ops():
    # -(-x) where x=10  →  10
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(10)),
        ExprStmt(FuncCall("printInt", [
            PrefixOp("-", PrefixOp("-", Identifier("x")))
        ]))
    )
    _run(ast, "10")


def test_018_prefix_inc_dec():
    # x=5, ++x → 6, --x → 5
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(FuncCall("printInt", [PrefixOp("++", Identifier("x"))])),
        ExprStmt(FuncCall("printInt", [PrefixOp("--", Identifier("x"))]))
    )
    _run(ast, "65")


def test_019_postfix_inc_dec():
    # x=5, x++ prints 5 (old), x-- prints 6 (old), x prints 5
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(FuncCall("printInt", [PostfixOp("++", Identifier("x"))])),
        ExprStmt(FuncCall("printInt", [PostfixOp("--", Identifier("x"))])),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    )
    _run(ast, "565")


def test_020_complex_assignment():
    # x = y = 42  →  prints 42 42
    ast = _main(
        VarDecl(IntType(), "x", None),
        VarDecl(IntType(), "y", None),
        ExprStmt(AssignExpr(
            Identifier("x"),
            AssignExpr(Identifier("y"), IntLiteral(42))
        )),
        ExprStmt(FuncCall("printInt", [Identifier("x")])),
        ExprStmt(FuncCall("printInt", [Identifier("y")]))
    )
    _run(ast, "4242")


def test_021_nested_if():
    # if x>5: if y>15: A else B  else C  →  A
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(10)),
        VarDecl(IntType(), "y", IntLiteral(20)),
        IfStmt(
            BinaryOp(Identifier("x"), ">", IntLiteral(5)),
            IfStmt(
                BinaryOp(Identifier("y"), ">", IntLiteral(15)),
                ExprStmt(FuncCall("printString", [StringLiteral("A")])),
                ExprStmt(FuncCall("printString", [StringLiteral("B")]))
            ),
            ExprStmt(FuncCall("printString", [StringLiteral("C")]))
        )
    )
    _run(ast, "A")


def test_022_nested_while():
    # i∈[0,2), j∈[0,2): print i,j  →  00011011
    ast = _main(
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(
            BinaryOp(Identifier("i"), "<", IntLiteral(2)),
            BlockStmt([
                VarDecl(IntType(), "j", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("j"), "<", IntLiteral(2)),
                    BlockStmt([
                        ExprStmt(FuncCall("printInt", [Identifier("i")])),
                        ExprStmt(FuncCall("printInt", [Identifier("j")])),
                        ExprStmt(PostfixOp("++", Identifier("j")))
                    ])
                ),
                ExprStmt(PostfixOp("++", Identifier("i")))
            ])
        )
    )
    _run(ast, "00011011")


def test_023_for_loop_break():
    # for i=0; i<10; i++: if i==3 break; print i  →  012
    ast = _main(
        ForStmt(
            VarDecl(IntType(), "i", IntLiteral(0)),
            BinaryOp(Identifier("i"), "<", IntLiteral(10)),
            PostfixOp("++", Identifier("i")),
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("i"), "==", IntLiteral(3)),
                    BreakStmt(),
                    None
                ),
                ExprStmt(FuncCall("printInt", [Identifier("i")]))
            ])
        )
    )
    _run(ast, "012")


def test_024_for_loop_continue():
    # for i=0; i<5; i++: if i==2 continue; print i  →  0134
    ast = _main(
        ForStmt(
            VarDecl(IntType(), "i", IntLiteral(0)),
            BinaryOp(Identifier("i"), "<", IntLiteral(5)),
            PostfixOp("++", Identifier("i")),
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("i"), "==", IntLiteral(2)),
                    ContinueStmt(),
                    None
                ),
                ExprStmt(FuncCall("printInt", [Identifier("i")]))
            ])
        )
    )
    _run(ast, "0134")


def test_025_nested_loop_mixed_break():
    # for i∈[0,2): while j<5: if j==2 break; print i,j; j++  →  00011011
    ast = _main(
        ForStmt(
            VarDecl(IntType(), "i", IntLiteral(0)),
            BinaryOp(Identifier("i"), "<", IntLiteral(2)),
            PostfixOp("++", Identifier("i")),
            BlockStmt([
                VarDecl(IntType(), "j", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("j"), "<", IntLiteral(5)),
                    BlockStmt([
                        IfStmt(
                            BinaryOp(Identifier("j"), "==", IntLiteral(2)),
                            BreakStmt(),
                            None
                        ),
                        ExprStmt(FuncCall("printInt", [Identifier("i")])),
                        ExprStmt(FuncCall("printInt", [Identifier("j")])),
                        ExprStmt(PostfixOp("++", Identifier("j")))
                    ])
                )
            ])
        )
    )
    _run(ast, "00011011")


def test_026_switch_fallthrough():
    # x=1, case 1: print "1", case 2: print "2" break  →  "12"
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(1)),
        SwitchStmt(
            Identifier("x"),
            [
                CaseStmt(IntLiteral(1), [
                    ExprStmt(FuncCall("printString", [StringLiteral("1")]))
                ]),
                CaseStmt(IntLiteral(2), [
                    ExprStmt(FuncCall("printString", [StringLiteral("2")])),
                    BreakStmt()
                ]),
            ],
            DefaultStmt([ExprStmt(FuncCall("printString", [StringLiteral("D")]))])
        )
    )
    _run(ast, "12")


def test_027_switch_default_only():
    # switch(10): default: print "def"
    ast = _main(
        SwitchStmt(
            IntLiteral(10),
            [],
            DefaultStmt([ExprStmt(FuncCall("printString", [StringLiteral("def")]))])
        )
    )
    _run(ast, "def")


def test_028_switch_nested():
    # x=1,y=2: switch x: case 1: switch y: case 2: print "inner" break; break  →  "inner"
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(1)),
        VarDecl(IntType(), "y", IntLiteral(2)),
        SwitchStmt(
            Identifier("x"),
            [
                CaseStmt(IntLiteral(1), [
                    SwitchStmt(
                        Identifier("y"),
                        [
                            CaseStmt(IntLiteral(2), [
                                ExprStmt(FuncCall("printString", [StringLiteral("inner")])),
                                BreakStmt()
                            ])
                        ],
                        None
                    ),
                    BreakStmt()
                ])
            ],
            None
        )
    )
    _run(ast, "inner")


def test_029_recursion_factorial():
    # fact(5) = 120
    ast = Program([
        FuncDecl(
            IntType(), "fact",
            [Param(IntType(), "n")],
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("n"), "<=", IntLiteral(1)),
                    ReturnStmt(IntLiteral(1)),
                    None
                ),
                ReturnStmt(BinaryOp(
                    Identifier("n"), "*",
                    FuncCall("fact", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])
                ))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("fact", [IntLiteral(5)])]))
        ]))
    ])
    _run(ast, "120")


def test_030_recursion_fibonacci():
    # fib(7) = 13
    ast = Program([
        FuncDecl(
            IntType(), "fib",
            [Param(IntType(), "n")],
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("n"), "<=", IntLiteral(1)),
                    ReturnStmt(Identifier("n")),
                    None
                ),
                ReturnStmt(BinaryOp(
                    FuncCall("fib", [BinaryOp(Identifier("n"), "-", IntLiteral(1))]),
                    "+",
                    FuncCall("fib", [BinaryOp(Identifier("n"), "-", IntLiteral(2))])
                ))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("fib", [IntLiteral(7)])]))
        ]))
    ])
    _run(ast, "13")


def test_031_struct_simple():
    # struct Point{x,y}; p={10,20}; print p.x, p.y  →  1020
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p", StructLiteral([IntLiteral(10), IntLiteral(20)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "y")]))
        ]))
    ])
    _run(ast, "1020")


def test_032_struct_nested():
    # struct Point; struct Rect{p1,p2}; r={{1,2},{3,4}}; print r.p1.x, r.p2.y  →  14
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        StructDecl("Rect", [
            MemberDecl(StructType("Point"), "p1"),
            MemberDecl(StructType("Point"), "p2")
        ]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Rect"), "r", StructLiteral([
                StructLiteral([IntLiteral(1), IntLiteral(2)]),
                StructLiteral([IntLiteral(3), IntLiteral(4)])
            ])),
            ExprStmt(FuncCall("printInt", [
                MemberAccess(MemberAccess(Identifier("r"), "p1"), "x")
            ])),
            ExprStmt(FuncCall("printInt", [
                MemberAccess(MemberAccess(Identifier("r"), "p2"), "y")
            ]))
        ]))
    ])
    _run(ast, "14")


def test_033_struct_assignment():
    # p1={1,2}; p2; p2=p1; print p2.x, p2.y  →  12
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p1", StructLiteral([IntLiteral(1), IntLiteral(2)])),
            VarDecl(StructType("Point"), "p2", None),
            ExprStmt(AssignExpr(Identifier("p2"), Identifier("p1"))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p2"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p2"), "y")]))
        ]))
    ])
    _run(ast, "12")


def test_034_function_returning_struct():
    # makePoint(42,43) returns Point{42,43}; print p.x, p.y  →  4243
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(
            StructType("Point"), "makePoint",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([
                VarDecl(StructType("Point"), "p", StructLiteral([Identifier("a"), Identifier("b")])),
                ReturnStmt(Identifier("p"))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p",
                    FuncCall("makePoint", [IntLiteral(42), IntLiteral(43)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "y")]))
        ]))
    ])
    _run(ast, "4243")


def test_035_auto_inference_complex():
    # auto x = 10+20=30; auto y = x*1.5=45.0
    ast = _main(
        VarDecl(None, "x", BinaryOp(IntLiteral(10), "+", IntLiteral(20))),
        VarDecl(None, "y", BinaryOp(Identifier("x"), "*", FloatLiteral(1.5))),
        ExprStmt(FuncCall("printFloat", [Identifier("y")]))
    )
    _run(ast, "45.0")


def test_036_scope_shadowing():
    # x=1; {x=2; print x} print x  →  21
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(1)),
        BlockStmt([
            VarDecl(IntType(), "x", IntLiteral(2)),
            ExprStmt(FuncCall("printInt", [Identifier("x")]))
        ]),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    )
    _run(ast, "21")


def test_037_many_params():
    # sum of 6 params: 1+2+3+4+5+6 = 21
    ast = Program([
        FuncDecl(
            VoidType(), "test",
            [Param(IntType(), p) for p in ["a", "b", "c", "d", "e", "f"]],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(
                        BinaryOp(
                            BinaryOp(
                                BinaryOp(
                                    BinaryOp(Identifier("a"), "+", Identifier("b")),
                                    "+", Identifier("c")
                                ),
                                "+", Identifier("d")
                            ),
                            "+", Identifier("e")
                        ),
                        "+", Identifier("f")
                    )
                ]))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("test", [
                IntLiteral(1), IntLiteral(2), IntLiteral(3),
                IntLiteral(4), IntLiteral(5), IntLiteral(6)
            ]))
        ]))
    ])
    _run(ast, "21")


def test_038_mutual_recursion():
    # isEven(4)=1, isOdd(4)=0
    ast = Program([
        FuncDecl(
            IntType(), "isOdd",
            [Param(IntType(), "n")],
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("n"), "==", IntLiteral(0)),
                    ReturnStmt(IntLiteral(0)), None
                ),
                ReturnStmt(FuncCall("isEven", [BinaryOp(Identifier("n"), "-", IntLiteral(1))]))
            ])
        ),
        FuncDecl(
            IntType(), "isEven",
            [Param(IntType(), "n")],
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("n"), "==", IntLiteral(0)),
                    ReturnStmt(IntLiteral(1)), None
                ),
                ReturnStmt(FuncCall("isOdd", [BinaryOp(Identifier("n"), "-", IntLiteral(1))]))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("isEven", [IntLiteral(4)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("isOdd", [IntLiteral(4)])]))
        ]))
    ])
    _run(ast, "10")


def test_039_complex_condition():
    # (x<15 && y>15) || (x==0) with x=10,y=20  →  "ok"
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(10)),
        VarDecl(IntType(), "y", IntLiteral(20)),
        IfStmt(
            BinaryOp(
                BinaryOp(
                    BinaryOp(Identifier("x"), "<", IntLiteral(15)),
                    "&&",
                    BinaryOp(Identifier("y"), ">", IntLiteral(15))
                ),
                "||",
                BinaryOp(Identifier("x"), "==", IntLiteral(0))
            ),
            ExprStmt(FuncCall("printString", [StringLiteral("ok")])),
            None
        )
    )
    _run(ast, "ok")


def test_040_while_true_break():
    # while(1): if i==5 break; i++  →  i=5
    ast = _main(
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(
            IntLiteral(1),
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("i"), "==", IntLiteral(5)),
                    BreakStmt(), None
                ),
                ExprStmt(PostfixOp("++", Identifier("i")))
            ])
        ),
        ExprStmt(FuncCall("printInt", [Identifier("i")]))
    )
    _run(ast, "5")


def test_041_for_no_init_cond_update():
    # for(;;): if i==3 break; print i; i++  →  012
    ast = _main(
        VarDecl(IntType(), "i", IntLiteral(0)),
        ForStmt(
            None, None, None,
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("i"), "==", IntLiteral(3)),
                    BreakStmt(), None
                ),
                ExprStmt(FuncCall("printInt", [Identifier("i")])),
                ExprStmt(PostfixOp("++", Identifier("i")))
            ])
        )
    )
    _run(ast, "012")


def test_042_postfix_inc_in_expr():
    # x=5; y = x++ + 1 = 5+1=6; x is now 6
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(5)),
        VarDecl(IntType(), "y",
                BinaryOp(PostfixOp("++", Identifier("x")), "+", IntLiteral(1))),
        ExprStmt(FuncCall("printInt", [Identifier("x")])),
        ExprStmt(FuncCall("printInt", [Identifier("y")]))
    )
    _run(ast, "66")


def test_043_prefix_inc_in_expr():
    # x=5; y = ++x + 1 = 6+1=7; x is now 6
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(5)),
        VarDecl(IntType(), "y",
                BinaryOp(PrefixOp("++", Identifier("x")), "+", IntLiteral(1))),
        ExprStmt(FuncCall("printInt", [Identifier("x")])),
        ExprStmt(FuncCall("printInt", [Identifier("y")]))
    )
    _run(ast, "67")


def test_044_modulus_op():
    # 10%3=1,  -10%3=-1
    ast = _main(
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(10), "%", IntLiteral(3))])),
        ExprStmt(FuncCall("printInt", [
            BinaryOp(PrefixOp("-", IntLiteral(10)), "%", IntLiteral(3))
        ]))
    )
    _run(ast, "1-1")


def test_045_float_division():
    # 10.0 / 4.0 = 2.5
    ast = _main(
        ExprStmt(FuncCall("printFloat", [
            BinaryOp(FloatLiteral(10.0), "/", FloatLiteral(4.0))
        ]))
    )
    _run(ast, "2.5")


def test_046_int_division():
    # 10 / 4 = 2  (integer division)
    ast = _main(
        ExprStmt(FuncCall("printInt", [
            BinaryOp(IntLiteral(10), "/", IntLiteral(4))
        ]))
    )
    _run(ast, "2")


def test_047_chained_relational():
    # (1 < 2) < 3  →  1 < 3  →  1
    ast = _main(
        ExprStmt(FuncCall("printInt", [
            BinaryOp(
                BinaryOp(IntLiteral(1), "<", IntLiteral(2)),
                "<",
                IntLiteral(3)
            )
        ]))
    )
    _run(ast, "1")


def test_048_string_escape_sequences():
    # "a\nb\tt"  →  a newline b tab t
    ast = _main(
        ExprStmt(FuncCall("printString", [StringLiteral("a\nb\tt")]))
    )
    _run(ast, "a\nb\tt")


def test_049_empty_function():
    # nop() does nothing; print "done"
    ast = Program([
        FuncDecl(VoidType(), "nop", [], BlockStmt([])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("nop", [])),
            ExprStmt(FuncCall("printString", [StringLiteral("done")]))
        ]))
    ])
    _run(ast, "done")


def test_050_nested_struct_access_in_assign():
    # struct A{x}; struct B{a}; B b; b.a.x=100; print b.a.x  →  100
    ast = Program([
        StructDecl("A", [MemberDecl(IntType(), "x")]),
        StructDecl("B", [MemberDecl(StructType("A"), "a")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("B"), "b", None),
            ExprStmt(AssignExpr(
                MemberAccess(MemberAccess(Identifier("b"), "a"), "x"),
                IntLiteral(100)
            )),
            ExprStmt(FuncCall("printInt", [
                MemberAccess(MemberAccess(Identifier("b"), "a"), "x")
            ]))
        ]))
    ])
    _run(ast, "100")


def test_051_gcd_recursive():
    # gcd(48,18) = 6
    ast = Program([
        FuncDecl(
            IntType(), "gcd",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("b"), "==", IntLiteral(0)),
                    ReturnStmt(Identifier("a")), None
                ),
                ReturnStmt(FuncCall("gcd", [
                    Identifier("b"),
                    BinaryOp(Identifier("a"), "%", Identifier("b"))
                ]))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [
                FuncCall("gcd", [IntLiteral(48), IntLiteral(18)])
            ]))
        ]))
    ])
    _run(ast, "6")


def test_052_power_function():
    # 2^10 = 1024
    ast = Program([
        FuncDecl(
            IntType(), "power",
            [Param(IntType(), "base"), Param(IntType(), "exp")],
            BlockStmt([
                VarDecl(IntType(), "res", IntLiteral(1)),
                WhileStmt(
                    BinaryOp(Identifier("exp"), ">", IntLiteral(0)),
                    BlockStmt([
                        ExprStmt(AssignExpr(
                            Identifier("res"),
                            BinaryOp(Identifier("res"), "*", Identifier("base"))
                        )),
                        ExprStmt(PostfixOp("--", Identifier("exp")))
                    ])
                ),
                ReturnStmt(Identifier("res"))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [
                FuncCall("power", [IntLiteral(2), IntLiteral(10)])
            ]))
        ]))
    ])
    _run(ast, "1024")


def test_053_prime_check():
    # primes in [1,10] = 2,3,5,7
    ast = Program([
        FuncDecl(
            IntType(), "isPrime",
            [Param(IntType(), "n")],
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("n"), "<", IntLiteral(2)),
                    ReturnStmt(IntLiteral(0)), None
                ),
                ForStmt(
                    VarDecl(IntType(), "i", IntLiteral(2)),
                    BinaryOp(
                        BinaryOp(Identifier("i"), "*", Identifier("i")),
                        "<=", Identifier("n")
                    ),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([
                        IfStmt(
                            BinaryOp(
                                BinaryOp(Identifier("n"), "%", Identifier("i")),
                                "==", IntLiteral(0)
                            ),
                            ReturnStmt(IntLiteral(0)), None
                        )
                    ])
                ),
                ReturnStmt(IntLiteral(1))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ForStmt(
                VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(10)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    IfStmt(
                        FuncCall("isPrime", [Identifier("i")]),
                        ExprStmt(FuncCall("printInt", [Identifier("i")])),
                        None
                    )
                ])
            )
        ]))
    ])
    _run(ast, "2357")


def test_054_bubble_sort_simplified():
    # sort a=4,b=3,c=2,d=1 → 1234
    ast = _main(
        VarDecl(IntType(), "a", IntLiteral(4)),
        VarDecl(IntType(), "b", IntLiteral(3)),
        VarDecl(IntType(), "c", IntLiteral(2)),
        VarDecl(IntType(), "d", IntLiteral(1)),
        ForStmt(
            VarDecl(IntType(), "i", IntLiteral(0)),
            BinaryOp(Identifier("i"), "<", IntLiteral(4)),
            PostfixOp("++", Identifier("i")),
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("a"), ">", Identifier("b")),
                    BlockStmt([
                        VarDecl(IntType(), "t", Identifier("a")),
                        ExprStmt(AssignExpr(Identifier("a"), Identifier("b"))),
                        ExprStmt(AssignExpr(Identifier("b"), Identifier("t")))
                    ]), None
                ),
                IfStmt(
                    BinaryOp(Identifier("b"), ">", Identifier("c")),
                    BlockStmt([
                        VarDecl(IntType(), "t", Identifier("b")),
                        ExprStmt(AssignExpr(Identifier("b"), Identifier("c"))),
                        ExprStmt(AssignExpr(Identifier("c"), Identifier("t")))
                    ]), None
                ),
                IfStmt(
                    BinaryOp(Identifier("c"), ">", Identifier("d")),
                    BlockStmt([
                        VarDecl(IntType(), "t", Identifier("c")),
                        ExprStmt(AssignExpr(Identifier("c"), Identifier("d"))),
                        ExprStmt(AssignExpr(Identifier("d"), Identifier("t")))
                    ]), None
                ),
            ])
        ),
        ExprStmt(FuncCall("printInt", [Identifier("a")])),
        ExprStmt(FuncCall("printInt", [Identifier("b")])),
        ExprStmt(FuncCall("printInt", [Identifier("c")])),
        ExprStmt(FuncCall("printInt", [Identifier("d")]))
    )
    _run(ast, "1234")


def test_055_nested_ternary_logic():
    # x=10: if x>5: if x<15: res=1 else res=2  else res=3  →  1
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(10)),
        VarDecl(IntType(), "res", IntLiteral(0)),
        IfStmt(
            BinaryOp(Identifier("x"), ">", IntLiteral(5)),
            IfStmt(
                BinaryOp(Identifier("x"), "<", IntLiteral(15)),
                ExprStmt(AssignExpr(Identifier("res"), IntLiteral(1))),
                ExprStmt(AssignExpr(Identifier("res"), IntLiteral(2)))
            ),
            ExprStmt(AssignExpr(Identifier("res"), IntLiteral(3)))
        ),
        ExprStmt(FuncCall("printInt", [Identifier("res")]))
    )
    _run(ast, "1")


def test_056_auto_inference_from_assignment():
    # auto x; x=42; print x
    ast = _main(
        VarDecl(None, "x", None),
        ExprStmt(AssignExpr(Identifier("x"), IntLiteral(42))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    )
    _run(ast, "42")


def test_057_return_in_middle_of_loop():
    # find(5)=5, find(15)=-1
    ast = Program([
        FuncDecl(
            IntType(), "find",
            [Param(IntType(), "n")],
            BlockStmt([
                ForStmt(
                    VarDecl(IntType(), "i", IntLiteral(0)),
                    BinaryOp(Identifier("i"), "<", IntLiteral(10)),
                    PostfixOp("++", Identifier("i")),
                    BlockStmt([
                        IfStmt(
                            BinaryOp(Identifier("i"), "==", Identifier("n")),
                            ReturnStmt(Identifier("i")), None
                        )
                    ])
                ),
                ReturnStmt(PrefixOp("-", IntLiteral(1)))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("find", [IntLiteral(5)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("find", [IntLiteral(15)])]))
        ]))
    ])
    _run(ast, "5-1")


def test_058_many_args_recursion():
    # sum(10,0,0,0) = 10
    ast = Program([
        FuncDecl(
            IntType(), "sum",
            [Param(IntType(), p) for p in ["a", "b", "c", "d"]],
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("a"), "==", IntLiteral(0)),
                    ReturnStmt(BinaryOp(
                        BinaryOp(Identifier("b"), "+", Identifier("c")),
                        "+", Identifier("d")
                    )),
                    None
                ),
                ReturnStmt(FuncCall("sum", [
                    BinaryOp(Identifier("a"), "-", IntLiteral(1)),
                    BinaryOp(Identifier("b"), "+", IntLiteral(1)),
                    Identifier("c"),
                    Identifier("d")
                ]))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [
                FuncCall("sum", [IntLiteral(10), IntLiteral(0), IntLiteral(0), IntLiteral(0)])
            ]))
        ]))
    ])
    _run(ast, "10")


def test_059_struct_member_as_arg():
    # s={42}; test(s.x)  →  42
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "x")]),
        FuncDecl(
            VoidType(), "test",
            [Param(IntType(), "n")],
            BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("n")]))])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "s", StructLiteral([IntLiteral(42)])),
            ExprStmt(FuncCall("test", [MemberAccess(Identifier("s"), "x")]))
        ]))
    ])
    _run(ast, "42")


def test_060_switch_with_expression():
    # switch(x+1) where x=5: case 6: "six"  →  "six"
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(5)),
        SwitchStmt(
            BinaryOp(Identifier("x"), "+", IntLiteral(1)),
            [
                CaseStmt(IntLiteral(6), [
                    ExprStmt(FuncCall("printString", [StringLiteral("six")])),
                    BreakStmt()
                ])
            ],
            DefaultStmt([ExprStmt(FuncCall("printString", [StringLiteral("other")]))])
        )
    )
    _run(ast, "six")


# ===========================================================================
# Batch 2: Advanced Scenarios & Algorithms (061 – 110)
# ===========================================================================

def test_061_struct_literal_in_return():
    # getOrigin() returns {0,0}; print p.x, p.y  →  00
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(
            StructType("Point"), "getOrigin", [],
            BlockStmt([ReturnStmt(StructLiteral([IntLiteral(0), IntLiteral(0)]))])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p", FuncCall("getOrigin", [])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "y")]))
        ]))
    ])
    _run(ast, "00")


def test_062_nested_struct_literal_init():
    # struct Dim{w,h}; struct Rect{x,y,size}; r={0,0,{100,200}}; print r.size.w, r.size.h
    ast = Program([
        StructDecl("Dim", [MemberDecl(IntType(), "w"), MemberDecl(IntType(), "h")]),
        StructDecl("Rect", [
            MemberDecl(IntType(), "x"),
            MemberDecl(IntType(), "y"),
            MemberDecl(StructType("Dim"), "size")
        ]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Rect"), "r", StructLiteral([
                IntLiteral(0),
                IntLiteral(0),
                StructLiteral([IntLiteral(100), IntLiteral(200)])
            ])),
            ExprStmt(FuncCall("printInt", [
                MemberAccess(MemberAccess(Identifier("r"), "size"), "w")
            ])),
            ExprStmt(FuncCall("printInt", [
                MemberAccess(MemberAccess(Identifier("r"), "size"), "h")
            ]))
        ]))
    ])
    _run(ast, "100200")


def test_063_struct_member_assignment_chain():
    # S s1; S s2; s1.x = s2.x = 42; print s1.x, s2.x  →  4242
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "x")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "s1", None),
            VarDecl(StructType("S"), "s2", None),
            ExprStmt(AssignExpr(
                MemberAccess(Identifier("s1"), "x"),
                AssignExpr(MemberAccess(Identifier("s2"), "x"), IntLiteral(42))
            )),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s1"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s2"), "x")]))
        ]))
    ])
    _run(ast, "4242")


def test_064_recursive_struct_like_traversal():
    # n1={1}; n2={2}; print n1.val,n2.val; n1=n2; print n1.val  →  122
    ast = Program([
        StructDecl("Node", [MemberDecl(IntType(), "val")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Node"), "n1", StructLiteral([IntLiteral(1)])),
            VarDecl(StructType("Node"), "n2", StructLiteral([IntLiteral(2)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("n1"), "val")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("n2"), "val")])),
            ExprStmt(AssignExpr(Identifier("n1"), Identifier("n2"))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("n1"), "val")]))
        ]))
    ])
    _run(ast, "122")


def test_065_auto_in_for_init():
    # for(auto i=0.5; i<3.0; i=i+1.0): print i  →  0.51.52.5
    ast = _main(
        ForStmt(
            VarDecl(None, "i", FloatLiteral(0.5)),
            BinaryOp(Identifier("i"), "<", FloatLiteral(3.0)),
            AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "+", FloatLiteral(1.0))),
            BlockStmt([ExprStmt(FuncCall("printFloat", [Identifier("i")]))])
        )
    )
    _run(ast, "0.51.52.5")


def test_066_auto_inferred_from_complex_return():
    # getVal(10) = 10*1.1 = 11.0; auto v = getVal(10); print v
    ast = Program([
        FuncDecl(
            FloatType(), "getVal",
            [Param(IntType(), "x")],
            BlockStmt([ReturnStmt(BinaryOp(Identifier("x"), "*", FloatLiteral(1.1)))])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(None, "v", FuncCall("getVal", [IntLiteral(10)])),
            ExprStmt(FuncCall("printFloat", [Identifier("v")]))
        ]))
    ])
    _run(ast, "11.0")


def test_067_logical_not_precedence():
    # !x==1 parsed as (!x)==1; x=0 → !0=1 → 1==1 → 1
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(0)),
        ExprStmt(FuncCall("printInt", [
            BinaryOp(PrefixOp("!", Identifier("x")), "==", IntLiteral(1))
        ]))
    )
    _run(ast, "1")


def test_068_logical_not_on_complex_expr():
    # !(x>y) where x=10,y=20  →  !(false)=1
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(10)),
        VarDecl(IntType(), "y", IntLiteral(20)),
        ExprStmt(FuncCall("printInt", [
            PrefixOp("!", BinaryOp(Identifier("x"), ">", Identifier("y")))
        ]))
    )
    _run(ast, "1")


def test_069_deeply_nested_if_else():
    # a=1,b=2,c=3: if a==1: if b==2: if c==4: "no" else "yes"  →  "yes"
    ast = _main(
        VarDecl(IntType(), "a", IntLiteral(1)),
        VarDecl(IntType(), "b", IntLiteral(2)),
        VarDecl(IntType(), "c", IntLiteral(3)),
        IfStmt(
            BinaryOp(Identifier("a"), "==", IntLiteral(1)),
            IfStmt(
                BinaryOp(Identifier("b"), "==", IntLiteral(2)),
                IfStmt(
                    BinaryOp(Identifier("c"), "==", IntLiteral(4)),
                    ExprStmt(FuncCall("printString", [StringLiteral("no")])),
                    ExprStmt(FuncCall("printString", [StringLiteral("yes")]))
                ),
                ExprStmt(FuncCall("printString", [StringLiteral("no")]))
            ),
            ExprStmt(FuncCall("printString", [StringLiteral("no")]))
        )
    )
    _run(ast, "yes")


def test_070_dangling_else():
    # if(1) if(0) "no" else "yes"  →  "yes"  (else binds to inner if)
    ast = _main(
        IfStmt(
            IntLiteral(1),
            IfStmt(
                IntLiteral(0),
                ExprStmt(FuncCall("printString", [StringLiteral("no")])),
                ExprStmt(FuncCall("printString", [StringLiteral("yes")]))
            ),
            None
        )
    )
    _run(ast, "yes")


def test_071_while_with_complex_condition():
    # while(i<5 && j>5): print i; i++; j--  →  01234
    ast = _main(
        VarDecl(IntType(), "i", IntLiteral(0)),
        VarDecl(IntType(), "j", IntLiteral(10)),
        WhileStmt(
            BinaryOp(
                BinaryOp(Identifier("i"), "<", IntLiteral(5)),
                "&&",
                BinaryOp(Identifier("j"), ">", IntLiteral(5))
            ),
            BlockStmt([
                ExprStmt(FuncCall("printInt", [Identifier("i")])),
                ExprStmt(PostfixOp("++", Identifier("i"))),
                ExprStmt(PostfixOp("--", Identifier("j")))
            ])
        )
    )
    _run(ast, "01234")


def test_072_for_with_empty_body():
    # int i; for(i=0; i<5; i++) {} print i  →  5
    ast = _main(
        VarDecl(IntType(), "i", None),
        ForStmt(
            ExprStmt(AssignExpr(Identifier("i"), IntLiteral(0))),
            BinaryOp(Identifier("i"), "<", IntLiteral(5)),
            PostfixOp("++", Identifier("i")),
            BlockStmt([])
        ),
        ExprStmt(FuncCall("printInt", [Identifier("i")]))
    )
    _run(ast, "5")


def test_073_break_in_switch_in_for():
    # for i∈[0,3): switch(i): case 1: break (switch only); default: print i; print "-"
    # →  "0--2-"
    ast = _main(
        ForStmt(
            VarDecl(IntType(), "i", IntLiteral(0)),
            BinaryOp(Identifier("i"), "<", IntLiteral(3)),
            PostfixOp("++", Identifier("i")),
            BlockStmt([
                SwitchStmt(
                    Identifier("i"),
                    [CaseStmt(IntLiteral(1), [BreakStmt()])],
                    DefaultStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))])
                ),
                ExprStmt(FuncCall("printString", [StringLiteral("-")]))
            ])
        )
    )
    _run(ast, "0--2-")


def test_074_continue_in_for_in_switch():
    # switch(1): case 1: for i∈[0,3): if i==1 continue; print i; break  →  02
    ast = _main(
        SwitchStmt(
            IntLiteral(1),
            [
                CaseStmt(IntLiteral(1), [
                    ForStmt(
                        VarDecl(IntType(), "i", IntLiteral(0)),
                        BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                        PostfixOp("++", Identifier("i")),
                        BlockStmt([
                            IfStmt(
                                BinaryOp(Identifier("i"), "==", IntLiteral(1)),
                                ContinueStmt(), None
                            ),
                            ExprStmt(FuncCall("printInt", [Identifier("i")]))
                        ])
                    ),
                    BreakStmt()
                ])
            ],
            None
        )
    )
    _run(ast, "02")


def test_075_nested_switch_fallthrough():
    # x=1,y=1: switch x: case 1: switch y: case 1: "A"; case 2: "B"; case 2: "C"
    # →  "ABC"  (fall-through in both inner and outer)
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(1)),
        VarDecl(IntType(), "y", IntLiteral(1)),
        SwitchStmt(
            Identifier("x"),
            [
                CaseStmt(IntLiteral(1), [
                    SwitchStmt(
                        Identifier("y"),
                        [
                            CaseStmt(IntLiteral(1), [
                                ExprStmt(FuncCall("printString", [StringLiteral("A")]))
                            ]),
                            CaseStmt(IntLiteral(2), [
                                ExprStmt(FuncCall("printString", [StringLiteral("B")]))
                            ])
                        ],
                        None
                    )
                ]),
                CaseStmt(IntLiteral(2), [
                    ExprStmt(FuncCall("printString", [StringLiteral("C")]))
                ])
            ],
            None
        )
    )
    _run(ast, "ABC")


def test_076_complex_switch_cases():
    # x=5: case 1,3,5 → "odd" break; case 2,4,6 → "even" break  →  "odd"
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(5)),
        SwitchStmt(
            Identifier("x"),
            [
                CaseStmt(IntLiteral(1), []),
                CaseStmt(IntLiteral(3), []),
                CaseStmt(IntLiteral(5), [
                    ExprStmt(FuncCall("printString", [StringLiteral("odd")])),
                    BreakStmt()
                ]),
                CaseStmt(IntLiteral(2), []),
                CaseStmt(IntLiteral(4), []),
                CaseStmt(IntLiteral(6), [
                    ExprStmt(FuncCall("printString", [StringLiteral("even")])),
                    BreakStmt()
                ]),
            ],
            None
        )
    )
    _run(ast, "odd")


def test_077_return_void_explicit():
    # test(-1) returns early; test(1) prints 1  →  "1"
    ast = Program([
        FuncDecl(
            VoidType(), "test",
            [Param(IntType(), "x")],
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("x"), "<", IntLiteral(0)),
                    ReturnStmt(None), None
                ),
                ExprStmt(FuncCall("printInt", [Identifier("x")]))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("test", [PrefixOp("-", IntLiteral(1))])),
            ExprStmt(FuncCall("test", [IntLiteral(1)]))
        ]))
    ])
    _run(ast, "1")


def test_078_shadowing_in_for_init():
    # i=100; for(int i=0; i<3; i++) print i; print i (outer=100)  →  012100
    ast = _main(
        VarDecl(IntType(), "i", IntLiteral(100)),
        ForStmt(
            VarDecl(IntType(), "i", IntLiteral(0)),
            BinaryOp(Identifier("i"), "<", IntLiteral(3)),
            PostfixOp("++", Identifier("i")),
            BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("i")]))])
        ),
        ExprStmt(FuncCall("printInt", [Identifier("i")]))
    )
    _run(ast, "012100")


def test_079_shadowing_in_while_block():
    # x=10; while(x>8): int x=1; print x; break; print x (outer=10)  →  110
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(10)),
        WhileStmt(
            BinaryOp(Identifier("x"), ">", IntLiteral(8)),
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(1)),
                ExprStmt(FuncCall("printInt", [Identifier("x")])),
                BreakStmt()
            ])
        ),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    )
    _run(ast, "110")


def test_080_complex_expression_stmt():
    # add(1,2) result discarded; print "ok"
    ast = Program([
        FuncDecl(
            IntType(), "add",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("add", [IntLiteral(1), IntLiteral(2)])),
            ExprStmt(FuncCall("printString", [StringLiteral("ok")]))
        ]))
    ])
    _run(ast, "ok")


def test_081_fibonacci_iterative():
    # fib(10) iterative = 55
    ast = _main(
        VarDecl(IntType(), "n", IntLiteral(10)),
        VarDecl(IntType(), "a", IntLiteral(0)),
        VarDecl(IntType(), "b", IntLiteral(1)),
        ForStmt(
            VarDecl(IntType(), "i", IntLiteral(0)),
            BinaryOp(Identifier("i"), "<", Identifier("n")),
            PostfixOp("++", Identifier("i")),
            BlockStmt([
                VarDecl(IntType(), "temp", Identifier("a")),
                ExprStmt(AssignExpr(Identifier("a"), Identifier("b"))),
                ExprStmt(AssignExpr(
                    Identifier("b"),
                    BinaryOp(Identifier("temp"), "+", Identifier("b"))
                ))
            ])
        ),
        ExprStmt(FuncCall("printInt", [Identifier("a")]))
    )
    _run(ast, "55")


def test_082_sum_of_digits():
    # sumDigits(12345) = 15
    ast = Program([
        FuncDecl(
            IntType(), "sumDigits",
            [Param(IntType(), "n")],
            BlockStmt([
                VarDecl(IntType(), "sum", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("n"), ">", IntLiteral(0)),
                    BlockStmt([
                        ExprStmt(AssignExpr(
                            Identifier("sum"),
                            BinaryOp(
                                Identifier("sum"), "+",
                                BinaryOp(Identifier("n"), "%", IntLiteral(10))
                            )
                        )),
                        ExprStmt(AssignExpr(
                            Identifier("n"),
                            BinaryOp(Identifier("n"), "/", IntLiteral(10))
                        ))
                    ])
                ),
                ReturnStmt(Identifier("sum"))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("sumDigits", [IntLiteral(12345)])]))
        ]))
    ])
    _run(ast, "15")


def test_083_reverse_integer():
    # reverse(1234) = 4321
    ast = Program([
        FuncDecl(
            IntType(), "reverse",
            [Param(IntType(), "n")],
            BlockStmt([
                VarDecl(IntType(), "rev", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("n"), ">", IntLiteral(0)),
                    BlockStmt([
                        ExprStmt(AssignExpr(
                            Identifier("rev"),
                            BinaryOp(
                                BinaryOp(Identifier("rev"), "*", IntLiteral(10)),
                                "+",
                                BinaryOp(Identifier("n"), "%", IntLiteral(10))
                            )
                        )),
                        ExprStmt(AssignExpr(
                            Identifier("n"),
                            BinaryOp(Identifier("n"), "/", IntLiteral(10))
                        ))
                    ])
                ),
                ReturnStmt(Identifier("rev"))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("reverse", [IntLiteral(1234)])]))
        ]))
    ])
    _run(ast, "4321")


def test_084_leap_year_check():
    # isLeap(2000)=1, isLeap(1900)=0, isLeap(2024)=1  →  101
    ast = Program([
        FuncDecl(
            IntType(), "isLeap",
            [Param(IntType(), "y")],
            BlockStmt([
                IfStmt(
                    BinaryOp(BinaryOp(Identifier("y"), "%", IntLiteral(400)), "==", IntLiteral(0)),
                    ReturnStmt(IntLiteral(1)), None
                ),
                IfStmt(
                    BinaryOp(BinaryOp(Identifier("y"), "%", IntLiteral(100)), "==", IntLiteral(0)),
                    ReturnStmt(IntLiteral(0)), None
                ),
                IfStmt(
                    BinaryOp(BinaryOp(Identifier("y"), "%", IntLiteral(4)), "==", IntLiteral(0)),
                    ReturnStmt(IntLiteral(1)), None
                ),
                ReturnStmt(IntLiteral(0))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("isLeap", [IntLiteral(2000)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("isLeap", [IntLiteral(1900)])])),
            ExprStmt(FuncCall("printInt", [FuncCall("isLeap", [IntLiteral(2024)])]))
        ]))
    ])
    _run(ast, "101")


def test_085_max_of_three():
    # max(10,30,20) = 30
    ast = Program([
        FuncDecl(
            IntType(), "max",
            [Param(IntType(), "a"), Param(IntType(), "b"), Param(IntType(), "c")],
            BlockStmt([
                IfStmt(
                    BinaryOp(
                        BinaryOp(Identifier("a"), ">=", Identifier("b")),
                        "&&",
                        BinaryOp(Identifier("a"), ">=", Identifier("c"))
                    ),
                    ReturnStmt(Identifier("a")), None
                ),
                IfStmt(
                    BinaryOp(
                        BinaryOp(Identifier("b"), ">=", Identifier("a")),
                        "&&",
                        BinaryOp(Identifier("b"), ">=", Identifier("c"))
                    ),
                    ReturnStmt(Identifier("b")), None
                ),
                ReturnStmt(Identifier("c"))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [
                FuncCall("max", [IntLiteral(10), IntLiteral(30), IntLiteral(20)])
            ]))
        ]))
    ])
    _run(ast, "30")


def test_086_nested_member_access_complex():
    # struct A{v}; struct B{a1,a2}; struct C{b}; c={{{10},{20}}}; print c.b.a1.v+c.b.a2.v
    ast = Program([
        StructDecl("A", [MemberDecl(IntType(), "v")]),
        StructDecl("B", [
            MemberDecl(StructType("A"), "a1"),
            MemberDecl(StructType("A"), "a2")
        ]),
        StructDecl("C", [MemberDecl(StructType("B"), "b")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("C"), "c", StructLiteral([
                StructLiteral([
                    StructLiteral([IntLiteral(10)]),
                    StructLiteral([IntLiteral(20)])
                ])
            ])),
            ExprStmt(FuncCall("printInt", [
                BinaryOp(
                    MemberAccess(MemberAccess(MemberAccess(Identifier("c"), "b"), "a1"), "v"),
                    "+",
                    MemberAccess(MemberAccess(MemberAccess(Identifier("c"), "b"), "a2"), "v")
                )
            ]))
        ]))
    ])
    _run(ast, "30")


def test_087_struct_literal_as_func_arg():
    # printP({100,200})  →  100200
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(
            VoidType(), "printP",
            [Param(StructType("Point"), "p")],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")])),
                ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "y")]))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printP", [StructLiteral([IntLiteral(100), IntLiteral(200)])]))
        ]))
    ])
    _run(ast, "100200")


def test_088_large_loop_stress():
    # sum of 1000 ones = 1000
    ast = _main(
        VarDecl(IntType(), "sum", IntLiteral(0)),
        ForStmt(
            VarDecl(IntType(), "i", IntLiteral(0)),
            BinaryOp(Identifier("i"), "<", IntLiteral(1000)),
            PostfixOp("++", Identifier("i")),
            ExprStmt(AssignExpr(
                Identifier("sum"),
                BinaryOp(Identifier("sum"), "+", IntLiteral(1))
            ))
        ),
        ExprStmt(FuncCall("printInt", [Identifier("sum")]))
    )
    _run(ast, "1000")


def test_089_nested_loops_many_levels():
    # 3×3×3 = 27
    ast = _main(
        VarDecl(IntType(), "count", IntLiteral(0)),
        ForStmt(
            VarDecl(IntType(), "i", IntLiteral(0)),
            BinaryOp(Identifier("i"), "<", IntLiteral(3)),
            PostfixOp("++", Identifier("i")),
            ForStmt(
                VarDecl(IntType(), "j", IntLiteral(0)),
                BinaryOp(Identifier("j"), "<", IntLiteral(3)),
                PostfixOp("++", Identifier("j")),
                ForStmt(
                    VarDecl(IntType(), "k", IntLiteral(0)),
                    BinaryOp(Identifier("k"), "<", IntLiteral(3)),
                    PostfixOp("++", Identifier("k")),
                    ExprStmt(PostfixOp("++", Identifier("count")))
                )
            )
        ),
        ExprStmt(FuncCall("printInt", [Identifier("count")]))
    )
    _run(ast, "27")


def test_090_switch_with_negative_cases():
    # x=-1: case -1 → "neg"; case 1 → "pos"; default → "zero"  →  "neg"
    ast = _main(
        VarDecl(IntType(), "x", PrefixOp("-", IntLiteral(1))),
        SwitchStmt(
            Identifier("x"),
            [
                CaseStmt(PrefixOp("-", IntLiteral(1)), [
                    ExprStmt(FuncCall("printString", [StringLiteral("neg")])),
                    BreakStmt()
                ]),
                CaseStmt(IntLiteral(1), [
                    ExprStmt(FuncCall("printString", [StringLiteral("pos")])),
                    BreakStmt()
                ])
            ],
            DefaultStmt([ExprStmt(FuncCall("printString", [StringLiteral("zero")]))])
        )
    )
    _run(ast, "neg")


def test_091_auto_in_nested_expr():
    # auto x=10; auto y=(x=20)+5=25; print x,y  →  2025
    ast = _main(
        VarDecl(None, "x", IntLiteral(10)),
        VarDecl(None, "y",
                BinaryOp(AssignExpr(Identifier("x"), IntLiteral(20)), "+", IntLiteral(5))),
        ExprStmt(FuncCall("printInt", [Identifier("x")])),
        ExprStmt(FuncCall("printInt", [Identifier("y")]))
    )
    _run(ast, "2025")


def test_092_float_unary_minus():
    # -3.14
    ast = _main(
        ExprStmt(FuncCall("printFloat", [PrefixOp("-", FloatLiteral(3.14))]))
    )
    _run(ast, "-3.14")


def test_093_complex_boolean_logic():
    # (a&&b)||(a&&c) where a=1,b=0,c=1  →  "yes"
    ast = _main(
        VarDecl(IntType(), "a", IntLiteral(1)),
        VarDecl(IntType(), "b", IntLiteral(0)),
        VarDecl(IntType(), "c", IntLiteral(1)),
        IfStmt(
            BinaryOp(
                BinaryOp(Identifier("a"), "&&", Identifier("b")),
                "||",
                BinaryOp(Identifier("a"), "&&", Identifier("c"))
            ),
            ExprStmt(FuncCall("printString", [StringLiteral("yes")])),
            None
        )
    )
    _run(ast, "yes")


def test_094_return_type_inference_void():
    # foo() with no return type declared → inferred void; prints "foo"
    ast = Program([
        FuncDecl(
            None, "foo", [],
            BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("foo")]))])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("foo", []))]))
    ])
    _run(ast, "foo")


def test_095_return_type_inference_int():
    # bar() with no return type but returns 42 → inferred int
    ast = Program([
        FuncDecl(
            None, "bar", [],
            BlockStmt([ReturnStmt(IntLiteral(42))])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("bar", [])]))
        ]))
    ])
    _run(ast, "42")


def test_096_assignment_result_in_if():
    # if(x=1) → truthy; print "true"
    ast = _main(
        VarDecl(IntType(), "x", None),
        IfStmt(
            AssignExpr(Identifier("x"), IntLiteral(1)),
            ExprStmt(FuncCall("printString", [StringLiteral("true")])),
            None
        )
    )
    _run(ast, "true")


def test_097_nested_assignment_chained():
    # a=(b=(c=10)+1)+1 → c=10, b=11, a=12  →  121110
    ast = _main(
        VarDecl(IntType(), "a", None),
        VarDecl(IntType(), "b", None),
        VarDecl(IntType(), "c", None),
        ExprStmt(AssignExpr(
            Identifier("a"),
            BinaryOp(
                AssignExpr(
                    Identifier("b"),
                    BinaryOp(
                        AssignExpr(Identifier("c"), IntLiteral(10)),
                        "+", IntLiteral(1)
                    )
                ),
                "+", IntLiteral(1)
            )
        )),
        ExprStmt(FuncCall("printInt", [Identifier("a")])),
        ExprStmt(FuncCall("printInt", [Identifier("b")])),
        ExprStmt(FuncCall("printInt", [Identifier("c")]))
    )
    _run(ast, "121110")


def test_098_struct_copy_and_modify():
    # s1={10}; s2=s1 (deep copy); s2.x=20; print s1.x,s2.x  →  1020
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "x")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "s1", StructLiteral([IntLiteral(10)])),
            VarDecl(StructType("S"), "s2", Identifier("s1")),
            ExprStmt(AssignExpr(MemberAccess(Identifier("s2"), "x"), IntLiteral(20))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s1"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s2"), "x")]))
        ]))
    ])
    _run(ast, "1020")


def test_099_empty_string_literal():
    # print "" then "end"  →  "end"
    ast = _main(
        ExprStmt(FuncCall("printString", [StringLiteral("")])),
        ExprStmt(FuncCall("printString", [StringLiteral("end")]))
    )
    _run(ast, "end")


def test_100_many_string_literals():
    ast = _main(
        ExprStmt(FuncCall("printString", [StringLiteral("a")])),
        ExprStmt(FuncCall("printString", [StringLiteral("b")])),
        ExprStmt(FuncCall("printString", [StringLiteral("c")]))
    )
    _run(ast, "abc")


def test_101_read_int_basic():
    # readInt() → x; print x+1
    ast = _main(
        VarDecl(IntType(), "x", FuncCall("readInt", [])),
        ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("x"), "+", IntLiteral(1))]))
    )
    _run(ast, "43", "42")


def test_102_read_float_basic():
    # readFloat() → f; print f*2.0
    ast = _main(
        VarDecl(FloatType(), "f", FuncCall("readFloat", [])),
        ExprStmt(FuncCall("printFloat", [BinaryOp(Identifier("f"), "*", FloatLiteral(2.0))]))
    )
    _run(ast, "6.28", "3.14")


def test_103_read_string_basic():
    # readString() → s; print "Hello "; print s
    ast = _main(
        VarDecl(StringType(), "s", FuncCall("readString", [])),
        ExprStmt(FuncCall("printString", [StringLiteral("Hello ")])),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    )
    _run(ast, "Hello World", "World")


def test_104_struct_with_string_member():
    # struct User{name,age}; u={"Alice",30}; print u.name, u.age  →  "Alice30"
    ast = Program([
        StructDecl("User", [
            MemberDecl(StringType(), "name"),
            MemberDecl(IntType(), "age")
        ]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("User"), "u",
                    StructLiteral([StringLiteral("Alice"), IntLiteral(30)])),
            ExprStmt(FuncCall("printString", [MemberAccess(Identifier("u"), "name")])),
            ExprStmt(FuncCall("printInt",    [MemberAccess(Identifier("u"), "age")]))
        ]))
    ])
    _run(ast, "Alice30")


def test_105_complicated_math_expression():
    # (x*x + y*y) / (x+y) where x=2.0,y=3.0 → (4+9)/5 = 2.6
    ast = _main(
        VarDecl(FloatType(), "x", FloatLiteral(2.0)),
        VarDecl(FloatType(), "y", FloatLiteral(3.0)),
        VarDecl(FloatType(), "z", BinaryOp(
            BinaryOp(
                BinaryOp(Identifier("x"), "*", Identifier("x")),
                "+",
                BinaryOp(Identifier("y"), "*", Identifier("y"))
            ),
            "/",
            BinaryOp(Identifier("x"), "+", Identifier("y"))
        )),
        ExprStmt(FuncCall("printFloat", [Identifier("z")]))
    )
    _run(ast, "2.6")


def test_106_inc_dec_on_struct_member():
    # s={10}; s.x++ → 11; ++s.x → 12; print s.x
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "x")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "s", StructLiteral([IntLiteral(10)])),
            ExprStmt(PostfixOp("++", MemberAccess(Identifier("s"), "x"))),
            ExprStmt(PrefixOp("++",  MemberAccess(Identifier("s"), "x"))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s"), "x")]))
        ]))
    ])
    _run(ast, "12")


def test_107_nested_blocks_with_variable_decls():
    # x=1; {y=2; {z=3; print x+y+z=6}; print x+y=3}; print x=1  →  631
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(1)),
        BlockStmt([
            VarDecl(IntType(), "y", IntLiteral(2)),
            BlockStmt([
                VarDecl(IntType(), "z", IntLiteral(3)),
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(BinaryOp(Identifier("x"), "+", Identifier("y")), "+", Identifier("z"))
                ]))
            ]),
            ExprStmt(FuncCall("printInt", [
                BinaryOp(Identifier("x"), "+", Identifier("y"))
            ]))
        ]),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    )
    _run(ast, "631")


def test_108_function_call_as_switch_expr():
    # switch(getVal()): case 42: "yes" break
    ast = Program([
        FuncDecl(IntType(), "getVal", [], BlockStmt([ReturnStmt(IntLiteral(42))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            SwitchStmt(
                FuncCall("getVal", []),
                [
                    CaseStmt(IntLiteral(42), [
                        ExprStmt(FuncCall("printString", [StringLiteral("yes")])),
                        BreakStmt()
                    ])
                ],
                None
            )
        ]))
    ])
    _run(ast, "yes")


def test_109_recursive_sum_of_n():
    # sum(10) = 55
    ast = Program([
        FuncDecl(
            IntType(), "sum",
            [Param(IntType(), "n")],
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("n"), "==", IntLiteral(0)),
                    ReturnStmt(IntLiteral(0)), None
                ),
                ReturnStmt(BinaryOp(
                    Identifier("n"), "+",
                    FuncCall("sum", [BinaryOp(Identifier("n"), "-", IntLiteral(1))])
                ))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [FuncCall("sum", [IntLiteral(10)])]))
        ]))
    ])
    _run(ast, "55")


def test_110_complex_integrated():
    # struct S{val}; process(s,factor): if s.val>10: return s.val*factor else s.val+factor
    # process({5},2)=7, process({15},2)=30  →  730
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "val")]),
        FuncDecl(
            IntType(), "process",
            [Param(StructType("S"), "s"), Param(IntType(), "factor")],
            BlockStmt([
                IfStmt(
                    BinaryOp(MemberAccess(Identifier("s"), "val"), ">", IntLiteral(10)),
                    ReturnStmt(BinaryOp(
                        MemberAccess(Identifier("s"), "val"), "*", Identifier("factor")
                    )),
                    None
                ),
                ReturnStmt(BinaryOp(
                    MemberAccess(Identifier("s"), "val"), "+", Identifier("factor")
                ))
            ])
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "s1", StructLiteral([IntLiteral(5)])),
            VarDecl(StructType("S"), "s2", StructLiteral([IntLiteral(15)])),
            ExprStmt(FuncCall("printInt", [
                FuncCall("process", [Identifier("s1"), IntLiteral(2)])
            ])),
            ExprStmt(FuncCall("printInt", [
                FuncCall("process", [Identifier("s2"), IntLiteral(2)])
            ]))
        ]))
    ])
    _run(ast, "730")