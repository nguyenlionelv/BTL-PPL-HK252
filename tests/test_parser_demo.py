"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser

def sp_test_valid(source):
    parser = Parser(source)
    assert parser.parse() == "success"

def sp_test_invalid(source):
    parser = Parser(source)
    assert parser.parse() != "success"
    assert "Error on line" in parser.parse()


# ============================================================================
# PROGRAM STRUCTURE TESTS (20 tests)
# ============================================================================

def test_parser_001():
    sp_test_valid("")

def test_parser_002():
    sp_test_valid("void main() { }")

def test_parser_003():
    sp_test_valid("struct Point { int x; };")

def test_parser_004():
    sp_test_valid("struct Point { int x; }; void main() { }")

def test_parser_005():
    sp_test_valid("""
        int add(int a, int b) { return a + b; }
        void main() { }
    """)

def test_parser_006():
    sp_test_valid("""
        struct Point { int x; int y; };
        struct Person { string name; int age; };
    """)

def test_parser_007():
    sp_test_valid("""
        struct Point { int x; };
        int helper() { return 0; }
        struct Person { string name; };
        void main() { }
    """)

def test_parser_008():
    sp_test_invalid("struct Point { int x; }")

def test_parser_009():
    sp_test_invalid("1 + 2;")

def test_parser_010():
    sp_test_invalid("int x = 5;")

def test_parser_101():
    sp_test_invalid("""
        struct Point { int x; int help() {} };
        int helper() { return 0; }
        struct Person { string name; };
        void main() { }
    """)

def test_parser_102():
    sp_test_invalid("""
        struct Point { int x; int y; };
        int helper() { return 0; struct Help { int x; int y; }; }
        struct Person { string name; };
        void main() { }
    """)

def test_parser_103():
    sp_test_invalid("""
        struct Point { int x; int y; };
        int helper() { return 0; }
        struct Person { string name; };
        void main() { int help() { x = 5; } return 0; }
    """)

def test_parser_104():
    sp_test_invalid("""
        struct Point { int x; int y; struct Point2 { int x; int y; }; };
        int helper() { return 0; }
        struct Person { string name; };
        void main() { int help() { x = 5; } }
    """)

def test_parser_105():
    sp_test_invalid("""
        struct Point { int x; int y; };
        int helper() { return 0; }
        struct Person { string name; };
        void main() { int help() { x = 5; return 0; } }
    """)

def test_parser_106():
    sp_test_invalid("""
        struct Point { int x; int y; }
        void main() { int help() { x = 5; return 0; } }
    """)

def test_parser_107():
    sp_test_invalid("""
        struct Point { int x; int y; };
        void main() { return 0; };
    """)

def test_parser_108():
    sp_test_valid("""
        struct Point { int x; int y; };
        struct Point2 { int x; Point2 y;};
        void main() { Point2 p; Point p2; }
    """)

def test_parser_109():
    sp_test_valid("""
        struct Point { int x; int y; };
        struct Point2 { int x; Point y;};
        struct Point3 { int x; Point2 y;};
        void main() { Point3 p; }
    """)

def test_parser_110():
    sp_test_invalid("""
        struct Point { int x; int y; };
        struct Point2 { int x; Point y;};
        string func() { return "hello"; Point p;}
        struct Point3 { int x; Point2 y;};
        void main() { Point3 p; };
    """)
# ============================================================================
# STRUCT DECLARATION TESTS (10 tests)
# ============================================================================

def test_parser_011():
    sp_test_valid("""struct Empty {};""")


def test_parser_012():
    sp_test_valid("""struct Point { int x; };""")


def test_parser_013():
    sp_test_valid("""struct Point { int x; int y; float z; };""")


def test_parser_014():
    sp_test_valid("""struct Person { string name; int age; float height; };""")


def test_parser_015():
    sp_test_valid("""
        struct Point { int x; int y; };
        struct Shape { Point center; int radius; };
    """)


def test_parser_016():
    sp_test_invalid("struct Bad { auto x; };")


def test_parser_017():
    sp_test_invalid("struct Point { int x };")


def test_parser_018():
    sp_test_invalid("struct Bad { x; };")


def test_parser_019():
    sp_test_invalid("struct Bad { void x; };")


def test_parser_020():
    sp_test_invalid("struct Outer { struct Inner { int x; }; };")

def test_parser_111():
    sp_test_invalid("struct Bad { void x; };")

def test_parser_112():
    sp_test_invalid("struct Bad() { int x; };")

def test_parser_113():
    sp_test_invalid("struct Bad { int x = 5; };")

def test_parser_114():
    sp_test_valid("struct Bad { int x; ABC x;};")

def test_parser_115():
    sp_test_valid("""
        struct Point { int x; int y; };
        struct Shape { Point center; int radius; };
        struct Circle { int radius; };
    """)

def test_parser_116():
    sp_test_invalid("""
        struct Point { int x; int y; struct Point2 { int x; int y; };};
    """)

def test_parser_117():
    sp_test_invalid("""
        struct Point { int x; int y; Struct Point2 { int x; int y; };};
    """)

def test_parser_118():
    sp_test_invalid("""
        struct Point { int x; int y; int Point2 { int x; int y; };};
    """)

def test_parser_119():
    sp_test_invalid("""
        Struct Point { int x; int y; int Point2;};
    """)

def test_parser_120():
    sp_test_valid("""
        struct Point { int x; int y; Struct Point2;};
    """)

# ============================================================================
# FUNCTION DECLARATION TESTS (15 tests)
# ============================================================================

def test_parser_021():
    """Void function no params"""
    parser = Parser("void main() { }")
    assert parser.parse() == "success"


def test_parser_022():
    """Int function no params"""
    parser = Parser("int getZero() { return 0; }")
    assert parser.parse() == "success"


def test_parser_023():
    """Function with single parameter"""
    parser = Parser("int double(int x) { return x * 2; }")
    assert parser.parse() == "success"


def test_parser_024():
    """Function with multiple parameters"""
    parser = Parser("int add(int a, int b, int c) { return a + b + c; }")
    assert parser.parse() == "success"


def test_parser_025():
    """Function with struct parameter"""
    parser = Parser("""
        struct Point { int x; int y; };
        int getX(Point p) { return p.x; }
    """)
    assert parser.parse() == "success"


def test_parser_026():
    """Function with inferred return type"""
    parser = Parser("add(int a, int b) { return a + b; }")
    assert parser.parse() == "success"


def test_parser_027():
    """Function returning string"""
    parser = Parser('string getName() { return "test"; }')
    assert parser.parse() == "success"


def test_parser_028():
    """Function returning float"""
    parser = Parser("float pi() { return 3.14; }")
    assert parser.parse() == "success"


def test_parser_029():
    """Function returning struct"""
    parser = Parser("""
        struct Point { int x; int y; };
        Point origin() { return {0, 0}; }
    """)
    assert parser.parse() == "success"


def test_parser_030():
    """Complex function body"""
    parser = Parser("""
        int factorial(int n) {
            if (n <= 1) {
                return 1;
            } else {
                return n * factorial(n - 1);
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_031():
    """Auto parameter - should fail"""
    parser = Parser("int bad(auto x) { return 0; }")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


def test_parser_032():
    """Function without body - should fail"""
    parser = Parser("int test();")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


def test_parser_033():
    """Parameter without type - should fail"""
    parser = Parser("int bad(x) { return 0; }")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


def test_parser_034():
    """Void parameter - should fail"""
    parser = Parser("int bad(void x) { return 0; }")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


def test_parser_035():
    """Missing parentheses - should fail"""
    parser = Parser("int test { return 0; }")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


# ============================================================================
# VARIABLE DECLARATION TESTS (10 tests)
# ============================================================================

def test_parser_036():
    """Auto with init"""
    parser = Parser("void main() { auto x = 10; }")
    assert parser.parse() == "success"


def test_parser_037():
    """Auto without init"""
    parser = Parser("void main() { auto x; }")
    assert parser.parse() == "success"


def test_parser_038():
    """Int with init"""
    parser = Parser("void main() { int x = 10; }")
    assert parser.parse() == "success"


def test_parser_039():
    """Int without init"""
    parser = Parser("void main() { int x; }")
    assert parser.parse() == "success"


def test_parser_040():
    """Float and string declarations"""
    parser = Parser('void main() { float x = 3.14; string s = "hello"; }')
    assert parser.parse() == "success"


def test_parser_041():
    """Struct variable with init"""
    parser = Parser("""
        struct Point { int x; int y; };
        void main() { Point p = {10, 20}; }
    """)
    assert parser.parse() == "success"


def test_parser_042():
    """Multiple variable declarations"""
    parser = Parser("""
        void main() {
            int x = 5;
            float y = 3.14;
            auto z = x + y;
        }
    """)
    assert parser.parse() == "success"


def test_parser_043():
    """Variable initialized with expression"""
    parser = Parser("""
        void main() {
            int a = 5;
            int b = 10;
            auto sum = a + b * 2;
        }
    """)
    assert parser.parse() == "success"


def test_parser_044():
    """Missing semicolon - should fail"""
    parser = Parser("void main() { int x }")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


def test_parser_045():
    """Void variable - should fail"""
    parser = Parser("void main() { void x; }")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


# ============================================================================
# IF STATEMENT TESTS (5 tests)
# ============================================================================

def test_parser_046():
    """Simple if statement"""
    parser = Parser("void main() { if (1) { } }")
    assert parser.parse() == "success"


def test_parser_047():
    """If with else"""
    parser = Parser("void main() { if (1) { } else { } }")
    assert parser.parse() == "success"


def test_parser_048():
    """If without braces"""
    parser = Parser("void main() { if (x > 0) x = x + 1; }")
    assert parser.parse() == "success"


def test_parser_049():
    """Nested if"""
    parser = Parser("""
        void main() {
            if (x > 0) {
                if (y < 10) {
                    x = y;
                }
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_050():
    """If without condition - should fail"""
    parser = Parser("void main() { if () { } }")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


# ============================================================================
# WHILE STATEMENT TESTS (5 tests)
# ============================================================================

def test_parser_051():
    """Simple while loop"""
    parser = Parser("void main() { while (1) { } }")
    assert parser.parse() == "success"


def test_parser_052():
    """While with condition"""
    parser = Parser("void main() { while (x < 10) { x = x + 1; } }")
    assert parser.parse() == "success"


def test_parser_053():
    """While with break and continue"""
    parser = Parser("""
        void main() {
            while (1) {
                if (x == 5) break;
                if (x == 3) continue;
                x = x + 1;
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_054():
    """Nested while loops"""
    parser = Parser("""
        void main() {
            while (i < 10) {
                while (j < 10) {
                    j = j + 1;
                }
                i = i + 1;
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_055():
    """While without condition - should fail"""
    parser = Parser("void main() { while () { } }")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


# ============================================================================
# FOR STATEMENT TESTS (10 tests)
# ============================================================================

def test_parser_056():
    """Complete for loop"""
    parser = Parser("void main() { for (int i = 0; i < 10; i++) { } }")
    assert parser.parse() == "success"


def test_parser_057():
    """For with empty init"""
    parser = Parser("void main() { for (; i < 10; i++) { } }")
    assert parser.parse() == "success"


def test_parser_058():
    """For with empty condition"""
    parser = Parser("void main() { for (int i = 0; ; i++) { } }")
    assert parser.parse() == "success"


def test_parser_059():
    """For with empty update"""
    parser = Parser("void main() { for (int i = 0; i < 10; ) { } }")
    assert parser.parse() == "success"


def test_parser_060():
    """For with all empty (infinite loop)"""
    parser = Parser("void main() { for (; ; ) { } }")
    assert parser.parse() == "success"


def test_parser_061():
    """For with auto init"""
    parser = Parser("void main() { for (auto i = 0; i < 10; i++) { } }")
    assert parser.parse() == "success"


def test_parser_062():
    """For without type in init"""
    parser = Parser("void main() { for (i = 0; i < 10; i++) { } }")
    assert parser.parse() == "success"


def test_parser_063():
    """For without braces"""
    parser = Parser("void main() { for (int i = 0; i < 10; i++) printInt(i); }")
    assert parser.parse() == "success"


def test_parser_064():
    """Nested for loops"""
    parser = Parser("""
        void main() {
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    printInt(i + j);
                }
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_065():
    """For missing semicolon - should fail"""
    parser = Parser("void main() { for (int i = 0 i < 10; i++) { } }")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


# ============================================================================
# SWITCH STATEMENT TESTS (10 tests)
# ============================================================================

def test_parser_066():
    """Simple switch statement"""
    parser = Parser("void main() { switch (1) { case 1: break; } }")
    assert parser.parse() == "success"


def test_parser_067():
    """Switch with default"""
    parser = Parser("void main() { switch (1) { case 1: break; default: break; } }")
    assert parser.parse() == "success"


def test_parser_068():
    """Switch with multiple cases"""
    parser = Parser("""
        void main() {
            switch (x) {
                case 1: printInt(1); break;
                case 2: printInt(2); break;
                case 3: printInt(3); break;
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_069():
    """Switch with fall-through"""
    parser = Parser("""
        void main() {
            switch (x) {
                case 1:
                case 2:
                    printInt(2);
                    break;
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_070():
    """Switch with empty case"""
    parser = Parser("void main() { switch (x) { case 1: } }")
    assert parser.parse() == "success"


def test_parser_071():
    """Switch case with expression"""
    parser = Parser("void main() { switch (x) { case 1+2: break; case -5: break; } }")
    assert parser.parse() == "success"


def test_parser_072():
    """Switch with empty body"""
    parser = Parser("void main() { switch (x) { } }")
    assert parser.parse() == "success"


def test_parser_073():
    """Switch with only default"""
    parser = Parser("void main() { switch (x) { default: break; } }")
    assert parser.parse() == "success"


def test_parser_074():
    """Nested switch"""
    parser = Parser("""
        void main() {
            switch (x) {
                case 1:
                    switch (y) {
                        case 2: break;
                    }
                    break;
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_075():
    """Switch case without colon - should fail"""
    parser = Parser("void main() { switch (x) { case 1 break; } }")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


# ============================================================================
# EXPRESSION TESTS (15 tests)
# ============================================================================

def test_parser_076():
    """Arithmetic expressions"""
    parser = Parser("void main() { auto x = 1 + 2 - 3 * 4 / 5 % 2; }")
    assert parser.parse() == "success"


def test_parser_077():
    """Comparison expressions"""
    parser = Parser("void main() { auto x = 1 < 2 && 3 > 4 || 5 <= 6 && 7 >= 8; }")
    assert parser.parse() == "success"


def test_parser_078():
    """Logical expressions"""
    parser = Parser("void main() { auto x = 1 && 2 || !3; }")
    assert parser.parse() == "success"


def test_parser_079():
    """Increment and decrement"""
    parser = Parser("void main() { int x; --x; x++; --x; x--; }")
    assert parser.parse() == "success"


def test_parser_080():
    """Unary operators"""
    parser = Parser("void main() { auto x = -5; auto y = +3; auto z = !0; }")
    assert parser.parse() == "success"


def test_parser_081():
    """Parenthesized expressions"""
    parser = Parser("void main() { auto x = (1 + 2) * (3 - 4); }")
    assert parser.parse() == "success"


def test_parser_082():
    """Member access"""
    parser = Parser("""
        struct Point { int x; int y; };
        void main() {
            Point p = {1, 2};
            auto a = p.x;
            auto b = p.y;
        }
    """)
    assert parser.parse() == "success"


def test_parser_083():
    """Nested member access"""
    parser = Parser("""
        struct Inner { int value; };
        struct Outer { Inner inner; };
        void main() {
            Outer o;
            auto x = o.inner.value;
        }
    """)
    assert parser.parse() == "success"


def test_parser_084():
    """Function call"""
    parser = Parser("""
        int getValue() { return 42; }
        void main() { auto x = getValue(); }
    """)
    assert parser.parse() == "success"


def test_parser_085():
    """Function call with arguments"""
    parser = Parser("""
        int add(int a, int b, int c) { return a + b + c; }
        void main() { auto x = add(3, 5, 7); }
    """)
    assert parser.parse() == "success"


def test_parser_086():
    """Struct literal"""
    parser = Parser("""
        struct Point { int x; int y; };
        void main() { Point p = {10, 20}; }
    """)
    assert parser.parse() == "success"


def test_parser_087():
    """Complex precedence"""
    parser = Parser("void main() { auto x = 1 + 2 * 3 < 4 && 5 || !6; }")
    assert parser.parse() == "success"


def test_parser_088():
    """Chained assignment"""
    parser = Parser("void main() { int a, b, c; a = b = c = 5; }")
    assert parser.parse() == "success"


def test_parser_089():
    """Assignment in expression"""
    parser = Parser("void main() { int x, y; y = (x = 5) + 7; }")
    assert parser.parse() == "success"


def test_parser_090():
    """Member access with postfix"""
    parser = Parser("""
        struct Point { int x; };
        void main() {
            Point p;
            p.x = 10;
            ++p.x;
        }
    """)
    assert parser.parse() == "success"


# ============================================================================
# COMPLEX/INTEGRATION TESTS (5 tests)
# ============================================================================

def test_parser_091():
    """Factorial function"""
    parser = Parser("""
        int factorial(int n) {
            if (n <= 1) {
                return 1;
            } else {
                return n * factorial(n - 1);
            }
        }
        void main() {
            auto result = factorial(5);
        }
    """)
    assert parser.parse() == "success"


def test_parser_092():
    """Loop with calculations"""
    parser = Parser("""
        void main() {
            int sum = 0;
            for (int i = 1; i <= 10; i++) {
                sum = sum + i;
                if (sum > 30) break;
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_093():
    """Struct operations"""
    parser = Parser("""
        struct Point { int x; int y; };
        
        Point createPoint(int x, int y) {
            return {x, y};
        }
        
        void main() {
            Point p1 = createPoint(10, 20);
            Point p2;
            p2 = p1;
            p2.x = p2.x + 5;
        }
    """)
    assert parser.parse() == "success"


def test_parser_094():
    """All statement types"""
    parser = Parser("""
        void main() {
            int x = 0;
            
            if (x == 0) {
                x = 1;
            }
            
            while (x < 10) {
                x++;
            }
            
            for (int i = 0; i < 5; i++) {
                x = x + i;
            }
            
            switch (x) {
                case 10:
                    break;
                default:
                    x = 0;
                    break;
            }
            
            return;
        }
    """)
    assert parser.parse() == "success"


def test_parser_095():
    """Complex expressions with all operators"""
    parser = Parser("""
        struct Point { int x; };
        int getValue() { return 5; }
        void main() {
            Point p = {5};
            auto result = p.x++ + getValue() * 2 < 10 && 1 || !0;
        }
    """)
    assert parser.parse() == "success"


# ============================================================================
# ERROR/EDGE CASE TESTS (5 tests)
# ============================================================================

def test_parser_096():
    """Missing brace - should fail"""
    parser = Parser("void main() { int x = 5;")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


def test_parser_097():
    """Mismatched braces - should fail"""
    parser = Parser("void main() { if (1) { }")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


def test_parser_098():
    """Invalid expression - should fail"""
    parser = Parser("void main() { int x = + * 5; }")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


def test_parser_099():
    """Incomplete struct - should fail"""
    parser = Parser("struct Point {")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result


def test_parser_100():
    """Empty parameter (just comma) - should fail"""
    parser = Parser("int add(int a, , int b) { return 0; }")
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result

def test_demo_1():
    parser = Parser("""
        void main() {
            int x,y;
        }        
    """)
    assert parser.parse() == "success"

def test_demo_2():
    parser = Parser("""
        void main() { auto x; x = 5; }       
    """)
    assert parser.parse() == "success"
