"""
COMPREHENSIVE EXTREME EDGE CASE TESTS FOR TyC PARSER
100 extremely difficult test cases covering all subtle parser ambiguities,
operator precedence extremes, expression disambiguation, and hidden errors.
"""

import pytest
from tests.utils import Parser

def test_valid(source):
    parser = Parser(source)
    assert parser.parse() == "success"

def test_invalid(source):
    parser = Parser(source)
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result

# ============================================================================
# GROUP 1: EXPRESSION STATEMENT DISAMBIGUATION (15 tests)
# Testing the ambiguity between assignments, calls, and standalone expressions
# ============================================================================

def test_extreme_001():
    """Standalone expression statement - just expression"""
    test_valid("void main() { 1 + 2 * 3; }")

def test_extreme_002():
    """Function call as expression statement"""
    test_valid("void main() { print(); }")

def test_extreme_003():
    """Postfix increment as expression statement"""
    test_valid("void main() { int x; x++; }")

def test_extreme_004():
    """Prefix increment as expression statement"""
    test_valid("void main() { int x; ++x; }")

def test_extreme_005():
    """Member access assignment"""
    test_valid("""
        struct S { int x; };
        void main() {
            S s;
            s.x = 10;
        }
    """)

def test_extreme_006():
    """Chained member access assignment"""
    test_valid("""
        struct A { B b; };
        struct B { int x; };
        void main() {
            A a;
            a.b.x = 5;
        }
    """)

def test_extreme_007():
    """Function call with member access"""
    test_valid("void main() { obj.method(); }")

def test_extreme_008():
    """Assignment within function call argument"""
    test_valid("void main() { int x; f(x = 5); }")

def test_extreme_009():
    """Parenthesized expression as statement"""
    test_valid("void main() { int x; (x); }")

def test_extreme_010():
    """Multiple assignments in one statement"""
    test_valid("void main() { int a, b, c; a = b = c = 10; }")

def test_extreme_011():
    """Assignment in expression context"""
    test_valid("void main() { int a, b; auto x = (a = 5) + (b = 10); }")

def test_extreme_012():
    """Postfix on member access"""
    test_valid("""
        struct S { int x; };
        void main() {
            S s;
            s.x++;
        }
    """)

def test_extreme_013():
    """Prefix on member access"""
    test_valid("""
        struct S { int x; };
        void main() {
            S s;
            ++s.x;
        }
    """)

def test_extreme_014():
    """Cannot increment function call result - INVALID"""
    test_invalid("""
        int f() { return 5; }
        void main() {
            f()++;
        }
    """)

def test_extreme_015():
    """Cannot assign to function call - INVALID"""
    test_invalid("void main() { f() = 5; }")

# ============================================================================
# GROUP 2: OPERATOR PRECEDENCE EXTREMES (20 tests)
# Testing all 11 precedence levels in complex combinations
# ============================================================================

def test_extreme_016():
    """Member access (highest) > postfix > prefix > unary"""
    test_valid("""
        struct S { int x; };
        void main() {
            S s;
            auto v = !++s.x++;
        }
    """)

def test_extreme_017():
    """All unary operators stacked"""
    test_valid("void main() { auto x = !-+!-5; }")

def test_extreme_018():
    """Multiple prefix increments"""
    test_valid("void main() { int x; +++++x; }")

def test_extreme_019():
    """Postfix cannot be stacked - INVALID"""
    test_invalid("void main() { int x; x++++; }")

def test_extreme_020():
    """Assignment has lowest precedence"""
    test_valid("void main() { int a, b; a = b = 1 + 2 * 3 < 5 && 10 || 0; }")

def test_extreme_021():
    """Logical OR > logical AND"""
    test_valid("void main() { auto x = 1 && 2 || 3 && 4; }")

def test_extreme_022():
    """Equality > relational"""
    test_valid("void main() { auto x = 1 < 2 == 3 > 4; }")

def test_extreme_023():
    """Additive > multiplicative"""
    test_valid("void main() { auto x = 1 + 2 * 3 - 4 / 5; }")

def test_extreme_024():
    """Unary minus on plus"""
    test_valid("void main() { auto x = -+5; }")

def test_extreme_025():
    """Double logical NOT"""
    test_valid("void main() { auto x = !!5; }")

def test_extreme_026():
    """Assignment in condition"""
    test_valid("void main() { int x; if ((x = 5) > 0) { } }")

def test_extreme_027():
    """Assignment in while condition"""
    test_valid("void main() { int x; while ((x = getVal()) > 0) { } }")

def test_extreme_028():
    """Assignment in for condition"""
    test_valid("void main() { int x; for (; (x = f()) < 10; ) { } }")

def test_extreme_029():
    """Chained relational operators (left associative)"""
    test_valid("void main() { auto x = 1 < 2 < 3; }")  # ((1 < 2) < 3)

def test_extreme_030():
    """Chained equality operators"""
    test_valid("void main() { auto x = 1 == 2 != 3 == 4; }")

def test_extreme_031():
    """Mixed arithmetic operators"""
    test_valid("void main() { auto x = 1 + 2 - 3 * 4 / 5 % 2; }")

def test_extreme_032():
    """Postfix on function call result followed by member access - INVALID"""
    test_invalid("""
        struct S { int x; };
        S f() { return {5}; }
        void main() {
            f()++.x;
        }
    """)

def test_extreme_033():
    """Member access on function call result"""
    test_valid("""
        struct S { int x; };
        S f() { return {5}; }
        void main() {
            auto v = f().x;
        }
    """)

def test_extreme_034():
    """Postfix on member of function result"""
    test_valid("""
        struct S { int x; };
        S f() { return {5}; }
        void main() {
            f().x++;
        }
    """)

def test_extreme_035():
    """Complex precedence chain"""
    test_valid("""
        struct S { int v; };
        void main() {
            S s;
            int a, b;
            a = s.v++ * -b + !a < 10 && 5 || b;
        }
    """)

# ============================================================================
# GROUP 3: NESTED STRUCTURES (10 tests)
# Testing deep nesting limits
# ============================================================================

def test_extreme_036():
    """Deeply nested if-else (dangling else problem)"""
    test_valid("""
        void main() {
            if (1) if (2) if (3) x = 1; else y = 2; else z = 3;
        }
    """)

def test_extreme_037():
    """Deeply nested blocks"""
    test_valid("""
        void main() {
            { { { { { { { { int x; } } } } } } } }
        }
    """)

def test_extreme_038():
    """Nested switch in switch in switch"""
    test_valid("""
        void main() {
            switch(a) {
                case 1:
                    switch(b) {
                        case 2:
                            switch(c) {
                                case 3: break;
                            }
                            break;
                    }
                    break;
            }
        }
    """)

def test_extreme_039():
    """Nested for in while in for"""
    test_valid("""
        void main() {
            for (;;) {
                while (1) {
                    for (int i = 0; i < 10; i++) {
                        break;
                    }
                }
            }
        }
    """)

def test_extreme_040():
    """Deeply nested parentheses"""
    test_valid("void main() { auto x = ((((((1 + 2) * 3) / 4) - 5) % 6)); }")

def test_extreme_041():
    """Deeply nested member access"""
    test_valid("""
        struct E { int val; };
        struct D { E e; };
        struct C { D d; };
        struct B { C c; };
        struct A { B b; };
        void main() {
            A a;
            a.b.c.d.e.val = 42;
        }
    """)

def test_extreme_042():
    """Deeply nested function calls"""
    test_valid("void main() { f(g(h(i(j(k(l(m()))))))); }")

def test_extreme_043():
    """Nested struct literals"""
    test_valid("""
        struct Inner { int x; int y; };
        struct Outer { Inner i; int z; };
        void main() {
            Outer o = {{1, 2}, 3};
        }
    """)

def test_extreme_044():
    """Mixed deep nesting"""
    test_valid("""
        void main() {
            {
                for (;;) {
                    {
                        while (1) {
                            {
                                if (x) {
                                    {
                                        switch (y) {
                                            case 1: { int z; } break;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    """)

def test_extreme_045():
    """Deep expression nesting in all operator levels"""
    test_valid("""
        void main() {
            auto x = (a = (b || (c && (d == (e < (f + (g * (h++)))))))); 
        }
    """)

# ============================================================================
# GROUP 4: FOR LOOP EDGE CASES (10 tests)
# Testing complex for loop variations
# ============================================================================

def test_extreme_046():
    """For with comma-separated multiple inits"""
    test_valid("void main() { for (int x = 0, y = 10; x < y; x++, y--) { } }")

def test_extreme_047():
    """For with all parts empty"""
    test_valid("void main() { for (;;) { } }")

def test_extreme_048():
    """For with assignment init (no type)"""
    test_valid("void main() { for (x = 0; x < 10; x++) { } }")

def test_extreme_049():
    """For with auto init"""
    test_valid("void main() { for (auto i = 0; i < 10; i++) { } }")

def test_extreme_050():
    """For with complex init expression"""
    test_valid("void main() { for (int x = f(g(h())); x < 10; x++) { } }")

def test_extreme_051():
    """For with complex condition"""
    test_valid("void main() { for (int i = 0; i < n && j > 0; i++) { } }")

def test_extreme_052():
    """For with complex update"""
    test_valid("void main() { for (int i = 0; i < 10; i = i * 2 + 1) { } }")

def test_extreme_053():
    """For with multiple updates separated by comma"""
    test_valid("void main() { for (int i = 0; i < 10; i++, j--, k = k * 2) { } }")

def test_extreme_054():
    """For init with multiple declarations separated by comma"""
    test_valid("void main() { for (int a = 1, b = 2, c = 3; a < 10; a++) { } }")

def test_extreme_055():
    """For with wrong separator - semicolon instead of comma - INVALID"""
    test_invalid("void main() { for (int i = 0; i < 10; i++) { } }")

# ============================================================================
# GROUP 5: SWITCH STATEMENT EDGE CASES (10 tests)
# Testing switch variations and edge cases
# ============================================================================

def test_extreme_056():
    """Switch with no cases or default"""
    test_valid("void main() { switch (x) { } }")

def test_extreme_057():
    """Switch with only default"""
    test_valid("void main() { switch (x) { default: break; } }")

def test_extreme_058():
    """Switch with case expression (not just literal)"""
    test_valid("void main() { switch (x) { case 1 + 2 * 3: break; } }")

def test_extreme_059():
    """Switch with negative case"""
    test_valid("void main() { switch (x) { case -5: break; } }")

def test_extreme_060():
    """Switch with parenthesized case value"""
    test_valid("void main() { switch (x) { case (5): break; } }")

def test_extreme_061():
    """Switch with fall-through cases"""
    test_valid("""
        void main() {
            switch (x) {
                case 1:
                case 2:
                case 3:
                    y = 10;
                    break;
            }
        }
    """)

def test_extreme_062():
    """Switch with empty case"""
    test_valid("void main() { switch (x) { case 1: } }")

def test_extreme_063():
    """Switch case without colon - INVALID"""
    test_invalid("void main() { switch (x) { case 1 break; } }")

def test_extreme_064():
    """Switch with default before cases"""
    test_valid("""
        void main() {
            switch (x) {
                default: x = 0; break;
                case 1: x = 1; break;
            }
        }
    """)

def test_extreme_065():
    """Switch with multiple defaults - INVALID (grammar might allow but semantically wrong)"""
    test_invalid("""
        void main() {
            switch (x) {
                default: break;
                default: break;
            }
        }
    """)

# ============================================================================
# GROUP 6: EXPRESSION vs STATEMENT DISAMBIGUATION (10 tests)
# Testing cases where grammar might be ambiguous
# ============================================================================

def test_extreme_066():
    """ID() - function call statement"""
    test_valid("void main() { f(); }")

def test_extreme_067():
    """ID.ID - member access as expression statement"""
    test_valid("""
        struct S { int x; };
        void main() {
            S s;
            s.x;
        }
    """)

def test_extreme_068():
    """ID.ID() - member function call"""
    test_valid("void main() { obj.method(); }")

def test_extreme_069():
    """ID++ - postfix as statement"""
    test_valid("void main() { int x; x++; }")

def test_extreme_070():
    """++ID - prefix as statement"""
    test_valid("void main() { int x; ++x; }")

def test_extreme_071():
    """ID = expr - assignment statement"""
    test_valid("void main() { int x; x = 5; }")

def test_extreme_072():
    """(expr) - parenthesized expression as statement"""
    test_valid("void main() { (1 + 2); }")

def test_extreme_073():
    """Struct literal as statement - INVALID"""
    test_invalid("void main() { {1, 2, 3}; }")

def test_extreme_074():
    """Assignment to rvalue - INVALID"""
    test_invalid("void main() { 5 = x; }")

def test_extreme_075():
    """Member access on literal - INVALID"""
    test_invalid("void main() { 5.x; }")

# ============================================================================
# GROUP 7: STRUCT LITERAL EDGE CASES (10 tests)
# Testing struct literal variations
# ============================================================================

def test_extreme_076():
    """Empty struct literal"""
    test_valid("""
        struct Empty {};
        void main() {
            Empty e = {};
        }
    """)

def test_extreme_077():
    """Struct literal with expressions"""
    test_valid("""
        struct Point { int x; int y; };
        void main() {
            Point p = {1 + 2, 3 * 4};
        }
    """)

def test_extreme_078():
    """Struct literal with function calls"""
    test_valid("""
        struct Point { int x; int y; };
        void main() {
            Point p = {f(), g()};
        }
    """)

def test_extreme_079():
    """Nested struct literals"""
    test_valid("""
        struct Inner { int a; int b; };
        struct Outer { Inner i; int c; };
        void main() {
            Outer o = {{1, 2}, 3};
        }
    """)

def test_extreme_080():
    """Triple-nested struct literals"""
    test_valid("""
        struct A { int x; };
        struct B { A a; };
        struct C { B b; };
        void main() {
            C c = {{{5}}};
        }
    """)

def test_extreme_081():
    """Struct literal in function argument"""
    test_valid("""
        struct Point { int x; int y; };
        void f(Point p) { }
        void main() {
            f({5, 10});
        }
    """)

def test_extreme_082():
    """Struct literal in return statement"""
    test_valid("""
        struct Point { int x; int y; };
        Point getPoint() {
            return {5, 10};
        }
    """)

def test_extreme_083():
    """Struct literal with complex nested expressions"""
    test_valid("""
        struct Point { int x; int y; };
        void main() {
            Point p = {a + b * c, (d = e) + f};
        }
    """)

def test_extreme_084():
    """Struct literal with too many initializers (parser allows, semantic error)"""
    test_valid("""
        struct Point { int x; };
        void main() {
            Point p = {1, 2, 3, 4, 5};
        }
    """)

def test_extreme_085():
    """Struct literal with too few initializers"""
    test_valid("""
        struct Point { int x; int y; int z; };
        void main() {
            Point p = {1};
        }
    """)

# ============================================================================
# GROUP 8: SUBTLE SYNTAX ERRORS (10 tests)
# Testing cases that should fail parsing
# ============================================================================

def test_extreme_086():
    """Empty statement (single semicolon) - INVALID per spec"""
    test_invalid("void main() { ; }")

def test_extreme_087():
    """Multiple semicolons - INVALID"""
    test_invalid("void main() { ;; }")

def test_extreme_088():
    """Missing semicolon after statement"""
    test_invalid("void main() { int x = 5 }")

def test_extreme_089():
    """Missing closing brace"""
    test_invalid("void main() { int x = 5;")

def test_extreme_090():
    """Mismatched braces"""
    test_invalid("void main() { { int x; }")

def test_extreme_091():
    """Invalid operator sequence"""
    test_invalid("void main() { auto x = 5 ++ 2; }")

def test_extreme_092():
    """Function call without closing paren"""
    test_invalid("void main() { f(1, 2; }")

def test_extreme_093():
    """Case without colon"""
    test_invalid("void main() { switch(x) { case 1 break; } }")

def test_extreme_094():
    """If without condition"""
    test_invalid("void main() { if () { } }")

def test_extreme_095():
    """While without condition"""
    test_invalid("void main() { while () { } }")

# ============================================================================
# GROUP 9: COMPLEX REAL-WORLD SCENARIOS (5 tests)
# Testing realistic complex code
# ============================================================================

def test_extreme_096():
    """Recursive factorial with all statement types"""
    test_valid("""
        int factorial(int n) {
            if (n <= 1) {
                return 1;
            }
            auto result = n * factorial(n - 1);
            return result;
        }
        void main() {
            int x = factorial(5);
        }
    """)

def test_extreme_097():
    """Complex nested control flow"""
    test_valid("""
        void main() {
            for (int i = 0; i < 10; i++) {
                while (j < i) {
                    switch (k) {
                        case 1:
                            if (m) {
                                for (auto n = 0; n < 5; n++) {
                                    if (p) break;
                                    else continue;
                                }
                            } else {
                                while (q) {
                                    if (r) break;
                                }
                            }
                            break;
                        default:
                            break;
                    }
                    j++;
                }
            }
        }
    """)

def test_extreme_098():
    """Complex struct operations"""
    test_valid("""
        struct Point { int x; int y; };
        struct Line { Point start; Point end; };
        
        Point midpoint(Line l) {
            return {(l.start.x + l.end.x) / 2, (l.start.y + l.end.y) / 2};
        }
        
        void main() {
            Line line = {{0, 0}, {10, 10}};
            Point mid = midpoint(line);
            mid.x++;
            auto val = mid.x + mid.y;
        }
    """)

def test_extreme_099():
    """Complex expression with all operators"""
    test_valid("""
        struct S { int v; };
        void main() {
            S s, t;
            int a, b, c, d;
            auto result = (a = s.v++ * -b + !c < d) && (t.v-- / +a > b) || !(--c == ++d);
        }
    """)

def test_extreme_100():
    """All features combined in realistic code"""
    test_valid("""
        struct Node { int data; Node next; };
        
        Node createNode(int val) {
            Node n;
            n.data = val;
            return n;
        }
        
        void main() {
            auto head = createNode(1);
            
            for (int i = 2; i <= 10; i++) {
                Node current = head;
                while (current.next.data != 0) {
                    current = current.next;
                }
                current.next = createNode(i);
            }
            
            int sum = 0;
            Node iter = head;
            while (iter.data != 0) {
                sum = sum + iter.data;
                iter = iter.next;
                if (sum > 100) break;
            }
            
            switch (sum) {
                case 0:
                case 10:
                case 20:
                    printInt(sum);
                    break;
                default:
                    printString("Other value");
                    break;
            }
        }
    """)
