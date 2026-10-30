"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


def test_parser_001():
    """Test 1"""
    parser = Parser("")
    assert parser.parse() == "success"


def test_parser_002():
    """Test 2"""
    parser = Parser("void main() { }")
    assert parser.parse() == "success"


def test_parser_003():
    """Test 3"""
    parser = Parser("struct Circle { int rad; };")
    assert parser.parse() == "success"


def test_parser_004():
    """Test 4"""
    parser = Parser("struct Vector { int dx; }; void main() { }")
    assert parser.parse() == "success"


def test_parser_005():
    """Test 5"""
    parser = Parser("""
        int multiply(int m, int n) { return m * n; }
        void main() { }
    """)
    assert parser.parse() == "success"


def test_parser_006():
    """Test 6"""
    parser = Parser("""
        struct Node { int val; int next; };
        struct Student { string fullname; int score; };
    """)
    assert parser.parse() == "success"


def test_parser_007():
    """Test 7"""
    parser = Parser("""
        struct Rectangle { int w; };
        int utility() { return 1; }
        struct Employee { string title; };
        void main() { }
    """)
    assert parser.parse() == "success"


def test_parser_008():
    """Test 8"""
    parser = Parser("struct Circle { int rad; }")
    result = parser.parse()
    assert result != "success"


def test_parser_009():
    """Test 9"""
    parser = Parser("3 * 7;")
    result = parser.parse()
    assert result != "success"


def test_parser_010():
    """Test 10"""
    parser = Parser("int num = 42;")
    result = parser.parse()
    assert result != "success"


def test_parser_011():
    """Test 11"""
    parser = Parser("""struct Blank {};""")
    assert parser.parse() == "success"


def test_parser_012():
    """Test 12"""
    parser = Parser("struct Node { int data; };")
    assert parser.parse() == "success"


def test_parser_013():
    """Test 13"""
    parser = Parser("struct Vector { int dx; int dy; float w; };")
    assert parser.parse() == "success"


def test_parser_014():
    """Test 14"""
    parser = Parser("struct Employee { string title; int id; float salary; };")
    assert parser.parse() == "success"


def test_parser_015():
    """Test 15"""
    parser = Parser("""
        struct Circle { int rad; int cy; };
        struct Drawing { Circle center; int scale; };
    """)
    assert parser.parse() == "success"


def test_parser_016():
    """Test 16"""
    parser = Parser("struct Invalid { auto field; };")
    result = parser.parse()
    assert result != "success"


def test_parser_017():
    """Test 17"""
    parser = Parser("struct Node { int val }")
    result = parser.parse()
    assert result != "success"


def test_parser_018():
    """Test 18"""
    parser = Parser("struct Wrong { item; };")
    result = parser.parse()
    assert result != "success"


def test_parser_019():
    """Test 19"""
    parser = Parser("struct Invalid { void member; };")
    result = parser.parse()
    assert result != "success"


def test_parser_020():
    """Test 20"""
    parser = Parser("struct Container { struct Item { int id; }; };")
    result = parser.parse()
    assert result != "success"


def test_parser_021():
    """Test 21"""
    parser = Parser("void main() { }")
    assert parser.parse() == "success"


def test_parser_022():
    """Test 22"""
    parser = Parser("int getOne() { return 1; }")
    assert parser.parse() == "success"


def test_parser_023():
    """Test 23"""
    parser = Parser("int triple(int num) { return num * 3; }")
    assert parser.parse() == "success"


def test_parser_024():
    """Test 24"""
    parser = Parser("int sum(int p, int q, int r) { return p + q + r; }")
    assert parser.parse() == "success"


def test_parser_025():
    """Test 25"""
    parser = Parser("""
        struct Circle { int radius; int cy; };
        int getRadius(Circle c) { return c.radius; }
    """)
    assert parser.parse() == "success"


def test_parser_026():
    """Test 26"""
    parser = Parser("compute(int m, int n) { return m + n; }")
    assert parser.parse() == "success"


def test_parser_027():
    """Test 27"""
    parser = Parser('string getTitle() { return "demo"; }')
    assert parser.parse() == "success"


def test_parser_028():
    """Test 28"""
    parser = Parser("float getPi() { return 3.14159; }")
    assert parser.parse() == "success"


def test_parser_029():
    """Test 29"""
    parser = Parser("""
        struct Vector { int dx; int dy; };
        Vector zero() { return {0, 0}; }
    """)
    assert parser.parse() == "success"


def test_parser_030():
    """Test 30"""
    parser = Parser("""
        int fib(int n) {
            if (n <= 2) {
                return 1;
            } else {
                return fib(n - 1) + fib(n - 2);
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_031():
    """Test 31"""
    parser = Parser("int invalid(auto param) { return 0; }")
    result = parser.parse()
    assert result != "success"


def test_parser_032():
    """Test 32"""
    parser = Parser("int declaration();")
    result = parser.parse()
    assert result != "success"


def test_parser_033():
    """Test 33"""
    parser = Parser("int wrong(arg) { return 0; }")
    result = parser.parse()
    assert result != "success"


def test_parser_034():
    """Test 34"""
    parser = Parser("int wrong(void param) { return 0; }")
    result = parser.parse()
    assert result != "success"


def test_parser_035():
    """Test 35"""
    parser = Parser("int broken { return 0; }")
    result = parser.parse()
    assert result != "success"


def test_parser_036():
    """Test 36"""
    parser = Parser("void main() { auto val = 25; }")
    assert parser.parse() == "success"


def test_parser_037():
    """Test 37"""
    parser = Parser("void main() { auto num; }")
    assert parser.parse() == "success"


def test_parser_038():
    """Test 38"""
    parser = Parser("void main() { int count = 17; }")
    assert parser.parse() == "success"


def test_parser_039():
    """Test 39"""
    parser = Parser("void main() { int total; }")
    assert parser.parse() == "success"


def test_parser_040():
    """Test 40"""
    parser = Parser('void main() { float pi = 3.14159; string msg = "hi"; }')
    assert parser.parse() == "success"


def test_parser_041():
    """Test 41"""
    parser = Parser("""
        struct Vector { int dx; int dy; };
        void main() { Vector v = {15, 30}; }
    """)
    assert parser.parse() == "success"


def test_parser_042():
    """Test 42"""
    parser = Parser("""
        void main() {
            int num = 7;
            float ratio = 2.718;
            auto result = num + ratio;
        }
    """)
    assert parser.parse() == "success"


def test_parser_043():
    """Test 43"""
    parser = Parser("""
        void main() {
            int m = 8;
            int n = 12;
            auto product = m * n - 4;
        }
    """)
    assert parser.parse() == "success"


def test_parser_044():
    """Test 44"""
    parser = Parser("void main() { int total }")
    result = parser.parse()
    assert result != "success"


def test_parser_045():
    """Test 45"""
    parser = Parser("void main() { void invalid; }")
    result = parser.parse()
    assert result != "success"


def test_parser_046():
    """Test 46"""
    parser = Parser("void main() { if (1) { } }")
    assert parser.parse() == "success"


def test_parser_047():
    """Test 47"""
    parser = Parser("void main() { if (0) { } else { } }")
    assert parser.parse() == "success"


def test_parser_048():
    """Test 48"""
    parser = Parser("void main() { if (count > 5) count = count + 2; }")
    assert parser.parse() == "success"


def test_parser_049():
    """Test 49"""
    parser = Parser("""
        void main() {
            if (num > 3) {
                if (val < 20) {
                    num = val;
                }
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_050():
    """Test 50"""
    parser = Parser("void main() { if () { } }")
    result = parser.parse()
    assert result != "success"


def test_parser_051():
    """Test 51"""
    parser = Parser("void main() { while (1) { } }")
    assert parser.parse() == "success"


def test_parser_052():
    """Test 52"""
    parser = Parser("void main() { while (count < 15) { count = count + 3; } }")
    assert parser.parse() == "success"


def test_parser_053():
    """Test 53"""
    parser = Parser("""
        void main() {
            while (1) {
                if (total == 7) break;
                if (total == 4) continue;
                total = total + 2;
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_054():
    """Test 54"""
    parser = Parser("""
        void main() {
            while (row < 8) {
                while (col < 12) {
                    col = col + 2;
                }
                row = row + 1;
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_055():
    """Test 55"""
    parser = Parser("void main() { while () { } }")
    result = parser.parse()
    assert result != "success"


def test_parser_056():
    """Test 56"""
    parser = Parser("void main() { for (int idx = 1; idx < 20; idx++) { } }")
    assert parser.parse() == "success"


def test_parser_057():
    """Test 57"""
    parser = Parser("void main() { for (; row < 15; row++) { } }")
    assert parser.parse() == "success"


def test_parser_058():
    """Test 58"""
    parser = Parser("void main() { for (int k = 2; ; k++) { } }")
    assert parser.parse() == "success"


def test_parser_059():
    """Test 59"""
    parser = Parser("void main() { for (int j = 3; j < 25; ) { } }")
    assert parser.parse() == "success"


def test_parser_060():
    """Test 60"""
    parser = Parser("void main() { for (; ; ) { } }")
    assert parser.parse() == "success"


def test_parser_061():
    """Test 61"""
    parser = Parser("void main() { for (auto n = 1; n < 18; n++) { } }")
    assert parser.parse() == "success"


def test_parser_062():
    """Test 62"""
    parser = Parser("void main() { for (counter = 2; counter < 16; counter++) { } }")
    assert parser.parse() == "success"


def test_parser_063():
    """Test 63"""
    parser = Parser("void main() { for (int pos = 0; pos < 14; pos++) printInt(pos); }")
    assert parser.parse() == "success"


def test_parser_064():
    """Test 64"""
    parser = Parser("""
        void main() {
            for (int row = 1; row < 9; row++) {
                for (int col = 1; col < 7; col++) {
                    printInt(row + col);
                }
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_065():
    """Test 65"""
    parser = Parser("void main() { for (int idx = 0 idx < 20; idx++) { } }")
    result = parser.parse()
    assert result != "success"


def test_parser_066():
    """Test 66"""
    parser = Parser("void main() { switch (2) { case 2: break; } }")
    assert parser.parse() == "success"


def test_parser_067():
    """Test 67"""
    parser = Parser("void main() { switch (3) { case 3: break; default: break; } }")
    assert parser.parse() == "success"


def test_parser_068():
    """Test 68"""
    parser = Parser("""
        void main() {
            switch (choice) {
                case 2: printInt(2); break;
                case 4: printInt(4); break;
                case 6: printInt(6); break;
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_069():
    """Test 69"""
    parser = Parser("""
        void main() {
            switch (val) {
                case 2:
                case 4:
                    printInt(4);
                    break;
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_070():
    """Test 70"""
    parser = Parser("void main() { switch (num) { case 3: } }")
    assert parser.parse() == "success"


def test_parser_071():
    """Test 71"""
    parser = Parser("void main() { switch (val) { case 2+4: break; case -7: break; } }")
    assert parser.parse() == "success"


def test_parser_072():
    """Test 72"""
    parser = Parser("void main() { switch (choice) { } }")
    assert parser.parse() == "success"


def test_parser_073():
    """Test 73"""
    parser = Parser("void main() { switch (input) { default: break; } }")
    assert parser.parse() == "success"


def test_parser_074():
    """Test 74"""
    parser = Parser("""
        void main() {
            switch (outer) {
                case 2:
                    switch (inner) {
                        case 4: break;
                    }
                    break;
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_075():
    """Test 75"""
    parser = Parser("void main() { switch (val) { case 2 break; } }")
    result = parser.parse()
    assert result != "success"


def test_parser_076():
    """Test 76"""
    parser = Parser("void main() { auto res = 2 + 4 - 6 * 8 / 3 % 5; }")
    assert parser.parse() == "success"


def test_parser_077():
    """Test 77"""
    parser = Parser("void main() { auto res = 2 < 5 && 6 > 8 || 9 <= 11 && 13 >= 15; }")
    assert parser.parse() == "success"


def test_parser_078():
    """Test 78"""
    parser = Parser("void main() { auto res = 2 && 5 || !7; }")
    assert parser.parse() == "success"


def test_parser_079():
    """Test 79"""
    parser = Parser("void main() { int count; --count; count++; --count; count--; }")
    assert parser.parse() == "success"


def test_parser_080():
    """Test 80"""
    parser = Parser("void main() { auto num = -8; auto val = +6; auto flag = !1; }")
    assert parser.parse() == "success"


def test_parser_081():
    """Test 81"""
    parser = Parser("void main() { auto total = (2 + 5) * (7 - 9); }")
    assert parser.parse() == "success"


def test_parser_082():
    """Test 82"""
    parser = Parser("""
        struct Circle { int radius; int cy; };
        void main() {
            Circle c = {3, 7};
            auto r = c.radius;
            auto cy = c.cy;
        }
    """)
    assert parser.parse() == "success"


def test_parser_083():
    """Test 83"""
    parser = Parser("""
        struct Core { int data; };
        struct Shell { Core inside; };
        void main() {
            Shell obj;
            auto val = obj.inside.data;
        }
    """)
    assert parser.parse() == "success"


def test_parser_084():
    """Test 84"""
    parser = Parser("""
        int compute() { return 84; }
        void main() { auto num = compute(); }
    """)
    assert parser.parse() == "success"


def test_parser_085():
    """Test 85"""
    parser = Parser("""
        int sum(int m, int n, int p) { return m + n + p; }
        void main() { auto total = sum(4, 9, 13); }
    """)
    assert parser.parse() == "success"


def test_parser_086():
    """Test 86"""
    parser = Parser("""
        struct Vector { int dx; int dy; };
        void main() { Vector v = {18, 24}; }
    """)
    assert parser.parse() == "success"


def test_parser_087():
    """Test 87"""
    parser = Parser("void main() { auto res = 3 + 5 * 7 < 9 && 11 || !13; }")
    assert parser.parse() == "success"


def test_parser_088():
    """Test 88"""
    parser = Parser("void main() { int p, q, r; p = q = r = 8; }")
    assert parser.parse() != "success"


def test_parser_089():
    """Test 89"""
    parser = Parser("void main() { int m; int n; n = (m = 9) + 15; }")
    assert parser.parse() == "success"


def test_parser_090():
    """Test 90"""
    parser = Parser("""
        struct Node { int val; };
        void main() {
            Node nd;
            nd.val = 18;
            ++nd.val;
        }
    """)
    assert parser.parse() == "success"


def test_parser_091():
    """Test 91"""
    parser = Parser("""
        int power(int base, int exp) {
            if (exp <= 0) {
                return 1;
            } else {
                return base * power(base, exp - 1);
            }
        }
        void main() {
            auto answer = power(3, 4);
        }
    """)
    assert parser.parse() == "success"


def test_parser_092():
    """Test 92"""
    parser = Parser("""
        void main() {
            int total = 1;
            for (int k = 2; k <= 15; k++) {
                total = total + k;
                if (total > 50) break;
            }
        }
    """)
    assert parser.parse() == "success"


def test_parser_093():
    """Test 93"""
    parser = Parser("""
        struct Vector { int dx; int dy; };
        
        Vector makeVector(int dx, int dy) {
            return {dx, dy};
        }
        
        void main() {
            Vector v1 = makeVector(12, 24);
            Vector v2;
            v2 = v1;
            v2.dx = v2.dx + 8;
        }
    """)
    assert parser.parse() == "success"


def test_parser_094():
    """Test 94"""
    parser = Parser("""
        void main() {
            int num = 1;
            
            if (num == 1) {
                num = 2;
            }
            
            while (num < 18) {
                num++;
            }
            
            for (int k = 1; k < 9; k++) {
                num = num + k;
            }
            
            switch (num) {
                case 18:
                    break;
                default:
                    num = 1;
                    break;
            }
            
            return;
        }
    """)
    assert parser.parse() == "success"


def test_parser_095():
    """Test 95"""
    parser = Parser("""
        struct Node { int data; };
        int compute() { return 9; }
        void main() {
            Node nd = {7};
            auto answer = nd.data++ + compute() * 3 < 18 && 2 || !1;
        }
    """)
    assert parser.parse() == "success"


def test_parser_096():
    """Test 96"""
    parser = Parser("void main() { int count = 9;")
    result = parser.parse()
    assert result != "success"


def test_parser_097():
    """Test 97"""
    parser = Parser("void main() { if (2) { }")
    result = parser.parse()
    assert result != "success"


def test_parser_098():
    """Test 98"""
    parser = Parser("void main() { int num = + * 7; }")
    result = parser.parse()
    assert result != "success"


def test_parser_099():
    """Test 99"""
    parser = Parser("struct Vector {")
    result = parser.parse()
    assert result != "success"


def test_parser_100():
    """Test 100"""
    parser = Parser("int compute(int m, , int n) { return 0; }")
    result = parser.parse()
    assert result != "success"
    