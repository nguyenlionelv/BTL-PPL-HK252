"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer

# ========== Keywords (5 tests) ==========

def test_keyword_001():
    """Test 1"""
    tokenizer = Tokenizer("int")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"

def test_keyword_002():
    """Test 2"""
    tokenizer = Tokenizer("auto float")
    assert tokenizer.get_tokens_as_string() == "auto,float,<EOF>"

def test_keyword_003():
    """Test 3"""
    tokenizer = Tokenizer("struct Point")
    assert tokenizer.get_tokens_as_string() == "struct,Point,<EOF>"

def test_keyword_004():
    """Test 4"""
    tokenizer = Tokenizer("int AUTO")
    assert tokenizer.get_tokens_as_string() == "int,AUTO,<EOF>"

def test_keyword_005():
    """Test 5"""
    tokenizer = Tokenizer("if while for switch break continue return")
    assert tokenizer.get_tokens_as_string() == "if,while,for,switch,break,continue,return,<EOF>"

# ========== Operators (5 tests) ==========

def test_operator_006():
    """Test 6"""
    tokenizer = Tokenizer("+")
    assert tokenizer.get_tokens_as_string() == "+,<EOF>"

def test_operator_007():
    """Test 7"""
    tokenizer = Tokenizer("< > <= >=")
    assert tokenizer.get_tokens_as_string() == "<,>,<=,>=,<EOF>"

def test_operator_008():
    """Test 8"""
    tokenizer = Tokenizer("a==b")
    assert tokenizer.get_tokens_as_string() == "a,==,b,<EOF>"

def test_operator_009():
    """Test 9"""
    tokenizer = Tokenizer("x+++y")
    assert tokenizer.get_tokens_as_string() == "x,++,+,y,<EOF>"

def test_operator_010():
    """Test 10"""
    tokenizer = Tokenizer("a+b-c*d/e%f==g!=h&&i||!j")
    assert tokenizer.get_tokens_as_string() == "a,+,b,-,c,*,d,/,e,%,f,==,g,!=,h,&&,i,||,!,j,<EOF>"

# ========== Separators (5 tests) ==========

def test_separator_011():
    """Test 11"""
    tokenizer = Tokenizer("{ }")
    assert tokenizer.get_tokens_as_string() == "{,},<EOF>"

def test_separator_012():
    """Test 12"""
    tokenizer = Tokenizer("()")
    assert tokenizer.get_tokens_as_string() == "(,),<EOF>"

def test_separator_013():
    """Test 13"""
    tokenizer = Tokenizer("; , :")
    assert tokenizer.get_tokens_as_string() == ";,,,:,<EOF>"

def test_separator_014():
    """Test 14"""
    tokenizer = Tokenizer("func(a, b)")
    assert tokenizer.get_tokens_as_string() == "func,(,a,,,b,),<EOF>"

def test_separator_015():
    """Test 15"""
    tokenizer = Tokenizer("{ ( ) ; , : }")
    assert tokenizer.get_tokens_as_string() == "{,(,),;,,,:,},<EOF>"

# ========== Identifiers (5 tests) ==========

def test_identifier_016():
    """Test 16"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"

def test_identifier_017():
    """Test 17"""
    tokenizer = Tokenizer("var123")
    assert tokenizer.get_tokens_as_string() == "var123,<EOF>"

def test_identifier_018():
    """Test 18"""
    tokenizer = Tokenizer("_private my_var")
    assert tokenizer.get_tokens_as_string() == "_private,my_var,<EOF>"

def test_identifier_019():
    """Test 19"""
    tokenizer = Tokenizer("myVariableName")
    assert tokenizer.get_tokens_as_string() == "myVariableName,<EOF>"

def test_identifier_020():
    """Test 20"""
    tokenizer = Tokenizer("integer automat")
    assert tokenizer.get_tokens_as_string() == "integer,automat,<EOF>"

# ========== Comments (5 tests) ==========

def test_comment_021():
    """Test 21"""
    tokenizer = Tokenizer("// comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_comment_022():
    """Test 22"""
    tokenizer = Tokenizer("/* comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_comment_023():
    """Test 23"""
    tokenizer = Tokenizer("// comment\nint x")
    assert tokenizer.get_tokens_as_string() == "int,x,<EOF>"

def test_comment_024():
    """Test 24"""
    tokenizer = Tokenizer("/* line1\nline2 */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_comment_025():
    """Test 25"""
    tokenizer = Tokenizer("/* // not line comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

# ========== Integer Literals (5 tests) ==========

def test_integer_026():
    """Test 26"""
    tokenizer = Tokenizer("0")
    assert tokenizer.get_tokens_as_string() == "0,<EOF>"

def test_integer_027():
    """Test 27"""
    tokenizer = Tokenizer("7")
    assert tokenizer.get_tokens_as_string() == "7,<EOF>"

def test_integer_028():
    """Test 28"""
    tokenizer = Tokenizer("2147483647")
    assert tokenizer.get_tokens_as_string() == "2147483647,<EOF>"

def test_integer_029():
    """Test 29"""
    tokenizer = Tokenizer("007")
    assert tokenizer.get_tokens_as_string() == "007,<EOF>"

def test_integer_030():
    """Test 30"""
    tokenizer = Tokenizer("100*50/25%3")
    assert tokenizer.get_tokens_as_string() == "100,*,50,/,25,%,3,<EOF>"

# ========== Float Literals (10 tests) ==========

def test_float_031():
    """Test 31"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"

def test_float_032():
    """Test 32"""
    tokenizer = Tokenizer("42.")
    assert tokenizer.get_tokens_as_string() == "42.,<EOF>"

def test_float_033():
    """Test 33"""
    tokenizer = Tokenizer(".5")
    assert tokenizer.get_tokens_as_string() == ".5,<EOF>"

def test_float_034():
    """Test 34"""
    tokenizer = Tokenizer("1e4")
    assert tokenizer.get_tokens_as_string() == "1e4,<EOF>"

def test_float_035():
    """Test 35"""
    tokenizer = Tokenizer("2E-3")
    assert tokenizer.get_tokens_as_string() == "2E-3,<EOF>"

def test_float_036():
    """Test 36"""
    tokenizer = Tokenizer("5E+10")
    assert tokenizer.get_tokens_as_string() == "5E+10,<EOF>"

def test_float_037():
    """Test 37"""
    tokenizer = Tokenizer("3.14159e-10")
    assert tokenizer.get_tokens_as_string() == "3.14159e-10,<EOF>"

def test_float_038():
    """Test 38"""
    tokenizer = Tokenizer("1.e10")
    assert tokenizer.get_tokens_as_string() == "1.e10,<EOF>"

def test_float_039():
    """Test 39"""
    tokenizer = Tokenizer(".5e3")
    assert tokenizer.get_tokens_as_string() == ".5e3,<EOF>"

def test_float_040():
    """Test 40"""
    tokenizer = Tokenizer("1.5+2.3e4-.7")
    assert tokenizer.get_tokens_as_string() == "1.5,+,2.3e4,-,.7,<EOF>"

# ========== String Literals (10 tests) ==========

def test_string_041():
    """Test 41"""
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"

def test_string_042():
    """Test 42"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"

def test_string_043():
    """Test 43"""
    tokenizer = Tokenizer('"hello world"')
    assert tokenizer.get_tokens_as_string() == "hello world,<EOF>"

def test_string_044():
    """Test 44"""
    tokenizer = Tokenizer('"hello\\tworld"')
    assert tokenizer.get_tokens_as_string() == "hello\\tworld,<EOF>"

def test_string_045():
    """Test 45"""
    tokenizer = Tokenizer('"line1\\nline2"')
    assert tokenizer.get_tokens_as_string() == "line1\\nline2,<EOF>"

def test_string_046():
    """Test 46"""
    tokenizer = Tokenizer('"He said \\"Hi\\""')
    assert tokenizer.get_tokens_as_string() == 'He said \\"Hi\\",<EOF>'

def test_string_047():
    """Test 47"""
    tokenizer = Tokenizer('"C:\\\\path"')
    assert tokenizer.get_tokens_as_string() == "C:\\\\path,<EOF>"

def test_string_048():
    """Test 48"""
    tokenizer = Tokenizer('"\\b\\f\\r\\n\\t\\"\\\\"')
    assert tokenizer.get_tokens_as_string() == '\\b\\f\\r\\n\\t\\"\\\\,<EOF>'

def test_string_049():
    """Test 49"""
    tokenizer = Tokenizer('"first" "second"')
    assert tokenizer.get_tokens_as_string() == "first,second,<EOF>"

def test_string_050():
    """Test 50"""
    tokenizer = Tokenizer('print("Hello")')
    assert tokenizer.get_tokens_as_string() == "print,(,Hello,),<EOF>"

# ========== Error Tokens (10 tests) ==========

def test_error_051():
    """Test 51"""
    tokenizer = Tokenizer("@")
    assert tokenizer.get_tokens_as_string() == "Error Token @"

def test_error_052():
    """Test 52"""
    tokenizer = Tokenizer("#define")
    assert tokenizer.get_tokens_as_string() == "Error Token #"

def test_error_053():
    """Test 53"""
    tokenizer = Tokenizer("$var")
    assert tokenizer.get_tokens_as_string() == "Error Token $"

def test_error_054():
    """Test 54"""
    tokenizer = Tokenizer("a|b")
    assert tokenizer.get_tokens_as_string() == "a,Error Token |"

def test_error_055():
    """Test 55"""
    tokenizer = Tokenizer("a&b")
    assert tokenizer.get_tokens_as_string() == "a,Error Token &"

def test_error_056():
    """Test 56"""
    tokenizer = Tokenizer("array[0]")
    assert tokenizer.get_tokens_as_string() == "array,Error Token ["

def test_error_057():
    """Test 57"""
    tokenizer = Tokenizer("2^3")
    assert tokenizer.get_tokens_as_string() == "2,Error Token ^"

def test_error_058():
    """Test 58"""
    tokenizer = Tokenizer("`template`")
    assert tokenizer.get_tokens_as_string() == "Error Token `"

def test_error_059():
    """Test 59"""
    tokenizer = Tokenizer("x ? y")
    assert tokenizer.get_tokens_as_string() == "x,Error Token ?"

def test_error_060():
    """Test 60"""
    tokenizer = Tokenizer("~x")
    assert tokenizer.get_tokens_as_string() == "Error Token ~"

# ========== Illegal Escape in String (10 tests) ==========

def test_illegal_061():
    """Test 61"""
    tokenizer = Tokenizer('"hello\\g"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: hello\\g"

def test_illegal_062():
    """Test 62"""
    tokenizer = Tokenizer('"test\\\\\\a"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: test\\\\\\a"

def test_illegal_063():
    """Test 63"""
    tokenizer = Tokenizer('"\\1"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\1"

def test_illegal_064():
    """Test 64"""
    tokenizer = Tokenizer('"\\\\\\o "')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\\\\\o"

def test_illegal_065():
    """Test 65"""
    tokenizer = Tokenizer('"\\u0041"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\u"

def test_illegal_066():
    """Test 66"""
    tokenizer = Tokenizer('"valid\\z"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: valid\\z"

def test_illegal_067():
    """Test 67"""
    tokenizer = Tokenizer('"\\\\n\\\\x"')
    assert tokenizer.get_tokens_as_string() == "\\\\n\\\\x,<EOF>"

def test_illegal_068():
    """Test 68"""
    tokenizer = Tokenizer('"\\\\\\0"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\\\\\0"

def test_illegal_069():
    """Test 69"""
    tokenizer = Tokenizer('"\\\\\\a"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\\\\\a"

def test_illegal_070():
    """Test 70"""
    tokenizer = Tokenizer('"path\\\\\\/file"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: path\\\\\\/"

# ========== Unclosed String (10 tests) ==========

def test_unclosed_071():
    """Test 71"""
    tokenizer = Tokenizer('"hello')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: hello"

def test_unclosed_072():
    """Test 72"""
    tokenizer = Tokenizer('"hello\n')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: hello"

def test_unclosed_073():
    """Test 73"""
    tokenizer = Tokenizer('"')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: "

def test_unclosed_074():
    """Test 74"""
    tokenizer = Tokenizer('"text\\\\n')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: text\\\\n"

def test_unclosed_075():
    """Test 75"""
    tokenizer = Tokenizer('"This is a long string without closing')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: This is a long string without closing"

def test_unclosed_076():
    """Test 76"""
    tokenizer = Tokenizer('"test\r')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: test"

def test_unclosed_077():
    """Test 77"""
    tokenizer = Tokenizer('auto x = "hello')
    assert tokenizer.get_tokens_as_string() == "auto,x,=,Unclosed String: hello"

def test_unclosed_078():
    """Test 78"""
    tokenizer = Tokenizer('"He said \\"Hi')
    assert tokenizer.get_tokens_as_string() == 'Unclosed String: He said \\"Hi'

def test_unclosed_079():
    """Test 79"""
    tokenizer = Tokenizer('"line1\nline2"')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: line1"

def test_unclosed_080():
    """Test 80"""
    tokenizer = Tokenizer('"\\\\t\\\\n\\\\r')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: \\\\t\\\\n\\\\r"

# ========== Real Programs & Mixed (20 tests) ==========

def test_comprehensive_081():
    """Test 81"""
    tokenizer = Tokenizer("int x = 5;")
    assert tokenizer.get_tokens_as_string() == "int,x,=,5,;,<EOF>"

def test_comprehensive_082():
    """Test 82"""
    tokenizer = Tokenizer("auto y = 3.14;")
    assert tokenizer.get_tokens_as_string() == "auto,y,=,3.14,;,<EOF>"

def test_comprehensive_083():
    """Test 83"""
    tokenizer = Tokenizer("int add(int x, int y) {")
    assert tokenizer.get_tokens_as_string() == "int,add,(,int,x,,,int,y,),{,<EOF>"

def test_comprehensive_084():
    """Test 84"""
    tokenizer = Tokenizer("if (x > 0) { return x; }")
    assert tokenizer.get_tokens_as_string() == "if,(,x,>,0,),{,return,x,;,},<EOF>"

def test_comprehensive_085():
    """Test 85"""
    tokenizer = Tokenizer("while (i < 10) { i++; }")
    assert tokenizer.get_tokens_as_string() == "while,(,i,<,10,),{,i,++,;,},<EOF>"

def test_comprehensive_086():
    """Test 86"""
    tokenizer = Tokenizer("for (auto i = 0; i < 10; ++i)")
    assert tokenizer.get_tokens_as_string() == "for,(,auto,i,=,0,;,i,<,10,;,++,i,),<EOF>"

def test_comprehensive_087():
    """Test 87"""
    tokenizer = Tokenizer("switch (x) { case 1: break; default: }")
    assert tokenizer.get_tokens_as_string() == "switch,(,x,),{,case,1,:,break,;,default,:,},<EOF>"

def test_comprehensive_088():
    """Test 88"""
    tokenizer = Tokenizer("struct Point { int x; int y; };")
    assert tokenizer.get_tokens_as_string() == "struct,Point,{,int,x,;,int,y,;,},;,<EOF>"

def test_comprehensive_089():
    """Test 89"""
    tokenizer = Tokenizer("Point p = {10, 20};")
    assert tokenizer.get_tokens_as_string() == "Point,p,=,{,10,,,20,},;,<EOF>"

def test_comprehensive_090():
    """Test 90"""
    tokenizer = Tokenizer("p.x = obj.y.z;")
    assert tokenizer.get_tokens_as_string() == "p,.,x,=,obj,.,y,.,z,;,<EOF>"

def test_comprehensive_091():
    """Test 91"""
    tokenizer = Tokenizer('print("Hello, World!");')
    assert tokenizer.get_tokens_as_string() == "print,(,Hello, World!,),;,<EOF>"

def test_comprehensive_092():
    """Test 92"""
    tokenizer = Tokenizer("result = (a + b) * c - d / e % f;")
    assert tokenizer.get_tokens_as_string() == "result,=,(,a,+,b,),*,c,-,d,/,e,%,f,;,<EOF>"

def test_comprehensive_093():
    """Test 93"""
    tokenizer = Tokenizer("int x; // variable\nfloat y;")
    assert tokenizer.get_tokens_as_string() == "int,x,;,float,y,;,<EOF>"

def test_comprehensive_094():
    """Test 94"""
    tokenizer = Tokenizer("int x = @")
    assert tokenizer.get_tokens_as_string() == "int,x,=,Error Token @"

def test_comprehensive_095():
    """Test 95"""
    tokenizer = Tokenizer('auto s = "hello\\\\x";')
    assert tokenizer.get_tokens_as_string() == "auto,s,=,hello\\\\x,;,<EOF>"

def test_comprehensive_096():
    """Test 96"""
    tokenizer = Tokenizer('print("hello')
    assert tokenizer.get_tokens_as_string() == "print,(,Unclosed String: hello"

def test_comprehensive_097():
    """Test 97"""
    tokenizer = Tokenizer("a+b-c*d/e%f==g!=h<i>j<=k>=l&&m||!n")
    assert tokenizer.get_tokens_as_string() == "a,+,b,-,c,*,d,/,e,%,f,==,g,!=,h,<,i,>,j,<=,k,>=,l,&&,m,||,!,n,<EOF>"

def test_comprehensive_098():
    """Test 98"""
    tokenizer = Tokenizer("int factorial(int n) { if (n <= 1) return 1; return n * factorial(n - 1); }")
    assert tokenizer.get_tokens_as_string() == "int,factorial,(,int,n,),{,if,(,n,<=,1,),return,1,;,return,n,*,factorial,(,n,-,1,),;,},<EOF>"

def test_comprehensive_099():
    """Test 99"""
    tokenizer = Tokenizer("float x = 3.14; obj.member;")
    assert tokenizer.get_tokens_as_string() == "float,x,=,3.14,;,obj,.,member,;,<EOF>"

def test_comprehensive_100():
    """Test 100"""
    tokenizer = Tokenizer('int x=5; /* comment */ "test\\\\x" @')
    assert tokenizer.get_tokens_as_string() == "int,x,=,5,;,test\\\\x,Error Token @"
