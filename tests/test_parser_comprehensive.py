"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser

def test_valid(source):
    parser = Parser(source)
    assert parser.parse() == "success"

def test_invalid(source):
    parser = Parser(source)
    assert parser.parse() != "success"
    assert "Error on line" in parser.parse()


# ============================================================================
# PROGRAM STRUCTURE TESTS (20 tests)
# ============================================================================

def test_parser_001():
    test_valid("")

def test_parser_002():
    test_valid("void main() { }")

def test_parser_003():
    test_valid("struct Point { int x; };")

def test_parser_004():
    test_valid("struct Point { int x; }; void main() { }")

def test_parser_005():
    test_valid("""
        int add(int a, int b) { return a + b; }
        void main() { }
    """)

def test_parser_006():
    test_valid("""
        struct Point { int x; int y; };
        struct Person { string name; int age; };
    """)

def test_parser_007():
    test_valid("""
        struct Point { int x; };
        int helper() { return 0; }
        struct Person { string name; };
        void main() { }
    """)

def test_parser_008():
    test_invalid("struct Point { int x; }")

def test_parser_009():
    test_invalid("1 + 2;")

def test_parser_010():
    test_invalid("int x = 5;")

def test_parser_101():
    test_invalid("""
        struct Point { int x; int help() {} };
        int helper() { return 0; }
        struct Person { string name; };
        void main() { }
    """)

def test_parser_102():
    test_invalid("""
        struct Point { int x; int y; };
        int helper() { return 0; struct Help { int x; int y; }; }
        struct Person { string name; };
        void main() { }
    """)

def test_parser_103():
    test_invalid("""
        struct Point { int x; int y; };
        int helper() { return 0; }
        struct Person { string name; };
        void main() { int help() { x = 5; } return 0; }
    """)

def test_parser_104():
    test_invalid("""
        struct Point { int x; int y; struct Point2 { int x; int y; }; };
        int helper() { return 0; }
        struct Person { string name; };
        void main() { int help() { x = 5; } }
    """)

def test_parser_105():
    test_invalid("""
        struct Point { int x; int y; };
        int helper() { return 0; }
        struct Person { string name; };
        void main() { int help() { x = 5; return 0; } }
    """)

def test_parser_106():
    test_invalid("""
        struct Point { int x; int y; }
        void main() { int help() { x = 5; return 0; } }
    """)

def test_parser_107():
    test_invalid("""
        struct Point { int x; int y; };
        void main() { return 0; };
    """)

def test_parser_108():
    test_valid("""
        struct Point { int x; int y; };
        struct Point2 { int x; Point2 y;};
        void main() { Point2 p; Point p2; };
    """)

def test_parser_109():
    test_valid("""
        struct Point { int x; int y; };
        struct Point2 { int x; Point y;};
        struct Point3 { int x; Point2 y;};
        void main() { Point3 p; };
    """)

def test_parser_110():
    test_invalid("""
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
    test_valid("""struct Empty {};""")


def test_parser_012():
    test_valid("""struct Point { int x; };""")


def test_parser_013():
    test_valid("""struct Point { int x; int y; float z; };""")


def test_parser_014():
    test_valid("""struct Person { string name; int age; float height; };""")


def test_parser_015():
    test_valid("""
        struct Point { int x; int y; };
        struct Shape { Point center; int radius; };
    """)


def test_parser_016():
    test_invalid("struct Bad { auto x; };")


def test_parser_017():
    test_invalid("struct Point { int x };")


def test_parser_018():
    test_invalid("struct Bad { x; };")


def test_parser_019():
    test_invalid("struct Bad { void x; };")


def test_parser_020():
    test_invalid("struct Outer { struct Inner { int x; }; };")

def test_parser_111():
    test_invalid("struct Bad { void x; };")

def test_parser_112():
    test_invalid("struct Bad() { int x; };")

def test_parser_113():
    test_invalid("struct Bad { int x = 5; };")

def test_parser_114():
    test_valid("struct Bad { int x; ABC x;};")

def test_parser_115():
    test_valid("""
        struct Point { int x; int y; };
        struct Shape { Point center; int radius; };
        struct Circle { int radius; };
    """)

def test_parser_116():
    test_invalid("""
        struct Point { int x; int y; struct Point2 { int x; int y; };};
    """)

def test_parser_117():
    test_invalid("""
        struct Point { int x; int y; Struct Point2 { int x; int y; };};
    """)

def test_parser_118():
    test_invalid("""
        struct Point { int x; int y; int Point2 { int x; int y; };};
    """)

def test_parser_119():
    test_invalid("""
        Struct Point { int x; int y; int Point2;};
    """)

def test_parser_120():
    test_valid("""
        struct Point { int x; int y; Struct Point2;};
    """)

# ============================================================================
# FUNCTION DECLARATION TESTS (15 tests)
# ============================================================================

def test_parser_021():
    """Void function with empty body"""
    test_valid("void main() { }")


def test_parser_022():
    """Int function with return statement"""
    test_valid("int getZero() { return 0; }")


def test_parser_023():
    """Float function with parameter and return statement"""
    test_valid("float double(int x) { return x * 2 - 0.5; }")


def test_parser_024():
    """Int function with multiple parameters and return statement"""
    test_valid("int add(int a, int b, int c) { return a + b + c; }")


def test_parser_025():
    """Int function with struct parameter and return statement"""
    test_valid("""
        struct Point { int x; int y; };
        int getX(Point p) { return p.x; }
    """)


def test_parser_026():
    """Int function with multiple parameters (wrong) and return statement"""
    test_invalid("int add(int a, int b, int c,) { return a + b + c; }")


def test_parser_027():
    """String function with return statement"""
    test_valid('string getName() { return "test"; }')


def test_parser_028():
    """Float function with return statement"""
    test_valid("float pi() { return 3.14; }")


def test_parser_029():
    """Struct function with return statement"""
    test_valid("""
        struct Point { int x; int y; };
        Point origin() { return {0, 0}; }
    """)


def test_parser_030():
    """Int function with recursive call"""
    test_valid("""
        int factorial(int n) {
            if (n <= 1) {
                return 1;
            } else {
                return n * factorial(n - 1);
            }
        }
    """)


def test_parser_031():
    """Int function with auto parameter (wrong)"""
    test_invalid("int bad(auto x) { return 0; }")


def test_parser_032():
    """Int function with no body (wrong)"""
    test_invalid("int test();")


def test_parser_033():
    """Int function with wrong parameter declaration (wrong)"""
    test_invalid("int bad(x) { return 0; }")


def test_parser_034():
    """Int function with void parameter (wrong)"""
    test_invalid("int bad(void x) { return 0; }")


def test_parser_035():
    """Int function with no parenthesis (wrong)"""
    test_invalid("int test { return 0; }")

def test_parser_120():
    """Int function with no return statement (wrong)"""
    test_invalid("int add(int a, int b) { a = b; b = 1; c = a + b; }")

def test_parser_121():
    """Int function with no return statement (wrong)"""
    test_invalid("int add(int a, int b) { a = b; b = 1; c = a + b; }")

def test_parser_122():
    """Int function with auto parameter (wrong)"""
    test_invalid("int add(auto a, int b) { a = b; b = 1; c = a + b; }")

def test_parser_123():
    """Int function with auto parameter (wrong)"""
    test_invalid("int add(auto a, int b) { a = b; b = 1; c = a + b; }")

def test_parser_124():
    """Function with no ftype"""
    test_valid("add(int a, int b) { a = b; b = 1; c = a + b; }")

def test_parser_125():
    """Function with no ftype"""
    test_valid("add(int a, int b) { return a + b; }")

def test_parser_126():
    """Function with no ftype (wrong)"""
    test_invalid("add(int a, int b) { return a + b; }")
# ============================================================================
# VARIABLE DECLARATION TESTS (10 tests)
# ============================================================================

def test_parser_036():
    """Auto with init"""
    test_valid("void main() { auto x = 10; }")


def test_parser_037():
    """Auto without init"""
    test_valid("void main() { auto x; }")


def test_parser_038():
    """Int with init"""
    test_valid("void main() { int x = 10; }")


def test_parser_039():
    """Int without init"""
    test_valid("void main() { int x; }")


def test_parser_040():
    """Float and string declarations"""
    test_valid('void main() { float x = 3.14; string s = "hello"; }')


def test_parser_041():
    """Struct variable with init"""
    test_valid("""
        struct Point { int x; int y; };
        void main() { Point p = {10, 20}; }
    """)


def test_parser_042():
    """Multiple variable declarations"""
    test_valid("""
        void main() {
            int x = 5;
            float y = 3.14;
            auto z = x + y;
        }
    """)


def test_parser_043():
    """Variable initialized with expression"""
    test_valid("""
        void main() {
            int a = 5;
            int b = 10;
            auto sum = a + b * 2;
        }
    """)


def test_parser_044():
    """Missing semicolon - should fail"""
    test_invalid("void main() { int x }")


def test_parser_045():
    """Void variable - should fail"""
    test_invalid("void main() { void x; }")


# ============================================================================
# IF STATEMENT TESTS (5 tests)
# ============================================================================

def test_parser_046():
    """Simple if statement"""
    test_valid("void main() { if (1) { } }")


def test_parser_047():
    """If with else"""
    test_valid("void main() { if (1) { } else { } }")


def test_parser_048():
    """If without braces"""
    test_valid("void main() { if (x > 0) x = x + 1; }")


def test_parser_049():
    """Nested if"""
    test_valid("""
        void main() {
            if (x > 0) {
                if (y < 10) {
                    x = y;
                }
            }
        }
    """)


def test_parser_050():
    """If without condition - should fail"""
    test_invalid("void main() { if () { } }")


# ============================================================================
# WHILE STATEMENT TESTS (5 tests)
# ============================================================================

def test_parser_051():
    """Simple while loop"""
    test_valid("void main() { while (1) { } }")


def test_parser_052():
    """While with condition"""
    test_valid("void main() { while (x < 10) { x = x + 1; } }")


def test_parser_053():
    """While with break and continue"""
    test_valid("""
        void main() {
            while (1) {
                if (x == 5) break;
                if (x == 3) continue;
                x = x + 1;
            }
        }
    """)


def test_parser_054():
    """Nested while loops"""
    test_valid("""
        void main() {
            while (i < 10) {
                while (j < 10) {
                    j = j + 1;
                }
                i = i + 1;
            }
        }
    """)


def test_parser_055():
    """While without condition - should fail"""
    test_invalid("void main() { while () { } }")


# ============================================================================
# FOR STATEMENT TESTS (10 tests)
# ============================================================================

def test_parser_056():
    """Complete for loop"""
    test_valid("void main() { for (int i = 0; i < 10; i++) { } }")


def test_parser_057():
    """For with empty init"""
    test_valid("void main() { for (; i < 10; i++) { } }")


def test_parser_058():
    """For with empty condition"""
    test_valid("void main() { for (int i = 0; ; i++) { } }")


def test_parser_059():
    """For with empty update"""
    test_valid("void main() { for (int i = 0; i < 10; ) { } }")


def test_parser_060():
    """For with all empty (infinite loop)"""
    test_valid("void main() { for (; ; ) { } }")


def test_parser_061():
    """For with auto init"""
    test_valid("void main() { for (auto i = 0; i < 10; i++) { } }")


def test_parser_062():
    """For without type in init"""
    test_valid("void main() { for (i = 0; i < 10; i++) { } }")


def test_parser_063():
    """For without braces"""
    test_valid("void main() { for (int i = 0; i < 10; i++) printInt(i); }")


def test_parser_064():
    """Nested for loops"""
    test_valid("""
        void main() {
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    printInt(i + j);
                }
            }
        }
    """)


def test_parser_065():
    """For missing semicolon - should fail"""
    test_invalid("void main() { for (int i = 0 i < 10; i++) { } }")


# ============================================================================
# SWITCH STATEMENT TESTS (10 tests)
# ============================================================================

def test_parser_066():
    """Simple switch statement"""
    test_valid("void main() { switch (1) { case 1: break; } }")


def test_parser_067():
    """Switch with default"""
    test_valid("void main() { switch (1) { case 1: break; default: break; } }")


def test_parser_068():
    """Switch with multiple cases"""
    test_valid("""
        void main() {
            switch (x) {
                case 1: printInt(1); break;
                case 2: printInt(2); break;
                case 3: printInt(3); break;
            }
        }
    """)


def test_parser_069():
    """Switch with fall-through"""
    test_valid("""
        void main() {
            switch (x) {
                case 1:
                case 2:
                    printInt(2);
                    break;
            }
        }
    """)


def test_parser_070():
    """Switch with empty case"""
    test_valid("void main() { switch (x) { case 1: } }")


def test_parser_071():
    """Switch case with expression"""
    test_valid("void main() { switch (x) { case 1+2: break; case -5: break; } }")


def test_parser_072():
    """Switch with empty body"""
    test_valid("void main() { switch (x) { } }")


def test_parser_073():
    """Switch with only default"""
    test_valid("void main() { switch (x) { default: break; } }")


def test_parser_074():
    """Nested switch"""
    test_valid("""
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


def test_parser_075():
    """Switch case without colon - should fail"""
    test_invalid("void main() { switch (x) { case 1 break; } }")


# ============================================================================
# EXPRESSION TESTS (15 tests)
# ============================================================================

def test_parser_076():
    """Arithmetic expressions"""
    test_valid("void main() { auto x = 1 + 2 - 3 * 4 / 5 % 2; }")


def test_parser_077():
    """Comparison expressions"""
    test_valid("void main() { auto x = 1 < 2 && 3 > 4 || 5 <= 6 && 7 >= 8; }")


def test_parser_078():
    """Logical expressions"""
    test_valid("void main() { auto x = 1 && 2 || !3; }")


def test_parser_079():
    """Increment and decrement"""
    test_valid("void main() { int x; --x; x++; --x; x--; }")


def test_parser_080():
    """Unary operators"""
    test_valid("void main() { auto x = -5; auto y = +3; auto z = !0; }")


def test_parser_081():
    """Parenthesized expressions"""
    test_valid("void main() { auto x = (1 + 2) * (3 - 4); }")


def test_parser_082():
    """Member access"""
    test_valid("""
        struct Point { int x; int y; };
        void main() {
            Point p = {1, 2};
            auto a = p.x;
            auto b = p.y;
        }
    """)


def test_parser_083():
    """Nested member access"""
    test_valid("""
        struct Inner { int value; };
        struct Outer { Inner inner; };
        void main() {
            Outer o;
            auto x = o.inner.value;
        }
    """)


def test_parser_084():
    """Function call"""
    test_valid("""
        int getValue() { return 42; }
        void main() { auto x = getValue(); }
    """)


def test_parser_085():
    """Function call with arguments"""
    test_valid("""
        int add(int a, int b, int c) { return a + b + c; }
        void main() { auto x = add(3, 5, 7); }
    """)


def test_parser_086():
    """Struct literal"""
    test_valid("""
        struct Point { int x; int y; };
        void main() { Point p = {10, 20}; }
    """)


def test_parser_087():
    """Complex precedence"""
    test_valid("void main() { auto x = 1 + 2 * 3 < 4 && 5 || !6; }")


def test_parser_088():
    """Chained assignment"""
    test_valid("void main() { int a, b, c; a = b = c = 5; }")


def test_parser_089():
    """Assignment in expression"""
    test_valid("void main() { int x, y; y = (x = 5) + 7; }")


def test_parser_090():
    """Member access with postfix"""
    test_valid("""
        struct Point { int x; };
        void main() {
            Point p;
            p.x = 10;
            ++p.x;
        }
    """)


# ============================================================================
# COMPLEX/INTEGRATION TESTS (5 tests)
# ============================================================================

def test_parser_091():
    """Factorial function"""
    test_valid("""
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


def test_parser_092():
    """Loop with calculations"""
    test_valid("""
        void main() {
            int sum = 0;
            for (int i = 1; i <= 10; i++) {
                sum = sum + i;
                if (sum > 30) break;
            }
        }
    """)


def test_parser_093():
    """Struct operations"""
    test_valid("""
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


def test_parser_094():
    """All statement types"""
    test_valid("""
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


def test_parser_095():
    """Complex expressions with all operators"""
    test_valid("""
        struct Point { int x; };
        int getValue() { return 5; }
        void main() {
            Point p = {5};
            auto result = p.x++ + getValue() * 2 < 10 && 1 || !0;
        }
    """)


# ============================================================================
# ERROR/EDGE CASE TESTS (5 tests)
# ============================================================================

def test_parser_096():
    """Missing brace - should fail"""
    test_invalid("void main() { int x = 5;")


def test_parser_097():
    """Mismatched braces - should fail"""
    test_invalid("void main() { if (1) { }")


def test_parser_098():
    """Invalid expression - should fail"""
    test_invalid("void main() { int x = + * 5; }")


def test_parser_099():
    """Incomplete struct - should fail"""
    test_invalid("struct Point {")


def test_parser_100():
    """Empty parameter (just comma) - should fail"""
    test_invalid("int add(int a, , int b) { return 0; }")

def test_demo_1():
    test_valid("""
        void main() {
            int x,y;
        }        
    """)

def test_demo_2():
    test_valid("""
        void main() { auto x; x = 5; }       
    """)
