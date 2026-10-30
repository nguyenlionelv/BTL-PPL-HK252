"""
Test cases for TyC Static Semantic Checker

This module contains test cases for the static semantic checker.
100 test cases covering all error types and comprehensive scenarios.
"""

from tests.utils import Checker

# ===========================================================================
# VALID PROGRAMS (001–020)
# ===========================================================================

def test_001():
    source = """
        void main() {
            int x = 5;
            int y = x + 1;
        }
        int A() {
            int a = A();
            int y;
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_002():
    source = """
        void main() {
            printString("Hello, World!");
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_003():
    source = """
        struct Point {
            int x;
            int y;
        };
        void main() {
            Point p = {10, 20};
            printInt(p.x);
            printInt(p.y);
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_004():
    source = """
        int add(int x, int y) {
            return x + y;
        }
        void main() {
            int result = add(3, 5);
            printInt(result);
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_005():
    source = """
        void main() {
            auto x = 10;
            auto y = 3.14;
            auto msg = "hello";
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_006():
    source = """
        void main() {
            auto a;
            a = 10;
            auto b;
            b = 3.14;
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_007():
    source = """
        void main() {
            auto i = 0;
            while (i < 10) {
                if (i == 3) {
                    continue;
                }
                if (i == 8) {
                    break;
                }
                printInt(i);
                ++i;
            }
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_008():
    source = """
        void main() {
            for (auto i = 0; i < 10; ++i) {
                if (i == 5) {
                    break;
                }
                printInt(i);
            }
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_009():
    source = """
        void main() {
            int day = 2;
            switch (day) {
                case 1:
                printInt(1);
                break;
                case 2:
                printInt(2);
                break;
                default:
                printInt(0);
            }
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_010():
    source = """
        struct Point {
            int x;
            int y;
        };
        struct Line {
            Point start;
            Point end;
        };
        void main() {
            Line l;
            l.start.x = 1;
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_011():
    source = """
        struct foo {
            int x;
            int y;
        };
        int foo(int x, int y) {
            return x + y;
        }
        void main() {
            foo f = {1, 2};
            int r = foo(3, 4);
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_012():
    source = """
        void main() {
            int value = 100;
            {
                int value = 200;
                {
                    int value = 300;
                }
            }
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_013():
    source = """
        void main() {
            auto x;
            x = readInt();
            auto y;
            y = readFloat();
            auto s;
            s = readString();
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_014():
    source = """
        void main() {
            auto x;
            printInt(x);
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_015():
    source = """
        void main() {
            int a;
            int b;
            int c;
            a = b = c = 10;
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_016():
    source = """
        add(int x, int y) {
            return x + y;
        }
        void main() {
            auto result = add(3, 5);
            printInt(result);
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_017():
    source = """
        struct Point {
            int x;
            int y;
        };
        void main() {
            Point p1 = {10, 20};
            Point p2;
            p2 = p1;
            printInt(p2.x);
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_018():
    source = """
        void main() {
            int x;
            int y = (x = 5) + 7;
            printInt(y);
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_019():
    source = """
        void main() {
            auto value;
            auto result = value + 5;
            printInt(result);
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_020():
    source = """
        void main() {
            for (auto i = 0; i < 5; ++i) {
                for (auto j = 0; j < 5; ++j) {
                    if (i == j) {
                        continue;
                    }
                    if (j > 3) {
                        break;
                    }
                }
            }
        }
    """
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

# ===========================================================================
# REDECLARED (021–032)
# ===========================================================================

def test_021():
    source = """
        void main() {
            int count = 10;
            int count = 20;
        }
    """
    expected = "Redeclared(Variable, count)"
    assert Checker(source).check_from_source() == expected

def test_022():
    source = """
        int add(int x, int y) {
            return x + y;
        }
        int add(int a, int b) {
            return a + b;
        }
        void main() {}
    """
    expected = "Redeclared(Function, add)"
    assert Checker(source).check_from_source() == expected

def test_023():
    source = """
        struct Point {
            int x;
            int y;
        };
        struct Point {
            int z;
        };
        void main() {}
    """
    expected = "Redeclared(Struct, Point)"
    assert Checker(source).check_from_source() == expected

def test_024():
    source = """
        int calculate(int x, float y, int x) {
            return x;
        }
        void main() {}
    """
    expected = "Redeclared(Parameter, x)"
    assert Checker(source).check_from_source() == expected

def test_025():
    source = """
        struct Point {
            int x;
            int x;
        };
        void main() {}
    """
    expected = "Redeclared(Member, x)"
    assert Checker(source).check_from_source() == expected

def test_026():
    source = """
        void func(int x) {
            int x = 10;
        }
        void main() {}
    """
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_027():
    source = """
        void func(int a) {
            {
                int a = 5;
            }
        }
        void main() {}
    """
    expected = "Redeclared(Variable, a)"
    assert Checker(source).check_from_source() == expected

def test_028():
    source = """
        void main() {
            int x = 1;
            int y = 2;
            int x = 3;
        }
    """
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_029():
    source = """
        struct A {
            int val;
        };
        struct A {
            float val;
        };
        void main() {
            A a;
        }
    """
    expected = "Redeclared(Struct, A)"
    assert Checker(source).check_from_source() == expected

def test_030():
    source = """
        int compute() {
            return 1;
        }
        float compute() {
            return 1.0;
        }
        void main() {}
    """
    expected = "Redeclared(Function, compute)"
    assert Checker(source).check_from_source() == expected

def test_031():
    source = """
        void f(int a, int b, int a) {}
        void main() {}
    """
    expected = "Redeclared(Parameter, a)"
    assert Checker(source).check_from_source() == expected

def test_032():
    source = """
        struct Rect {
            int width;
            int height;
            int width;
        };
        void main() {}
    """
    expected = "Redeclared(Member, width)"
    assert Checker(source).check_from_source() == expected

# ===========================================================================
# UNDECLARED IDENTIFIER (033–040)
# ===========================================================================

def test_033():
    source = """
        void main() {
            int result = undeclaredVar + 10;
        }
    """
    expected = "UndeclaredIdentifier(undeclaredVar)"
    assert Checker(source).check_from_source() == expected

def test_034():
    source = """
        void main() {
            int x = y + 5;
            int y = 10;
        }
    """
    expected = "UndeclaredIdentifier(y)"
    assert Checker(source).check_from_source() == expected

def test_035():
    source = """
        void method1() {
            int localVar = 42;
        }
        void main() {
            int value = localVar + 1;
        }
    """
    expected = "UndeclaredIdentifier(localVar)"
    assert Checker(source).check_from_source() == expected

def test_036():
    source = """
        void main() {
            {
                int inner = 5;
            }
            int x = inner + 1;
        }
    """
    expected = "UndeclaredIdentifier(inner)"
    assert Checker(source).check_from_source() == expected

def test_037():
    source = """
        void main() {
            int x = 10;
            int z = x + ghost;
        }
    """
    expected = "UndeclaredIdentifier(ghost)"
    assert Checker(source).check_from_source() == expected

def test_038():
    source = """
        void main() {
            auto result = unknown * 2;
        }
    """
    expected = "UndeclaredIdentifier(unknown)"
    assert Checker(source).check_from_source() == expected

def test_039():
    source = """
        void main() {
            notDeclared = 5;
        }
    """
    expected = "UndeclaredIdentifier(notDeclared)"
    assert Checker(source).check_from_source() == expected

def test_040():
    source = """
        void main() {
            int x = x + 1;
        }
    """
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

# ===========================================================================
# UNDECLARED FUNCTION (041–047)
# ===========================================================================

def test_041():
    source = """
        void main() {
            int result = calculate(5, 3);
        }
    """
    expected = "UndeclaredFunction(calculate)"
    assert Checker(source).check_from_source() == expected

def test_042():
    source = """
        void main() {
            int value = add(10, 20);
        }
        int add(int x, int y) {
            return x + y;
        }
    """
    expected = "UndeclaredFunction(add)"
    assert Checker(source).check_from_source() == expected

def test_043():
    source = """
        void main() {
            printInt(doSomething());
        }
    """
    expected = "UndeclaredFunction(doSomething)"
    assert Checker(source).check_from_source() == expected

def test_044():
    source = """
        int helper() {
            return mystery(3);
        }
        void main() {}
    """
    expected = "UndeclaredFunction(mystery)"
    assert Checker(source).check_from_source() == expected

def test_045():
    source = """
        void main() {
            if (getFlag()) {
                printInt(1);
            }
        }
    """
    expected = "UndeclaredFunction(getFlag)"
    assert Checker(source).check_from_source() == expected

def test_046():
    source = """
        void main() {
            for (auto i = 0; i < 10; doStep()) {
                printInt(i);
            }
        }
    """
    expected = "UndeclaredFunction(doStep)"
    assert Checker(source).check_from_source() == expected

def test_047():
    source = """
        struct Math {
            int value;
        };
        void main() {
            int r = Math(5);
        }
    """
    expected = "UndeclaredFunction(Math)"
    assert Checker(source).check_from_source() == expected

# ===========================================================================
# UNDECLARED STRUCT (048–053)
# ===========================================================================

def test_048():
    source = """
        void main() {
            Point p;
        }
        struct Point {
            int x;
            int y;
        };
    """
    expected = "UndeclaredStruct(Point)"
    assert Checker(source).check_from_source() == expected

def test_049():
    source = """
        struct Address {
            string street;
            City city;
        };
        struct City {
            string name;
        };
        void main() {}
    """
    expected = "UndeclaredStruct(City)"
    assert Checker(source).check_from_source() == expected

def test_050():
    source = """
        void main() {
            Person someone;
        }
    """
    expected = "UndeclaredStruct(Person)"
    assert Checker(source).check_from_source() == expected

def test_051():
    source = """
        void process(Vehicle v) {}
        void main() {}
    """
    expected = "UndeclaredStruct(Vehicle)"
    assert Checker(source).check_from_source() == expected

def test_052():
    source = """
        Shape getShape() {
            Shape s;
            return s;
        }
        void main() {}
    """
    expected = "UndeclaredStruct(Shape)"
    assert Checker(source).check_from_source() == expected

def test_053():
    source = """
        struct Node {
            int val;
            Node next;
        };
        void main() {}
    """
    expected = "UndeclaredStruct(Node)"
    assert Checker(source).check_from_source() == expected

# ===========================================================================
# TYPE CANNOT BE INFERRED (054–065)
# ===========================================================================

def test_054():
    source = """
        void main() {
            auto x;
            auto y;
            auto result = x + y;
        }
    """
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), +, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_055():
    source = """
        void main() {
            auto x;
            auto y;
            x = y;
        }
    """
    expected = "TypeCannotBeInferred(AssignExpr(Identifier(x) = Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_056():
    source = """
        void main() {
            auto x;
        }
    """
    expected = "TypeCannotBeInferred(BlockStmt([VarDecl(auto, x)]))"
    assert Checker(source).check_from_source() == expected

def test_057():
    source = """
        func() {
            auto x;
            return x;
        }
        void main() {}
    """
    expected = "TypeCannotBeInferred(ReturnStmt(return Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_058():
    source = """
        void main() {
            auto x;
            auto y;
            int result = x < y;
        }
    """
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), <, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_059():
    source = """
        void main() {
            auto a;
            auto b;
            int c = a * b;
        }
    """
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(a), *, Identifier(b)))"
    assert Checker(source).check_from_source() == expected

def test_060():
    source = """
        void main() {
            auto x;
            auto result = x + "hello";
        }
    """
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), +, StringLiteral('hello')))"
    assert Checker(source).check_from_source() == expected

def test_061():
    source = """
        void circular() {
            auto a;
            auto b;
            a = b;
        }
        void main() {}
    """
    expected = "TypeCannotBeInferred(AssignExpr(Identifier(a) = Identifier(b)))"
    assert Checker(source).check_from_source() == expected

def test_062():
    source = """
        void main() {
            auto p;
            auto q;
        }
    """
    expected = "TypeCannotBeInferred(BlockStmt([VarDecl(auto, p), VarDecl(auto, q)]))"
    assert Checker(source).check_from_source() == expected

def test_063():
    source = """
        void main() {
            auto m;
            auto n;
            auto k = m / n;
        }
    """
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(m), /, Identifier(n)))"
    assert Checker(source).check_from_source() == expected

def test_064():
    source = """
        void main() {
            auto i;
            auto j;
            auto diff = i - j;
        }
    """
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(i), -, Identifier(j)))"
    assert Checker(source).check_from_source() == expected

def test_065():
    source = """
        void main() {
            auto u;
            auto v;
            int eq = u == v;
        }
    """
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(u), ==, Identifier(v)))"
    assert Checker(source).check_from_source() == expected

# ===========================================================================
# TYPE MISMATCH IN STATEMENT (066–079)
# ===========================================================================

def test_066():
    source = """
        void main() {
            float x = 5.0;
            if (x) {
                printInt(1);
            }
        }
    """
    expected = "TypeMismatchInStatement(IfStmt(if Identifier(x) then BlockStmt([ExprStmt(FuncCall(printInt, [IntLiteral(1)]))]))"
    expected = "TypeMismatchInStatement(IfStmt(if Identifier(x) then BlockStmt([ExprStmt(FuncCall(printInt, [IntLiteral(1)]))])))"
    assert Checker(source).check_from_source() == expected

def test_067():
    source = """
        void main() {
            string message = "hello";
            if (message) {
                printString(message);
            }
        }
    """
    expected = "TypeMismatchInStatement(IfStmt(if Identifier(message) then BlockStmt([ExprStmt(FuncCall(printString, [Identifier(message)]))])))"
    assert Checker(source).check_from_source() == expected

def test_068():
    source = """
        void main() {
            float f = 1.5;
            while (f) {
                printFloat(f);
            }
        }
    """
    expected = "TypeMismatchInStatement(WhileStmt(while Identifier(f) do BlockStmt([ExprStmt(FuncCall(printFloat, [Identifier(f)]))])))"
    assert Checker(source).check_from_source() == expected

def test_069():
    source = """
        void main() {
            int x = 10;
            string text = "hello";
            x = text;
        }
    """
    expected = "TypeMismatchInStatement(AssignExpr(Identifier(x) = Identifier(text)))"
    assert Checker(source).check_from_source() == expected

def test_070():
    source = """
        void main() {
            float f = 3.14;
            int x = 10;
            f = x;
        }
    """
    expected = "TypeMismatchInStatement(AssignExpr(Identifier(f) = Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_071():
    source = """
        int getValue() {
            return "invalid";
        }
        void main() {}
    """
    expected = "TypeMismatchInStatement(ReturnStmt(return StringLiteral('invalid')))"
    assert Checker(source).check_from_source() == expected

def test_072():
    source = """
        string getText() {
            return 42;
        }
        void main() {}
    """
    expected = "TypeMismatchInStatement(ReturnStmt(return IntLiteral(42)))"
    assert Checker(source).check_from_source() == expected

def test_073():
    source = """
        void main() {
            return 10;
        }
    """
    expected = "TypeMismatchInStatement(ReturnStmt(return IntLiteral(10)))"
    assert Checker(source).check_from_source() == expected

def test_074():
    source = """
        int returnVoidError() {
            return;
        }
        void main() {}
    """
    expected = "TypeMismatchInStatement(ReturnStmt(return))"
    assert Checker(source).check_from_source() == expected

def test_075():
    source = """
        void main() {
            float f = 3.14;
            switch (f) {
                case 1: break;
            }
        }
    """
    expected = "TypeMismatchInStatement(SwitchStmt(switch Identifier(f) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])]))"
    assert Checker(source).check_from_source() == expected

def test_076():
    source = """
        struct Point {
            int x;
            int y;
        };
        struct Person {
            string name;
            int age;
        };
        void main() {
            Point p;
            Person person;
            p = person;
        }
    """
    expected = "TypeMismatchInStatement(AssignExpr(Identifier(p) = Identifier(person)))"
    assert Checker(source).check_from_source() == expected

def test_077():
    source = """
        void main() {
            string text = "hello";
            int x = 5;
            text = x;
        }
    """
    expected = "TypeMismatchInStatement(AssignExpr(Identifier(text) = Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_078():
    source = """
        void main() {
            string s = "abc";
            for (auto i = 0; s; ++i) {
                printInt(i);
            }
        }
    """
    expected = "TypeMismatchInStatement(ForStmt(for VarDecl(auto, i = IntLiteral(0)); Identifier(s); PrefixOp(++Identifier(i)) do BlockStmt([ExprStmt(FuncCall(printInt, [Identifier(i)]))])))"
    assert Checker(source).check_from_source() == expected

def test_079():
    source = """
        myFunc() {
            return 1;
            return "oops";
        }
        void main() {}
    """
    expected = "TypeMismatchInStatement(ReturnStmt(return StringLiteral('oops')))"
    assert Checker(source).check_from_source() == expected

# ===========================================================================
# TYPE MISMATCH IN EXPRESSION (080–094)
# ===========================================================================

def test_080():
    source = """
        void main() {
            int x = 5;
            string text = "hello";
            int sum = x + text;
        }
    """
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(x), +, Identifier(text)))"
    assert Checker(source).check_from_source() == expected

def test_081():
    source = """
        void main() {
            float f = 3.14;
            int x = 10;
            int result = f % x;
        }
    """
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(f), %, Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_082():
    source = """
        void main() {
            int x = 10;
            float f = 3.14;
            int result = x % f;
        }
    """
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(x), %, Identifier(f)))"
    assert Checker(source).check_from_source() == expected

def test_083():
    source = """
        void main() {
            int x = 10;
            string text = "hello";
            int result = x < text;
        }
    """
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(x), <, Identifier(text)))"
    assert Checker(source).check_from_source() == expected

def test_084():
    source = """
        void main() {
            float f = 3.14;
            int x = 10;
            int result = f && x;
        }
    """
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(f), &&, Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_085():
    source = """
        void main() {
            float f = 3.14;
            int result = !f;
        }
    """
    expected = "TypeMismatchInExpression(PrefixOp(!Identifier(f)))"
    assert Checker(source).check_from_source() == expected

def test_086():
    source = """
        void main() {
            float f = 3.14;
            ++f;
        }
    """
    expected = "TypeMismatchInExpression(PrefixOp(++Identifier(f)))"
    assert Checker(source).check_from_source() == expected

def test_087():
    source = """
        void main() {
            float f = 3.14;
            f++;
        }
    """
    expected = "TypeMismatchInExpression(PostfixOp(Identifier(f)++))"
    assert Checker(source).check_from_source() == expected

def test_088():
    source = """
        void main() {
            int x = 10;
            int value = x.member;
        }
    """
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(x).member))"
    assert Checker(source).check_from_source() == expected

def test_089():
    source = """
        struct Point {
            int x;
            int y;
        };
        void main() {
            Point p = {10, 20};
            int invalid = p.z;
        }
    """
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(p).z))"
    assert Checker(source).check_from_source() == expected

def test_090():
    source = """
        void process(int x) {}
        void main() {
            string text = "123";
            process(text);
        }
    """
    expected = "TypeMismatchInExpression(FuncCall(process, [Identifier(text)]))"
    assert Checker(source).check_from_source() == expected

def test_091():
    source = """
        int add(int x, int y) {
            return x + y;
        }
        void main() {
            int result = add(10);
        }
    """
    expected = "TypeMismatchInExpression(FuncCall(add, [IntLiteral(10)]))"
    assert Checker(source).check_from_source() == expected

def test_092():
    source = """
        int add(int x, int y) {
            return x + y;
        }
        void main() {
            int result = add(10, 20, 30);
        }
    """
    expected = "TypeMismatchInExpression(FuncCall(add, [IntLiteral(10), IntLiteral(20), IntLiteral(30)]))"
    assert Checker(source).check_from_source() == expected

def test_093():
    source = """
        struct Point {
            int x;
            int y;
        };
        void main() {
            Point p = {10, 20, 30};
        }
    """
    expected = "TypeMismatchInExpression(StructLiteral({IntLiteral(10), IntLiteral(20), IntLiteral(30)}))"
    assert Checker(source).check_from_source() == expected

def test_094():
    source = """
        struct Point {
            int x;
            int y;
        };
        void main() {
            Point p = {10, "hello"};
        }
    """
    expected = "TypeMismatchInExpression(StructLiteral({IntLiteral(10), StringLiteral('hello')}))"
    assert Checker(source).check_from_source() == expected

# ===========================================================================
# MUST IN LOOP (095–100)
# ===========================================================================

def test_095():
    source = """
        void main() {
            break;
        }
    """
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_096():
    source = """
        void main() {
            continue;
        }
    """
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_097():
    source = """
        void main() {
            if (1) {
                break;
            }
        }
    """
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected

def test_098():
    source = """
        void main() {
            if (1) {
                continue;
            }
        }
    """
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_099():
    source = """
        void main() {
            int x = 1;
            switch (x) {
                case 1:
                continue;
                break;
            }
        }
    """
    expected = "MustInLoop(ContinueStmt())"
    assert Checker(source).check_from_source() == expected

def test_100():
    source = """
        void helper() {
            break;
        }
        void main() {
            for (auto i = 0; i < 10; ++i) {
                helper();
            }
        }
    """
    expected = "MustInLoop(BreakStmt())"
    assert Checker(source).check_from_source() == expected
