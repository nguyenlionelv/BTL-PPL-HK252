"""
Comprehensive Lexer Test Suite for TyC Compiler
150 test cases covering all lexical features
"""

import pytest
from tests.utils import Tokenizer


# ========== SECTION 1: Keywords (18 tests) ==========

def test_keyword_auto_001():
    """Test 1: Keyword auto"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"

def test_keyword_break_002():
    """Test 2: Keyword break"""
    tokenizer = Tokenizer("break")
    assert tokenizer.get_tokens_as_string() == "break,<EOF>"

def test_keyword_case_003():
    """Test 3: Keyword case"""
    tokenizer = Tokenizer("case")
    assert tokenizer.get_tokens_as_string() == "case,<EOF>"

def test_keyword_continue_004():
    """Test 4: Keyword continue"""
    tokenizer = Tokenizer("continue")
    assert tokenizer.get_tokens_as_string() == "continue,<EOF>"

def test_keyword_default_005():
    """Test 5: Keyword default"""
    tokenizer = Tokenizer("default")
    assert tokenizer.get_tokens_as_string() == "default,<EOF>"

def test_keyword_else_006():
    """Test 6: Keyword else"""
    tokenizer = Tokenizer("else")
    assert tokenizer.get_tokens_as_string() == "else,<EOF>"

def test_keyword_float_007():
    """Test 7: Keyword float"""
    tokenizer = Tokenizer("float")
    assert tokenizer.get_tokens_as_string() == "float,<EOF>"

def test_keyword_for_008():
    """Test 8: Keyword for"""
    tokenizer = Tokenizer("for")
    assert tokenizer.get_tokens_as_string() == "for,<EOF>"

def test_keyword_if_009():
    """Test 9: Keyword if"""
    tokenizer = Tokenizer("if")
    assert tokenizer.get_tokens_as_string() == "if,<EOF>"

def test_keyword_int_010():
    """Test 10: Keyword int"""
    tokenizer = Tokenizer("int")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"

def test_keyword_return_011():
    """Test 11: Keyword return"""
    tokenizer = Tokenizer("return")
    assert tokenizer.get_tokens_as_string() == "return,<EOF>"

def test_keyword_string_012():
    """Test 12: Keyword string"""
    tokenizer = Tokenizer("string")
    assert tokenizer.get_tokens_as_string() == "string,<EOF>"

def test_keyword_struct_013():
    """Test 13: Keyword struct"""
    tokenizer = Tokenizer("struct")
    assert tokenizer.get_tokens_as_string() == "struct,<EOF>"

def test_keyword_switch_014():
    """Test 14: Keyword switch"""
    tokenizer = Tokenizer("switch")
    assert tokenizer.get_tokens_as_string() == "switch,<EOF>"

def test_keyword_void_015():
    """Test 15: Keyword void"""
    tokenizer = Tokenizer("void")
    assert tokenizer.get_tokens_as_string() == "void,<EOF>"

def test_keyword_while_016():
    """Test 16: Keyword while"""
    tokenizer = Tokenizer("while")
    assert tokenizer.get_tokens_as_string() == "while,<EOF>"

def test_keyword_all_together_017():
    """Test 17: All keywords together"""
    tokenizer = Tokenizer("auto break case continue default else float for if int return string struct switch void while")
    assert tokenizer.get_tokens_as_string() == "auto,break,case,continue,default,else,float,for,if,int,return,string,struct,switch,void,while,<EOF>"

def test_keyword_case_sensitive_018():
    """Test 18: Keywords are case-sensitive (AUTO is identifier)"""
    tokenizer = Tokenizer("AUTO Auto aUto")
    assert tokenizer.get_tokens_as_string() == "AUTO,Auto,aUto,<EOF>"


# ========== SECTION 2: Operators (20 tests) ==========

def test_operator_plus_019():
    """Test 19: Plus operator"""
    tokenizer = Tokenizer("+")
    assert tokenizer.get_tokens_as_string() == "+,<EOF>"

def test_operator_minus_020():
    """Test 20: Minus operator"""
    tokenizer = Tokenizer("-")
    assert tokenizer.get_tokens_as_string() == "-,<EOF>"

def test_operator_multiply_021():
    """Test 21: Multiply operator"""
    tokenizer = Tokenizer("*")
    assert tokenizer.get_tokens_as_string() == "*,<EOF>"

def test_operator_divide_022():
    """Test 22: Divide operator"""
    tokenizer = Tokenizer("/")
    assert tokenizer.get_tokens_as_string() == "/,<EOF>"

def test_operator_modulo_023():
    """Test 23: Modulo operator"""
    tokenizer = Tokenizer("%")
    assert tokenizer.get_tokens_as_string() == "%,<EOF>"

def test_operator_equal_024():
    """Test 24: Equal operator"""
    tokenizer = Tokenizer("==")
    assert tokenizer.get_tokens_as_string() == "==,<EOF>"

def test_operator_not_equal_025():
    """Test 25: Not equal operator"""
    tokenizer = Tokenizer("!=")
    assert tokenizer.get_tokens_as_string() == "!=,<EOF>"

def test_operator_less_than_026():
    """Test 26: Less than operator"""
    tokenizer = Tokenizer("<")
    assert tokenizer.get_tokens_as_string() == "<,<EOF>"

def test_operator_greater_than_027():
    """Test 27: Greater than operator"""
    tokenizer = Tokenizer(">")
    assert tokenizer.get_tokens_as_string() == ">,<EOF>"

def test_operator_less_equal_028():
    """Test 28: Less than or equal operator"""
    tokenizer = Tokenizer("<=")
    assert tokenizer.get_tokens_as_string() == "<=,<EOF>"

def test_operator_greater_equal_029():
    """Test 29: Greater than or equal operator"""
    tokenizer = Tokenizer(">=")
    assert tokenizer.get_tokens_as_string() == ">=,<EOF>"

def test_operator_logical_or_030():
    """Test 30: Logical OR operator"""
    tokenizer = Tokenizer("||")
    assert tokenizer.get_tokens_as_string() == "||,<EOF>"

def test_operator_logical_and_031():
    """Test 31: Logical AND operator"""
    tokenizer = Tokenizer("&&")
    assert tokenizer.get_tokens_as_string() == "&&,<EOF>"

def test_operator_logical_not_032():
    """Test 32: Logical NOT operator"""
    tokenizer = Tokenizer("!")
    assert tokenizer.get_tokens_as_string() == "!,<EOF>"

def test_operator_increment_033():
    """Test 33: Increment operator"""
    tokenizer = Tokenizer("++")
    assert tokenizer.get_tokens_as_string() == "++,<EOF>"

def test_operator_decrement_034():
    """Test 34: Decrement operator"""
    tokenizer = Tokenizer("--")
    assert tokenizer.get_tokens_as_string() == "--,<EOF>"

def test_operator_assign_035():
    """Test 35: Assignment operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"

def test_operator_dot_036():
    """Test 36: Dot operator (member access)"""
    tokenizer = Tokenizer(".")
    assert tokenizer.get_tokens_as_string() == ".,<EOF>"

def test_operator_longest_match_037():
    """Test 37: Operator longest match (== vs =)"""
    tokenizer = Tokenizer("a==b")
    assert tokenizer.get_tokens_as_string() == "a,==,b,<EOF>"

def test_operator_mixed_chain_038():
    """Test 38: Mixed operator chain"""
    tokenizer = Tokenizer("a+++b")
    assert tokenizer.get_tokens_as_string() == "a,++,+,b,<EOF>"


# ========== SECTION 3: Separators (7 tests) ==========

def test_separator_left_brace_039():
    """Test 39: Left brace"""
    tokenizer = Tokenizer("{")
    assert tokenizer.get_tokens_as_string() == "{,<EOF>"

def test_separator_right_brace_040():
    """Test 40: Right brace"""
    tokenizer = Tokenizer("}")
    assert tokenizer.get_tokens_as_string() == "},<EOF>"

def test_separator_left_paren_041():
    """Test 41: Left parenthesis"""
    tokenizer = Tokenizer("(")
    assert tokenizer.get_tokens_as_string() == "(,<EOF>"

def test_separator_right_paren_042():
    """Test 42: Right parenthesis"""
    tokenizer = Tokenizer(")")
    assert tokenizer.get_tokens_as_string() == "),<EOF>"

def test_separator_semicolon_043():
    """Test 43: Semicolon"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"

def test_separator_comma_044():
    """Test 44: Comma"""
    tokenizer = Tokenizer(",")
    assert tokenizer.get_tokens_as_string() == ",,<EOF>"

def test_separator_colon_045():
    """Test 45: Colon"""
    tokenizer = Tokenizer(":")
    assert tokenizer.get_tokens_as_string() == ":,<EOF>"


# ========== SECTION 4: Integer Literals (10 tests) ==========

def test_integer_zero_046():
    """Test 46: Zero"""
    tokenizer = Tokenizer("0")
    assert tokenizer.get_tokens_as_string() == "0,<EOF>"

def test_integer_single_digit_047():
    """Test 47: Single digit"""
    tokenizer = Tokenizer("7")
    assert tokenizer.get_tokens_as_string() == "7,<EOF>"

def test_integer_multi_digit_048():
    """Test 48: Multi-digit integer"""
    tokenizer = Tokenizer("123456")
    assert tokenizer.get_tokens_as_string() == "123456,<EOF>"

def test_integer_large_049():
    """Test 49: Large integer"""
    tokenizer = Tokenizer("2147483647")
    assert tokenizer.get_tokens_as_string() == "2147483647,<EOF>"

def test_integer_leading_zero_050():
    """Test 50: Leading zeros split into multiple tokens"""
    tokenizer = Tokenizer("007")
    assert tokenizer.get_tokens_as_string() == "0,0,7,<EOF>"

def test_integer_in_expression_051():
    """Test 51: Integers in expression"""
    tokenizer = Tokenizer("5+10-3")
    assert tokenizer.get_tokens_as_string() == "5,+,10,-,3,<EOF>"

def test_integer_sequence_052():
    """Test 52: Sequence of integers"""
    tokenizer = Tokenizer("1 22 333 4444")
    assert tokenizer.get_tokens_as_string() == "1,22,333,4444,<EOF>"

def test_integer_with_operators_053():
    """Test 53: Integers with all arithmetic operators"""
    tokenizer = Tokenizer("100*50/25%3")
    assert tokenizer.get_tokens_as_string() == "100,*,50,/,25,%,3,<EOF>"

def test_integer_negative_context_054():
    """Test 54: Minus as operator (not negative literal)"""
    tokenizer = Tokenizer("5-3")
    assert tokenizer.get_tokens_as_string() == "5,-,3,<EOF>"

def test_integer_boundaries_055():
    """Test 55: Integer at boundaries"""
    tokenizer = Tokenizer("(42)")
    assert tokenizer.get_tokens_as_string() == "(,42,),<EOF>"


# ========== SECTION 5: Float Literals (15 tests) ==========

def test_float_simple_decimal_056():
    """Test 56: Simple decimal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"

def test_float_decimal_at_end_057():
    """Test 57: Decimal point at end"""
    tokenizer = Tokenizer("42.")
    assert tokenizer.get_tokens_as_string() == "42.,<EOF>"

def test_float_decimal_at_start_058():
    """Test 58: Decimal point at start"""
    tokenizer = Tokenizer(".5")
    assert tokenizer.get_tokens_as_string() == ".5,<EOF>"

def test_float_exponent_positive_059():
    """Test 59: Exponent with positive sign"""
    tokenizer = Tokenizer("1e4")
    assert tokenizer.get_tokens_as_string() == "1e4,<EOF>"

def test_float_exponent_negative_060():
    """Test 60: Exponent with negative sign"""
    tokenizer = Tokenizer("2E-3")
    assert tokenizer.get_tokens_as_string() == "2E-3,<EOF>"

def test_float_exponent_explicit_plus_061():
    """Test 61: Exponent with explicit plus"""
    tokenizer = Tokenizer("5E+10")
    assert tokenizer.get_tokens_as_string() == "5E+10,<EOF>"

def test_float_full_format_062():
    """Test 62: Float with all components"""
    tokenizer = Tokenizer("3.14159e-10")
    assert tokenizer.get_tokens_as_string() == "3.14159e-10,<EOF>"

def test_float_zero_formats_063():
    """Test 63: Different zero representations"""
    tokenizer = Tokenizer("0.0 .0 0.")
    assert tokenizer.get_tokens_as_string() == "0.0,.0,0.,<EOF>"

def test_float_scientific_large_064():
    """Test 64: Large scientific notation"""
    tokenizer = Tokenizer("9.99E+100")
    assert tokenizer.get_tokens_as_string() == "9.99E+100,<EOF>"

def test_float_scientific_tiny_065():
    """Test 65: Tiny scientific notation"""
    tokenizer = Tokenizer("1e-100")
    assert tokenizer.get_tokens_as_string() == "1e-100,<EOF>"

def test_float_edge_case_dot_exp_066():
    """Test 66: Decimal at end with exponent"""
    tokenizer = Tokenizer("1.e10")
    assert tokenizer.get_tokens_as_string() == "1.e10,<EOF>"

def test_float_edge_case_start_exp_067():
    """Test 67: Decimal at start with exponent"""
    tokenizer = Tokenizer(".5e3")
    assert tokenizer.get_tokens_as_string() == ".5e3,<EOF>"

def test_float_in_expression_068():
    """Test 68: Floats in expression"""
    tokenizer = Tokenizer("1.5+2.3e4-.7")
    assert tokenizer.get_tokens_as_string() == "1.5,+,2.3e4,-,.7,<EOF>"

def test_float_vs_member_access_069():
    """Test 69: Float vs member access"""
    tokenizer = Tokenizer("3.14 obj.member")
    assert tokenizer.get_tokens_as_string() == "3.14,obj,.,member,<EOF>"

def test_float_both_e_and_E_070():
    """Test 70: Both lowercase and uppercase E"""
    tokenizer = Tokenizer("1e5 2E3")
    assert tokenizer.get_tokens_as_string() == "1e5,2E3,<EOF>"


# ========== SECTION 6: String Literals (15 tests) ==========

def test_string_empty_071():
    """Test 71: Empty string"""
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"

def test_string_simple_072():
    """Test 72: Simple string"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"

def test_string_with_spaces_073():
    """Test 73: String with spaces"""
    tokenizer = Tokenizer('"hello world"')
    assert tokenizer.get_tokens_as_string() == "hello world,<EOF>"

def test_string_escape_tab_074():
    """Test 74: Escape sequence tab"""
    tokenizer = Tokenizer('"hello\\\\tworld"')
    assert tokenizer.get_tokens_as_string() == "hello\\\\tworld,<EOF>"

def test_string_escape_newline_075():
    """Test 75: Escape sequence newline"""
    tokenizer = Tokenizer('"line1\\\\nline2"')
    assert tokenizer.get_tokens_as_string() == "line1\\\\nline2,<EOF>"

def test_string_escape_quote_076():
    """Test 76: Escaped quote"""
    tokenizer = Tokenizer('"He said \\\\\\"Hi\\\\\\""')
    assert tokenizer.get_tokens_as_string() == r'He said \\\"Hi\\\",<EOF>'

def test_string_escape_backslash_077():
    """Test 77: Escaped backslash"""
    tokenizer = Tokenizer('"C:\\\\\\\\\\\\\\\\path"')
    assert tokenizer.get_tokens_as_string() == "C:\\\\\\\\\\\\\\\\path,<EOF>"

def test_string_all_escapes_078():
    """Test 78: All valid escape sequences"""
    tokenizer = Tokenizer('"\\\\b\\\\f\\\\r\\\\n\\\\t\\\\\\"\\\\\\\\\\\\\\\\."')
    assert tokenizer.get_tokens_as_string() == '\\\\b\\\\f\\\\r\\\\n\\\\t\\\\\\"\\\\\\\\\\\\\\\\.,<EOF>'

def test_string_multiple_079():
    """Test 79: Multiple strings"""
    tokenizer = Tokenizer('"first" "second" "third"')
    assert tokenizer.get_tokens_as_string() == "first,second,third,<EOF>"

def test_string_with_numbers_080():
    """Test 80: String with numbers"""
    tokenizer = Tokenizer('"Value: 12345"')
    assert tokenizer.get_tokens_as_string() == "Value: 12345,<EOF>"

def test_string_with_special_chars_081():
    """Test 81: String with special characters"""
    tokenizer = Tokenizer('"!@#$%^&*()_+-="')
    assert tokenizer.get_tokens_as_string() == "!@#$%^&*()_+-=,<EOF>"

def test_string_long_082():
    """Test 82: Long string"""
    tokenizer = Tokenizer('"' + 'a'*100 + '"')
    assert tokenizer.get_tokens_as_string() == 'a'*100 + ",<EOF>"

def test_string_in_function_083():
    """Test 83: String in function call"""
    tokenizer = Tokenizer('print("Hello")')
    assert tokenizer.get_tokens_as_string() == "print,(,Hello,),<EOF>"

def test_string_mixed_content_084():
    """Test 84: Mixed content in string"""
    tokenizer = Tokenizer('"Mix: 123 abc !@# \\\\n\\\\t"')
    assert tokenizer.get_tokens_as_string() == "Mix: 123 abc !@# \\\\n\\\\t,<EOF>"

def test_string_quotes_removed_085():
    """Test 85: Verify quotes are removed"""
    tokenizer = Tokenizer('"test"')
    result = tokenizer.get_tokens_as_string()
    assert '"' not in result.replace('<EOF>', '').replace(',', '')


# ========== SECTION 7: Identifiers (10 tests) ==========

def test_identifier_single_letter_086():
    """Test 86: Single letter identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"

def test_identifier_multi_letter_087():
    """Test 87: Multi-letter identifier"""
    tokenizer = Tokenizer("variable")
    assert tokenizer.get_tokens_as_string() == "variable,<EOF>"

def test_identifier_with_digits_088():
    """Test 88: Identifier with digits"""
    tokenizer = Tokenizer("var123")
    assert tokenizer.get_tokens_as_string() == "var123,<EOF>"

def test_identifier_with_underscores_089():
    """Test 89: Identifier with underscores"""
    tokenizer = Tokenizer("_private my_var __special")
    assert tokenizer.get_tokens_as_string() == "_private,my_var,__special,<EOF>"

def test_identifier_starts_underscore_090():
    """Test 90: Identifier starting with underscore"""
    tokenizer = Tokenizer("_test")
    assert tokenizer.get_tokens_as_string() == "_test,<EOF>"

def test_identifier_camelCase_091():
    """Test 91: CamelCase identifier"""
    tokenizer = Tokenizer("myVariableName")
    assert tokenizer.get_tokens_as_string() == "myVariableName,<EOF>"

def test_identifier_PascalCase_092():
    """Test 92: PascalCase identifier"""
    tokenizer = Tokenizer("MyClassName")
    assert tokenizer.get_tokens_as_string() == "MyClassName,<EOF>"

def test_identifier_snake_case_093():
    """Test 93: snake_case identifier"""
    tokenizer = Tokenizer("my_function_name")
    assert tokenizer.get_tokens_as_string() == "my_function_name,<EOF>"

def test_identifier_not_keyword_094():
    """Test 94: Similar to keyword but not keyword"""
    tokenizer = Tokenizer("integer automat")
    assert tokenizer.get_tokens_as_string() == "integer,automat,<EOF>"

def test_identifier_long_095():
    """Test 95: Very long identifier"""
    tokenizer = Tokenizer("thisIsAVeryLongIdentifierName123")
    assert tokenizer.get_tokens_as_string() == "thisIsAVeryLongIdentifierName123,<EOF>"


# ========== SECTION 8: Comments (8 tests) ==========

def test_comment_line_simple_096():
    """Test 96: Simple line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_comment_line_before_code_097():
    """Test 97: Line comment before code"""
    tokenizer = Tokenizer("// comment\nint x")
    assert tokenizer.get_tokens_as_string() == "int,x,<EOF>"

def test_comment_block_simple_098():
    """Test 98: Simple block comment"""
    tokenizer = Tokenizer("/* comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_comment_block_multiline_099():
    """Test 99: Multiline block comment"""
    tokenizer = Tokenizer("/* line1\\nline2\\nline3 */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_comment_block_with_slashes_100():
    """Test 100: Block comment with //"""
    tokenizer = Tokenizer("/* // not line comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_comment_line_with_block_101():
    """Test 101: Line comment with /* */"""
    tokenizer = Tokenizer("// /* not block */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_comment_block_empty_102():
    """Test 102: Empty block comment"""
    tokenizer = Tokenizer("/**/")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_comment_mixed_with_code_103():
    """Test 103: Comments mixed with code"""
    tokenizer = Tokenizer("int x; // variable\n/* block */ int y;")
    assert tokenizer.get_tokens_as_string() == "int,x,;,int,y,;,<EOF>"


# ========== SECTION 9: Error Cases (20 tests) ==========

def test_error_illegal_escape_x_104():
    """Test 104: Illegal escape \\\\x"""
    tokenizer = Tokenizer('"hello\\\\x"')
    assert tokenizer.get_tokens_as_string() == "hello\\\\x,<EOF>"

def test_error_illegal_escape_a_105():
    """Test 105: Illegal escape \\\\a"""
    tokenizer = Tokenizer('"test\\\\a"')
    assert tokenizer.get_tokens_as_string() == "test\\\\a,<EOF>"

def test_error_illegal_escape_digit_106():
    """Test 106: Illegal escape \\\\1"""
    tokenizer = Tokenizer('"\\\\1"')
    assert tokenizer.get_tokens_as_string() == "\\\\1,<EOF>"

def test_error_illegal_escape_space_107():
    """Test 107: Illegal escape with space"""
    tokenizer = Tokenizer('"\\ "')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\ "

def test_error_illegal_escape_unicode_108():
    """Test 108: Illegal unicode escape"""
    tokenizer = Tokenizer('"\\u0041"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\u"

def test_error_unclose_string_eof_109():
    """Test 109: Unclosed string at EOF"""
    tokenizer = Tokenizer('"hello')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: hello"

def test_error_unclose_string_newline_110():
    """Test 110: Unclosed string at newline"""
    tokenizer = Tokenizer('"hello\\n')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: hello\\n"

def test_error_unclose_string_empty_111():
    """Test 111: Unclosed empty string"""
    tokenizer = Tokenizer('"')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: "

def test_error_unclose_string_with_escape_112():
    """Test 112: Unclosed with valid escape"""
    tokenizer = Tokenizer('"text\\\\n')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: text\\\\n"

def test_error_char_at_sign_113():
    """Test 113: Invalid character @"""
    tokenizer = Tokenizer("@")
    assert tokenizer.get_tokens_as_string() == "Error Token @"

def test_error_char_hash_114():
    """Test 114: Invalid character #"""
    tokenizer = Tokenizer("#")
    assert tokenizer.get_tokens_as_string() == "Error Token #"

def test_error_char_dollar_115():
    """Test 115: Invalid character $"""
    tokenizer = Tokenizer("$")
    assert tokenizer.get_tokens_as_string() == "Error Token $"

def test_error_char_single_pipe_116():
    """Test 116: Single pipe (|| valid, | not)"""
    tokenizer = Tokenizer("a|b")
    assert tokenizer.get_tokens_as_string() == "a,Error Token |"

def test_error_char_single_ampersand_117():
    """Test 117: Single ampersand (&& valid, & not)"""
    tokenizer = Tokenizer("a&b")
    assert tokenizer.get_tokens_as_string() == "a,Error Token &"

def test_error_char_question_118():
    """Test 118: Question mark not valid"""
    tokenizer = Tokenizer("?")
    assert tokenizer.get_tokens_as_string() == "Error Token ?"

def test_error_char_bracket_119():
    """Test 119: Square brackets not valid"""
    tokenizer = Tokenizer("[")
    assert tokenizer.get_tokens_as_string() == "Error Token ["

def test_error_char_tilde_120():
    """Test 120: Tilde not valid"""
    tokenizer = Tokenizer("~")
    assert tokenizer.get_tokens_as_string() == "Error Token ~"

def test_error_char_backtick_121():
    """Test 121: Backtick not valid"""
    tokenizer = Tokenizer("`")
    assert tokenizer.get_tokens_as_string() == "Error Token `"

def test_error_char_caret_122():
    """Test 122: Caret not valid"""
    tokenizer = Tokenizer("^")
    assert tokenizer.get_tokens_as_string() == "Error Token ^"

def test_error_priority_illegal_over_unclose_123():
    """Test 123: Illegal escape detected before unclosed"""
    tokenizer = Tokenizer('"test\\x')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: test\\x"


# ========== SECTION 10: Real Program Fragments (15 tests) ==========

def test_program_var_decl_124():
    """Test 124: Variable declaration"""
    tokenizer = Tokenizer("int x = 5;")
    assert tokenizer.get_tokens_as_string() == "int,x,=,5,;,<EOF>"

def test_program_auto_var_125():
    """Test 125: Auto variable"""
    tokenizer = Tokenizer("auto y = 3.14;")
    assert tokenizer.get_tokens_as_string() == "auto,y,=,3.14,;,<EOF>"

def test_program_function_decl_126():
    """Test 126: Function declaration"""
    tokenizer = Tokenizer("int add(int x, int y) {")
    assert tokenizer.get_tokens_as_string() == "int,add,(,int,x,,,int,y,),{,<EOF>"

def test_program_if_statement_127():
    """Test 127: If statement"""
    tokenizer = Tokenizer("if (x > 0) { return x; }")
    assert tokenizer.get_tokens_as_string() == "if,(,x,>,0,),{,return,x,;,},<EOF>"

def test_program_if_else_128():
    """Test 128: If-else statement"""
    tokenizer = Tokenizer("if (x) { y = 1; } else { y = 0; }")
    assert tokenizer.get_tokens_as_string() == "if,(,x,),{,y,=,1,;,},else,{,y,=,0,;,},<EOF>"

def test_program_while_loop_129():
    """Test 129: While loop"""
    tokenizer = Tokenizer("while (i < 10) { i++; }")
    assert tokenizer.get_tokens_as_string() == "while,(,i,<,10,),{,i,++,;,},<EOF>"

def test_program_for_loop_130():
    """Test 130: For loop"""
    tokenizer = Tokenizer("for (auto i = 0; i < 10; ++i) { }")
    assert tokenizer.get_tokens_as_string() == "for,(,auto,i,=,0,;,i,<,10,;,++,i,),{,},<EOF>"

def test_program_switch_131():
    """Test 131: Switch statement"""
    tokenizer = Tokenizer("switch (x) { case 1: break; default: }")
    assert tokenizer.get_tokens_as_string() == "switch,(,x,),{,case,1,:,break,;,default,:,},<EOF>"

def test_program_struct_def_132():
    """Test 132: Struct definition"""
    tokenizer = Tokenizer("struct Point { int x; int y; };")
    assert tokenizer.get_tokens_as_string() == "struct,Point,{,int,x,;,int,y,;,},;,<EOF>"

def test_program_struct_init_133():
    """Test 133: Struct initialization"""
    tokenizer = Tokenizer("Point p = {10, 20};")
    assert tokenizer.get_tokens_as_string() == "Point,p,=,{,10,,,20,},;,<EOF>"

def test_program_member_access_134():
    """Test 134: Member access"""
    tokenizer = Tokenizer("p.x = 5;")
    assert tokenizer.get_tokens_as_string() == "p,.,x,=,5,;,<EOF>"

def test_program_function_call_135():
    """Test 135: Function call"""
    tokenizer = Tokenizer('printString("Hello, World!");')
    assert tokenizer.get_tokens_as_string() == "printString,(,Hello, World!,),;,<EOF>"

def test_program_complex_expr_136():
    """Test 136: Complex expression"""
    tokenizer = Tokenizer("result = (a + b) * c - d / e % f;")
    assert tokenizer.get_tokens_as_string() == "result,=,(,a,+,b,),*,c,-,d,/,e,%,f,;,<EOF>"

def test_program_return_stmt_137():
    """Test 137: Return statement"""
    tokenizer = Tokenizer("return x * 2;")
    assert tokenizer.get_tokens_as_string() == "return,x,*,2,;,<EOF>"

def test_program_void_return_138():
    """Test 138: Void return"""
    tokenizer = Tokenizer("return;")
    assert tokenizer.get_tokens_as_string() == "return,;,<EOF>"


# ========== SECTION 11: Whitespace & Edge Cases (12 tests) ==========

def test_whitespace_no_space_139():
    """Test 139: No whitespace"""
    tokenizer = Tokenizer("int x=5;")
    assert tokenizer.get_tokens_as_string() == "int,x,=,5,;,<EOF>"

def test_whitespace_excessive_140():
    """Test 140: Excessive whitespace"""
    tokenizer = Tokenizer("auto     x     =     10;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,10,;,<EOF>"

def test_whitespace_all_types_141():
    """Test 141: All whitespace types"""
    tokenizer = Tokenizer("a \t\f\r\n b")
    assert tokenizer.get_tokens_as_string() == "a,b,<EOF>"

def test_whitespace_tabs_142():
    """Test 142: Tabs in code"""
    tokenizer = Tokenizer("int\tx\t=\t5;")
    assert tokenizer.get_tokens_as_string() == "int,x,=,5,;,<EOF>"

def test_edge_zero_followed_by_digit_143():
    """Test 143: Zero followed by digit splits"""
    tokenizer = Tokenizer("0123")
    assert tokenizer.get_tokens_as_string() == "0,123,<EOF>"

def test_edge_multiple_zeros_144():
    """Test 144: Multiple zeros"""
    tokenizer = Tokenizer("000")
    assert tokenizer.get_tokens_as_string() == "0,0,0,<EOF>"

def test_edge_float_vs_dot_145():
    """Test 145: Float vs member access ambiguity"""
    tokenizer = Tokenizer("3.14 a.b")
    assert tokenizer.get_tokens_as_string() == "3.14,a,.,b,<EOF>"

def test_edge_division_vs_comment_146():
    """Test 146: Division not confused with comment"""
    tokenizer = Tokenizer("10/2")
    assert tokenizer.get_tokens_as_string() == "10,/,2,<EOF>"

def test_edge_star_vs_comment_147():
    """Test 147: Multiply not part of comment"""
    tokenizer = Tokenizer("5*3 /* real comment */")
    assert tokenizer.get_tokens_as_string() == "5,*,3,<EOF>"

def test_edge_increment_chain_148():
    """Test 148: Triple plus splits correctly"""
    tokenizer = Tokenizer("x+++y")
    assert tokenizer.get_tokens_as_string() == "x,++,+,y,<EOF>"

def test_edge_decrement_chain_149():
    """Test 149: Triple minus splits correctly"""
    tokenizer = Tokenizer("x---y")
    assert tokenizer.get_tokens_as_string() == "x,--,-,y,<EOF>"

def test_edge_equal_chain_150():
    """Test 150: Triple equals splits correctly"""
    tokenizer = Tokenizer("a===b")
    assert tokenizer.get_tokens_as_string() == "a,==,=,b,<EOF>"


# # import pytest
# # from tests.utils import Tokenizer

# # def test_float_with_exponent_positive_01():
# #     """Test 1: Float with positive exponent"""
# #     tokenizer = Tokenizer("1e4")
# #     assert tokenizer.get_tokens_as_string() == "1e4,<EOF>"


# # def test_float_with_exponent_negative_02():
# #     """Test 2: Float with negative exponent"""
# #     tokenizer = Tokenizer("2E-3")
# #     assert tokenizer.get_tokens_as_string() == "2E-3,<EOF>"


# # def test_float_with_exponent_plus_sign_03():
# #     """Test 3: Float with explicit plus in exponent"""
# #     tokenizer = Tokenizer("5E+10")
# #     assert tokenizer.get_tokens_as_string() == "5E+10,<EOF>"


# # def test_float_decimal_only_before_04():
# #     """Test 4: Float with decimal point at end"""
# #     tokenizer = Tokenizer("42.")
# #     assert tokenizer.get_tokens_as_string() == "42.,<EOF>"


# # def test_float_decimal_only_after_05():
# #     """Test 5: Float with decimal point at start"""
# #     tokenizer = Tokenizer(".5")
# #     assert tokenizer.get_tokens_as_string() == ".5,<EOF>"


# # def test_float_full_format_06():
# #     """Test 6: Float with all components"""
# #     tokenizer = Tokenizer("3.14159e-10")
# #     assert tokenizer.get_tokens_as_string() == "3.14159e-10,<EOF>"


# # def test_float_in_expression_07():
# #     """Test 7: Multiple floats in expression"""
# #     tokenizer = Tokenizer("1.5 + 2.3e4 - .7")
# #     assert tokenizer.get_tokens_as_string() == "1.5,+,2.3e4,-,.7,<EOF>"


# # def test_float_zero_formats_08():
# #     """Test 8: Different zero float formats"""
# #     tokenizer = Tokenizer("0.0 .0 0.")
# #     assert tokenizer.get_tokens_as_string() == "0.0,.0,0.,<EOF>"


# # def test_float_scientific_large_09():
# #     """Test 9: Large scientific notation"""
# #     tokenizer = Tokenizer("9.99999E+308")
# #     assert tokenizer.get_tokens_as_string() == "9.99999E+308,<EOF>"


# # def test_float_scientific_tiny_10():
# #     """Test 10: Tiny scientific notation"""
# #     tokenizer = Tokenizer("1e-100")
# #     assert tokenizer.get_tokens_as_string() == "1e-100,<EOF>"


# # # ========== SECTION 2: Integer Edge Cases (5 tests) ==========

# # def test_integer_zero_11():
# #     """Test 11: Zero is valid"""
# #     tokenizer = Tokenizer("0")
# #     assert tokenizer.get_tokens_as_string() == "0,<EOF>"


# # def test_integer_large_12():
# #     """Test 12: Large integer"""
# #     tokenizer = Tokenizer("2147483647")
# #     assert tokenizer.get_tokens_as_string() == "2147483647,<EOF>"


# # def test_integer_sequence_13():
# #     """Test 13: Multiple integers"""
# #     tokenizer = Tokenizer("1 22 333 4444")
# #     assert tokenizer.get_tokens_as_string() == "1,22,333,4444,<EOF>"


# # def test_integer_no_leading_zero_14():
# #     """Test 14: Leading zero creates multiple tokens (0 and number)"""
# #     # "007" should be parsed as "0" and "07" -> but "07" has leading zero
# #     # Actually based on spec, this should be 0, 0, 7 (three separate tokens)
# #     tokenizer = Tokenizer("007")
# #     assert tokenizer.get_tokens_as_string() == "0,0,7,<EOF>"


# # def test_integer_in_calculation_15():
# #     """Test 15: Integers in complex math"""
# #     tokenizer = Tokenizer("100 * 50 / 25 % 3")
# #     assert tokenizer.get_tokens_as_string() == "100,*,50,/,25,%,3,<EOF>"


# # # ========== EXTREME TEST CASES - LEXER HELL MODE ==========

# # def test_extreme_float_ambiguity_101():
# #     """Test 101: EXTREME - Float vs member access ambiguity"""
# #     tokenizer = Tokenizer("0.e10")
# #     # Should be: 0. (float) followed by identifier "e10"
# #     assert tokenizer.get_tokens_as_string() == "0.,e10,<EOF>"


# # def test_extreme_triple_dots_102():
# #     """Test 102: EXTREME - Triple dots (not valid)"""
# #     tokenizer = Tokenizer("a...b")
# #     # Should be: a . . . b
# #     assert tokenizer.get_tokens_as_string() == "a,.,.,.,b,<EOF>"


# # def test_extreme_float_no_digit_after_dot_103():
# #     """Test 103: EXTREME - Dot followed by non-digit"""
# #     tokenizer = Tokenizer(".e10")
# #     # Should be: . (DOT) followed by e10 (identifier)
# #     assert tokenizer.get_tokens_as_string() == ".,e10,<EOF>"


# # def test_extreme_nested_escape_sequences_104():
# #     """Test 104: EXTREME - Multiple backslashes"""
# #     tokenizer = Tokenizer('"\\\\\\\\\\\\n"')
# #     # Should be: three backslashes followed by n
# #     assert tokenizer.get_tokens_as_string() == "\\\\\\\\\\\\n,<EOF>"


# # def test_extreme_almost_comment_105():
# #     """Test 105: EXTREME - Single slash not a comment"""
# #     tokenizer = Tokenizer("a / * b")
# #     # Should be: a / * b (division, then multiplication)
# #     assert tokenizer.get_tokens_as_string() == "a,/,*,b,<EOF>"


# # def test_extreme_operator_chaos_106():
# #     """Test 106: EXTREME - Operator ambiguity nightmare"""
# #     tokenizer = Tokenizer("x+++++y")
# #     # Should be: x ++ ++ + y
# #     assert tokenizer.get_tokens_as_string() == "x,++,++,+,y,<EOF>"


# # def test_extreme_minus_minus_minus_107():
# #     """Test 107: EXTREME - Multiple minus operators"""
# #     tokenizer = Tokenizer("a-----b")
# #     # Should be: a -- -- - b
# #     assert tokenizer.get_tokens_as_string() == "a,--,--,-,b,<EOF>"


# # def test_extreme_float_exponent_edge_108():
# #     """Test 108: EXTREME - Float with exponent but no fraction"""
# #     tokenizer = Tokenizer("5e")
# #     # Should be: 5 (int) e (identifier)
# #     assert tokenizer.get_tokens_as_string() == "5,e,<EOF>"


# # def test_extreme_zero_dot_zero_e_109():
# #     """Test 109: EXTREME - Complex float edge case"""
# #     tokenizer = Tokenizer("0.0e")
# #     # Should be: 0.0 (float) e (identifier)
# #     assert tokenizer.get_tokens_as_string() == "0.0,e,<EOF>"


# # def test_extreme_comparison_chain_110():
# #     """Test 110: EXTREME - Comparison operator chain"""
# #     tokenizer = Tokenizer("a<<=b")
# #     # Should be: a << (ERROR because no <<) OR a < <= b
# #     # Based on longest match: a < <= b
# #     assert tokenizer.get_tokens_as_string() == "a,<,<=,b,<EOF>"


# # def test_extreme_equals_chain_111():
# #     """Test 111: EXTREME - Equals operator ambiguity"""
# #     tokenizer = Tokenizer("a===b")
# #     # Should be: a == = b
# #     assert tokenizer.get_tokens_as_string() == "a,==,=,b,<EOF>"


# # def test_extreme_not_equals_chain_112():
# #     """Test 112: EXTREME - Not equals chain"""
# #     tokenizer = Tokenizer("a!==b")
# #     # Should be: a != = b
# #     assert tokenizer.get_tokens_as_string() == "a,!=,=,b,<EOF>"


# # def test_extreme_logical_or_partial_113():
# #     """Test 113: EXTREME - Single pipe (error)"""
# #     tokenizer = Tokenizer("a||b|c")
# #     # Should be: a || b ERROR(|)
# #     assert tokenizer.get_tokens_as_string() == "a,||,b,Error Token |"


# # def test_extreme_logical_and_partial_114():
# #     """Test 114: EXTREME - Single ampersand (error)"""
# #     tokenizer = Tokenizer("a&&b&c")
# #     # Should be: a && b ERROR(&)
# #     assert tokenizer.get_tokens_as_string() == "a,&&,b,Error Token &"


# # def test_extreme_string_escape_at_end_115():
# #     """Test 115: EXTREME - Backslash at end of string before close"""
# #     tokenizer = Tokenizer('"test\\\\"')
# #     # Should be valid: test followed by escaped backslash
# #     assert tokenizer.get_tokens_as_string() == "test\\\\,<EOF>"


# # def test_extreme_string_four_backslashes_116():
# #     """Test 116: EXTREME - Four backslashes"""
# #     tokenizer = Tokenizer('"\\\\\\\\"')
# #     # Should be: two escaped backslashes
# #     assert tokenizer.get_tokens_as_string() == "\\\\\\\\,<EOF>"


# # def test_extreme_comment_almost_117():
# #     """Test 117: EXTREME - Almost block comment"""
# #     tokenizer = Tokenizer("/**/")
# #     # Unclosed block comment - should skip to EOF
# #     assert tokenizer.get_tokens_as_string() == "<EOF>"


# # def test_extreme_comment_almost_end_118():
# #     """Test 118: EXTREME - Comment with single asterisk inside"""
# #     tokenizer = Tokenizer("/* * */")
# #     # Valid block comment
# #     assert tokenizer.get_tokens_as_string() == "<EOF>"


# # def test_extreme_identifier_numbers_119():
# #     """Test 119: EXTREME - Identifier starting with underscore and numbers"""
# #     tokenizer = Tokenizer("_123abc __456")
# #     assert tokenizer.get_tokens_as_string() == "_123abc,__456,<EOF>"


# # def test_extreme_keyword_prefix_120():
# #     """Test 120: EXTREME - Keywords as prefix of identifiers"""
# #     tokenizer = Tokenizer("integer floaty struct_name")
# #     assert tokenizer.get_tokens_as_string() == "integer,floaty,struct_name,<EOF>"


# # def test_extreme_division_vs_comment_121():
# #     """Test 121: EXTREME - Division followed by asterisk"""
# #     tokenizer = Tokenizer("a/*/b")
# #     # Should be: a followed by /* comment start
# #     # Everything after /* is comment until */
# #     assert tokenizer.get_tokens_as_string() == "a,/,*,/,b,<EOF>"


# # def test_extreme_nested_comment_attempt_122():
# #     """Test 122: EXTREME - Nested comment symbols"""
# #     tokenizer = Tokenizer("/* /* */ */")
# #     # Block comments don't nest: first */ closes the comment
# #     # Remaining */ causes error
# #     assert tokenizer.get_tokens_as_string() == "*,/,<EOF>"

# # def test_extreme_nested_comment_attempt_1221():
# #     """Test 122: EXTREME - Nested comment symbols"""
# #     tokenizer = Tokenizer("/* /* */ */**/")
# #     # Block comments don't nest: first */ closes the comment
# #     # Remaining */ causes error
# #     assert tokenizer.get_tokens_as_string() == "*,<EOF>"

# # def test_extreme_float_edge_double_dot_123():
# #     """Test 123: EXTREME - Two dots in sequence"""
# #     tokenizer = Tokenizer("3..14")
# #     # Should be: 3. (float) .14 (float)
# #     assert tokenizer.get_tokens_as_string() == "3.,.14,<EOF>"


# # def test_extreme_exponent_case_sensitive_124():
# #     """Test 124: EXTREME - Both e and E in expression"""
# #     tokenizer = Tokenizer("1e5+2E3")
# #     # Both should work
# #     assert tokenizer.get_tokens_as_string() == "1e5,+,2E3,<EOF>"


# # def test_extreme_zero_followed_by_digit_125():
# #     """Test 125: EXTREME - Zero followed by multiple digits"""
# #     tokenizer = Tokenizer("0123456789")
# #     # Each digit is separate token after leading 0
# #     assert tokenizer.get_tokens_as_string() == "0,123456789,<EOF>"


# # # ========== MEGA EXTREME SECTION - 75 MORE TESTS (126-200) ==========

# # # Float Nightmare Series (126-145)
# # def test_mega_float_dot_exponent_126():
# #     """Test 126: Float with dot but no fraction before exponent"""
# #     tokenizer = Tokenizer("5.e10")
# #     assert tokenizer.get_tokens_as_string() == "5.,e10,<EOF>"

# # def test_mega_float_multiple_e_127():
# #     """Test 127: Multiple e characters (second is identifier)"""
# #     tokenizer = Tokenizer("1e5e3")
# #     assert tokenizer.get_tokens_as_string() == "1e5,e3,<EOF>"

# # def test_mega_float_exponent_no_sign_128():
# #     """Test 128: Exponent without sign after e"""
# #     tokenizer = Tokenizer("2.5e+")
# #     assert tokenizer.get_tokens_as_string() == "2.5,e,+,<EOF>"

# # def test_mega_float_leading_zeros_129():
# #     """Test 129: Float with leading zeros in fraction"""
# #     tokenizer = Tokenizer("1.00000001")
# #     assert tokenizer.get_tokens_as_string() == "1.00000001,<EOF>"

# # def test_mega_float_dot_at_end_of_expr_130():
# #     """Test 130: Dot at end of expression"""
# #     tokenizer = Tokenizer("3.+5")
# #     assert tokenizer.get_tokens_as_string() == "3.,+,5,<EOF>"

# # def test_mega_float_miniscule_131():
# #     """Test 131: Extremely small float"""
# #     tokenizer = Tokenizer(".0000000001")
# #     assert tokenizer.get_tokens_as_string() == ".0000000001,<EOF>"

# # def test_mega_float_huge_exponent_132():
# #     """Test 132: Huge positive exponent"""
# #     tokenizer = Tokenizer("1e999999")
# #     assert tokenizer.get_tokens_as_string() == "1e999999,<EOF>"

# # def test_mega_float_negative_huge_exponent_133():
# #     """Test 133: Huge negative exponent"""
# #     tokenizer = Tokenizer("9.9e-999999")
# #     assert tokenizer.get_tokens_as_string() == "9.9e-999999,<EOF>"

# # def test_mega_float_chain_134():
# #     """Test 134: Chain of floats and dots"""
# #     tokenizer = Tokenizer("1.2.3.4")
# #     assert tokenizer.get_tokens_as_string() == "1.2,.3,.4,<EOF>"

# # def test_mega_float_exp_uppercase_lowercase_135():
# #     """Test 135: Mixed case exponent"""
# #     tokenizer = Tokenizer("1E5e3")
# #     assert tokenizer.get_tokens_as_string() == "1E5,e3,<EOF>"

# # def test_mega_float_zero_exponent_136():
# #     """Test 136: Zero in exponent"""
# #     tokenizer = Tokenizer("5e0")
# #     assert tokenizer.get_tokens_as_string() == "5e0,<EOF>"

# # def test_mega_float_plus_zero_exp_137():
# #     """Test 137: Plus zero exponent"""
# #     tokenizer = Tokenizer("3.14e+0")
# #     assert tokenizer.get_tokens_as_string() == "3.14e+0,<EOF>"

# # def test_mega_float_minus_zero_exp_138():
# #     """Test 138: Minus zero exponent"""
# #     tokenizer = Tokenizer("2.71e-0")
# #     assert tokenizer.get_tokens_as_string() == "2.71e-0,<EOF>"

# # def test_mega_float_dot_only_139():
# #     """Test 139: Just a dot"""
# #     tokenizer = Tokenizer(".")
# #     assert tokenizer.get_tokens_as_string() == ".,<EOF>"

# # def test_mega_float_multiple_dots_number_140():
# #     """Test 140: Number with multiple internal dots"""
# #     tokenizer = Tokenizer("1.2.3")
# #     assert tokenizer.get_tokens_as_string() == "1.2,.3,<EOF>"

# # def test_mega_float_exp_no_digit_141():
# #     """Test 141: e without any digit"""
# #     tokenizer = Tokenizer("e5")
# #     assert tokenizer.get_tokens_as_string() == "e5,<EOF>"

# # def test_mega_float_E_no_digit_142():
# #     """Test 142: E without any digit"""
# #     tokenizer = Tokenizer("E10")
# #     assert tokenizer.get_tokens_as_string() == "E10,<EOF>"

# # def test_mega_float_dot_e_143():
# #     """Test 143: Dot followed by e"""
# #     tokenizer = Tokenizer(".e")
# #     assert tokenizer.get_tokens_as_string() == ".,e,<EOF>"

# # def test_mega_float_fraction_e_no_exp_144():
# #     """Test 144: Fraction with e but no exponent number"""
# #     tokenizer = Tokenizer("3.14e")
# #     assert tokenizer.get_tokens_as_string() == "3.14,e,<EOF>"

# # def test_mega_float_all_nines_145():
# #     """Test 145: All nines float"""
# #     tokenizer = Tokenizer("999.999e999")
# #     assert tokenizer.get_tokens_as_string() == "999.999e999,<EOF>"

# # # String Escape Hell Series (146-165)
# # def test_mega_string_five_backslashes_146():
# #     """Test 146: Five backslashes"""
# #     tokenizer = Tokenizer('"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n"')
# #     assert tokenizer.get_tokens_as_string() == "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n,<EOF>"

# # def test_mega_string_all_escapes_mixed_147():
# #     """Test 147: All escape types in one string"""
# #     tokenizer = Tokenizer('"\\\\b\\\\f\\\\r\\\\n\\\\t\\\\\\\"\\\\\\\\"')
# #     # Lexer sees: "\\b\\f\\r\\n\\t\\"\\\\"
# #     # Output: \\b\\f\\r\\n\\t\\"\\\\
# #     assert tokenizer.get_tokens_as_string() == r"\\b\\f\\r\\n\\t\\\"\\\\,<EOF>".replace(" ", "")

# # def test_mega_string_escape_then_normal_148():
# #     """Test 148: Escaped char followed by same char"""
# #     tokenizer = Tokenizer('"\\\\nn"')
# #     assert tokenizer.get_tokens_as_string() == "\\\\nn,<EOF>"

# # def test_mega_string_backslash_quote_end_149():
# #     """Test 149: Backslash quote at end"""
# #     tokenizer = Tokenizer('"\\\\\\"test"')
# #     assert tokenizer.get_tokens_as_string() == '\\\\\\"test,<EOF>'

# # def test_mega_string_empty_with_escapes_150():
# #     """Test 150: Only escapes in string"""
# #     tokenizer = Tokenizer('"\\\\n\\\\t\\\\r"')
# #     assert tokenizer.get_tokens_as_string() == "\\\\n\\\\t\\\\r,<EOF>"

# # def test_mega_string_text_backslash_text_151():
# #     """Test 151: Text, escaped backslash, text"""
# #     tokenizer = Tokenizer('"hello\\\\\\\\\\\\\\\\world"')
# #     assert tokenizer.get_tokens_as_string() == r"hello\\\\\\\\world,<EOF>"

# # def test_mega_string_tab_spaces_mix_153():
# #     """Test 153: Mix of escaped and real tabs/spaces"""
# #     tokenizer = Tokenizer('"\\\\t \\t \\\\t"')
# #     assert tokenizer.get_tokens_as_string() == r"\\t \t \\t,<EOF>"

# # def test_mega_string_newline_escape_only_154():
# #     """Test 154: Just newline escape"""
# #     tokenizer = Tokenizer('"\\\\n"')
# #     assert tokenizer.get_tokens_as_string() == "\\\\n,<EOF>"

# # def test_mega_string_backslash_at_start_155():
# #     """Test 155: Backslash at very start"""
# #     tokenizer = Tokenizer('"\\\\\\\\start"')
# #     assert tokenizer.get_tokens_as_string() == "\\\\\\\\start,<EOF>"

# # def test_mega_string_long_with_escapes_156():
# #     """Test 156: Long string with scattered escapes"""
# #     tokenizer = Tokenizer('"The\\\\nquick\\\\tbrown\\\\nfox"')
# #     assert tokenizer.get_tokens_as_string() == "The\\\\nquick\\\\tbrown\\\\nfox,<EOF>"

# # def test_mega_string_quote_in_middle_157():
# #     """Test 157: Escaped quote in middle of text"""
# #     tokenizer = Tokenizer('"say \\\\\\"hi\\\\\\" now"')
# #     assert tokenizer.get_tokens_as_string() == 'say \\\\\\"hi\\\\\\" now,<EOF>'

# # def test_mega_string_special_chars_158():
# #     """Test 158: String with special characters"""
# #     tokenizer = Tokenizer('"!@#$%^*()_+-=[]{}|;:<>?,./"')
# #     assert tokenizer.get_tokens_as_string() == "!@#$%^*()_+-=[]{}|;:<>?,./,<EOF>"

# # def test_mega_string_numbers_159():
# #     """Test 159: String full of numbers"""
# #     tokenizer = Tokenizer('"0123456789"')
# #     assert tokenizer.get_tokens_as_string() == "0123456789,<EOF>"

# # def test_mega_string_path_like_160():
# #     """Test 160: Path-like string"""
# #     tokenizer = Tokenizer('"C:\\\\\\\\Users\\\\\\\\file.txt"')
# #     assert tokenizer.get_tokens_as_string() == "C:\\\\\\\\Users\\\\\\\\file.txt,<EOF>"

# # def test_mega_string_url_like_161():
# #     """Test 161: URL-like string"""
# #     tokenizer = Tokenizer('"https://example.com/path?query=value"')
# #     assert tokenizer.get_tokens_as_string() == "https://example.com/path?query=value,<EOF>"

# # def test_mega_string_json_like_162():
# #     """Test 162: JSON-like content in string"""
# #     tokenizer = Tokenizer('"{\\\"key}"')
# #     assert tokenizer.get_tokens_as_string() == r'{\"key},<EOF>'

# # def test_mega_string_sql_like_163():
# #     """Test 163: SQL-like string"""
# #     tokenizer = Tokenizer('"SELECT * FROM users WHERE id=1"')
# #     assert tokenizer.get_tokens_as_string() == "SELECT * FROM users WHERE id=1,<EOF>"

# # def test_mega_string_with_parentheses_164():
# #     """Test 164: String with many parentheses"""
# #     tokenizer = Tokenizer('"((()))(())()"')
# #     assert tokenizer.get_tokens_as_string() == "((()))(())(),<EOF>"

# # def test_mega_string_backspace_char_165():
# #     """Test 165: Backspace escape"""
# #     tokenizer = Tokenizer('"test\\\\bback"')
# #     assert tokenizer.get_tokens_as_string() == "test\\\\bback,<EOF>"

# # # Operator Chaos Series (166-180)
# # def test_mega_op_all_inc_dec_166():
# #     """Test 166: All ++ and -- together"""
# #     tokenizer = Tokenizer("++a--++b--")
# #     assert tokenizer.get_tokens_as_string() == "++,a,--,++,b,--,<EOF>"

# # def test_mega_op_assign_chain_long_167():
# #     """Test 167: Very long assignment chain"""
# #     tokenizer = Tokenizer("a=b=c=d=e=f=0")
# #     assert tokenizer.get_tokens_as_string() == "a,=,b,=,c,=,d,=,e,=,f,=,0,<EOF>"

# # def test_mega_op_comparison_all_168():
# #     """Test 168: All comparison operators"""
# #     tokenizer = Tokenizer("a<b<=c>d>=e==f!=g")
# #     assert tokenizer.get_tokens_as_string() == "a,<,b,<=,c,>,d,>=,e,==,f,!=,g,<EOF>"

# # def test_mega_op_arithmetic_no_space_169():
# #     """Test 169: All arithmetic without spaces"""
# #     tokenizer = Tokenizer("a+b-c*d/e%f")
# #     assert tokenizer.get_tokens_as_string() == "a,+,b,-,c,*,d,/,e,%,f,<EOF>"

# # def test_mega_op_logical_chain_170():
# #     """Test 170: Long logical chain"""
# #     tokenizer = Tokenizer("a&&b||c&&d||e")
# #     assert tokenizer.get_tokens_as_string() == "a,&&,b,||,c,&&,d,||,e,<EOF>"

# # def test_mega_op_not_chain_171():
# #     """Test 171: Multiple NOT operators"""
# #     tokenizer = Tokenizer("!!!a")
# #     assert tokenizer.get_tokens_as_string() == "!,!,!,a,<EOF>"

# # def test_mega_op_mixed_chaos_172():
# #     """Test 172: Complete operator chaos"""
# #     tokenizer = Tokenizer("++a--+b*c/d%e==f!=g")
# #     assert tokenizer.get_tokens_as_string() == "++,a,--,+,b,*,c,/,d,%,e,==,f,!=,g,<EOF>"

# # def test_mega_op_dots_everywhere_173():
# #     """Test 173: Dots everywhere"""
# #     tokenizer = Tokenizer("a.b.c.d.e.f")
# #     assert tokenizer.get_tokens_as_string() == "a,.,b,.,c,.,d,.,e,.,f,<EOF>"

# # def test_mega_op_parentheses_nest_174():
# #     """Test 174: Deep parentheses nesting"""
# #     tokenizer = Tokenizer("((((a))))")
# #     assert tokenizer.get_tokens_as_string() == "(,(,(,(,a,),),),),<EOF>"

# # def test_mega_op_brackets_curly_175():
# #     """Test 175: Curly brackets nested"""
# #     tokenizer = Tokenizer("{{{a}}}")
# #     assert tokenizer.get_tokens_as_string() == "{,{,{,a,},},},<EOF>"

# # def test_mega_op_all_separators_176():
# #     """Test 176: All separators together"""
# #     tokenizer = Tokenizer("(){};,:")
# #     assert tokenizer.get_tokens_as_string() == "(,),{,},;,,,:,<EOF>"

# # def test_mega_op_division_multiply_177():
# #     """Test 177: Division and multiplication chain"""
# #     tokenizer = Tokenizer("a/b*c/d*e")
# #     assert tokenizer.get_tokens_as_string() == "a,/,b,*,c,/,d,*,e,<EOF>"

# # def test_mega_op_modulo_chain_178():
# #     """Test 178: Modulo chain"""
# #     tokenizer = Tokenizer("a%b%c%d")
# #     assert tokenizer.get_tokens_as_string() == "a,%,b,%,c,%,d,<EOF>"

# # def test_mega_op_plus_minus_alternate_179():
# #     """Test 179: Alternating plus and minus"""
# #     tokenizer = Tokenizer("a+b-c+d-e+f")
# #     assert tokenizer.get_tokens_as_string() == "a,+,b,-,c,+,d,-,e,+,f,<EOF>"

# # def test_mega_op_prefix_postfix_mix_180():
# #     """Test 180: Mix of prefix and postfix"""
# #     tokenizer = Tokenizer("++a++ --b--")
# #     assert tokenizer.get_tokens_as_string() == "++,a,++,--,b,--,<EOF>"

# # # Comment Madness Series (181-190)
# # def test_mega_comment_nested_stars_181():
# #     """Test 181: Many stars in comment"""
# #     tokenizer = Tokenizer("/* ***** */")
# #     assert tokenizer.get_tokens_as_string() == "<EOF>"

# # def test_mega_comment_nested_slashes_182():
# #     """Test 182: Slashes in block comment"""
# #     tokenizer = Tokenizer("/* /// */")
# #     assert tokenizer.get_tokens_as_string() == "<EOF>"

# # def test_mega_comment_code_in_comment_183():
# #     """Test 183: Code in block comment"""
# #     tokenizer = Tokenizer("/* int x = 5; */")
# #     assert tokenizer.get_tokens_as_string() == "<EOF>"

# # def test_mega_comment_line_with_code_184():
# #     """Test 184: Line comment with code"""
# #     tokenizer = Tokenizer("// int x = 5;")
# #     assert tokenizer.get_tokens_as_string() == "<EOF>"

# # def test_mega_comment_multiple_line_comments_185():
# #     """Test 185: Multiple line comments"""
# #     tokenizer = Tokenizer("// comment1\n// comment2\nint x")
# #     assert tokenizer.get_tokens_as_string() == "int,x,<EOF>"

# # def test_mega_comment_block_after_code_186():
# #     """Test 186: Block comment after code"""
# #     tokenizer = Tokenizer("int x /* comment */")
# #     assert tokenizer.get_tokens_as_string() == "int,x,<EOF>"

# # def test_mega_comment_inline_187():
# #     """Test 187: Inline block comment"""
# #     tokenizer = Tokenizer("int /* type */ x")
# #     assert tokenizer.get_tokens_as_string() == "int,x,<EOF>"

# # def test_mega_comment_line_end_of_line_188():
# #     """Test 188: Line comment at end"""
# #     tokenizer = Tokenizer("int x; // comment")
# #     assert tokenizer.get_tokens_as_string() == "int,x,;,<EOF>"

# # def test_mega_comment_empty_line_comment_189():
# #     """Test 189: Empty line comment"""
# #     tokenizer = Tokenizer("//")
# #     assert tokenizer.get_tokens_as_string() == "<EOF>"

# # def test_mega_comment_url_in_comment_190():
# #     """Test 190: URL in comment"""
# #     tokenizer = Tokenizer("// https://example.com")
# #     assert tokenizer.get_tokens_as_string() == "<EOF>"

# # # Identifier Madness Series (191-200)
# # def test_mega_id_all_underscores_191():
# #     """Test 191: All underscores identifier"""
# #     tokenizer = Tokenizer("_____")
# #     assert tokenizer.get_tokens_as_string() == "_____,<EOF>"

# # def test_mega_id_underscore_number_mix_192():
# #     """Test 192: Underscores and numbers"""
# #     tokenizer = Tokenizer("_1_2_3_")
# #     assert tokenizer.get_tokens_as_string() == "_1_2_3_,<EOF>"

# # def test_mega_id_all_keywords_together_193():
# #     """Test 193: All keywords in sequence"""
# #     tokenizer = Tokenizer("auto int float string void struct if else while for switch case default break continue return")
# #     assert tokenizer.get_tokens_as_string() == "auto,int,float,string,void,struct,if,else,while,for,switch,case,default,break,continue,return,<EOF>"

# # def test_mega_id_keyword_like_194():
# #     """Test 194: Keyword-like identifiers"""
# #     tokenizer = Tokenizer("integer floating whileloop forloop")
# #     assert tokenizer.get_tokens_as_string() == "integer,floating,whileloop,forloop,<EOF>"

# # def test_mega_id_single_letter_195():
# #     """Test 195: Single letter identifiers"""
# #     tokenizer = Tokenizer("a b c d e f g")
# #     assert tokenizer.get_tokens_as_string() == "a,b,c,d,e,f,g,<EOF>"

# # def test_mega_id_camelCase_196():
# #     """Test 196: camelCase identifiers"""
# #     tokenizer = Tokenizer("myVariable yourVariable hisVariable")
# #     assert tokenizer.get_tokens_as_string() == "myVariable,yourVariable,hisVariable,<EOF>"

# # def test_mega_id_snake_case_197():
# #     """Test 197: snake_case identifiers"""
# #     tokenizer = Tokenizer("my_var your_var his_var")
# #     assert tokenizer.get_tokens_as_string() == "my_var,your_var,his_var,<EOF>"

# # def test_mega_id_long_identifier_198():
# #     """Test 198: Very long identifier"""
# #     tokenizer = Tokenizer("thisIsAVeryLongIdentifierNameThatGoesOnAndOnAndOn")
# #     assert tokenizer.get_tokens_as_string() == "thisIsAVeryLongIdentifierNameThatGoesOnAndOnAndOn,<EOF>"

# # def test_mega_id_mixed_with_numbers_199():
# #     """Test 199: Identifiers with numbers everywhere"""
# #     tokenizer = Tokenizer("var1 var2 var3 var123")
# #     assert tokenizer.get_tokens_as_string() == "var1,var2,var3,var123,<EOF>"

# # def test_mega_ultimate_chaos_200():
# #     """Test 200: ULTIMATE CHAOS - Everything combined"""
# #     tokenizer = Tokenizer('int x=5;float y=3.14e-10;string s="hi\\\\\\\\n";x++;/* comment */y--')
# #     assert tokenizer.get_tokens_as_string() == 'int,x,=,5,;,float,y,=,3.14e-10,;,string,s,=,hi\\\\\\\\n,;,x,++,;,y,--,<EOF>'


# # # ========== OPERATOR LONGEST MATCH TESTS (201-225) ==========
# # # Test maximal munch principle: lexer must prefer longer tokens

# # def test_operator_eq_vs_assign_201():
# #     """Test 201: == vs = - Longest match for equality"""
# #     tokenizer = Tokenizer("a==b")
# #     assert tokenizer.get_tokens_as_string() == "a,==,b,<EOF>"

# # def test_operator_neq_vs_not_202():
# #     """Test 202: != vs ! - Longest match for not equal"""
# #     tokenizer = Tokenizer("a!=b")
# #     assert tokenizer.get_tokens_as_string() == "a,!=,b,<EOF>"

# # def test_operator_lte_vs_lt_203():
# #     """Test 203: <= vs < - Longest match"""
# #     tokenizer = Tokenizer("a<=b")
# #     assert tokenizer.get_tokens_as_string() == "a,<=,b,<EOF>"

# # def test_operator_gte_vs_gt_204():
# #     """Test 204: >= vs > - Longest match"""
# #     tokenizer = Tokenizer("a>=b")
# #     assert tokenizer.get_tokens_as_string() == "a,>=,b,<EOF>"

# # def test_operator_inc_vs_plus_205():
# #     """Test 205: ++ vs + - Longest match for increment"""
# #     tokenizer = Tokenizer("a++")
# #     assert tokenizer.get_tokens_as_string() == "a,++,<EOF>"

# # def test_operator_dec_vs_minus_206():
# #     """Test 206: -- vs - - Longest match for decrement"""
# #     tokenizer = Tokenizer("a--")
# #     assert tokenizer.get_tokens_as_string() == "a,--,<EOF>"

# # def test_operator_and_vs_single_amp_207():
# #     """Test 207: && vs & - Logical AND (& alone is error)"""
# #     tokenizer = Tokenizer("a&&b")
# #     assert tokenizer.get_tokens_as_string() == "a,&&,b,<EOF>"

# # def test_operator_or_vs_single_pipe_208():
# #     """Test 208: || vs | - Logical OR (| alone is error)"""
# #     tokenizer = Tokenizer("a||b")
# #     assert tokenizer.get_tokens_as_string() == "a,||,b,<EOF>"

# # def test_operator_mixed_eq_and_assign_209():
# #     """Test 209: Mix of == and = in sequence"""
# #     tokenizer = Tokenizer("a=b==c")
# #     assert tokenizer.get_tokens_as_string() == "a,=,b,==,c,<EOF>"

# # def test_operator_mixed_comparison_210():
# #     """Test 210: Mix of <, <=, >, >= in sequence"""
# #     tokenizer = Tokenizer("a<b<=c>d>=e")
# #     assert tokenizer.get_tokens_as_string() == "a,<,b,<=,c,>,d,>=,e,<EOF>"

# # def test_operator_triple_plus_211():
# #     """Test 211: +++ should be ++ then +"""
# #     tokenizer = Tokenizer("a+++b")
# #     assert tokenizer.get_tokens_as_string() == "a,++,+,b,<EOF>"

# # def test_operator_triple_minus_212():
# #     """Test 212: --- should be -- then -"""
# #     tokenizer = Tokenizer("a---b")
# #     assert tokenizer.get_tokens_as_string() == "a,--,-,b,<EOF>"

# # def test_operator_quad_plus_213():
# #     """Test 213: ++++ should be ++ then ++"""
# #     tokenizer = Tokenizer("a++++b")
# #     assert tokenizer.get_tokens_as_string() == "a,++,++,b,<EOF>"

# # def test_operator_eq_chain_214():
# #     """Test 214: === should be == then ="""
# #     tokenizer = Tokenizer("a===b")
# #     assert tokenizer.get_tokens_as_string() == "a,==,=,b,<EOF>"

# # def test_operator_neq_chain_215():
# #     """Test 215: !== should be != then ="""
# #     tokenizer = Tokenizer("a!==b")
# #     assert tokenizer.get_tokens_as_string() == "a,!=,=,b,<EOF>"

# # def test_operator_not_vs_neq_216():
# #     """Test 216: ! vs != - Single NOT vs not-equal"""
# #     tokenizer = Tokenizer("!a")
# #     assert tokenizer.get_tokens_as_string() == "!,a,<EOF>"

# # def test_operator_assign_vs_eq_217():
# #     """Test 217: Single = should be assign"""
# #     tokenizer = Tokenizer("a=b")
# #     assert tokenizer.get_tokens_as_string() == "a,=,b,<EOF>"

# # def test_operator_lt_vs_lte_218():
# #     """Test 218: Single < should be less-than"""
# #     tokenizer = Tokenizer("a<b")
# #     assert tokenizer.get_tokens_as_string() == "a,<,b,<EOF>"

# # def test_operator_gt_vs_gte_219():
# #     """Test 219: Single > should be greater-than"""
# #     tokenizer = Tokenizer("a>b")
# #     assert tokenizer.get_tokens_as_string() == "a,>,b,<EOF>"

# # def test_operator_plus_vs_inc_220():
# #     """Test 220: Single + should be plus"""
# #     tokenizer = Tokenizer("a+b")
# #     assert tokenizer.get_tokens_as_string() == "a,+,b,<EOF>"

# # def test_operator_minus_vs_dec_221():
# #     """Test 221: Single - should be minus"""
# #     tokenizer = Tokenizer("a-b")
# #     assert tokenizer.get_tokens_as_string() == "a,-,b,<EOF>"

# # def test_operator_complex_combo_222():
# #     """Test 222: Complex operator combination"""
# #     tokenizer = Tokenizer("a++==b--")
# #     assert tokenizer.get_tokens_as_string() == "a,++,==,b,--,<EOF>"

# # def test_operator_all_two_char_223():
# #     """Test 223: All two-character operators together"""
# #     tokenizer = Tokenizer("==!=<=>=++--&&||")
# #     assert tokenizer.get_tokens_as_string() == "==,!=,<=,>=,++,--,&&,||,<EOF>"

# # def test_operator_error_single_amp_224():
# #     """Test 224: Single & is error (not valid operator)"""
# #     tokenizer = Tokenizer("a&b")
# #     assert tokenizer.get_tokens_as_string() == "a,Error Token &"

# # def test_operator_error_single_pipe_225():
# #     """Test 225: Single | is error (not valid operator)"""
# #     tokenizer = Tokenizer("a|b")
# #     assert tokenizer.get_tokens_as_string() == "a,Error Token |"

# # """
# # Parser test cases for TyC compiler
# # TODO: Implement 100 test cases for parser
# # """

# # import pytest
# # from tests.utils import Parser


# # # ========== Simple Test Cases (10 types) ==========
# # def test_empty_program():
# #     """1. Empty program"""
# #     assert Parser("").parse() == "success"


# # def test_program_with_only_main():
# #     """2. Program with only main function"""
# #     assert Parser("void main() {}").parse() == "success"


# # def test_struct_simple():
# #     """3. Struct declaration"""
# #     source = "struct Point { int x; int y; };"
# #     assert Parser(source).parse() == "success"


# # def test_function_no_params():
# #     """4. Function with no parameters"""
# #     source = "void greet() { printString(\"Hello\"); }"
# #     assert Parser(source).parse() == "success"


# # def test_var_decl_auto_with_init():
# #     """5. Variable declaration"""
# #     source = "void main() { auto x = 5; }"
# #     assert Parser(source).parse() == "success"


# # def test_if_simple():
# #     """6. If statement"""
# #     source = "void main() { if (1) printInt(1); }"
# #     assert Parser(source).parse() == "success"


# # def test_while_simple():
# #     """7. While statement"""
# #     source = "void main() { while (1) printInt(1); }"
# #     assert Parser(source).parse() == "success"


# # def test_for_simple():
# #     """8. For statement"""
# #     source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
# #     assert Parser(source).parse() == "success"


# # def test_switch_simple():
# #     """9. Switch statement"""
# #     source = "void main() { switch (1) { case 1: printInt(1); break; } }"
# #     assert Parser(source).parse() == "success"


# # def test_assignment_simple():
# #     """10. Assignment statement"""
# #     source = "void main() { int x; x = 5; }"
# #     assert Parser(source).parse() == "success"

# # """
# # COMPREHENSIVE EXTREME EDGE CASE TESTS FOR TyC PARSER
# # 100 extremely difficult test cases covering all subtle parser ambiguities,
# # operator precedence extremes, expression disambiguation, and hidden errors.
# # """

# # import pytest
# # from tests.utils import Parser

# # def test_valid(source):
# #     parser = Parser(source)
# #     assert parser.parse() == "success"

# # def test_invalid(source):
# #     parser = Parser(source)
# #     result = parser.parse()
# #     assert result != "success"
# #     assert "Error on line" in result

# # # ============================================================================
# # # GROUP 1: EXPRESSION STATEMENT DISAMBIGUATION (15 tests)
# # # Testing the ambiguity between assignments, calls, and standalone expressions
# # # ============================================================================

# # def test_extreme_001():
# #     """Standalone expression statement - just expression"""
# #     test_valid("void main() { 1 + 2 * 3; }")

# # def test_extreme_002():
# #     """Function call as expression statement"""
# #     test_valid("void main() { print(); }")

# # def test_extreme_003():
# #     """Postfix increment as expression statement"""
# #     test_valid("void main() { int x; x++; }")

# # def test_extreme_004():
# #     """Prefix increment as expression statement"""
# #     test_valid("void main() { int x; ++x; }")

# # def test_extreme_005():
# #     """Member access assignment"""
# #     test_valid("""
# #         struct S { int x; };
# #         void main() {
# #             S s;
# #             s.x = 10;
# #         }
# #     """)

# # def test_extreme_006():
# #     """Chained member access assignment"""
# #     test_valid("""
# #         struct A { B b; };
# #         struct B { int x; };
# #         void main() {
# #             A a;
# #             a.b.x = 5;
# #         }
# #     """)

# # def test_extreme_007():
# #     """Function call with member access"""
# #     test_valid("void main() { obj.method(); }")

# # def test_extreme_008():
# #     """Assignment within function call argument"""
# #     test_valid("void main() { int x; f(x = 5); }")

# # def test_extreme_009():
# #     """Parenthesized expression as statement"""
# #     test_valid("void main() { int x; (x); }")

# # def test_extreme_010():
# #     """Multiple assignments in one statement"""
# #     test_valid("void main() { int a, b, c; a = b = c = 10; }")

# # def test_extreme_011():
# #     """Assignment in expression context"""
# #     test_valid("void main() { int a, b; auto x = (a = 5) + (b = 10); }")

# # def test_extreme_012():
# #     """Postfix on member access"""
# #     test_valid("""
# #         struct S { int x; };
# #         void main() {
# #             S s;
# #             s.x++;
# #         }
# #     """)

# # def test_extreme_013():
# #     """Prefix on member access"""
# #     test_valid("""
# #         struct S { int x; };
# #         void main() {
# #             S s;
# #             ++s.x;
# #         }
# #     """)

# # def test_extreme_014():
# #     """Cannot increment function call result - INVALID"""
# #     test_valid("""
# #         int f() { return 5; }
# #         void main() {
# #             f()++;
# #         }
# #     """)

# # def test_extreme_015():
# #     """Cannot assign to function call - INVALID"""
# #     test_valid("void main() { f() = 5; }")

# # # ============================================================================
# # # GROUP 2: OPERATOR PRECEDENCE EXTREMES (20 tests)
# # # Testing all 11 precedence levels in complex combinations
# # # ============================================================================

# # def test_extreme_016():
# #     """Member access (highest) > postfix > prefix > unary"""
# #     test_valid("""
# #         struct S { int x; };
# #         void main() {
# #             S s;
# #             auto v = !++s.x++;
# #         }
# #     """)

# # def test_extreme_017():
# #     """All unary operators stacked"""
# #     test_valid("void main() { auto x = !-+!-5; }")

# # def test_extreme_018():
# #     """Multiple prefix increments"""
# #     test_invalid("void main() { int x; +++++x; }")

# # def test_extreme_019():
# #     """Postfix cannot be stacked - INVALID"""
# #     test_valid("void main() { int x; +x++++; }")

# # def test_extreme_020():
# #     """Assignment has lowest precedence"""
# #     test_valid("void main() { int a, b; a = b = 1 + 2 * 3 < 5 && 10 || 0; }")

# # def test_extreme_021():
# #     """Logical OR > logical AND"""
# #     test_valid("void main() { auto x = 1 && 2 || 3 && 4; }")

# # def test_extreme_022():
# #     """Equality > relational"""
# #     test_valid("void main() { auto x = 1 < 2 == 3 > 4; }")

# # def test_extreme_023():
# #     """Additive > multiplicative"""
# #     test_valid("void main() { auto x = 1 + 2 * 3 - 4 / 5; }")

# # def test_extreme_024():
# #     """Unary minus on plus"""
# #     test_valid("void main() { auto x = -+5; }")

# # def test_extreme_025():
# #     """Double logical NOT"""
# #     test_valid("void main() { auto x = !!5; }")

# # def test_extreme_026():
# #     """Assignment in condition"""
# #     test_valid("void main() { int x; if ((x = 5) > 0) { } }")

# # def test_extreme_027():
# #     """Assignment in while condition"""
# #     test_valid("void main() { int x; while ((x = getVal()) > 0) { } }")

# # def test_extreme_028():
# #     """Assignment in for condition"""
# #     test_valid("void main() { int x; for (; (x = f()) < 10; ) { } }")

# # def test_extreme_029():
# #     """Chained relational operators (left associative)"""
# #     test_valid("void main() { auto x = 1 < 2 < 3; }")  # ((1 < 2) < 3)

# # def test_extreme_030():
# #     """Chained equality operators"""
# #     test_valid("void main() { auto x = 1 == 2 != 3 == 4; }")

# # def test_extreme_031():
# #     """Mixed arithmetic operators"""
# #     test_valid("void main() { auto x = 1 + 2 - 3 * 4 / 5 % 2; }")

# # def test_extreme_032():
# #     """Postfix on function call result followed by member access - INVALID"""
# #     test_invalid("""
# #         struct S { int x; };
# #         S f() { return {5}; }
# #         void main() {
# #             f()++.x;
# #         }
# #     """)

# # def test_extreme_033():
# #     """Member access on function call result"""
# #     test_valid("""
# #         struct S { int x; };
# #         S f() { return {5}; }
# #         void main() {
# #             auto v = f().x;
# #         }
# #     """)

# # def test_extreme_034():
# #     """Postfix on member of function result"""
# #     test_valid("""
# #         struct S { int x; };
# #         S f() { return {5}; }
# #         void main() {
# #             f().x++;
# #         }
# #     """)

# # def test_extreme_035():
# #     """Complex precedence chain"""
# #     test_valid("""
# #         struct S { int v; };
# #         void main() {
# #             S s;
# #             int a, b;
# #             a = s.v++ * -b + !a < 10 && 5 || b;
# #         }
# #     """)

# # # ============================================================================
# # # GROUP 3: NESTED STRUCTURES (10 tests)
# # # Testing deep nesting limits
# # # ============================================================================

# # def test_extreme_036():
# #     """Deeply nested if-else (dangling else problem)"""
# #     test_valid("""
# #         void main() {
# #             if (1) if (2) if (3) x = 1; else y = 2; else z = 3;
# #         }
# #     """)

# # def test_extreme_037():
# #     """Deeply nested blocks"""
# #     test_valid("""
# #         void main() {
# #             { { { { { { { { int x; } } } } } } } }
# #         }
# #     """)

# # def test_extreme_038():
# #     """Nested switch in switch in switch"""
# #     test_valid("""
# #         void main() {
# #             switch(a) {
# #                 case 1:
# #                     switch(b) {
# #                         case 2:
# #                             switch(c) {
# #                                 case 3: break;
# #                             }
# #                             break;
# #                     }
# #                     break;
# #             }
# #         }
# #     """)

# # def test_extreme_039():
# #     """Nested for in while in for"""
# #     test_valid("""
# #         void main() {
# #             for (;;) {
# #                 while (1) {
# #                     for (int i = 0; i < 10; i++) {
# #                         break;
# #                     }
# #                 }
# #             }
# #         }
# #     """)

# # def test_extreme_040():
# #     """Deeply nested parentheses"""
# #     test_valid("void main() { auto x = ((((((1 + 2) * 3) / 4) - 5) % 6)); }")

# # def test_extreme_041():
# #     """Deeply nested member access"""
# #     test_valid("""
# #         struct E { int val; };
# #         struct D { E e; };
# #         struct C { D d; };
# #         struct B { C c; };
# #         struct A { B b; };
# #         void main() {
# #             A a;
# #             a.b.c.d.e.val = 42;
# #         }
# #     """)

# # def test_extreme_042():
# #     """Deeply nested function calls"""
# #     test_valid("void main() { f(g(h(i(j(k(l(m()))))))); }")

# # def test_extreme_043():
# #     """Nested struct literals"""
# #     test_valid("""
# #         struct Inner { int x; int y; };
# #         struct Outer { Inner i; int z; };
# #         void main() {
# #             Outer o = {{1, 2}, 3};
# #         }
# #     """)

# # def test_extreme_044():
# #     """Mixed deep nesting"""
# #     test_valid("""
# #         void main() {
# #             {
# #                 for (;;) {
# #                     {
# #                         while (1) {
# #                             {
# #                                 if (x) {
# #                                     {
# #                                         switch (y) {
# #                                             case 1: { int z; } break;
# #                                         }
# #                                     }
# #                                 }
# #                             }
# #                         }
# #                     }
# #                 }
# #             }
# #         }
# #     """)

# # def test_extreme_045():
# #     """Deep expression nesting in all operator levels"""
# #     test_valid("""
# #         void main() {
# #             auto x = (a = (b || (c && (d == (e < (f + (g * (h++)))))))); 
# #         }
# #     """)

# # # ============================================================================
# # # GROUP 4: FOR LOOP EDGE CASES (10 tests)
# # # Testing complex for loop variations
# # # ============================================================================

# # def test_extreme_046():
# #     """For with comma-separated multiple inits"""
# #     test_valid("void main() { for (int x = 0, y = 10; x < y; x++, y--) { } }")

# # def test_extreme_047():
# #     """For with all parts empty"""
# #     test_valid("void main() { for (;;) { } }")

# # def test_extreme_048():
# #     """For with assignment init (no type)"""
# #     test_valid("void main() { for (x = 0; x < 10; x++) { } }")

# # def test_extreme_049():
# #     """For with auto init"""
# #     test_valid("void main() { for (auto i = 0; i < 10; i++) { } }")

# # def test_extreme_050():
# #     """For with complex init expression"""
# #     test_valid("void main() { for (int x = f(g(h())); x < 10; x++) { } }")

# # def test_extreme_051():
# #     """For with complex condition"""
# #     test_valid("void main() { for (int i = 0; i < n && j > 0; i++) { } }")

# # def test_extreme_052():
# #     """For with complex update"""
# #     test_valid("void main() { for (int i = 0; i < 10; i = i * 2 + 1) { } }")

# # def test_extreme_053():
# #     """For with multiple updates separated by comma"""
# #     test_valid("void main() { for (int i = 0; i < 10; i++, j--, k = k * 2) { } }")

# # def test_extreme_054():
# #     """For init with multiple declarations separated by comma"""
# #     test_valid("void main() { for (int a = 1, b = 2, c = 3; a < 10; a++) { } }")

# # def test_extreme_055():
# #     """For with wrong separator - semicolon instead of comma - INVALID"""
# #     test_valid("void main() { for (int i = 0; i < 10; i++) { } }")

# # # ============================================================================
# # # GROUP 5: SWITCH STATEMENT EDGE CASES (10 tests)
# # # Testing switch variations and edge cases
# # # ============================================================================

# # def test_extreme_056():
# #     """Switch with no cases or default"""
# #     test_valid("void main() { switch (x) { } }")

# # def test_extreme_057():
# #     """Switch with only default"""
# #     test_valid("void main() { switch (x) { default: break; } }")

# # def test_extreme_058():
# #     """Switch with case expression (not just literal)"""
# #     test_valid("void main() { switch (x) { case 1 + 2 * 3: break; } }")

# # def test_extreme_059():
# #     """Switch with negative case"""
# #     test_valid("void main() { switch (x) { case -5: break; } }")

# # def test_extreme_060():
# #     """Switch with parenthesized case value"""
# #     test_valid("void main() { switch (x) { case (5): break; } }")

# # def test_extreme_061():
# #     """Switch with fall-through cases"""
# #     test_valid("""
# #         void main() {
# #             switch (x) {
# #                 case 1:
# #                 case 2:
# #                 case 3:
# #                     y = 10;
# #                     break;
# #             }
# #         }
# #     """)

# # def test_extreme_062():
# #     """Switch with empty case"""
# #     test_valid("void main() { switch (x) { case 1: } }")

# # def test_extreme_063():
# #     """Switch case without colon - INVALID"""
# #     test_invalid("void main() { switch (x) { case 1 break; } }")

# # def test_extreme_064():
# #     """Switch with default before cases"""
# #     test_valid("""
# #         void main() {
# #             switch (x) {
# #                 default: x = 0; break;
# #                 case 1: x = 1; break;
# #             }
# #         }
# #     """)

# # def test_extreme_065():
# #     """Switch with multiple defaults - INVALID (grammar might allow but semantically wrong)"""
# #     test_invalid("""
# #         void main() {
# #             switch (x) {
# #                 default: break;
# #                 default: break;
# #             }
# #         }
# #     """)

# # # ============================================================================
# # # GROUP 6: EXPRESSION vs STATEMENT DISAMBIGUATION (10 tests)
# # # Testing cases where grammar might be ambiguous
# # # ============================================================================

# # def test_extreme_066():
# #     """ID() - function call statement"""
# #     test_valid("void main() { f(); }")

# # def test_extreme_067():
# #     """ID.ID - member access as expression statement"""
# #     test_valid("""
# #         struct S { int x; };
# #         void main() {
# #             S s;
# #             s.x;
# #         }
# #     """)

# # def test_extreme_068():
# #     """ID.ID() - member function call"""
# #     test_valid("void main() { obj.method(); }")

# # def test_extreme_069():
# #     """ID++ - postfix as statement"""
# #     test_valid("void main() { int x; x++; }")

# # def test_extreme_070():
# #     """++ID - prefix as statement"""
# #     test_valid("void main() { int x; ++x; }")

# # def test_extreme_071():
# #     """ID = expr - assignment statement"""
# #     test_valid("void main() { int x; x = 5; }")

# # def test_extreme_072():
# #     """(expr) - parenthesized expression as statement"""
# #     test_valid("void main() { (1 + 2); }")

# # def test_extreme_073():
# #     """Struct literal as statement - INVALID"""
# #     test_valid("void main() { {1, 2, 3}; }")

# # def test_extreme_074():
# #     """Assignment to rvalue - INVALID"""
# #     test_valid("void main() { 5 = x; }")

# # def test_extreme_075():
# #     """Member access on literal - INVALID"""
# #     test_invalid("void main() { 5.x; }")

# # # ============================================================================
# # # GROUP 7: STRUCT LITERAL EDGE CASES (10 tests)
# # # Testing struct literal variations
# # # ============================================================================

# # def test_extreme_076():
# #     """Empty struct literal"""
# #     test_valid("""
# #         struct Empty {};
# #         void main() {
# #             Empty e = {};
# #         }
# #     """)

# # def test_extreme_077():
# #     """Struct literal with expressions"""
# #     test_valid("""
# #         struct Point { int x; int y; };
# #         void main() {
# #             Point p = {1 + 2, 3 * 4};
# #         }
# #     """)

# # def test_extreme_078():
# #     """Struct literal with function calls"""
# #     test_valid("""
# #         struct Point { int x; int y; };
# #         void main() {
# #             Point p = {f(), g()};
# #         }
# #     """)

# # def test_extreme_079():
# #     """Nested struct literals"""
# #     test_valid("""
# #         struct Inner { int a; int b; };
# #         struct Outer { Inner i; int c; };
# #         void main() {
# #             Outer o = {{1, 2}, 3};
# #         }
# #     """)

# # def test_extreme_080():
# #     """Triple-nested struct literals"""
# #     test_valid("""
# #         struct A { int x; };
# #         struct B { A a; };
# #         struct C { B b; };
# #         void main() {
# #             C c = {{{5}}};
# #         }
# #     """)

# # def test_extreme_081():
# #     """Struct literal in function argument"""
# #     test_valid("""
# #         struct Point { int x; int y; };
# #         void f(Point p) { }
# #         void main() {
# #             f({5, 10});
# #         }
# #     """)

# # def test_extreme_082():
# #     """Struct literal in return statement"""
# #     test_valid("""
# #         struct Point { int x; int y; };
# #         Point getPoint() {
# #             return {5, 10};
# #         }
# #     """)

# # def test_extreme_083():
# #     """Struct literal with complex nested expressions"""
# #     test_valid("""
# #         struct Point { int x; int y; };
# #         void main() {
# #             Point p = {a + b * c, (d = e) + f};
# #         }
# #     """)

# # def test_extreme_084():
# #     """Struct literal with too many initializers (parser allows, semantic error)"""
# #     test_valid("""
# #         struct Point { int x; };
# #         void main() {
# #             Point p = {1, 2, 3, 4, 5};
# #         }
# #     """)

# # def test_extreme_085():
# #     """Struct literal with too few initializers"""
# #     test_valid("""
# #         struct Point { int x; int y; int z; };
# #         void main() {
# #             Point p = {1};
# #         }
# #     """)

# # # ============================================================================
# # # GROUP 8: SUBTLE SYNTAX ERRORS (10 tests)
# # # Testing cases that should fail parsing
# # # ============================================================================

# # def test_extreme_086():
# #     """Empty statement (single semicolon) - INVALID per spec"""
# #     test_invalid("void main() { ; }")

# # def test_extreme_087():
# #     """Multiple semicolons - INVALID"""
# #     test_invalid("void main() { ;; }")

# # def test_extreme_088():
# #     """Missing semicolon after statement"""
# #     test_invalid("void main() { int x = 5 }")

# # def test_extreme_089():
# #     """Missing closing brace"""
# #     test_invalid("void main() { int x = 5;")

# # def test_extreme_090():
# #     """Mismatched braces"""
# #     test_invalid("void main() { { int x; }")

# # def test_extreme_091():
# #     """Invalid operator sequence"""
# #     test_invalid("void main() { auto x = 5 ++ 2; }")

# # def test_extreme_092():
# #     """Function call without closing paren"""
# #     test_invalid("void main() { f(1, 2; }")

# # def test_extreme_093():
# #     """Case without colon"""
# #     test_invalid("void main() { switch(x) { case 1 break; } }")

# # def test_extreme_094():
# #     """If without condition"""
# #     test_invalid("void main() { if () { } }")

# # def test_extreme_095():
# #     """While without condition"""
# #     test_invalid("void main() { while () { } }")

# # # ============================================================================
# # # GROUP 9: COMPLEX REAL-WORLD SCENARIOS (5 tests)
# # # Testing realistic complex code
# # # ============================================================================

# # def test_extreme_096():
# #     """Recursive factorial with all statement types"""
# #     test_valid("""
# #         int factorial(int n) {
# #             if (n <= 1) {
# #                 return 1;
# #             }
# #             auto result = n * factorial(n - 1);
# #             return result;
# #         }
# #         void main() {
# #             int x = factorial(5);
# #         }
# #     """)

# # def test_extreme_097():
# #     """Complex nested control flow"""
# #     test_valid("""
# #         void main() {
# #             for (int i = 0; i < 10; i++) {
# #                 while (j < i) {
# #                     switch (k) {
# #                         case 1:
# #                             if (m) {
# #                                 for (auto n = 0; n < 5; n++) {
# #                                     if (p) break;
# #                                     else continue;
# #                                 }
# #                             } else {
# #                                 while (q) {
# #                                     if (r) break;
# #                                 }
# #                             }
# #                             break;
# #                         default:
# #                             break;
# #                     }
# #                     j++;
# #                 }
# #             }
# #         }
# #     """)

# # def test_extreme_098():
# #     """Complex struct operations"""
# #     test_valid("""
# #         struct Point { int x; int y; };
# #         struct Line { Point start; Point end; };
        
# #         Point midpoint(Line l) {
# #             return {(l.start.x + l.end.x) / 2, (l.start.y + l.end.y) / 2};
# #         }
        
# #         void main() {
# #             Line line = {{0, 0}, {10, 10}};
# #             Point mid = midpoint(line);
# #             mid.x++;
# #             auto val = mid.x + mid.y;
# #         }
# #     """)

# # def test_extreme_099():
# #     """Complex expression with all operators"""
# #     test_valid("""
# #         struct S { int v; };
# #         void main() {
# #             S s, t;
# #             int a, b, c, d;
# #             auto result = (a = s.v++ * -b + !c < d) && (t.v-- / +a > b) || !(--c == ++d);
# #         }
# #     """)

# # def test_extreme_100():
# #     """All features combined in realistic code"""
# #     test_valid("""
# #         struct Node { int data; Node next; };
        
# #         Node createNode(int val) {
# #             Node n;
# #             n.data = val;
# #             return n;
# #         }
        
# #         void main() {
# #             auto head = createNode(1);
            
# #             for (int i = 2; i <= 10; i++) {
# #                 Node current = head;
# #                 while (current.next.data != 0) {
# #                     current = current.next;
# #                 }
# #                 current.next = createNode(i);
# #             }
            
# #             int sum = 0;
# #             Node iter = head;
# #             while (iter.data != 0) {
# #                 sum = sum + iter.data;
# #                 iter = iter.next;
# #                 if (sum > 100) break;
# #             }
            
# #             switch (sum) {
# #                 case 0:
# #                 case 10:
# #                 case 20:
# #                     printInt(sum);
# #                     break;
# #                 default:
# #                     printString("Other value");
# #                     break;
# #             }
# #         }
# #     """)

# """
# Comprehensive Lexer Test Suite for TyC Compiler
# 150 test cases covering all lexical features
# """

# import pytest
# from tests.utils import Tokenizer


# # ========== SECTION 1: Keywords (18 tests) ==========

# def test_keyword_auto_001():
#     """Test 1: Keyword auto"""
#     tokenizer = Tokenizer("auto")
#     assert tokenizer.get_tokens_as_string() == "auto,<EOF>"

# def test_keyword_break_002():
#     """Test 2: Keyword break"""
#     tokenizer = Tokenizer("break")
#     assert tokenizer.get_tokens_as_string() == "break,<EOF>"

# def test_keyword_case_003():
#     """Test 3: Keyword case"""
#     tokenizer = Tokenizer("case")
#     assert tokenizer.get_tokens_as_string() == "case,<EOF>"

# def test_keyword_continue_004():
#     """Test 4: Keyword continue"""
#     tokenizer = Tokenizer("continue")
#     assert tokenizer.get_tokens_as_string() == "continue,<EOF>"

# def test_keyword_default_005():
#     """Test 5: Keyword default"""
#     tokenizer = Tokenizer("default")
#     assert tokenizer.get_tokens_as_string() == "default,<EOF>"

# def test_keyword_else_006():
#     """Test 6: Keyword else"""
#     tokenizer = Tokenizer("else")
#     assert tokenizer.get_tokens_as_string() == "else,<EOF>"

# def test_keyword_float_007():
#     """Test 7: Keyword float"""
#     tokenizer = Tokenizer("float")
#     assert tokenizer.get_tokens_as_string() == "float,<EOF>"

# def test_keyword_for_008():
#     """Test 8: Keyword for"""
#     tokenizer = Tokenizer("for")
#     assert tokenizer.get_tokens_as_string() == "for,<EOF>"

# def test_keyword_if_009():
#     """Test 9: Keyword if"""
#     tokenizer = Tokenizer("if")
#     assert tokenizer.get_tokens_as_string() == "if,<EOF>"

# def test_keyword_int_010():
#     """Test 10: Keyword int"""
#     tokenizer = Tokenizer("int")
#     assert tokenizer.get_tokens_as_string() == "int,<EOF>"

# def test_keyword_return_011():
#     """Test 11: Keyword return"""
#     tokenizer = Tokenizer("return")
#     assert tokenizer.get_tokens_as_string() == "return,<EOF>"

# def test_keyword_string_012():
#     """Test 12: Keyword string"""
#     tokenizer = Tokenizer("string")
#     assert tokenizer.get_tokens_as_string() == "string,<EOF>"

# def test_keyword_struct_013():
#     """Test 13: Keyword struct"""
#     tokenizer = Tokenizer("struct")
#     assert tokenizer.get_tokens_as_string() == "struct,<EOF>"

# def test_keyword_switch_014():
#     """Test 14: Keyword switch"""
#     tokenizer = Tokenizer("switch")
#     assert tokenizer.get_tokens_as_string() == "switch,<EOF>"

# def test_keyword_void_015():
#     """Test 15: Keyword void"""
#     tokenizer = Tokenizer("void")
#     assert tokenizer.get_tokens_as_string() == "void,<EOF>"

# def test_keyword_while_016():
#     """Test 16: Keyword while"""
#     tokenizer = Tokenizer("while")
#     assert tokenizer.get_tokens_as_string() == "while,<EOF>"

# def test_keyword_all_together_017():
#     """Test 17: All keywords together"""
#     tokenizer = Tokenizer("auto break case continue default else float for if int return string struct switch void while")
#     assert tokenizer.get_tokens_as_string() == "auto,break,case,continue,default,else,float,for,if,int,return,string,struct,switch,void,while,<EOF>"

# def test_keyword_case_sensitive_018():
#     """Test 18: Keywords are case-sensitive (AUTO is identifier)"""
#     tokenizer = Tokenizer("AUTO Auto aUto")
#     assert tokenizer.get_tokens_as_string() == "AUTO,Auto,aUto,<EOF>"


# # ========== SECTION 2: Operators (20 tests) ==========

# def test_operator_plus_019():
#     """Test 19: Plus operator"""
#     tokenizer = Tokenizer("+")
#     assert tokenizer.get_tokens_as_string() == "+,<EOF>"

# def test_operator_minus_020():
#     """Test 20: Minus operator"""
#     tokenizer = Tokenizer("-")
#     assert tokenizer.get_tokens_as_string() == "-,<EOF>"

# def test_operator_multiply_021():
#     """Test 21: Multiply operator"""
#     tokenizer = Tokenizer("*")
#     assert tokenizer.get_tokens_as_string() == "*,<EOF>"

# def test_operator_divide_022():
#     """Test 22: Divide operator"""
#     tokenizer = Tokenizer("/")
#     assert tokenizer.get_tokens_as_string() == "/,<EOF>"

# def test_operator_modulo_023():
#     """Test 23: Modulo operator"""
#     tokenizer = Tokenizer("%")
#     assert tokenizer.get_tokens_as_string() == "%,<EOF>"

# def test_operator_equal_024():
#     """Test 24: Equal operator"""
#     tokenizer = Tokenizer("==")
#     assert tokenizer.get_tokens_as_string() == "==,<EOF>"

# def test_operator_not_equal_025():
#     """Test 25: Not equal operator"""
#     tokenizer = Tokenizer("!=")
#     assert tokenizer.get_tokens_as_string() == "!=,<EOF>"

# def test_operator_less_than_026():
#     """Test 26: Less than operator"""
#     tokenizer = Tokenizer("<")
#     assert tokenizer.get_tokens_as_string() == "<,<EOF>"

# def test_operator_greater_than_027():
#     """Test 27: Greater than operator"""
#     tokenizer = Tokenizer(">")
#     assert tokenizer.get_tokens_as_string() == ">,<EOF>"

# def test_operator_less_equal_028():
#     """Test 28: Less than or equal operator"""
#     tokenizer = Tokenizer("<=")
#     assert tokenizer.get_tokens_as_string() == "<=,<EOF>"

# def test_operator_greater_equal_029():
#     """Test 29: Greater than or equal operator"""
#     tokenizer = Tokenizer(">=")
#     assert tokenizer.get_tokens_as_string() == ">=,<EOF>"

# def test_operator_logical_or_030():
#     """Test 30: Logical OR operator"""
#     tokenizer = Tokenizer("||")
#     assert tokenizer.get_tokens_as_string() == "||,<EOF>"

# def test_operator_logical_and_031():
#     """Test 31: Logical AND operator"""
#     tokenizer = Tokenizer("&&")
#     assert tokenizer.get_tokens_as_string() == "&&,<EOF>"

# def test_operator_logical_not_032():
#     """Test 32: Logical NOT operator"""
#     tokenizer = Tokenizer("!")
#     assert tokenizer.get_tokens_as_string() == "!,<EOF>"

# def test_operator_increment_033():
#     """Test 33: Increment operator"""
#     tokenizer = Tokenizer("++")
#     assert tokenizer.get_tokens_as_string() == "++,<EOF>"

# def test_operator_decrement_034():
#     """Test 34: Decrement operator"""
#     tokenizer = Tokenizer("--")
#     assert tokenizer.get_tokens_as_string() == "--,<EOF>"

# def test_operator_assign_035():
#     """Test 35: Assignment operator"""
#     tokenizer = Tokenizer("=")
#     assert tokenizer.get_tokens_as_string() == "=,<EOF>"

# def test_operator_dot_036():
#     """Test 36: Dot operator (member access)"""
#     tokenizer = Tokenizer(".")
#     assert tokenizer.get_tokens_as_string() == ".,<EOF>"

# def test_operator_longest_match_037():
#     """Test 37: Operator longest match (== vs =)"""
#     tokenizer = Tokenizer("a==b")
#     assert tokenizer.get_tokens_as_string() == "a,==,b,<EOF>"

# def test_operator_mixed_chain_038():
#     """Test 38: Mixed operator chain"""
#     tokenizer = Tokenizer("a+++b")
#     assert tokenizer.get_tokens_as_string() == "a,++,+,b,<EOF>"


# # ========== SECTION 3: Separators (7 tests) ==========

# def test_separator_left_brace_039():
#     """Test 39: Left brace"""
#     tokenizer = Tokenizer("{")
#     assert tokenizer.get_tokens_as_string() == "{,<EOF>"

# def test_separator_right_brace_040():
#     """Test 40: Right brace"""
#     tokenizer = Tokenizer("}")
#     assert tokenizer.get_tokens_as_string() == "},<EOF>"

# def test_separator_left_paren_041():
#     """Test 41: Left parenthesis"""
#     tokenizer = Tokenizer("(")
#     assert tokenizer.get_tokens_as_string() == "(,<EOF>"

# def test_separator_right_paren_042():
#     """Test 42: Right parenthesis"""
#     tokenizer = Tokenizer(")")
#     assert tokenizer.get_tokens_as_string() == "),<EOF>"

# def test_separator_semicolon_043():
#     """Test 43: Semicolon"""
#     tokenizer = Tokenizer(";")
#     assert tokenizer.get_tokens_as_string() == ";,<EOF>"

# def test_separator_comma_044():
#     """Test 44: Comma"""
#     tokenizer = Tokenizer(",")
#     assert tokenizer.get_tokens_as_string() == ",,<EOF>"

# def test_separator_colon_045():
#     """Test 45: Colon"""
#     tokenizer = Tokenizer(":")
#     assert tokenizer.get_tokens_as_string() == ":,<EOF>"


# # ========== SECTION 4: Integer Literals (10 tests) ==========

# def test_integer_zero_046():
#     """Test 46: Zero"""
#     tokenizer = Tokenizer("0")
#     assert tokenizer.get_tokens_as_string() == "0,<EOF>"

# def test_integer_single_digit_047():
#     """Test 47: Single digit"""
#     tokenizer = Tokenizer("7")
#     assert tokenizer.get_tokens_as_string() == "7,<EOF>"

# def test_integer_multi_digit_048():
#     """Test 48: Multi-digit integer"""
#     tokenizer = Tokenizer("123456")
#     assert tokenizer.get_tokens_as_string() == "123456,<EOF>"

# def test_integer_large_049():
#     """Test 49: Large integer"""
#     tokenizer = Tokenizer("2147483647")
#     assert tokenizer.get_tokens_as_string() == "2147483647,<EOF>"

# def test_integer_leading_zero_050():
#     """Test 50: Leading zeros split into multiple tokens"""
#     tokenizer = Tokenizer("007")
#     assert tokenizer.get_tokens_as_string() == "0,0,7,<EOF>"

# def test_integer_in_expression_051():
#     """Test 51: Integers in expression"""
#     tokenizer = Tokenizer("5+10-3")
#     assert tokenizer.get_tokens_as_string() == "5,+,10,-,3,<EOF>"

# def test_integer_sequence_052():
#     """Test 52: Sequence of integers"""
#     tokenizer = Tokenizer("1 22 333 4444")
#     assert tokenizer.get_tokens_as_string() == "1,22,333,4444,<EOF>"

# def test_integer_with_operators_053():
#     """Test 53: Integers with all arithmetic operators"""
#     tokenizer = Tokenizer("100*50/25%3")
#     assert tokenizer.get_tokens_as_string() == "100,*,50,/,25,%,3,<EOF>"

# def test_integer_negative_context_054():
#     """Test 54: Minus as operator (not negative literal)"""
#     tokenizer = Tokenizer("5-3")
#     assert tokenizer.get_tokens_as_string() == "5,-,3,<EOF>"

# def test_integer_boundaries_055():
#     """Test 55: Integer at boundaries"""
#     tokenizer = Tokenizer("(42)")
#     assert tokenizer.get_tokens_as_string() == "(,42,),<EOF>"


# # ========== SECTION 5: Float Literals (15 tests) ==========

# def test_float_simple_decimal_056():
#     """Test 56: Simple decimal"""
#     tokenizer = Tokenizer("3.14")
#     assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"

# def test_float_decimal_at_end_057():
#     """Test 57: Decimal point at end"""
#     tokenizer = Tokenizer("42.")
#     assert tokenizer.get_tokens_as_string() == "42.,<EOF>"

# def test_float_decimal_at_start_058():
#     """Test 58: Decimal point at start"""
#     tokenizer = Tokenizer(".5")
#     assert tokenizer.get_tokens_as_string() == ".5,<EOF>"

# def test_float_exponent_positive_059():
#     """Test 59: Exponent with positive sign"""
#     tokenizer = Tokenizer("1e4")
#     assert tokenizer.get_tokens_as_string() == "1e4,<EOF>"

# def test_float_exponent_negative_060():
#     """Test 60: Exponent with negative sign"""
#     tokenizer = Tokenizer("2E-3")
#     assert tokenizer.get_tokens_as_string() == "2E-3,<EOF>"

# def test_float_exponent_explicit_plus_061():
#     """Test 61: Exponent with explicit plus"""
#     tokenizer = Tokenizer("5E+10")
#     assert tokenizer.get_tokens_as_string() == "5E+10,<EOF>"

# def test_float_full_format_062():
#     """Test 62: Float with all components"""
#     tokenizer = Tokenizer("3.14159e-10")
#     assert tokenizer.get_tokens_as_string() == "3.14159e-10,<EOF>"

# def test_float_zero_formats_063():
#     """Test 63: Different zero representations"""
#     tokenizer = Tokenizer("0.0 .0 0.")
#     assert tokenizer.get_tokens_as_string() == "0.0,.0,0.,<EOF>"

# def test_float_scientific_large_064():
#     """Test 64: Large scientific notation"""
#     tokenizer = Tokenizer("9.99E+100")
#     assert tokenizer.get_tokens_as_string() == "9.99E+100,<EOF>"

# def test_float_scientific_tiny_065():
#     """Test 65: Tiny scientific notation"""
#     tokenizer = Tokenizer("1e-100")
#     assert tokenizer.get_tokens_as_string() == "1e-100,<EOF>"

# def test_float_edge_case_dot_exp_066():
#     """Test 66: Decimal at end with exponent"""
#     tokenizer = Tokenizer("1.e10")
#     assert tokenizer.get_tokens_as_string() == "1.e10,<EOF>"

# def test_float_edge_case_start_exp_067():
#     """Test 67: Decimal at start with exponent"""
#     tokenizer = Tokenizer(".5e3")
#     assert tokenizer.get_tokens_as_string() == ".5e3,<EOF>"

# def test_float_in_expression_068():
#     """Test 68: Floats in expression"""
#     tokenizer = Tokenizer("1.5+2.3e4-.7")
#     assert tokenizer.get_tokens_as_string() == "1.5,+,2.3e4,-,.7,<EOF>"

# def test_float_vs_member_access_069():
#     """Test 69: Float vs member access"""
#     tokenizer = Tokenizer("3.14 obj.member")
#     assert tokenizer.get_tokens_as_string() == "3.14,obj,.,member,<EOF>"

# def test_float_both_e_and_E_070():
#     """Test 70: Both lowercase and uppercase E"""
#     tokenizer = Tokenizer("1e5 2E3")
#     assert tokenizer.get_tokens_as_string() == "1e5,2E3,<EOF>"


# # ========== SECTION 6: String Literals (15 tests) ==========

# def test_string_empty_071():
#     """Test 71: Empty string"""
#     tokenizer = Tokenizer('""')
#     assert tokenizer.get_tokens_as_string() == ",<EOF>"

# def test_string_simple_072():
#     """Test 72: Simple string"""
#     tokenizer = Tokenizer('"hello"')
#     assert tokenizer.get_tokens_as_string() == "hello,<EOF>"

# def test_string_with_spaces_073():
#     """Test 73: String with spaces"""
#     tokenizer = Tokenizer('"hello world"')
#     assert tokenizer.get_tokens_as_string() == "hello world,<EOF>"

# def test_string_escape_tab_074():
#     """Test 74: Escape sequence tab"""
#     tokenizer = Tokenizer('"hello\\\\tworld"')
#     assert tokenizer.get_tokens_as_string() == "hello\\\\tworld,<EOF>"

# def test_string_escape_newline_075():
#     """Test 75: Escape sequence newline"""
#     tokenizer = Tokenizer('"line1\\\\nline2"')
#     assert tokenizer.get_tokens_as_string() == "line1\\\\nline2,<EOF>"

# def test_string_escape_quote_076():
#     """Test 76: Escaped quote"""
#     tokenizer = Tokenizer('"He said \\\\\\"Hi\\\\\\""')
#     assert tokenizer.get_tokens_as_string() == r'He said \\\"Hi\\\",<EOF>'

# def test_string_escape_backslash_077():
#     """Test 77: Escaped backslash"""
#     tokenizer = Tokenizer('"C:\\\\\\\\\\\\\\\\path"')
#     assert tokenizer.get_tokens_as_string() == "C:\\\\\\\\\\\\\\\\path,<EOF>"

# def test_string_all_escapes_078():
#     """Test 78: All valid escape sequences"""
#     tokenizer = Tokenizer('"\\\\b\\\\f\\\\r\\\\n\\\\t\\\\\\"\\\\\\\\\\\\\\\\."')
#     assert tokenizer.get_tokens_as_string() == '\\\\b\\\\f\\\\r\\\\n\\\\t\\\\\\"\\\\\\\\\\\\\\\\.,<EOF>'

# def test_string_multiple_079():
#     """Test 79: Multiple strings"""
#     tokenizer = Tokenizer('"first" "second" "third"')
#     assert tokenizer.get_tokens_as_string() == "first,second,third,<EOF>"

# def test_string_with_numbers_080():
#     """Test 80: String with numbers"""
#     tokenizer = Tokenizer('"Value: 12345"')
#     assert tokenizer.get_tokens_as_string() == "Value: 12345,<EOF>"

# def test_string_with_special_chars_081():
#     """Test 81: String with special characters"""
#     tokenizer = Tokenizer('"!@#$%^&*()_+-="')
#     assert tokenizer.get_tokens_as_string() == "!@#$%^&*()_+-=,<EOF>"

# def test_string_long_082():
#     """Test 82: Long string"""
#     tokenizer = Tokenizer('"' + 'a'*100 + '"')
#     assert tokenizer.get_tokens_as_string() == 'a'*100 + ",<EOF>"

# def test_string_in_function_083():
#     """Test 83: String in function call"""
#     tokenizer = Tokenizer('print("Hello")')
#     assert tokenizer.get_tokens_as_string() == "print,(,Hello,),<EOF>"

# def test_string_mixed_content_084():
#     """Test 84: Mixed content in string"""
#     tokenizer = Tokenizer('"Mix: 123 abc !@# \\\\n\\\\t"')
#     assert tokenizer.get_tokens_as_string() == "Mix: 123 abc !@# \\\\n\\\\t,<EOF>"

# def test_string_quotes_removed_085():
#     """Test 85: Verify quotes are removed"""
#     tokenizer = Tokenizer('"test"')
#     result = tokenizer.get_tokens_as_string()
#     assert '"' not in result.replace('<EOF>', '').replace(',', '')


# # ========== SECTION 7: Identifiers (10 tests) ==========

# def test_identifier_single_letter_086():
#     """Test 86: Single letter identifier"""
#     tokenizer = Tokenizer("x")
#     assert tokenizer.get_tokens_as_string() == "x,<EOF>"

# def test_identifier_multi_letter_087():
#     """Test 87: Multi-letter identifier"""
#     tokenizer = Tokenizer("variable")
#     assert tokenizer.get_tokens_as_string() == "variable,<EOF>"

# def test_identifier_with_digits_088():
#     """Test 88: Identifier with digits"""
#     tokenizer = Tokenizer("var123")
#     assert tokenizer.get_tokens_as_string() == "var123,<EOF>"

# def test_identifier_with_underscores_089():
#     """Test 89: Identifier with underscores"""
#     tokenizer = Tokenizer("_private my_var __special")
#     assert tokenizer.get_tokens_as_string() == "_private,my_var,__special,<EOF>"

# def test_identifier_starts_underscore_090():
#     """Test 90: Identifier starting with underscore"""
#     tokenizer = Tokenizer("_test")
#     assert tokenizer.get_tokens_as_string() == "_test,<EOF>"

# def test_identifier_camelCase_091():
#     """Test 91: CamelCase identifier"""
#     tokenizer = Tokenizer("myVariableName")
#     assert tokenizer.get_tokens_as_string() == "myVariableName,<EOF>"

# def test_identifier_PascalCase_092():
#     """Test 92: PascalCase identifier"""
#     tokenizer = Tokenizer("MyClassName")
#     assert tokenizer.get_tokens_as_string() == "MyClassName,<EOF>"

# def test_identifier_snake_case_093():
#     """Test 93: snake_case identifier"""
#     tokenizer = Tokenizer("my_function_name")
#     assert tokenizer.get_tokens_as_string() == "my_function_name,<EOF>"

# def test_identifier_not_keyword_094():
#     """Test 94: Similar to keyword but not keyword"""
#     tokenizer = Tokenizer("integer automat")
#     assert tokenizer.get_tokens_as_string() == "integer,automat,<EOF>"

# def test_identifier_long_095():
#     """Test 95: Very long identifier"""
#     tokenizer = Tokenizer("thisIsAVeryLongIdentifierName123")
#     assert tokenizer.get_tokens_as_string() == "thisIsAVeryLongIdentifierName123,<EOF>"


# # ========== SECTION 8: Comments (8 tests) ==========

# def test_comment_line_simple_096():
#     """Test 96: Simple line comment"""
#     tokenizer = Tokenizer("// This is a comment")
#     assert tokenizer.get_tokens_as_string() == "<EOF>"

# def test_comment_line_before_code_097():
#     """Test 97: Line comment before code"""
#     tokenizer = Tokenizer("// comment\nint x")
#     assert tokenizer.get_tokens_as_string() == "int,x,<EOF>"

# def test_comment_block_simple_098():
#     """Test 98: Simple block comment"""
#     tokenizer = Tokenizer("/* comment */")
#     assert tokenizer.get_tokens_as_string() == "<EOF>"

# def test_comment_block_multiline_099():
#     """Test 99: Multiline block comment"""
#     tokenizer = Tokenizer("/* line1\\nline2\\nline3 */")
#     assert tokenizer.get_tokens_as_string() == "<EOF>"

# def test_comment_block_with_slashes_100():
#     """Test 100: Block comment with //"""
#     tokenizer = Tokenizer("/* // not line comment */")
#     assert tokenizer.get_tokens_as_string() == "<EOF>"

# def test_comment_line_with_block_101():
#     """Test 101: Line comment with /* */"""
#     tokenizer = Tokenizer("// /* not block */")
#     assert tokenizer.get_tokens_as_string() == "<EOF>"

# def test_comment_block_empty_102():
#     """Test 102: Empty block comment"""
#     tokenizer = Tokenizer("/**/")
#     assert tokenizer.get_tokens_as_string() == "<EOF>"

# def test_comment_mixed_with_code_103():
#     """Test 103: Comments mixed with code"""
#     tokenizer = Tokenizer("int x; // variable\n/* block */ int y;")
#     assert tokenizer.get_tokens_as_string() == "int,x,;,int,y,;,<EOF>"


# # ========== SECTION 9: Error Cases (20 tests) ==========

# def test_error_illegal_escape_x_104():
#     """Test 104: Illegal escape \\\\x"""
#     tokenizer = Tokenizer('"hello\\\\x"')
#     assert tokenizer.get_tokens_as_string() == "hello\\\\x,<EOF>"

# def test_error_illegal_escape_a_105():
#     """Test 105: Illegal escape \\\\a"""
#     tokenizer = Tokenizer('"test\\\\a"')
#     assert tokenizer.get_tokens_as_string() == "test\\\\a,<EOF>"

# def test_error_illegal_escape_digit_106():
#     """Test 106: Illegal escape \\\\1"""
#     tokenizer = Tokenizer('"\\\\1"')
#     assert tokenizer.get_tokens_as_string() == "\\\\1,<EOF>"

# def test_error_illegal_escape_space_107():
#     """Test 107: Illegal escape with space"""
#     tokenizer = Tokenizer('"\\ "')
#     assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\ "

# def test_error_illegal_escape_unicode_108():
#     """Test 108: Illegal unicode escape"""
#     tokenizer = Tokenizer('"\\u0041"')
#     assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\u"

# def test_error_unclose_string_eof_109():
#     """Test 109: Unclosed string at EOF"""
#     tokenizer = Tokenizer('"hello')
#     assert tokenizer.get_tokens_as_string() == "Unclosed String: hello"

# def test_error_unclose_string_newline_110():
#     """Test 110: Unclosed string at newline"""
#     tokenizer = Tokenizer('"hello\\n')
#     assert tokenizer.get_tokens_as_string() == "Unclosed String: hello\\n"

# def test_error_unclose_string_empty_111():
#     """Test 111: Unclosed empty string"""
#     tokenizer = Tokenizer('"')
#     assert tokenizer.get_tokens_as_string() == "Unclosed String: "

# def test_error_unclose_string_with_escape_112():
#     """Test 112: Unclosed with valid escape"""
#     tokenizer = Tokenizer('"text\\\\n')
#     assert tokenizer.get_tokens_as_string() == "Unclosed String: text\\\\n"

# def test_error_char_at_sign_113():
#     """Test 113: Invalid character @"""
#     tokenizer = Tokenizer("@")
#     assert tokenizer.get_tokens_as_string() == "Error Token @"

# def test_error_char_hash_114():
#     """Test 114: Invalid character #"""
#     tokenizer = Tokenizer("#")
#     assert tokenizer.get_tokens_as_string() == "Error Token #"

# def test_error_char_dollar_115():
#     """Test 115: Invalid character $"""
#     tokenizer = Tokenizer("$")
#     assert tokenizer.get_tokens_as_string() == "Error Token $"

# def test_error_char_single_pipe_116():
#     """Test 116: Single pipe (|| valid, | not)"""
#     tokenizer = Tokenizer("a|b")
#     assert tokenizer.get_tokens_as_string() == "a,Error Token |"

# def test_error_char_single_ampersand_117():
#     """Test 117: Single ampersand (&& valid, & not)"""
#     tokenizer = Tokenizer("a&b")
#     assert tokenizer.get_tokens_as_string() == "a,Error Token &"

# def test_error_char_question_118():
#     """Test 118: Question mark not valid"""
#     tokenizer = Tokenizer("?")
#     assert tokenizer.get_tokens_as_string() == "Error Token ?"

# def test_error_char_bracket_119():
#     """Test 119: Square brackets not valid"""
#     tokenizer = Tokenizer("[")
#     assert tokenizer.get_tokens_as_string() == "Error Token ["

# def test_error_char_tilde_120():
#     """Test 120: Tilde not valid"""
#     tokenizer = Tokenizer("~")
#     assert tokenizer.get_tokens_as_string() == "Error Token ~"

# def test_error_char_backtick_121():
#     """Test 121: Backtick not valid"""
#     tokenizer = Tokenizer("`")
#     assert tokenizer.get_tokens_as_string() == "Error Token `"

# def test_error_char_caret_122():
#     """Test 122: Caret not valid"""
#     tokenizer = Tokenizer("^")
#     assert tokenizer.get_tokens_as_string() == "Error Token ^"

# def test_error_priority_illegal_over_unclose_123():
#     """Test 123: Illegal escape detected before unclosed"""
#     tokenizer = Tokenizer('"test\\x')
#     assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: test\\x"


# # ========== SECTION 10: Real Program Fragments (15 tests) ==========

# def test_program_var_decl_124():
#     """Test 124: Variable declaration"""
#     tokenizer = Tokenizer("int x = 5;")
#     assert tokenizer.get_tokens_as_string() == "int,x,=,5,;,<EOF>"

# def test_program_auto_var_125():
#     """Test 125: Auto variable"""
#     tokenizer = Tokenizer("auto y = 3.14;")
#     assert tokenizer.get_tokens_as_string() == "auto,y,=,3.14,;,<EOF>"

# def test_program_function_decl_126():
#     """Test 126: Function declaration"""
#     tokenizer = Tokenizer("int add(int x, int y) {")
#     assert tokenizer.get_tokens_as_string() == "int,add,(,int,x,,,int,y,),{,<EOF>"

# def test_program_if_statement_127():
#     """Test 127: If statement"""
#     tokenizer = Tokenizer("if (x > 0) { return x; }")
#     assert tokenizer.get_tokens_as_string() == "if,(,x,>,0,),{,return,x,;,},<EOF>"

# def test_program_if_else_128():
#     """Test 128: If-else statement"""
#     tokenizer = Tokenizer("if (x) { y = 1; } else { y = 0; }")
#     assert tokenizer.get_tokens_as_string() == "if,(,x,),{,y,=,1,;,},else,{,y,=,0,;,},<EOF>"

# def test_program_while_loop_129():
#     """Test 129: While loop"""
#     tokenizer = Tokenizer("while (i < 10) { i++; }")
#     assert tokenizer.get_tokens_as_string() == "while,(,i,<,10,),{,i,++,;,},<EOF>"

# def test_program_for_loop_130():
#     """Test 130: For loop"""
#     tokenizer = Tokenizer("for (auto i = 0; i < 10; ++i) { }")
#     assert tokenizer.get_tokens_as_string() == "for,(,auto,i,=,0,;,i,<,10,;,++,i,),{,},<EOF>"

# def test_program_switch_131():
#     """Test 131: Switch statement"""
#     tokenizer = Tokenizer("switch (x) { case 1: break; default: }")
#     assert tokenizer.get_tokens_as_string() == "switch,(,x,),{,case,1,:,break,;,default,:,},<EOF>"

# def test_program_struct_def_132():
#     """Test 132: Struct definition"""
#     tokenizer = Tokenizer("struct Point { int x; int y; };")
#     assert tokenizer.get_tokens_as_string() == "struct,Point,{,int,x,;,int,y,;,},;,<EOF>"

# def test_program_struct_init_133():
#     """Test 133: Struct initialization"""
#     tokenizer = Tokenizer("Point p = {10, 20};")
#     assert tokenizer.get_tokens_as_string() == "Point,p,=,{,10,,,20,},;,<EOF>"

# def test_program_member_access_134():
#     """Test 134: Member access"""
#     tokenizer = Tokenizer("p.x = 5;")
#     assert tokenizer.get_tokens_as_string() == "p,.,x,=,5,;,<EOF>"

# def test_program_function_call_135():
#     """Test 135: Function call"""
#     tokenizer = Tokenizer('printString("Hello, World!");')
#     assert tokenizer.get_tokens_as_string() == "printString,(,Hello, World!,),;,<EOF>"

# def test_program_complex_expr_136():
#     """Test 136: Complex expression"""
#     tokenizer = Tokenizer("result = (a + b) * c - d / e % f;")
#     assert tokenizer.get_tokens_as_string() == "result,=,(,a,+,b,),*,c,-,d,/,e,%,f,;,<EOF>"

# def test_program_return_stmt_137():
#     """Test 137: Return statement"""
#     tokenizer = Tokenizer("return x * 2;")
#     assert tokenizer.get_tokens_as_string() == "return,x,*,2,;,<EOF>"

# def test_program_void_return_138():
#     """Test 138: Void return"""
#     tokenizer = Tokenizer("return;")
#     assert tokenizer.get_tokens_as_string() == "return,;,<EOF>"


# # ========== SECTION 11: Whitespace & Edge Cases (12 tests) ==========

# def test_whitespace_no_space_139():
#     """Test 139: No whitespace"""
#     tokenizer = Tokenizer("int x=5;")
#     assert tokenizer.get_tokens_as_string() == "int,x,=,5,;,<EOF>"

# def test_whitespace_excessive_140():
#     """Test 140: Excessive whitespace"""
#     tokenizer = Tokenizer("auto     x     =     10;")
#     assert tokenizer.get_tokens_as_string() == "auto,x,=,10,;,<EOF>"

# def test_whitespace_all_types_141():
#     """Test 141: All whitespace types"""
#     tokenizer = Tokenizer("a \t\f\r\n b")
#     assert tokenizer.get_tokens_as_string() == "a,b,<EOF>"

# def test_whitespace_tabs_142():
#     """Test 142: Tabs in code"""
#     tokenizer = Tokenizer("int\tx\t=\t5;")
#     assert tokenizer.get_tokens_as_string() == "int,x,=,5,;,<EOF>"

# def test_edge_zero_followed_by_digit_143():
#     """Test 143: Zero followed by digit splits"""
#     tokenizer = Tokenizer("0123")
#     assert tokenizer.get_tokens_as_string() == "0,123,<EOF>"

# def test_edge_multiple_zeros_144():
#     """Test 144: Multiple zeros"""
#     tokenizer = Tokenizer("000")
#     assert tokenizer.get_tokens_as_string() == "0,0,0,<EOF>"

# def test_edge_float_vs_dot_145():
#     """Test 145: Float vs member access ambiguity"""
#     tokenizer = Tokenizer("3.14 a.b")
#     assert tokenizer.get_tokens_as_string() == "3.14,a,.,b,<EOF>"

# def test_edge_division_vs_comment_146():
#     """Test 146: Division not confused with comment"""
#     tokenizer = Tokenizer("10/2")
#     assert tokenizer.get_tokens_as_string() == "10,/,2,<EOF>"

# def test_edge_star_vs_comment_147():
#     """Test 147: Multiply not part of comment"""
#     tokenizer = Tokenizer("5*3 /* real comment */")
#     assert tokenizer.get_tokens_as_string() == "5,*,3,<EOF>"

# def test_edge_increment_chain_148():
#     """Test 148: Triple plus splits correctly"""
#     tokenizer = Tokenizer("x+++y")
#     assert tokenizer.get_tokens_as_string() == "x,++,+,y,<EOF>"

# def test_edge_decrement_chain_149():
#     """Test 149: Triple minus splits correctly"""
#     tokenizer = Tokenizer("x---y")
#     assert tokenizer.get_tokens_as_string() == "x,--,-,y,<EOF>"

# def test_edge_equal_chain_150():
#     """Test 150: Triple equals splits correctly"""
#     tokenizer = Tokenizer("a===b")
#     assert tokenizer.get_tokens_as_string() == "a,==,=,b,<EOF>"