"""
Test cases for TyC code generation.
"""

from src.utils.nodes import *
from tests.utils import CodeGenerator

def _run(ast: Program, expected: str, input_data: str = "") -> None:
    result = CodeGenerator().generate_and_run(ast, input_data)
    assert result == expected, f"Expected '{expected}', got '{result}'"


# Helper: wrap statements in a void main() function
def _main(*stmts) -> Program:
    return Program([FuncDecl(VoidType(), "main", [], BlockStmt(list(stmts)))])


def test_001():
    """Test 1: Hello World - print string"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printString", [StringLiteral("Hello World")]))
            ])
        )
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_002():
    """Test 2: Print integer"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [IntLiteral(42)]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_003():
    """Test 3: Print float"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printFloat", [FloatLiteral(3.14)]))
            ])
        )
    ])
    expected = "3.14"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_004():
    """Test 4: Variable declaration and assignment"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(10)),
                ExprStmt(FuncCall("printInt", [Identifier("x")]))
            ])
        )
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_005():
    """Test 5: Binary operation - addition"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(5), "+", IntLiteral(3))
                ]))
            ])
        )
    ])
    expected = "8"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_006():
    """Test 6: Binary operation - multiplication"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(6), "*", IntLiteral(7))
                ]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_007():
    """Test 7: If statement"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                IfStmt(
                    BinaryOp(IntLiteral(1), "<", IntLiteral(2)),
                    ExprStmt(FuncCall("printString", [StringLiteral("yes")])),
                    ExprStmt(FuncCall("printString", [StringLiteral("no")]))
                )
            ])
        )
    ])
    expected = "yes"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_008():
    """Test 8: While loop"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
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
            ])
        )
    ])
    expected = "012"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_009():
    """Test 9: Function call with return value"""
    ast = Program([
        FuncDecl(
            IntType(),
            "add",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([
                ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    FuncCall("add", [IntLiteral(20), IntLiteral(22)])
                ]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_010():
    """Test 10: Multiple statements - arithmetic operations"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(10)),
                VarDecl(IntType(), "y", IntLiteral(20)),
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(Identifier("x"), "+", Identifier("y"))
                ]))
            ])
        )
    ])
    expected = "30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_11():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "+", IntLiteral(2))])))
    _run(ast, "3")

def test_12():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(10), "-", IntLiteral(4))])))
    _run(ast, "6")

def test_13():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(3), "*", IntLiteral(5))])))
    _run(ast, "15")

def test_14():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(20), "/", IntLiteral(4))])))
    _run(ast, "5")

def test_15():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(10), "%", IntLiteral(3))])))
    _run(ast, "1")

def test_16():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "+", BinaryOp(IntLiteral(2), "*", IntLiteral(3)))])))
    _run(ast, "7")

def test_17():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(IntLiteral(1), "+", IntLiteral(2)), "*", IntLiteral(3))])))
    _run(ast, "9")

def test_18():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(IntLiteral(10), "-", IntLiteral(2)), "-", IntLiteral(1))])))
    _run(ast, "7")

def test_19():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(IntLiteral(100), "/", IntLiteral(2)), "/", IntLiteral(2))])))
    _run(ast, "25")

def test_20():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(BinaryOp(IntLiteral(5), "%", IntLiteral(2)), "+", IntLiteral(1))])))
    _run(ast, "2")

def test_21():
    ast = _main(ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(1.0), "+", FloatLiteral(2.0))])))
    _run(ast, "3.0")

def test_22():
    ast = _main(ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(5.5), "-", FloatLiteral(1.5))])))
    _run(ast, "4.0")

def test_23():
    ast = _main(ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(2.0), "*", FloatLiteral(3.5))])))
    _run(ast, "7.0")

def test_24():
    ast = _main(ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(10.0), "/", FloatLiteral(4.0))])))
    _run(ast, "2.5")

def test_25():
    ast = _main(ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(1.5), "+", BinaryOp(FloatLiteral(2.0), "*", FloatLiteral(3.0)))])))
    _run(ast, "7.5")

def test_26():
    ast = _main(ExprStmt(FuncCall("printFloat", [BinaryOp(BinaryOp(FloatLiteral(1.5), "+", FloatLiteral(2.5)), "*", FloatLiteral(2.0))])))
    _run(ast, "8.0")

def test_27():
    ast = _main(ExprStmt(FuncCall("printFloat", [BinaryOp(IntLiteral(1), "+", FloatLiteral(2.5))])))
    _run(ast, "3.5")

def test_28():
    ast = _main(ExprStmt(FuncCall("printFloat", [BinaryOp(FloatLiteral(5.0), "-", IntLiteral(2))])))
    _run(ast, "3.0")

def test_29():
    ast = _main(ExprStmt(FuncCall("printFloat", [BinaryOp(IntLiteral(3), "*", FloatLiteral(1.5))])))
    _run(ast, "4.5")

def test_30():
    ast = _main(ExprStmt(FuncCall("printFloat", [BinaryOp(IntLiteral(10), "/", FloatLiteral(2.5))])))
    _run(ast, "4.0")

def test_31():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "==", IntLiteral(1))])))
    _run(ast, "1")

def test_32():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "==", IntLiteral(2))])))
    _run(ast, "0")

def test_33():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "!=", IntLiteral(2))])))
    _run(ast, "1")

def test_34():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "!=", IntLiteral(1))])))
    _run(ast, "0")

def test_35():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(5), "<", IntLiteral(10))])))
    _run(ast, "1")

def test_36():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(10), "<", IntLiteral(5))])))
    _run(ast, "0")

def test_37():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(5), ">", IntLiteral(2))])))
    _run(ast, "1")

def test_38():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(2), ">", IntLiteral(5))])))
    _run(ast, "0")

def test_39():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(5), "<=", IntLiteral(5))])))
    _run(ast, "1")

def test_40():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(5), "<=", IntLiteral(6))])))
    _run(ast, "1")

def test_41():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(5), ">=", IntLiteral(5))])))
    _run(ast, "1")

def test_42():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(6), ">=", IntLiteral(5))])))
    _run(ast, "1")

def test_43():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "&&", IntLiteral(1))])))
    _run(ast, "1")

def test_44():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "&&", IntLiteral(0))])))
    _run(ast, "0")

def test_45():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(0), "||", IntLiteral(1))])))
    _run(ast, "1")

def test_46():
    ast = _main(ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(0), "||", IntLiteral(0))])))
    _run(ast, "0")

def test_47():
    ast = _main(ExprStmt(FuncCall("printInt", [PrefixOp("!", IntLiteral(1))])))
    _run(ast, "0")

def test_48():
    ast = _main(ExprStmt(FuncCall("printInt", [PrefixOp("!", IntLiteral(0))])))
    _run(ast, "1")

def test_49():
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(10)),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    )
    _run(ast, "10")

def test_50():
    ast = _main(
        VarDecl(FloatType(), "y", FloatLiteral(1.5)),
        ExprStmt(FuncCall("printFloat", [Identifier("y")]))
    )
    _run(ast, "1.5")

def test_51():
    ast = _main(
        VarDecl(StringType(), "s", StringLiteral("hi")),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    )
    _run(ast, "hi")

def test_52():
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(0)),
        ExprStmt(AssignExpr(Identifier("x"), IntLiteral(20))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    )
    _run(ast, "20")

def test_53():
    ast = _main(
        VarDecl(FloatType(), "y", FloatLiteral(0.0)),
        ExprStmt(AssignExpr(Identifier("y"), FloatLiteral(2.5))),
        ExprStmt(FuncCall("printFloat", [Identifier("y")]))
    )
    _run(ast, "2.5")

def test_54():
    ast = _main(
        VarDecl(StringType(), "s", StringLiteral("")),
        ExprStmt(AssignExpr(Identifier("s"), StringLiteral("bye"))),
        ExprStmt(FuncCall("printString", [Identifier("s")]))
    )
    _run(ast, "bye")

def test_55():
    ast = _main(
        VarDecl(None, "x", IntLiteral(10)),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    )
    _run(ast, "10")

def test_56():
    ast = _main(
        VarDecl(None, "y", FloatLiteral(1.1)),
        ExprStmt(FuncCall("printFloat", [Identifier("y")]))
    )
    _run(ast, "1.1")

def test_57():
    ast = _main(
        VarDecl(IntType(), "x", None),
        VarDecl(IntType(), "y", None),
        ExprStmt(AssignExpr(Identifier("x"), AssignExpr(Identifier("y"), IntLiteral(30)))),
        ExprStmt(FuncCall("printInt", [Identifier("x")])),
        ExprStmt(FuncCall("printInt", [Identifier("y")]))
    )
    _run(ast, "3030")

def test_58():
    ast = _main(
        VarDecl(IntType(), "y", None),
        VarDecl(IntType(), "x", BinaryOp(IntLiteral(1), "+", AssignExpr(Identifier("y"), IntLiteral(2)))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    )
    _run(ast, "3")

def test_59():
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(PostfixOp("++", Identifier("x"))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    )
    _run(ast, "6")

def test_60():
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(PrefixOp("++", Identifier("x"))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    )
    _run(ast, "6")

def test_61():
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(PostfixOp("--", Identifier("x"))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    )
    _run(ast, "4")

def test_62():
    ast = _main(
        VarDecl(IntType(), "x", IntLiteral(5)),
        ExprStmt(PrefixOp("--", Identifier("x"))),
        ExprStmt(FuncCall("printInt", [Identifier("x")]))
    )
    _run(ast, "4")

def test_63():
    ast = _main(
        IfStmt(IntLiteral(1), ExprStmt(FuncCall("printInt", [IntLiteral(1)])))
    )
    _run(ast, "1")

def test_64():
    ast = _main(
        IfStmt(IntLiteral(0), ExprStmt(FuncCall("printInt", [IntLiteral(1)])))
    )
    _run(ast, "")

def test_65():
    ast = _main(
        IfStmt(IntLiteral(1), 
               ExprStmt(FuncCall("printInt", [IntLiteral(1)])),
               ExprStmt(FuncCall("printInt", [IntLiteral(2)])))
    )
    _run(ast, "1")

def test_66():
    ast = _main(
        IfStmt(IntLiteral(0), 
               ExprStmt(FuncCall("printInt", [IntLiteral(1)])),
               ExprStmt(FuncCall("printInt", [IntLiteral(2)])))
    )
    _run(ast, "2")

def test_67():
    ast = _main(
        IfStmt(IntLiteral(1),
               IfStmt(IntLiteral(1), ExprStmt(FuncCall("printInt", [IntLiteral(3)]))))
    )
    _run(ast, "3")

def test_68():
    ast = _main(
        IfStmt(BinaryOp(IntLiteral(1), "&&", IntLiteral(1)),
               ExprStmt(FuncCall("printString", [StringLiteral("ok")])))
    )
    _run(ast, "ok")

def test_69():
    ast = _main(
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                  BlockStmt([
                      ExprStmt(FuncCall("printInt", [Identifier("i")])),
                      ExprStmt(PostfixOp("++", Identifier("i")))
                  ]))
    )
    _run(ast, "012")

def test_70():
    ast = _main(
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(IntLiteral(1),
                  BlockStmt([
                      IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(2)), BreakStmt()),
                      ExprStmt(FuncCall("printInt", [Identifier("i")])),
                      ExprStmt(PostfixOp("++", Identifier("i")))
                  ]))
    )
    _run(ast, "01")

def test_71():
    ast = _main(
        VarDecl(IntType(), "i", IntLiteral(0)),
        WhileStmt(BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                  BlockStmt([
                      ExprStmt(PostfixOp("++", Identifier("i"))),
                      IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(2)), ContinueStmt()),
                      ExprStmt(FuncCall("printInt", [Identifier("i")]))
                  ]))
    )
    _run(ast, "13")

def test_72():
    ast = _main(
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                PostfixOp("++", Identifier("i")),
                ExprStmt(FuncCall("printInt", [Identifier("i")])))
    )
    _run(ast, "012")

def test_73():
    ast = _main(
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                IntLiteral(1),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(2)), BreakStmt()),
                    ExprStmt(FuncCall("printInt", [Identifier("i")]))
                ]))
    )
    _run(ast, "01")

def test_74():
    ast = _main(
        ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                PostfixOp("++", Identifier("i")),
                BlockStmt([
                    IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(1)), ContinueStmt()),
                    ExprStmt(FuncCall("printInt", [Identifier("i")]))
                ]))
    )
    _run(ast, "02")

def test_75():
    ast = _main(
        SwitchStmt(IntLiteral(1), [
            CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printInt", [IntLiteral(10)]))])
        ])
    )
    _run(ast, "10")

def test_76():
    ast = _main(
        SwitchStmt(IntLiteral(2), [], DefaultStmt([ExprStmt(FuncCall("printInt", [IntLiteral(20)]))]))
    )
    _run(ast, "20")

def test_77():
    ast = _main(
        SwitchStmt(IntLiteral(1), [
            CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printInt", [IntLiteral(1)]))]),
            CaseStmt(IntLiteral(2), [ExprStmt(FuncCall("printInt", [IntLiteral(2)]))])
        ])
    )
    _run(ast, "12")

def test_78():
    ast = _main(
        SwitchStmt(IntLiteral(1), [
            CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printInt", [IntLiteral(1)])), BreakStmt()]),
            CaseStmt(IntLiteral(2), [ExprStmt(FuncCall("printInt", [IntLiteral(2)]))])
        ])
    )
    _run(ast, "1")

def test_79():
    ast = Program([
        FuncDecl(VoidType(), "foo", [], BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("foo")]))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("foo", []))]))
    ])
    _run(ast, "foo")

def test_80():
    ast = Program([
        FuncDecl(VoidType(), "foo", [Param(IntType(), "a")], BlockStmt([ExprStmt(FuncCall("printInt", [Identifier("a")]))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("foo", [IntLiteral(42)]))]))
    ])
    _run(ast, "42")

def test_81():
    ast = Program([
        FuncDecl(VoidType(), "foo", [Param(IntType(), "a"), Param(IntType(), "b")], 
                 BlockStmt([ExprStmt(FuncCall("printInt", [BinaryOp(Identifier("a"), "+", Identifier("b"))]))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("foo", [IntLiteral(10), IntLiteral(20)]))]))
    ])
    _run(ast, "30")

def test_82():
    ast = Program([
        FuncDecl(IntType(), "foo", [], BlockStmt([ReturnStmt(IntLiteral(42))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [FuncCall("foo", [])]))]))
    ])
    _run(ast, "42")

def test_83():
    ast = Program([
        FuncDecl(FloatType(), "foo", [], BlockStmt([ReturnStmt(FloatLiteral(3.14))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printFloat", [FuncCall("foo", [])]))]))
    ])
    _run(ast, "3.14")

def test_84():
    ast = Program([
        FuncDecl(StringType(), "foo", [], BlockStmt([ReturnStmt(StringLiteral("ok"))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printString", [FuncCall("foo", [])]))]))
    ])
    _run(ast, "ok")

def test_85():
    ast = Program([
        FuncDecl(IntType(), "fact", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "<=", IntLiteral(1)), ReturnStmt(IntLiteral(1))),
            ReturnStmt(BinaryOp(Identifier("n"), "*", FuncCall("fact", [BinaryOp(Identifier("n"), "-", IntLiteral(1)) ])))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [FuncCall("fact", [IntLiteral(5)])]))]))
    ])
    _run(ast, "120")

def test_86():
    ast = Program([
        FuncDecl(IntType(), "sum", [Param(IntType(), "n")], BlockStmt([
            IfStmt(BinaryOp(Identifier("n"), "==", IntLiteral(0)), ReturnStmt(IntLiteral(0))),
            ReturnStmt(BinaryOp(Identifier("n"), "+", FuncCall("sum", [BinaryOp(Identifier("n"), "-", IntLiteral(1)) ])))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("printInt", [FuncCall("sum", [IntLiteral(10)])]))]))
    ])
    _run(ast, "55")

def test_87():
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "g", IntLiteral(100)),
            ExprStmt(FuncCall("printInt", [Identifier("g")]))
        ]))
    ])
    _run(ast, "100")

def test_88():
    ast = Program([
        FuncDecl(VoidType(), "a", [], BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("a")]))])),
        FuncDecl(VoidType(), "b", [], BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("b")]))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("a", [])), ExprStmt(FuncCall("b", []))]))
    ])
    _run(ast, "ab")

def test_89():
    ast = Program([
        FuncDecl(VoidType(), "inner", [], BlockStmt([ExprStmt(FuncCall("printString", [StringLiteral("in")]))])),
        FuncDecl(VoidType(), "outer", [], BlockStmt([ExprStmt(FuncCall("inner", []))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([ExprStmt(FuncCall("outer", []))]))
    ])
    _run(ast, "in")

def test_90():
    ast = _main(
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(10), "==", IntLiteral(10))])),
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(10), "!=", IntLiteral(5))])),
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "&&", IntLiteral(1))])),
        ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(0), "||", IntLiteral(1))]))
    )
    _run(ast, "1111")

def test_91():
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "x")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "s", None),
            ExprStmt(FuncCall("printString", [StringLiteral("ok")]))
        ]))
    ])
    _run(ast, "ok")

def test_92():
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "x")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "s", StructLiteral([IntLiteral(42)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s"), "x")]))
        ]))
    ])
    _run(ast, "42")

def test_93():
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "s", StructLiteral([IntLiteral(1), IntLiteral(2)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s"), "y")]))
        ]))
    ])
    _run(ast, "12")

def test_94():
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "x")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "s", StructLiteral([IntLiteral(0)])),
            ExprStmt(AssignExpr(MemberAccess(Identifier("s"), "x"), IntLiteral(100))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s"), "x")]))
        ]))
    ])
    _run(ast, "100")

def test_95():
    ast = Program([
        StructDecl("A", [MemberDecl(IntType(), "v")]),
        StructDecl("B", [MemberDecl(StructType("A"), "a")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("B"), "b", StructLiteral([StructLiteral([IntLiteral(10)])])),
            ExprStmt(FuncCall("printInt", [MemberAccess(MemberAccess(Identifier("b"), "a"), "v")]))
        ]))
    ])
    _run(ast, "10")

def test_96():
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "x")]),
        FuncDecl(StructType("S"), "foo", [], BlockStmt([ReturnStmt(StructLiteral([IntLiteral(42)]))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "s", FuncCall("foo", [])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s"), "x")]))
        ]))
    ])
    _run(ast, "42")

def test_97():
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "x")]),
        FuncDecl(VoidType(), "foo", [Param(StructType("S"), "s")], BlockStmt([ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s"), "x")]))])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "s", StructLiteral([IntLiteral(42)])),
            ExprStmt(FuncCall("foo", [Identifier("s")]))
        ]))
    ])
    _run(ast, "42")

def test_98():
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "x"), MemberDecl(FloatType(), "y"), MemberDecl(StringType(), "z")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "s", StructLiteral([IntLiteral(1), FloatLiteral(2.0), StringLiteral("3")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("s"), "x")])),
            ExprStmt(FuncCall("printFloat", [MemberAccess(Identifier("s"), "y")])),
            ExprStmt(FuncCall("printString", [MemberAccess(Identifier("s"), "z")]))
        ]))
    ])
    _run(ast, "12.03")

def test_99():
    ast = Program([
        StructDecl("S", [MemberDecl(IntType(), "x")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("S"), "s", StructLiteral([IntLiteral(10)])),
            ExprStmt(FuncCall("printInt", [BinaryOp(MemberAccess(Identifier("s"), "x"), "+", IntLiteral(5))]))
        ]))
    ])
    _run(ast, "15")

def test_100():
    ast = _main(ExprStmt(FuncCall("printString", [StringLiteral("done")])))
    _run(ast, "done")
