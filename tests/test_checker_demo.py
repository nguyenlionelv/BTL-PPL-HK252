# ===========================================================================
# TESTS 101–300: ADVANCED / COMPREHENSIVE
# ===========================================================================

# ---------------------------------------------------------------------------
# SECTION A: Valid programs — complex interactions (101–140)
# ---------------------------------------------------------------------------


def test_checker_101():
    """Valid: inferred return type is void (no return stmt)."""
    source = """
greet(string name) {
    printString(name);
}
void main() {
    greet("Alice");
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_102():
    """Valid: inferred return type is float."""
    source = """
multiply(float a, float b) {
    return a * b;
}
void main() {
    auto r = multiply(2.5, 3.0);
    printFloat(r);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_103():
    """Valid: recursive function (factorial)."""
    source = """
int factorial(int n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}
void main() {
    int result = factorial(5);
    printInt(result);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_104():
    """Valid: struct with nested struct member, fully initialised."""
    source = """
struct Vec2 {
    float x;
    float y;
};
struct Transform {
    Vec2 position;
    Vec2 scale;
};
void main() {
    Vec2 pos = {1.0, 2.0};
    Vec2 sc = {1.0, 1.0};
    Transform t;
    t.position = pos;
    t.scale = sc;
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_105():
    """Valid: member access on function return value."""
    source = """
struct Point {
    int x;
    int y;
};
Point makePoint(int a, int b) {
    Point p = {a, b};
    return p;
}
void main() {
    int x = makePoint(3, 4).x;
    printInt(x);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_106():
    """Valid: auto var inferred from arithmetic with already-typed var."""
    source = """
void main() {
    int a = 10;
    float b = 2.5;
    auto c = a + b;
    printFloat(c);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_107():
    """Valid: multiple auto vars inferred sequentially."""
    source = """
void main() {
    auto x = readInt();
    auto y = x * 2;
    auto z = y + 1;
    printInt(z);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_108():
    """Valid: for-init variable leaks into outer scope."""
    source = """
void main() {
    for (auto i = 0; i < 5; ++i) {
        printInt(i);
    }
    printInt(i);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_109():
    """Valid: break inside nested if inside while."""
    source = """
void main() {
    int i = 0;
    while (i < 100) {
        if (i > 10) {
            if (i > 20) {
                break;
            }
        }
        ++i;
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_110():
    """Valid: switch with default clause only."""
    source = """
void main() {
    int x = readInt();
    switch (x) {
        default:
            printInt(0);
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_111():
    """Valid: empty switch body."""
    source = """
void main() {
    int x = 1;
    switch (x) {}
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_112():
    """Valid: chained member access (nested struct)."""
    source = """
struct Inner {
    int val;
};
struct Outer {
    Inner inner;
};
void main() {
    Outer o;
    o.inner.val = 42;
    printInt(o.inner.val);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_113():
    """Valid: auto inferred via printFloat parameter."""
    source = """
void main() {
    auto f;
    printFloat(f);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_114():
    """Valid: auto inferred via printString parameter."""
    source = """
void main() {
    auto s;
    printString(s);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_115():
    """Valid: struct literal passed as function argument."""
    source = """
struct Point {
    int x;
    int y;
};
void drawPoint(Point p) {
    printInt(p.x);
    printInt(p.y);
}
void main() {
    drawPoint({5, 10});
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_116():
    """Valid: assignment expression as initializer."""
    source = """
void main() {
    int x;
    int y = (x = 5) + 3;
    printInt(y);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_117():
    """Valid: member access as assignment lhs in expression."""
    source = """
struct Point {
    int x;
    int y;
};
void main() {
    Point p;
    int result = (p.x = 15) + 5;
    printInt(result);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_118():
    """Valid: logical operators chain."""
    source = """
void main() {
    int a = 1;
    int b = 0;
    int c = 1;
    int result = a && b || c;
    printInt(result);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_119():
    """Valid: unary minus and plus on float."""
    source = """
void main() {
    float f = 3.14;
    float neg = -f;
    float pos = +f;
    printFloat(neg);
    printFloat(pos);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_120():
    """Valid: function with no parameters returning struct."""
    source = """
struct Config {
    int debug;
    int verbose;
};
Config defaultConfig() {
    Config c = {0, 0};
    return c;
}
void main() {
    Config cfg = defaultConfig();
    printInt(cfg.debug);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_121():
    """Valid: multiple structs, one used inside the other."""
    source = """
struct Color {
    int r;
    int g;
    int b;
};
struct Pixel {
    int x;
    int y;
    Color color;
};
void main() {
    Color red = {255, 0, 0};
    Pixel px = {10, 20, red};
    printInt(px.color.r);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_122():
    """Valid: for loop with no init and no update."""
    source = """
void main() {
    int i = 0;
    for (; i < 10;) {
        printInt(i);
        ++i;
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_123():
    """Valid: for loop with no condition (infinite, break inside)."""
    source = """
void main() {
    for (auto i = 0;; ++i) {
        if (i >= 5) break;
        printInt(i);
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_124():
    """Valid: auto var inferred from modulo result (int)."""
    source = """
void main() {
    int x = 10;
    int y = 3;
    auto r = x % y;
    printInt(r);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_125():
    """Valid: auto var inferred from relational expression (int result)."""
    source = """
void main() {
    float a = 1.5;
    float b = 2.5;
    auto cmp = a < b;
    printInt(cmp);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_126():
    """Valid: variable declared outside block, used inside."""
    source = """
void main() {
    int outer = 42;
    {
        int inner = outer + 1;
        printInt(inner);
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_127():
    """Valid: variable in inner block shadows outer local (not param)."""
    source = """
void process(int x) {
    int local = x + 1;
    {
        int local = 99;
        printInt(local);
    }
    printInt(local);
}
void main() {
    process(5);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_128():
    """Valid: empty struct declaration."""
    source = """
struct Empty {};
void main() {
    Empty e;
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_129():
    """Valid: function using built-in readInt and printInt."""
    source = """
void readAndPrint() {
    int x = readInt();
    printInt(x);
}
void main() {
    readAndPrint();
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_130():
    """Valid: auto with init from another auto (already resolved)."""
    source = """
void main() {
    auto x = 5;
    auto y = x;
    printInt(y);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_131():
    """Valid: postfix decrement on int var."""
    source = """
void main() {
    int n = 10;
    n--;
    printInt(n);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_132():
    """Valid: prefix decrement on int var."""
    source = """
void main() {
    int n = 10;
    --n;
    printInt(n);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_133():
    """Valid: auto struct type inferred from struct variable."""
    source = """
struct Point {
    int x;
    int y;
};
void main() {
    Point p1 = {1, 2};
    auto p2 = p1;
    printInt(p2.x);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_134():
    """Valid: multiple return statements same type in inferred-return func."""
    source = """
getVal(int flag) {
    if (flag) {
        return 1;
    }
    return 0;
}
void main() {
    printInt(getVal(1));
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_135():
    """Valid: function called after definition."""
    source = """
int helper(int x) {
    return x * 2;
}
int compute(int n) {
    return helper(n) + 1;
}
void main() {
    printInt(compute(5));
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_136():
    """Valid: block statement with multiple independent vars."""
    source = """
void main() {
    {
        int a = 1;
        int b = 2;
        int c = a + b;
        printInt(c);
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_137():
    """Valid: deep nested blocks with shadowing."""
    source = """
void main() {
    int x = 0;
    {
        int x = 1;
        {
            int x = 2;
            {
                int x = 3;
                printInt(x);
            }
            printInt(x);
        }
        printInt(x);
    }
    printInt(x);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_138():
    """Valid: switch with multiple cases and fall-through."""
    source = """
void main() {
    int x = 2;
    switch (x) {
        case 1:
        case 2:
        case 3:
            printInt(1);
            break;
        default:
            printInt(0);
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_139():
    """Valid: auto inferred via modulo (% requires int, so auto → int)."""
    source = """
void main() {
    auto x;
    int y = 3;
    auto r = x % y;
    printInt(r);
}
"""
    assert Checker(source).check_from_source() == "TypeCannotBeInferred(BinaryOp(Identifier(x), %, Identifier(y)))"


def test_checker_140():
    """Valid: deep function call chain."""
    source = """
int f1(int x) { return x + 1; }
int f2(int x) { return f1(x) + 1; }
int f3(int x) { return f2(x) + 1; }
void main() {
    printInt(f3(0));
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


# ---------------------------------------------------------------------------
# SECTION B: Redeclared — edge cases (141–155)
# ---------------------------------------------------------------------------


def test_checker_141():
    """Error: Redeclared Variable — for-init var then same name in same block."""
    source = """
void main() {
    for (auto i = 0; i < 5; ++i) {}
    int i = 10;
}
"""
    # for-init leaks into outer scope, then 'int i = 10' redeclares it
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, i)"


def test_checker_142():
    """Error: Redeclared Variable — same name declared twice in same for body."""
    source = """
void main() {
    for (auto i = 0; i < 5; ++i) {
        int z = 1;
        int z = 2;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, z)"


def test_checker_143():
    """Error: Redeclared Parameter — two params share a name."""
    source = """
float compute(float a, int b, float a) {
    return a;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Parameter, a)"


def test_checker_144():
    """Error: Redeclared Variable — local param shadow deep in nested block."""
    source = """
void f(int val) {
    {
        {
            int val = 99;
        }
    }
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, val)"


def test_checker_145():
    """Error: Redeclared Function — three functions, third duplicates first."""
    source = """
int a() { return 1; }
int b() { return 2; }
int a() { return 3; }
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Function, a)"


def test_checker_146():
    """Error: Redeclared Struct — second struct with same name."""
    source = """
struct Vec {
    int x;
};
struct Vec {
    int x;
    int y;
};
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Struct, Vec)"


def test_checker_147():
    """Error: Redeclared Member — last member repeats first."""
    source = """
struct Box {
    int width;
    int height;
    int depth;
    int width;
};
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Member, width)"


def test_checker_148():
    """Error: Redeclared Variable — two string vars with same name."""
    source = """
void main() {
    string s;
    string s;
}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, s)"


def test_checker_149():
    """Error: Redeclared Variable — auto then explicit same name."""
    source = """
void main() {
    auto x = 5;
    int x = 10;
}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, x)"


def test_checker_150():
    """Error: Redeclared Variable — explicit then auto same name."""
    source = """
void main() {
    int x = 5;
    auto x = 10;
}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, x)"


def test_checker_151():
    """Error: Redeclared Variable — param shadow in while body."""
    source = """
void f(int n) {
    while (n > 0) {
        int n = 5;
        --n;
    }
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, n)"


def test_checker_152():
    """Error: Redeclared Variable — param shadow inside switch case."""
    source = """
void g(int k) {
    switch (k) {
        case 1:
            int k = 2;
            break;
    }
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, k)"


def test_checker_153():
    """Error: Redeclared Member — int and float member same name."""
    source = """
struct Mixed {
    int value;
    float value;
};
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Member, value)"


def test_checker_154():
    """Error: Redeclared Function — redeclaring a builtin."""
    source = """
void printInt(int x) {}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Function, printInt)"


def test_checker_155():
    """Error: Redeclared — param redeclared in function with many params."""
    source = """
void manyParams(int a, string b, float c, int b) {}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Parameter, b)"


# ---------------------------------------------------------------------------
# SECTION C: UndeclaredIdentifier — edge cases (156–170)
# ---------------------------------------------------------------------------


def test_checker_156():
    """Error: UndeclaredIdentifier — var used in if condition."""
    source = """
void main() {
    if (ghost > 0) {
        printInt(1);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(ghost)"


def test_checker_157():
    """Error: UndeclaredIdentifier — var used in while condition."""
    source = """
void main() {
    while (phantom < 10) {
        printInt(1);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(phantom)"


def test_checker_158():
    """Error: UndeclaredIdentifier — var used in for condition."""
    source = """
void main() {
    for (auto i = 0; missing < 5; ++i) {
        printInt(i);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(missing)"


def test_checker_159():
    """Error: UndeclaredIdentifier — var used as function argument."""
    source = """
void main() {
    printInt(nowhere);
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(nowhere)"


def test_checker_160():
    """Error: UndeclaredIdentifier — var used in return stmt."""
    source = """
int f() {
    return ghost;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(ghost)"


def test_checker_161():
    """Error: UndeclaredIdentifier — member access on undeclared var."""
    source = """
struct Point {
    int x;
    int y;
};
void main() {
    int v = undeclaredPoint.x;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(undeclaredPoint)"


def test_checker_162():
    """Error: UndeclaredIdentifier — increment on undeclared var."""
    source = """
void main() {
    ++missing;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(missing)"


def test_checker_163():
    """Error: UndeclaredIdentifier — used in binary op rhs."""
    source = """
void main() {
    int x = 5;
    int y = x * notHere;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(notHere)"


def test_checker_164():
    """Error: UndeclaredIdentifier — switch expression."""
    source = """
void main() {
    switch (noVar) {
        case 1: break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(noVar)"


def test_checker_165():
    """Error: UndeclaredIdentifier — for update uses undeclared."""
    source = """
void main() {
    for (auto i = 0; i < 5; i = ghost + 1) {
        printInt(i);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(ghost)"


def test_checker_166():
    """Error: UndeclaredIdentifier — rhs of assignment is undeclared."""
    source = """
void main() {
    int x;
    x = unknownVar;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(unknownVar)"


def test_checker_167():
    """Error: UndeclaredIdentifier — out of scope in struct literal."""
    source = """
struct Point {
    int x;
    int y;
};
void main() {
    int coord = 10;
    Point p = {coord, outsideScope};
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(outsideScope)"


def test_checker_168():
    """Error: UndeclaredIdentifier — used after block ends."""
    source = """
void main() {
    {
        int tmp = 5;
    }
    int x = tmp + 1;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(tmp)"


def test_checker_169():
    """Error: UndeclaredIdentifier — for-body variable used after for ends."""
    source = """
void main() {
    for (auto i = 0; i < 3; ++i) {
        int body = i;
    }
    printInt(body);
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(body)"


def test_checker_170():
    """Error: UndeclaredIdentifier — postfix on undeclared."""
    source = """
void main() {
    missing++;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(missing)"


# ---------------------------------------------------------------------------
# SECTION D: UndeclaredFunction — edge cases (171–178)
# ---------------------------------------------------------------------------


def test_checker_171():
    """Error: UndeclaredFunction — call inside while body."""
    source = """
void main() {
    int i = 0;
    while (i < 5) {
        doWork(i);
        ++i;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(doWork)"


def test_checker_172():
    """Error: UndeclaredFunction — call inside switch case."""
    source = """
void main() {
    int x = 1;
    switch (x) {
        case 1:
            mystery(x);
            break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(mystery)"


def test_checker_173():
    """Error: UndeclaredFunction — call inside return statement."""
    source = """
int compute() {
    return unknown(5);
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(unknown)"


def test_checker_174():
    """Error: UndeclaredFunction — call inside if body."""
    source = """
void main() {
    int x = 5;
    if (x > 0) {
        doThing();
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(doThing)"


def test_checker_175():
    """Error: UndeclaredFunction — used as rhs of auto assignment."""
    source = """
void main() {
    auto result = missingFunc(42);
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(missingFunc)"


def test_checker_176():
    """Error: UndeclaredFunction — nested calls, outer is undeclared."""
    source = """
int square(int x) { return x * x; }
void main() {
    int r = outer(square(3));
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(outer)"


def test_checker_177():
    """Error: UndeclaredFunction — no main function declared."""
    source = """
void notMain() {
    printInt(1);
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(main)"


def test_checker_178():
    """Error: UndeclaredFunction — call inside for init."""
    source = """
void main() {
    for (int i = init(); i < 5; ++i) {
        printInt(i);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(init)"


# ---------------------------------------------------------------------------
# SECTION E: UndeclaredStruct — edge cases (179–185)
# ---------------------------------------------------------------------------


def test_checker_179():
    """Error: UndeclaredStruct — parameter type references missing struct."""
    source = """
void render(Canvas c) {}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(Canvas)"


def test_checker_180():
    """Error: UndeclaredStruct — member of struct references missing struct."""
    source = """
struct Node {
    Missing child;
    int value;
};
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(Missing)"


def test_checker_181():
    """Error: UndeclaredStruct — struct member uses later-declared struct."""
    source = """
struct A {
    B ref;
};
struct B {
    int val;
};
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(B)"


def test_checker_182():
    """Error: UndeclaredStruct — return type references missing struct."""
    source = """
Phantom getPhantom() {
    Phantom p;
    return p;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(Phantom)"


def test_checker_183():
    """Error: UndeclaredStruct — var declared with undeclared struct type."""
    source = """
struct Point { int x; int y; };
void main() {
    Rectangle r;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(Rectangle)"


def test_checker_184():
    """Error: UndeclaredStruct — function param uses struct declared after function."""
    source = """
void draw(Shape s) {}
struct Shape { int kind; };
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(Shape)"


def test_checker_185():
    """Error: UndeclaredStruct — self-referential member (current struct not declared)."""
    source = """
struct Tree {
    int val;
    Tree left;
};
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(Tree)"


# ---------------------------------------------------------------------------
# SECTION F: TypeCannotBeInferred — complex cases (186–210)
# ---------------------------------------------------------------------------


def test_checker_186():
    """Error: TypeCannotBeInferred — three unused autos."""
    source = """
void main() {
    auto a;
    auto b;
    auto c;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_187():
    """Error: TypeCannotBeInferred — two unknown autos subtraction."""
    source = """
void main() {
    auto p;
    auto q;
    auto r = p - q;
}
"""
    result = Checker(source).check_from_source()
    assert result == "TypeCannotBeInferred(BinaryOp(Identifier(p), -, Identifier(q)))"


def test_checker_188():
    """Error: TypeCannotBeInferred — struct literal without context."""
    source = """
struct Point { int x; int y; };
void main() {
    auto p = {1, 2};
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_189():
    """Error: TypeCannotBeInferred — auto used in logical AND with another auto."""
    source = """
void main() {
    auto a;
    auto b;
    int r = a && b;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_190():
    """Error: TypeCannotBeInferred — auto lhs, auto rhs chained assign."""
    source = """
void main() {
    auto x;
    auto y;
    auto z;
    x = y = z;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_191():
    """Error: TypeCannotBeInferred — auto used in greater-than both sides unknown."""
    source = """
void main() {
    auto m;
    auto n;
    int cmp = m > n;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_192():
    """Error: TypeCannotBeInferred — auto init from != of two unknowns."""
    source = """
void main() {
    auto x;
    auto y;
    auto flag = x != y;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_193():
    """Error: TypeCannotBeInferred — auto never resolved inside nested block."""
    source = """
void main() {
    {
        auto hidden;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_194():
    """Error: TypeCannotBeInferred — auto in inferred-return func with no return."""
    source = """
broken() {
    auto x;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_195():
    """Error: TypeCannotBeInferred — auto used only in prefix NOT."""
    source = """
void main() {
    auto f;
    int r = !f;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_196():
    """Error: TypeCannotBeInferred — auto used only in postfix ++."""
    source = """
void main() {
    auto x;
    x++;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_197():
    """Error: TypeCannotBeInferred — auto used only in prefix --."""
    source = """
void main() {
    auto x;
    --x;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_198():
    """Error: TypeCannotBeInferred — auto unused in if-else context."""
    source = """
void main() {
    auto x;
    if (1) {
        printInt(1);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_199():
    """Error: TypeCannotBeInferred — auto lhs unknown, rhs is string literal."""
    source = """
void main() {
    auto s;
    auto r = s + "world";
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_200():
    """Error: TypeCannotBeInferred — two auto vars in >= comparison."""
    source = """
void main() {
    auto p;
    auto q;
    int r = p >= q;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_201():
    """Error: TypeCannotBeInferred — auto used only in while condition."""
    source = """
void main() {
    auto flag;
    while (flag) {
        printInt(1);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_202():
    """Error: TypeCannotBeInferred — two autos in for condition."""
    source = """
void main() {
    auto i;
    auto n;
    for (; i < n;) {
        printInt(1);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_203():
    """Error: TypeCannotBeInferred — auto used only in struct member assignment."""
    source = """
struct Point { int x; int y; };
void main() {
    auto p;
    p.x = 5;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_204():
    """Error: TypeCannotBeInferred — inferred-return func, auto return."""
    source = """
badReturn(int x) {
    auto y;
    return y;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_205():
    """Error: TypeCannotBeInferred — auto used only as == with another unknown."""
    source = """
void main() {
    auto a;
    auto b;
    auto eq = (a == b);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_206():
    """Error: TypeCannotBeInferred — two unknowns passed as arg expression."""
    source = """
void twoArgs(int x, int y) {}
void main() {
    auto a;
    auto b;
    twoArgs(a + b, 0);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_207():
    """Error: TypeCannotBeInferred — division of two unknown autos."""
    source = """
void main() {
    auto m;
    auto n;
    auto k = m / n;
}
"""
    result = Checker(source).check_from_source()
    assert result == "TypeCannotBeInferred(BinaryOp(Identifier(m), /, Identifier(n)))"


def test_checker_208():
    """Error: TypeCannotBeInferred — subtraction of known+unknown reversed."""
    source = """
void main() {
    auto i;
    auto j;
    auto diff = i - j;
}
"""
    result = Checker(source).check_from_source()
    assert result == "TypeCannotBeInferred(BinaryOp(Identifier(i), -, Identifier(j)))"


def test_checker_209():
    """Error: TypeCannotBeInferred — equality check of two unknown autos."""
    source = """
void main() {
    auto u;
    auto v;
    int eq = u == v;
}
"""
    result = Checker(source).check_from_source()
    assert result == "TypeCannotBeInferred(BinaryOp(Identifier(u), ==, Identifier(v)))"


def test_checker_210():
    """Error: TypeCannotBeInferred — two unknowns in logical OR."""
    source = """
void main() {
    auto x;
    auto y;
    int r = x || y;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


# ---------------------------------------------------------------------------
# SECTION G: TypeMismatchInStatement — complex cases (211–235)
# ---------------------------------------------------------------------------


def test_checker_211():
    """Error: TypeMismatchInStatement — return float from explicit int function."""
    source = """
int getFloat() {
    return 3.14;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_212():
    """Error: TypeMismatchInStatement — return string from float function."""
    source = """
float getStr() {
    return "hello";
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_213():
    """Error: TypeMismatchInStatement — int var initialized with float literal."""
    source = """
void main() {
    int x = 3.14;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_214():
    """Error: TypeMismatchInStatement — float var initialized with string."""
    source = """
void main() {
    float f = "hello";
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_215():
    """Error: TypeMismatchInStatement — string var initialized with int."""
    source = """
void main() {
    string s = 42;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_216():
    """Error: TypeMismatchInStatement — int var initialized with float expression."""
    source = """
void main() {
    float a = 1.5;
    int b = a + 0.5;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_217():
    """Error: TypeMismatchInStatement — while condition is a struct."""
    source = """
struct Flag { int val; };
void main() {
    Flag f = {1};
    while (f) {}
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_218():
    """Error: TypeMismatchInStatement — for condition is a string variable."""
    source = """
void main() {
    string s = "abc";
    for (int i = 0; s; ++i) {}
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_219():
    """Error: TypeMismatchInStatement — assignment float = string."""
    source = """
void main() {
    float f;
    f = "text";
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_220():
    """Error: TypeMismatchInStatement — int assigned to struct variable."""
    source = """
struct Box { int w; int h; };
void main() {
    Box b;
    b = 5;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_221():
    """Error: TypeMismatchInStatement — assignment Point = Line."""
    source = """
struct Point { int x; int y; };
struct Line { int x1; int y1; int x2; int y2; };
void main() {
    Point p;
    Line l;
    p = l;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_222():
    """Error: TypeMismatchInStatement — return; from explicit int function."""
    source = """
int badReturn() {
    return;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_223():
    """Error: TypeMismatchInStatement — void function returns float."""
    source = """
void main() {
    return 3.14;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_224():
    """Error: TypeMismatchInStatement — if condition is a struct type."""
    source = """
struct Flag { int val; };
void main() {
    Flag f;
    if (f) {
        printInt(1);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_225():
    """Error: TypeMismatchInStatement — switch on string variable."""
    source = """
void main() {
    string s = "hello";
    switch (s) {
        default: break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_226():
    """Error: TypeMismatchInStatement — inferred func second return differs."""
    source = """
mixedReturn() {
    return 1;
    return 3.14;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_227():
    """Error: TypeMismatchInStatement — struct var init with wrong type for field."""
    source = """
struct Info {
    int code;
    string msg;
};
void main() {
    Info i = {3.14, "ok"};
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_228():
    """Error: TypeMismatchInStatement — assignment string = float."""
    source = """
void main() {
    string s = "hello";
    s = 3.14;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_229():
    """Error: TypeMismatchInStatement — string var initialised with int+int expression."""
    source = """
void main() {
    int a = 5;
    int b = 3;
    string s = a + b;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_230():
    """Error: TypeMismatchInStatement — float assignment from int explicit var."""
    source = """
void main() {
    int x = 10;
    float f = x;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_231():
    """Error: TypeMismatchInStatement — return int from string func."""
    source = """
string getString() {
    return 100;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_232():
    """Error: TypeMismatchInStatement — return float from string func."""
    source = """
string getStr2() {
    return 3.14;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_233():
    """Error: TypeMismatchInStatement — return int from void function."""
    source = """
void voidFunc() {
    return 42;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_234():
    """Error: TypeMismatchInStatement — assignment: struct from int."""
    source = """
struct Pair { int a; int b; };
void main() {
    Pair p;
    int x = 5;
    p = x;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_235():
    """Error: TypeMismatchInStatement — switch on float expression."""
    source = """
void main() {
    float x = 1.5;
    float y = 2.5;
    switch (x + y) {
        default: break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


# ---------------------------------------------------------------------------
# SECTION H: TypeMismatchInExpression — complex cases (236–265)
# ---------------------------------------------------------------------------


def test_checker_236():
    """Error: TypeMismatchInExpression — string * int."""
    source = """
void main() {
    string s = "hi";
    auto r = s * 2;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_237():
    """Error: TypeMismatchInExpression — int == string."""
    source = """
void main() {
    int x = 5;
    string s = "5";
    int eq = x == s;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_238():
    """Error: TypeMismatchInExpression — logical OR with float operand."""
    source = """
void main() {
    float f = 1.0;
    int x = 1;
    int r = x || f;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_239():
    """Error: TypeMismatchInExpression — float && float."""
    source = """
void main() {
    float a = 1.0;
    float b = 0.0;
    int r = a && b;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_240():
    """Error: TypeMismatchInExpression — unary NOT on string."""
    source = """
void main() {
    string s = "test";
    int r = !s;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_241():
    """Error: TypeMismatchInExpression — unary minus on string."""
    source = """
void main() {
    string s = "neg";
    auto r = -s;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_242():
    """Error: TypeMismatchInExpression — prefix increment on string."""
    source = """
void main() {
    string s = "abc";
    ++s;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_243():
    """Error: TypeMismatchInExpression — postfix decrement on float."""
    source = """
void main() {
    float f = 1.5;
    f--;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_244():
    """Error: TypeMismatchInExpression — member access nonexistent field."""
    source = """
struct Rectangle { int width; int height; };
void main() {
    Rectangle r = {10, 20};
    int area = r.area;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_245():
    """Error: TypeMismatchInExpression — call with wrong argument type (float→int)."""
    source = """
int double_it(int x) { return x * 2; }
void main() {
    float f = 2.5;
    int r = double_it(f);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_246():
    """Error: TypeMismatchInExpression — call with wrong type (string→float)."""
    source = """
float negate(float x) { return -x; }
void main() {
    string s = "bad";
    float r = negate(s);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_247():
    """Error: TypeMismatchInExpression — zero arguments to two-param function."""
    source = """
int add(int x, int y) { return x + y; }
void main() {
    int r = add();
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_248():
    """Error: TypeMismatchInExpression — member access on primitive (float)."""
    source = """
void main() {
    float x = 3.14;
    auto r = x.something;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_249():
    """Error: TypeMismatchInExpression — member access on string var."""
    source = """
void main() {
    string s = "hello";
    auto r = s.length;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_250():
    """Error: TypeMismatchInExpression — struct literal too few fields."""
    source = """
struct Point { int x; int y; };
void main() {
    Point p = {1};
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_251():
    """Error: TypeMismatchInExpression — struct literal field type mismatch (float→int)."""
    source = """
struct Item { int code; string name; };
void main() {
    Item it = {3.14, "widget"};
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_252():
    """Error: TypeMismatchInExpression — struct literal field type mismatch (string→int)."""
    source = """
struct Coord { int lat; int lon; };
void main() {
    Coord c = {"north", 30};
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_253():
    """Error: TypeMismatchInExpression — string % int."""
    source = """
void main() {
    string s = "abc";
    int r = s % 3;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_254():
    """Error: TypeMismatchInExpression — int > string comparison."""
    source = """
void main() {
    int x = 5;
    string s = "hi";
    int r = x > s;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_255():
    """Error: TypeMismatchInExpression — printInt given float arg."""
    source = """
void main() {
    float f = 1.5;
    printInt(f);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_256():
    """Error: TypeMismatchInExpression — printFloat given string arg."""
    source = """
void main() {
    string s = "bad";
    printFloat(s);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_257():
    """Error: TypeMismatchInExpression — printString given int arg."""
    source = """
void main() {
    printString(42);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_258():
    """Error: TypeMismatchInExpression — struct nested literal wrong field type."""
    source = """
struct Vec2 { int x; int y; };
struct Box { Vec2 origin; int size; };
void main() {
    Box b = {{1.0, 2}, 10};
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_259():
    """Error: TypeMismatchInExpression — function arg is struct literal with wrong field."""
    source = """
struct Point { int x; int y; };
void draw(Point p) { printInt(p.x); }
void main() {
    draw({1.5, 2});
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_260():
    """Error: TypeMismatchInExpression — float < string."""
    source = """
void main() {
    float f = 1.5;
    string s = "x";
    int r = f < s;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_261():
    """Error: TypeMismatchInExpression — prefix ++ applied to binary expression."""
    source = """
void main() {
    int x = 3;
    ++(x + 1);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_262():
    """Error: TypeMismatchInExpression — postfix ++ on expression (not lvalue)."""
    source = """
void main() {
    int x = 3;
    (x + 2)++;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_263():
    """Error: TypeMismatchInExpression — unary plus on string."""
    source = """
void main() {
    string s = "hi";
    auto r = +s;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_264():
    """Error: TypeMismatchInExpression — struct equality (structs cannot use ==)."""
    source = """
struct Point { int x; int y; };
void main() {
    Point a = {1, 2};
    Point b = {1, 2};
    int eq = a == b;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_265():
    """Error: TypeMismatchInExpression — three args to one-param function."""
    source = """
void single(int x) {}
void main() {
    single(1, 2, 3);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


# ---------------------------------------------------------------------------
# SECTION I: MustInLoop — complex cases (266–275)
# ---------------------------------------------------------------------------


def test_checker_266():
    """Error: MustInLoop — break in top-level function body."""
    source = """
void process() {
    break;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_267():
    """Error: MustInLoop — continue in top-level function body."""
    source = """
void process() {
    continue;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_268():
    """Error: MustInLoop — break inside else branch without loop."""
    source = """
void main() {
    int x = 5;
    if (x > 0) {
        printInt(1);
    } else {
        break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_269():
    """Error: MustInLoop — continue inside else branch without loop."""
    source = """
void main() {
    int x = 0;
    if (x > 0) {
        printInt(1);
    } else {
        continue;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_270():
    """Error: MustInLoop — continue in switch (not inside a loop)."""
    source = """
void main() {
    int x = 2;
    switch (x) {
        case 2:
            continue;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_271():
    """Error: MustInLoop — break inside nested function called from loop."""
    source = """
void inner() {
    break;
}
void main() {
    while (1) {
        inner();
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_272():
    """Error: MustInLoop — continue inside nested function called from loop."""
    source = """
void inner() {
    continue;
}
void main() {
    for (int i = 0; i < 5; ++i) {
        inner();
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_273():
    """Error: MustInLoop — continue after for loop ends."""
    source = """
void main() {
    for (int i = 0; i < 3; ++i) {
        printInt(i);
    }
    continue;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_274():
    """Error: MustInLoop — break after while loop ends."""
    source = """
void main() {
    int i = 0;
    while (i < 3) {
        ++i;
    }
    break;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_275():
    """Error: MustInLoop — break and continue both outside loop (break reported first)."""
    source = """
void main() {
    break;
    continue;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


# ---------------------------------------------------------------------------
# SECTION J: Mixed / interaction valid (276–288)
# ---------------------------------------------------------------------------


def test_checker_276():
    """Valid: struct passed to function, member used in return."""
    source = """
struct Point { int x; int y; };
int sumCoords(Point p) {
    return p.x + p.y;
}
void main() {
    Point pt = {3, 4};
    printInt(sumCoords(pt));
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_277():
    """Valid: auto struct inferred from function returning struct."""
    source = """
struct Point { int x; int y; };
Point origin() {
    Point p = {0, 0};
    return p;
}
void main() {
    auto p = origin();
    printInt(p.x);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_278():
    """Valid: chained member assignments."""
    source = """
struct Vec { int x; int y; int z; };
void main() {
    Vec v;
    v.x = 1;
    v.y = v.x + 1;
    v.z = v.x + v.y;
    printInt(v.z);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_279():
    """Valid: if-else inside while inside for."""
    source = """
void main() {
    for (auto i = 0; i < 5; ++i) {
        int j = 0;
        while (j < i) {
            if (j % 2 == 0) {
                printInt(j);
            } else {
                printInt(-j);
            }
            ++j;
        }
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_280():
    """Valid: multiple functions calling each other in correct order."""
    source = """
int square(int n) { return n * n; }
int cube(int n) { return n * square(n); }
void main() {
    printInt(cube(3));
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_281():
    """Valid: multiple parameters of different types."""
    source = """
void printAll(int i, float f, string s) {
    printInt(i);
    printFloat(f);
    printString(s);
}
void main() {
    printAll(1, 2.5, "hi");
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_282():
    """Valid: auto inferred as float from float+int arithmetic."""
    source = """
void main() {
    float f = 1.5;
    int i = 2;
    auto r = f + i;
    printFloat(r);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_283():
    """Valid: struct with float members, operations on them."""
    source = """
struct Vec2f { float x; float y; };
void main() {
    Vec2f v = {1.0, 2.0};
    float magnitude = v.x * v.x + v.y * v.y;
    printFloat(magnitude);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_284():
    """Valid: switch inside while inside function."""
    source = """
void process(int n) {
    int i = 0;
    while (i < n) {
        switch (i % 3) {
            case 0: printInt(0); break;
            case 1: printInt(1); break;
            default: printInt(2); break;
        }
        ++i;
    }
}
void main() {
    process(9);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_285():
    """Valid: function with explicit void return uses return;."""
    source = """
void doNothing() {
    return;
}
void main() {
    doNothing();
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_286():
    """Valid: auto resolved via && operator (both sides int)."""
    source = """
void main() {
    auto a;
    int b = 1;
    int r = a && b;
    printInt(r);
}
"""
    assert Checker(source).check_from_source() == "TypeCannotBeInferred(BinaryOp(Identifier(a), &&, Identifier(b)))"


def test_checker_287():
    """Valid: auto lhs resolved via known-type function return."""
    source = """
int getNum() { return 42; }
void main() {
    auto x;
    x = getNum();
    printInt(x);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_288():
    """Valid: autotype struct assigned from call returning struct."""
    source = """
struct Config { int debug; float level; };
Config getDefault() {
    Config c = {0, 1.0};
    return c;
}
void main() {
    auto cfg = getDefault();
    printInt(cfg.debug);
    printFloat(cfg.level);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


# ---------------------------------------------------------------------------
# SECTION K: Mixed / interaction errors — priority (289–300)
# ---------------------------------------------------------------------------


def test_checker_289():
    """Error: first error is Redeclared even though TypeMismatch also exists later."""
    source = """
void main() {
    int x = 5;
    int x = "hello";
}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, x)"


def test_checker_290():
    """Error: Undeclared fires before TypeMismatch in same expression."""
    source = """
void main() {
    int r = ghost + "wrong";
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(ghost)"


def test_checker_291():
    """Error: UndeclaredFunction fires before TypeMismatch."""
    source = """
void main() {
    int r = unknownFunc("bad_arg");
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(unknownFunc)"


def test_checker_292():
    """Error: Redeclared Struct fires before later UndeclaredStruct."""
    source = """
struct A { int x; };
struct A { B ref; };
struct B { int val; };
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Struct, A)"


def test_checker_293():
    """Error: TypeMismatchInExpression — member access on result of arithmetic."""
    source = """
void main() {
    int x = 5;
    int y = 3;
    int r = (x + y).field;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_294():
    """Error: TypeCannotBeInferred — auto used only as while condition body."""
    source = """
void main() {
    auto flag;
    while (flag) {
        printInt(1);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_295():
    """Error: Redeclared Variable — same-name local var twice in switch case."""
    source = """
void main() {
    int x = 2;
    switch (x) {
        case 2:
            int tmp = 1;
            int tmp = 2;
            break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, tmp)"


def test_checker_296():
    """Error: UndeclaredIdentifier — used inside struct literal field."""
    source = """
struct Point { int x; int y; };
void main() {
    Point p = {undeclared, 5};
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(undeclared)"


def test_checker_297():
    """Error: MustInLoop is first error (before TypeMismatch further down)."""
    source = """
void process() {
    break;
    int x = "wrong_type";
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_298():
    """Error: Redeclared reported even if UndeclaredStruct appears in second copy."""
    source = """
struct X { int val; };
struct X { float val; };
void main() {
    Y y;
}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Struct, X)"


def test_checker_299():
    """Error: TypeMismatchInExpression — nested struct literal missing a field."""
    source = """
struct Inner { int a; int b; };
struct Outer { Inner child; int extra; };
void main() {
    Outer o = {{1}, 5};
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_300():
    """Error: TypeMismatchInStatement — var init: int var given string expression."""
    source = """
void main() {
    string prefix = "hello_";
    int code = prefix;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


# ===========================================================================
# TESTS 301-500: EVEN MORE ADVANCED -- EDGE CASES AND DEEP COVERAGE
# ===========================================================================

# ---------------------------------------------------------------------------
# SECTION L: Valid programs -- advanced patterns (301-340)
# ---------------------------------------------------------------------------


def test_checker_301():
    """Valid: function returns auto-inferred int, caller uses it in arithmetic."""
    source = """
getN() {
    return 42;
}
void main() {
    int x = getN() + 1;
    printInt(x);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_302():
    """Valid: struct member modified via member access lhs."""
    source = """
struct Counter {
    int count;
};
void increment(Counter c) {
    c.count = c.count + 1;
}
void main() {
    Counter c = {0};
    increment(c);
    printInt(c.count);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_303():
    """Valid: multiple auto vars inferred via different builtins."""
    source = """
void main() {
    auto a = readInt();
    auto b = readFloat();
    auto c = readString();
    printInt(a);
    printFloat(b);
    printString(c);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_304():
    """Valid: nested if-else chains."""
    source = """
void classify(int n) {
    if (n < 0) {
        printInt(-1);
    } else {
        if (n == 0) {
            printInt(0);
        } else {
            printInt(1);
        }
    }
}
void main() {
    classify(5);
    classify(0);
    classify(-3);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_305():
    """Valid: for loop var used in body and condition."""
    source = """
void main() {
    for (int i = 0; i * i < 100; ++i) {
        printInt(i);
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_306():
    """Valid: while loop over int-read input."""
    source = """
void main() {
    int n = readInt();
    int i = 0;
    while (i < n) {
        printInt(i);
        ++i;
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_307():
    """Valid: auto var inferred via assignment from int param."""
    source = """
void f(int x) {
    auto y;
    y = x;
    printInt(y);
}
void main() {
    f(10);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_308():
    """Valid: auto var inferred via assignment from float param."""
    source = """
void f(float x) {
    auto y;
    y = x;
    printFloat(y);
}
void main() {
    f(3.14);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_309():
    """Valid: auto var inferred via assignment from string param."""
    source = """
void sf(string x) {
    auto y;
    y = x;
    printString(y);
}
void main() {
    sf("hi");
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_310():
    """Valid: struct with string fields."""
    source = """
struct Person {
    string name;
    int age;
};
void main() {
    Person p = {"Alice", 30};
    printString(p.name);
    printInt(p.age);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_311():
    """Valid: struct parameter, return same struct type."""
    source = """
struct Point { int x; int y; };
Point shift(Point p, int dx, int dy) {
    Point q = {p.x + dx, p.y + dy};
    return q;
}
void main() {
    Point origin = {0, 0};
    Point moved = shift(origin, 3, 4);
    printInt(moved.x);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_312():
    """Valid: two functions called in chain."""
    source = """
int double_val(int x) { return x * 2; }
int triple_val(int x) { return x * 3; }
void main() {
    printInt(double_val(triple_val(2)));
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_313():
    """Valid: break inside nested switch inside while."""
    source = """
void main() {
    int i = 0;
    while (i < 5) {
        switch (i % 2) {
            case 0:
                break;
            default:
                break;
        }
        ++i;
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_314():
    """Valid: auto inferred from chained multiplication with readInt."""
    source = """
void main() {
    auto x = readInt();
    auto y = x * 2;
    auto z = y * 3;
    printInt(z);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_315():
    """Valid: struct with only float fields."""
    source = """
struct Vec3 {
    float x;
    float y;
    float z;
};
void main() {
    Vec3 v = {1.0, 2.0, 3.0};
    float sum = v.x + v.y + v.z;
    printFloat(sum);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_316():
    """Valid: nested blocks each with independent vars."""
    source = """
void main() {
    int result = 0;
    {
        int a = 10;
        result = a;
    }
    {
        int b = 20;
        result = result + b;
    }
    printInt(result);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_317():
    """Valid: for loop with compound update expression."""
    source = """
void main() {
    int sum = 0;
    for (int i = 0; i < 10; i = i + 2) {
        sum = sum + i;
    }
    printInt(sum);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_318():
    """Valid: function with multiple early returns."""
    source = """
string grade(int score) {
    if (score >= 90) {
        return "A";
    }
    if (score >= 80) {
        return "B";
    }
    return "F";
}
void main() {
    printString(grade(85));
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_319():
    """Valid: global struct used by multiple functions."""
    source = """
struct Stats {
    int total;
    int count;
};
void addVal(Stats s, int val) {
    s.total = s.total + val;
}
int getTotal(Stats s) {
    return s.total;
}
void main() {
    Stats st = {0, 0};
    addVal(st, 10);
    printInt(getTotal(st));
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_320():
    """Valid: for loop init is assignment to existing var."""
    source = """
void main() {
    int i;
    for (i = 0; i < 5; ++i) {
        printInt(i);
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_321():
    """Valid: while loop condition is negation (!)."""
    source = """
void main() {
    int done = 0;
    int count = 0;
    while (!done) {
        ++count;
        if (count >= 5) {
            done = 1;
        }
    }
    printInt(count);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_322():
    """Valid: switch on result of function call."""
    source = """
int getCode() { return 2; }
void main() {
    switch (getCode()) {
        case 1: printInt(1); break;
        case 2: printInt(2); break;
        default: printInt(0); break;
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_323():
    """Valid: struct member used as function argument."""
    source = """
struct Config { int level; string name; };
void display(int lvl, string nm) {
    printInt(lvl);
    printString(nm);
}
void main() {
    Config cfg = {3, "test"};
    display(cfg.level, cfg.name);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_324():
    """Valid: auto inferred via struct member access."""
    source = """
struct Box { int size; };
void main() {
    Box b = {10};
    auto s = b.size;
    printInt(s);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_325():
    """Valid: int var used in multiple expressions without conflict."""
    source = """
void main() {
    int x = 10;
    int a = x + 1;
    int bc = x * 2;
    int cd = x - 3;
    int de = x % 3;
    printInt(a + bc + cd + de);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_326():
    """Valid: deeply nested struct access."""
    source = """
struct A { int val; };
struct B { A a; };
struct C { B b; };
void main() {
    A a = {42};
    B b = {a};
    C c = {b};
    printInt(c.b.a.val);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_327():
    """Valid: comparison of floats produces int result."""
    source = """
void main() {
    float x = 3.14;
    float y = 2.71;
    int gt = x > y;
    printInt(gt);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_328():
    """Valid: logical NOT chain."""
    source = """
void main() {
    int x = 1;
    int r = !!x;
    printInt(r);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_329():
    """Valid: inferred return func maxOf."""
    source = """
maxOf(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}
void main() {
    int m = maxOf(3, 7);
    printInt(m);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_330():
    """Valid: struct field assigned from another struct field."""
    source = """
struct Point { int x; int y; };
void main() {
    Point src = {10, 20};
    Point dst;
    dst.x = src.x;
    dst.y = src.y;
    printInt(dst.x + dst.y);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_331():
    """Valid: auto var used in all comparison variants."""
    source = """
void main() {
    auto val = readInt();
    int r1 = val < 10;
    int r2 = val > 0;
    int r3 = val <= 5;
    int r4 = val >= 1;
    int r5 = val == 3;
    int r6 = val != 0;
    printInt(r1 + r2 + r3 + r4 + r5 + r6);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_332():
    """Valid: auto var inferred from negation of known int."""
    source = """
void main() {
    int x = 5;
    auto neg = -x;
    printInt(neg);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_333():
    """Valid: auto var inferred from negation of known float."""
    source = """
void main() {
    float f = 3.14;
    auto neg = -f;
    printFloat(neg);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_334():
    """Valid: switch inside function with int param."""
    source = """
void printSeason(int month) {
    switch (month) {
        case 12:
        case 1:
            printString("Winter");
            break;
        case 3:
        case 4:
            printString("Spring");
            break;
        default:
            printString("Other");
    }
}
void main() {
    printSeason(1);
    printSeason(4);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_335():
    """Valid: struct returned, immediately member-accessed."""
    source = """
struct Pair { int first; int second; };
Pair makePair(int a, int b) {
    Pair p = {a, b};
    return p;
}
void main() {
    int f = makePair(10, 20).first;
    printInt(f);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_336():
    """Valid: for-loop var declared in init, used in condition."""
    source = """
void main() {
    for (int k = 10; k > 0; k = k - 1) {
        printInt(k);
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_337():
    """Valid: multiple return paths all return same type."""
    source = """
int sign(int x) {
    if (x > 0) return 1;
    if (x < 0) return -1;
    return 0;
}
void main() {
    printInt(sign(5));
    printInt(sign(0));
    printInt(sign(-3));
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_338():
    """Valid: complex for loop with nested while."""
    source = """
void main() {
    for (int i = 1; i <= 5; ++i) {
        int j = i;
        while (j > 0) {
            printInt(j);
            j = j - 1;
        }
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_339():
    """Valid: all 6 builtins used in one program."""
    source = """
void main() {
    int a = readInt();
    float b = readFloat();
    string c = readString();
    printInt(a);
    printFloat(b);
    printString(c);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_340():
    """Valid: function with auto return type inferred as string."""
    source = """
greeting(string name) {
    return name;
}
void main() {
    auto msg = greeting("World");
    printString(msg);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


# ---------------------------------------------------------------------------
# SECTION M: Redeclared -- deeper edge cases (341-355)
# ---------------------------------------------------------------------------


def test_checker_341():
    """Error: Redeclared Variable -- for-body var conflicts with for-init."""
    source = """
void main(){

auto a; auto b;

a=1;

a+b;

}
"""
    result = Checker(source).check_from_source()
    assert result == "TypeCannotBeInferred(BinaryOp(Identifier(a), +, Identifier(b)))"


def test_checker_342():
    """Error: Redeclared Variable -- two autos same name in same block."""
    source = """
void main() {
    auto val = 10;
    for (int i = 1; i < 10; i++) {
        auto x;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "TypeCannotBeInferred(BlockStmt([VarDecl(auto, x)]))"


def test_checker_343():
    """Error: Redeclared function -- readInt shadowed."""
    source = """
int readInt() { return 0; }
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Function, readInt)"


def test_checker_344():
    """Error: Redeclared function -- readFloat shadowed."""
    source = """
float readFloat() { return 0.0; }
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Function, readFloat)"


def test_checker_345():
    """Error: Redeclared function -- printString shadowed."""
    source = """
void printString(string s) {}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Function, printString)"


def test_checker_346():
    """Error: Redeclared Member -- second field repeats first."""
    source = """
struct Triple {
    int a;
    int a;
    int b;
};
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Member, a)"


def test_checker_347():
    """Error: Redeclared Parameter -- last param duplicates third."""
    source = """
void process(int x, string y, float z, float z) {}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Parameter, z)"


def test_checker_348():
    """Error: Redeclared Variable -- string then int same name."""
    source = """
void main() {
    string name = "Alice";
    int name = 0;
}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, name)"


def test_checker_349():
    """Error: Redeclared Variable -- float twice same name."""
    source = """
void main() {
    float ratio = 0.5;
    float ratio = 1.5;
}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, ratio)"


def test_checker_350():
    """Error: Redeclared -- param shadowed inside if-then body."""
    source = """
void check(int limit) {
    if (limit > 0) {
        int limit = 10;
        printInt(limit);
    }
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, limit)"


def test_checker_351():
    """Error: Redeclared Variable -- same name appears twice separated by code."""
    source = """
void main() {
    int alpha = 1;
    int beta = 2;
    int gamma = 3;
    int alpha = 4;
}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, alpha)"


def test_checker_352():
    """Error: Redeclared Struct -- second declaration is empty."""
    source = """
struct Data {
    int id;
    string label;
};
struct Data {};
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Struct, Data)"


def test_checker_353():
    """Error: Redeclared Variable -- param shadow in default case."""
    source = """
void f(int code) {
    switch (code) {
        default:
            int code = -1;
            break;
    }
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, code)"


def test_checker_354():
    """Error: Redeclared Function -- main declared twice."""
    source = """
void main() {
    printInt(1);
}
void main() {
    printInt(2);
}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Function, main)"


def test_checker_355():
    """Error: Redeclared Variable -- auto param-shadow in for body."""
    source = """
void f(int x) {
    for (int i = 0; i < 3; ++i) {
        auto x = 5;
    }
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Variable, x)"


# ---------------------------------------------------------------------------
# SECTION N: UndeclaredIdentifier -- more edge cases (356-372)
# ---------------------------------------------------------------------------


def test_checker_356():
    """Error: UndeclaredIdentifier -- used after inner loop block ends."""
    source = """
void main() {
    while (1) {
        int temp = 5;
        break;
    }
    printInt(temp);
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(temp)"


def test_checker_357():
    """Error: UndeclaredIdentifier -- first of two undeclared in &&."""
    source = """
void main() {
    int r = missing1 && missing2;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(missing1)"


def test_checker_358():
    """Error: UndeclaredIdentifier -- field of struct init is undeclared."""
    source = """
struct Point { int x; int y; };
void main() {
    int known = 5;
    Point p = {known, noSuch};
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(noSuch)"


def test_checker_359():
    """Error: UndeclaredIdentifier -- used in while update (prefix op)."""
    source = """
void main() {
    int x = 0;
    while (x < 5) {
        ++ghost;
        ++x;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(ghost)"


def test_checker_360():
    """Error: UndeclaredIdentifier -- used as case expression."""
    source = """
void main() {
    int x = 1;
    switch (x) {
        case missingConst:
            break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(missingConst)"


def test_checker_361():
    """Error: UndeclaredIdentifier -- member access on undeclared struct var."""
    source = """
struct Point { int x; int y; };
void main() {
    printInt(noDeclared.x);
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(noDeclared)"


def test_checker_362():
    """Error: UndeclaredIdentifier -- return in inferred func using unknown var."""
    source = """
getVal() {
    return noVar;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(noVar)"


def test_checker_363():
    """Error: UndeclaredIdentifier -- in assignment rhs of member."""
    source = """
struct Point { int x; int y; };
void main() {
    Point p;
    p.x = missingVar;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(missingVar)"


def test_checker_364():
    """Error: UndeclaredIdentifier -- binary expression lhs is undeclared."""
    source = """
void main() {
    int result = undecl - 5;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(undecl)"


def test_checker_365():
    """Error: UndeclaredIdentifier -- used as rhs of % op."""
    source = """
void main() {
    int x = 10;
    int r = x % noVar;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(noVar)"


def test_checker_366():
    """Error: UndeclaredIdentifier -- used as rhs of != op."""
    source = """
void main() {
    int x = 5;
    int r = x != missing;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(missing)"


def test_checker_367():
    """Error: UndeclaredIdentifier -- used in else-if condition."""
    source = """
void main() {
    int x = 5;
    if (x > 10) {
        printInt(1);
    } else {
        if (ghost < 5) {
            printInt(2);
        }
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(ghost)"


def test_checker_368():
    """Error: UndeclaredIdentifier -- rhs of auto init from undeclared."""
    source = """
void main() {
    auto x = undeclaredSrc;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(undeclaredSrc)"


def test_checker_369():
    """Error: UndeclaredIdentifier -- used in initializer before being declared."""
    source = """
void main() {
    int b = ghost + 1;
    int ghost = 5;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(ghost)"


def test_checker_370():
    """Error: UndeclaredIdentifier -- return uses undeclared."""
    source = """
int process() {
    return missing + 1;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(missing)"


def test_checker_371():
    """Error: UndeclaredIdentifier -- used in nested for body."""
    source = """
void main() {
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            printInt(nothere);
        }
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(nothere)"


def test_checker_372():
    """Error: UndeclaredIdentifier -- member access rhs from undeclared var."""
    source = """
struct Pt { int x; int y; };
void main() {
    Pt p;
    p.x = noSrcVar;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(noSrcVar)"


# ---------------------------------------------------------------------------
# SECTION O: UndeclaredFunction -- more edge cases (373-380)
# ---------------------------------------------------------------------------


def test_checker_373():
    """Error: UndeclaredFunction -- called inside nested for body."""
    source = """
void main() {
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            magic(i, j);
        }
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(magic)"


def test_checker_374():
    """Error: UndeclaredFunction -- used as switch expr."""
    source = """
void main() {
    switch (getCode()) {
        default: break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(getCode)"


def test_checker_375():
    """Error: UndeclaredFunction -- in comparison expression."""
    source = """
void main() {
    int r = getValue() > 5;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(getValue)"


def test_checker_376():
    """Error: UndeclaredFunction -- as argument to valid function."""
    source = """
void main() {
    printInt(produce());
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(produce)"


def test_checker_377():
    """Error: UndeclaredFunction -- in else branch."""
    source = """
void main() {
    int x = 5;
    if (x > 10) {
        printInt(1);
    } else {
        callMissing();
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(callMissing)"


def test_checker_378():
    """Error: UndeclaredFunction -- in while condition."""
    source = """
void main() {
    while (isDone()) {
        printInt(1);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(isDone)"


def test_checker_379():
    """Error: UndeclaredFunction -- used as struct field init via call."""
    source = """
struct Pair { int a; int b; };
void main() {
    Pair p = {compute(1), 2};
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(compute)"


def test_checker_380():
    """Error: UndeclaredFunction -- called in logical expression."""
    source = """
void main() {
    int r = 1 || missing();
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredFunction(missing)"


# ---------------------------------------------------------------------------
# SECTION P: UndeclaredStruct -- more edge cases (381-388)
# ---------------------------------------------------------------------------


def test_checker_381():
    """Error: UndeclaredStruct -- in nested struct member (second level)."""
    source = """
struct Inner { int x; };
struct Outer {
    Inner a;
    Missing b;
};
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(Missing)"


def test_checker_382():
    """Error: UndeclaredStruct -- parameter struct not declared."""
    source = """
void process(InputData d) {}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(InputData)"


def test_checker_383():
    """Error: UndeclaredStruct -- used in var before declaration."""
    source = """
void main() {
    Early e;
}
struct Early { int val; };
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(Early)"


def test_checker_384():
    """Error: UndeclaredStruct -- return type of function is missing struct."""
    source = """
Missing badFunc() {
    Missing m;
    return m;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(Missing)"


def test_checker_385():
    """Error: UndeclaredStruct -- struct field uses not-yet-declared struct."""
    source = """
struct Wrapper {
    Payload data;
};
struct Payload { int val; };
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(Payload)"


def test_checker_386():
    """Error: UndeclaredStruct -- parameter struct type not declared."""
    source = """
void f(TypeA a) {}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(TypeA)"


def test_checker_387():
    """Error: UndeclaredStruct -- used as local var type."""
    source = """
void main() {
    string s = "hello";
    int x = 5;
    Unknown u;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(Unknown)"


def test_checker_388():
    """Error: UndeclaredStruct -- explicit return type not declared (Phantom2)."""
    source = """
Phantom2 getPhantom2() {
    Phantom2 p;
    return p;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(Phantom2)"


# ---------------------------------------------------------------------------
# SECTION Q: TypeCannotBeInferred -- more edge cases (389-408)
# ---------------------------------------------------------------------------


def test_checker_389():
    """Error: TypeCannotBeInferred -- two unknowns in multiplication."""
    source = """
void main() {
    auto x;
    auto y;
    auto z = x * y;
}
"""
    result = Checker(source).check_from_source()
    assert result == "TypeCannotBeInferred(BinaryOp(Identifier(x), *, Identifier(y)))"


def test_checker_390():
    """Error: TypeCannotBeInferred -- auto never resolved in switch body."""
    source = """
void main() {
    int flag = 1;
    auto x;
    switch (flag) {
        case 1:
            break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_391():
    """Error: TypeCannotBeInferred -- two unknowns in !=."""
    source = """
void main() {
    auto a;
    auto b;
    int r = a != b;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_392():
    """Error: TypeCannotBeInferred -- auto in explicit void func, unused."""
    source = """
void broken() {
    auto x;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_393():
    """Error: TypeCannotBeInferred -- two unknowns assigned: sink = source."""
    source = """
void main() {
    auto sink;
    auto source;
    sink = source;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_394():
    """Error: TypeCannotBeInferred -- two unknowns: p + q."""
    source = """
void main() {
    auto p;
    auto q;
    auto r = p + q;
}
"""
    result = Checker(source).check_from_source()
    assert result == "TypeCannotBeInferred(BinaryOp(Identifier(p), +, Identifier(q)))"


def test_checker_395():
    """Error: TypeCannotBeInferred -- only used in postfix --."""
    source = """
void main() {
    auto n;
    n--;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_396():
    """Error: TypeCannotBeInferred -- struct literal no context."""
    source = """
void main() {
    auto x = {1, 2, 3};
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_397():
    """Error: TypeCannotBeInferred -- two unknowns in <=."""
    source = """
void main() {
    auto a;
    auto b;
    int r = a <= b;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_398():
    """Error: TypeCannotBeInferred -- auto inside nested while, unused."""
    source = """
void main() {
    int i = 0;
    while (i < 3) {
        auto hidden;
        ++i;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_399():
    """Error: TypeCannotBeInferred -- auto in case body unused."""
    source = """
void main() {
    int x = 1;
    switch (x) {
        case 1:
            auto unused;
            break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_400():
    """Error: TypeCannotBeInferred -- two unknowns in || op."""
    source = """
void main() {
    auto p;
    auto q;
    int r = p || q;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_401():
    """Error: TypeCannotBeInferred -- unresolved auto used in unary +."""
    source = """
void main() {
    auto x;
    auto y = +x;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_402():
    """Error: TypeCannotBeInferred -- auto never resolved in if-only block."""
    source = """
void main() {
    auto x;
    int flag = 1;
    if (flag) {
        printInt(1);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_403():
    """Error: TypeCannotBeInferred -- chained binary op, all unknowns."""
    source = """
void main() {
    auto a;
    auto b;
    auto c;
    auto d = a + b + c;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_404():
    """Error: TypeCannotBeInferred -- two unknowns in logical AND."""
    source = """
void main() {
    auto a;
    auto b;
    int r = a && b;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_405():
    """Error: TypeCannotBeInferred -- auto used only in prefix --."""
    source = """
void main() {
    auto x;
    --x;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_406():
    """Error: TypeCannotBeInferred -- two unknowns sum arg to consume(int)."""
    source = """
void consume(int x) {}
void main() {
    auto a;
    auto b;
    consume(a + b);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_407():
    """Error: TypeCannotBeInferred -- linked chain: a=b, b=c, all unknown."""
    source = """
void main() {
    auto a;
    auto b;
    auto c;
    a = b;
    b = c;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


def test_checker_408():
    """Error: TypeCannotBeInferred -- for condition: both i and n unknown."""
    source = """
void main() {
    auto i;
    auto n;
    for (; i < n;) {
        printInt(1);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeCannotBeInferred")


# ---------------------------------------------------------------------------
# SECTION R: TypeMismatchInStatement -- deeper cases (409-440)
# ---------------------------------------------------------------------------


def test_checker_409():
    """Error: TypeMismatchInStatement -- float var initialized with readInt()."""
    source = """
void main() {
    float f = readInt();
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_410():
    """Error: TypeMismatchInStatement -- int var initialized with readFloat()."""
    source = """
void main() {
    int x = readFloat();
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_411():
    """Error: TypeMismatchInStatement -- string var initialized with readInt()."""
    source = """
void main() {
    string s = readInt();
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_412():
    """Error: TypeMismatchInStatement -- int var init from float function."""
    source = """
float getF() { return 1.5; }
void main() {
    int x = getF();
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_413():
    """Error: TypeMismatchInStatement -- while condition is string variable."""
    source = """
void main() {
    string s = "hello";
    while (s) {
        break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_414():
    """Error: TypeMismatchInStatement -- return struct from int function."""
    source = """
struct Point { int x; int y; };
int badFuncA() {
    Point p = {1, 2};
    return p;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_415():
    """Error: TypeMismatchInStatement -- return int from struct function."""
    source = """
struct Point { int x; int y; };
Point badReturnA() {
    return 42;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_416():
    """Error: TypeMismatchInStatement -- member of struct assigned wrong type."""
    source = """
struct Box { int width; string label; };
void main() {
    Box b;
    b.width = "wrong";
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_417():
    """Error: TypeMismatchInStatement -- float member from int var."""
    source = """
struct Measure { float value; };
void main() {
    Measure m;
    int x = 5;
    m.value = x;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_418():
    """Error: TypeMismatchInStatement -- if condition is string variable."""
    source = """
void main() {
    string a = "hello";
    if (a) {
        printString(a);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_419():
    """Error: TypeMismatchInStatement -- return wrong struct type."""
    source = """
struct A { int x; };
struct B { int y; };
A getA2() {
    B b = {1};
    return b;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_420():
    """Error: TypeMismatchInStatement -- int var from struct."""
    source = """
struct Point { int x; int y; };
void main() {
    Point p = {1, 2};
    int x = p;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_421():
    """Error: TypeMismatchInStatement -- switch on float member."""
    source = """
struct Config { float ratio; };
void main() {
    Config c = {1.5};
    switch (c.ratio) {
        default: break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_422():
    """Error: TypeMismatchInStatement -- for condition uses float variable."""
    source = """
void main() {
    float step = 0.5;
    for (int i = 0; step; ++i) {
        printInt(i);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_423():
    """Error: TypeMismatchInStatement -- inferred func: int then string return."""
    source = """
mixed2() {
    return 1;
    return "oops";
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_424():
    """Error: TypeMismatchInStatement -- int var init from float arithmetic."""
    source = """
void main() {
    float a = 2.0;
    float b = 3.0;
    int result = a * b;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_425():
    """Error: TypeMismatchInStatement -- if condition is struct string member."""
    source = """
struct Info { string name; };
void main() {
    Info i = {"hello"};
    if (i.name) {
        printString("yes");
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_426():
    """Error: TypeMismatchInStatement -- inferred func: void return then value return."""
    source = """
confusing2() {
    return;
    return 5;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_427():
    """Error: TypeMismatchInStatement -- string var from struct expr."""
    source = """
struct Tag { string label; };
void main() {
    Tag t = {"info"};
    string s = t;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_428():
    """Error: TypeMismatchInStatement -- return float from int-expected func."""
    source = """
int isPositive(float x) {
    return x;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_429():
    """Error: TypeMismatchInStatement -- explicit int function returns struct."""
    source = """
struct Node { int val; };
int wrongStructReturn() {
    Node n = {5};
    return n;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_430():
    """Error: TypeMismatchInStatement -- string init from modulo (int)."""
    source = """
void main() {
    int x = 10;
    int y = 3;
    string s = x % y;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_431():
    """Error: TypeMismatchInStatement -- for condition is struct from function."""
    source = """
struct FlagB { int val; };
FlagB getFlagB() {
    FlagB f = {1};
    return f;
}
void main() {
    for (int i = 0; getFlagB(); ++i) {
        printInt(i);
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_432():
    """Error: TypeMismatchInStatement -- float member assigned string."""
    source = """
struct M { float val; };
void main() {
    M m;
    m.val = "text";
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_433():
    """Error: TypeMismatchInStatement -- struct member = different struct."""
    source = """
struct X { int n; };
struct Y { int n; };
struct Wrap { X x; };
void main() {
    Wrap w;
    Y y = {5};
    w.x = y;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_434():
    """Error: TypeMismatchInStatement -- float init from int comparison (int->float mismatch)."""
    source = """
void main() {
    int a = 5;
    int b = 3;
    float r = a > b;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_435():
    """Error: TypeMismatchInStatement -- assignment: int = readString()."""
    source = """
void main() {
    int x;
    x = readString();
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_436():
    """Error: TypeMismatchInStatement -- inferred func: float then int return."""
    source = """
mixedTypes() {
    return 3.14;
    return 1;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_437():
    """Error: TypeMismatchInStatement -- while condition is float struct member."""
    source = """
struct Sensor { float reading; };
void main() {
    Sensor s = {0.5};
    while (s.reading) {}
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_438():
    """Error: TypeMismatchInStatement -- return string from void function."""
    source = """
void voidButReturns() {
    return "oops";
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_439():
    """Error: TypeMismatchInStatement -- assignment: string = readFloat()."""
    source = """
void main() {
    string s;
    s = readFloat();
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_440():
    """Error: TypeMismatchInStatement -- switch expr is string variable."""
    source = """
void main() {
    string s = "hello";
    switch (s) {
        default: break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


# ---------------------------------------------------------------------------
# SECTION S: TypeMismatchInExpression -- deeper cases (441-470)
# ---------------------------------------------------------------------------


def test_checker_441():
    """Error: TypeMismatchInExpression -- struct + int."""
    source = """
struct PointA { int x; int y; };
void main() {
    PointA p = {1, 2};
    int r = p + 1;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_442():
    """Error: TypeMismatchInExpression -- struct - struct."""
    source = """
struct PointB { int x; int y; };
void main() {
    PointB a = {1, 2};
    PointB b = {3, 4};
    auto r = a - b;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_443():
    """Error: TypeMismatchInExpression -- string / string."""
    source = """
void main() {
    string a = "hello";
    string b = "world";
    auto r = a / b;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_444():
    """Error: TypeMismatchInExpression -- string - int."""
    source = """
void main() {
    string s = "test";
    int x = 3;
    auto r = s - x;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_445():
    """Error: TypeMismatchInExpression -- prefix ++ on string field."""
    source = """
struct InfoB { string label; };
void main() {
    InfoB i = {"test"};
    ++i.label;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_446():
    """Error: TypeMismatchInExpression -- postfix -- on string field."""
    source = """
struct ItemB { string name; };
void main() {
    ItemB it = {"hello"};
    it.name--;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_447():
    """Error: TypeMismatchInExpression -- prefix ++ on float member."""
    source = """
struct MeasureB { float value; };
void main() {
    MeasureB m = {3.14};
    ++m.value;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_448():
    """Error: TypeMismatchInExpression -- postfix ++ on float member."""
    source = """
struct ScoreB { float val; };
void main() {
    ScoreB s = {9.5};
    s.val++;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_449():
    """Error: TypeMismatchInExpression -- member access on auto resolved to int."""
    source = """
void main() {
    auto x = 5;
    int r = x.field;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_450():
    """Error: TypeMismatchInExpression -- passing struct to function expecting int."""
    source = """
struct BoxB { int size; };
void processB(int x) {}
void main() {
    BoxB b = {10};
    processB(b);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_451():
    """Error: TypeMismatchInExpression -- passing int to function expecting struct."""
    source = """
struct BoxC { int size; };
void drawB(BoxC b) {}
void main() {
    drawB(42);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_452():
    """Error: TypeMismatchInExpression -- passing float to function expecting string."""
    source = """
void doLog(string msg) {}
void main() {
    doLog(3.14);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_453():
    """Error: TypeMismatchInExpression -- passing string to function expecting int."""
    source = """
void setLevel(int n) {}
void main() {
    setLevel("high");
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_454():
    """Error: TypeMismatchInExpression -- member access on return of non-struct function."""
    source = """
int getNum2() { return 5; }
void main() {
    int r = getNum2().field;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_455():
    """Error: TypeMismatchInExpression -- ! applied to struct."""
    source = """
struct FlagC { int val; };
void main() {
    FlagC f = {1};
    int r = !f;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_456():
    """Error: TypeMismatchInExpression -- unary minus on struct."""
    source = """
struct VecB { int x; };
void main() {
    VecB v = {5};
    auto r = -v;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_457():
    """Error: TypeMismatchInExpression -- struct % int."""
    source = """
struct AmountB { int val; };
void main() {
    AmountB a = {10};
    int r = a % 3;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_458():
    """Error: TypeMismatchInExpression -- float % float."""
    source = """
void main() {
    float a = 5.5;
    float b = 2.5;
    float r = a % b;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_459():
    """Error: TypeMismatchInExpression -- string && string."""
    source = """
void main() {
    string a = "yes";
    string b = "no";
    int r = a && b;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_460():
    """Error: TypeMismatchInExpression -- string || int."""
    source = """
void main() {
    string s = "abc";
    int x = 1;
    int r = s || x;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_461():
    """Error: TypeMismatchInExpression -- access missing member on nested struct."""
    source = """
struct InnerB { int val; };
struct OuterB { InnerB i; };
void main() {
    OuterB o;
    int r = o.i.missing;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_462():
    """Error: TypeMismatchInExpression -- float used in modulo as dividend."""
    source = """
void main() {
    float f = 5.0;
    int n = 3;
    int r = f % n;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_463():
    """Error: TypeMismatchInExpression -- readString() compared with int using <."""
    source = """
void main() {
    string s = readString();
    int r = s < 5;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_464():
    """Error: TypeMismatchInExpression -- string as first arg where int expected."""
    source = """
void f2(int x, string y) {}
void main() {
    f2("bad", "good");
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_465():
    """Error: TypeMismatchInExpression -- struct >= struct."""
    source = """
struct ValA { int n; };
void main() {
    ValA a = {1};
    ValA b = {2};
    int r = a >= b;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_466():
    """Error: TypeMismatchInExpression -- extra float arg to single-param func."""
    source = """
void single2(int x) {}
void main() {
    single2(1, 2.5);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_467():
    """Error: TypeMismatchInExpression -- prefix ++ on bool result expression."""
    source = """
void main() {
    int x = 5;
    ++(x > 3);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_468():
    """Error: TypeMismatchInExpression -- struct nested literal missing a field."""
    source = """
struct Inner2 { int a; int b; };
struct Outer2 { Inner2 child; int extra; };
void main() {
    Outer2 o = {{1}, 5};
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_469():
    """Error: TypeMismatchInExpression -- printFloat given int+int arg."""
    source = """
void main() {
    int a = 2;
    int b = 3;
    printFloat(a + b);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


def test_checker_470():
    """Error: TypeMismatchInExpression -- printInt given float*float arg."""
    source = """
void main() {
    float a = 1.5;
    float b = 2.5;
    printInt(a * b);
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInExpression")


# ---------------------------------------------------------------------------
# SECTION T: MustInLoop -- more edge cases (471-480)
# ---------------------------------------------------------------------------


def test_checker_471():
    """Error: MustInLoop -- break in deeply nested if without any loop."""
    source = """
void main() {
    int x = 5;
    if (x > 0) {
        if (x > 2) {
            if (x > 4) {
                break;
            }
        }
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_472():
    """Error: MustInLoop -- continue in deeply nested if without any loop."""
    source = """
void main() {
    int x = 1;
    if (x == 1) {
        if (x > 0) {
            continue;
        }
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_473():
    """Error: MustInLoop -- continue in switch nested in if (no loop)."""
    source = """
void main() {
    int x = 1;
    switch (x) {
        case 1:
            if (x > 0) {
                continue;
            }
            break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_474():
    """Error: MustInLoop -- break at top level of non-main function."""
    source = """
void compute() {
    int val = 0;
    break;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_475():
    """Error: MustInLoop -- continue after all loops finished."""
    source = """
void f() {
    for (int i = 0; i < 3; ++i) {}
    while (0) {}
    continue;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_476():
    """Error: MustInLoop -- continue in process body with no loops."""
    source = """
void process() {
    int a = 1;
    int b = 2;
    continue;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_477():
    """Error: MustInLoop -- break in helper called inside a switch."""
    source = """
void badHelper() {
    break;
}
void main() {
    int x = 1;
    switch (x) {
        case 1:
            badHelper();
            break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_478():
    """Error: MustInLoop -- two breaks, first reported."""
    source = """
void main() {
    break;
    break;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_479():
    """Error: MustInLoop -- break after for but inside if."""
    source = """
void main() {
    for (int i = 0; i < 3; ++i) {
        printInt(i);
    }
    if (1) {
        break;
    }
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


def test_checker_480():
    """Error: MustInLoop -- break at top of function before any other statement."""
    source = """
void earlyBreak() {
    break;
    int x = 5;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("MustInLoop")


# ---------------------------------------------------------------------------
# SECTION U: Valid programs -- stress tests (481-495)
# ---------------------------------------------------------------------------


def test_checker_481():
    """Valid: deeply nested function calls, int and float."""
    source = """
int addInt(int a, int b) { return a + b; }
float addFloat(float a, float b) { return a + b; }
void main() {
    int r1 = addInt(addInt(1, 2), addInt(3, 4));
    float r2 = addFloat(addFloat(1.0, 2.0), addFloat(3.0, 4.0));
    printInt(r1);
    printFloat(r2);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_482():
    """Valid: struct with three levels of nesting."""
    source = """
struct L1 { int val; };
struct L2 { L1 inner; };
struct L3 { L2 mid; };
void main() {
    L1 l1 = {42};
    L2 l2 = {l1};
    L3 l3 = {l2};
    printInt(l3.mid.inner.val);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_483():
    """Valid: for loop creates auto vars each iteration."""
    source = """
void main() {
    for (auto i = 0; i < 10; ++i) {
        auto doubled = i * 2;
        auto tripled = i * 3;
        printInt(doubled + tripled);
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_484():
    """Valid: multiple structs, each in different function."""
    source = """
struct Circle { float radius; };
struct Square { int side; };
float circleArea(Circle c) {
    return c.radius * c.radius;
}
int squareArea(Square s) {
    return s.side * s.side;
}
void main() {
    Circle c = {3.0};
    Square s = {4};
    printFloat(circleArea(c));
    printInt(squareArea(s));
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_485():
    """Valid: complex comparison chain in condition."""
    source = """
void main() {
    int a = 5;
    int b = 10;
    int c = 15;
    int result = (a < b) && (b < c) && (a != c);
    printInt(result);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_486():
    """Valid: function taking two different structs."""
    source = """
struct AC { int x; };
struct BC { float y; };
void combine(AC a, BC b) {
    printInt(a.x);
    printFloat(b.y);
}
void main() {
    AC a = {5};
    BC b = {2.5};
    combine(a, b);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_487():
    """Valid: auto var inferred through sequence of assignments."""
    source = """
void main() {
    int known = 42;
    auto x;
    x = known;
    auto y;
    y = x;
    printInt(y);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_488():
    """Valid: while loop with compound condition."""
    source = """
void main() {
    int x = 0;
    int y = 10;
    while (x < y && y > 5) {
        ++x;
        y = y - 1;
    }
    printInt(x);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_489():
    """Valid: int and float operations kept separate."""
    source = """
void main() {
    int sum_int = 0;
    float sum_float = 0.0;
    sum_int = sum_int + 1;
    sum_float = sum_float + 1.5;
    printInt(sum_int);
    printFloat(sum_float);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_490():
    """Valid: struct returned and immediately accessed."""
    source = """
struct RangeB { int start; int end; };
RangeB fullRangeB() {
    RangeB r = {0, 100};
    return r;
}
void main() {
    int s = fullRangeB().start;
    int e = fullRangeB().end;
    printInt(s + e);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_491():
    """Valid: switch-case with multi-statement case body."""
    source = """
void main() {
    int x = 1;
    switch (x) {
        case 1:
            int a = 10;
            int b = 20;
            printInt(a + b);
            break;
        default:
            printInt(0);
    }
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_492():
    """Valid: auto struct var, member accessed after assignment."""
    source = """
struct PtB { int x; int y; };
PtB makeOriginB() {
    PtB p = {0, 0};
    return p;
}
void main() {
    auto origin = makeOriginB();
    auto shifted_x = origin.x + 5;
    auto shifted_y = origin.y + 3;
    printInt(shifted_x);
    printInt(shifted_y);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_493():
    """Valid: overloaded-style functions via struct wrappers."""
    source = """
struct IntValB { int n; };
struct FloatValB { float n; };
void showIntB(IntValB v) { printInt(v.n); }
void showFloatB(FloatValB v) { printFloat(v.n); }
void main() {
    IntValB iv = {5};
    FloatValB fv = {3.14};
    showIntB(iv);
    showFloatB(fv);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


def test_checker_494():
    """Valid: complex auto inference chain via binary ops."""
    source = """
void main() {
    int base = 10;
    auto x;
    auto y = x + base;
    printInt(y);
}
"""
    assert Checker(source).check_from_source() == "TypeCannotBeInferred(BinaryOp(Identifier(x), +, Identifier(base)))"


def test_checker_495():
    """Valid: nested structs with member modification."""
    source = """
struct InnerC { int val; };
struct OuterC { InnerC i; };
void modifyC(OuterC o) {
    o.i.val = 100;
}
void main() {
    InnerC i = {0};
    OuterC o = {i};
    modifyC(o);
    printInt(o.i.val);
}
"""
    assert Checker(source).check_from_source() == "Static checking passed"


# ---------------------------------------------------------------------------
# SECTION V: Priority / interaction tests (496-500)
# ---------------------------------------------------------------------------


def test_checker_496():
    """Error (priority): UndeclaredStruct before body errors."""
    source = """
void setup(GhostType g) {
    break;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredStruct(GhostType)"


def test_checker_497():
    """Error (priority): Redeclared Function before body-level TypeMismatch."""
    source = """
int compute(int x) { return x + 1; }
int compute(int y) { return "wrong"; }
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Function, compute)"


def test_checker_498():
    """Error (priority): TypeMismatch in first statement, not second."""
    source = """
void main() {
    int x = "oops";
    float y = 42;
}
"""
    result = Checker(source).check_from_source()
    assert result.startswith("TypeMismatchInStatement")


def test_checker_499():
    """Error (priority): UndeclaredIdentifier before TypeCannotBeInferred."""
    source = """
void main() {
    auto result = ghost + 1;
    auto x;
}
"""
    result = Checker(source).check_from_source()
    assert result == "UndeclaredIdentifier(ghost)"


def test_checker_500():
    """Error (priority): Redeclared Param before TypeMismatch in body."""
    source = """
void badFn(int x, float x) {
    int y = 3.14;
}
void main() {}
"""
    result = Checker(source).check_from_source()
    assert result == "Redeclared(Parameter, x)"
