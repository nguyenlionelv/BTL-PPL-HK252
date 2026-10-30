
import pytest
from tests.utils import Tokenizer

def test_float_with_exponent_positive_01():
    """Test 1: Float with positive exponent"""
    tokenizer = Tokenizer("1e4")
    assert tokenizer.get_tokens_as_string() == "1e4,<EOF>"


def test_float_with_exponent_negative_02():
    """Test 2: Float with negative exponent"""
    tokenizer = Tokenizer("2E-3")
    assert tokenizer.get_tokens_as_string() == "2E-3,<EOF>"


def test_float_with_exponent_plus_sign_03():
    """Test 3: Float with explicit plus in exponent"""
    tokenizer = Tokenizer("5E+10")
    assert tokenizer.get_tokens_as_string() == "5E+10,<EOF>"


def test_float_decimal_only_before_04():
    """Test 4: Float with decimal point at end"""
    tokenizer = Tokenizer("42.")
    assert tokenizer.get_tokens_as_string() == "42.,<EOF>"


def test_float_decimal_only_after_05():
    """Test 5: Float with decimal point at start"""
    tokenizer = Tokenizer(".5")
    assert tokenizer.get_tokens_as_string() == ".5,<EOF>"


def test_float_full_format_06():
    """Test 6: Float with all components"""
    tokenizer = Tokenizer("3.14159e-10")
    assert tokenizer.get_tokens_as_string() == "3.14159e-10,<EOF>"


def test_float_in_expression_07():
    """Test 7: Multiple floats in expression"""
    tokenizer = Tokenizer("1.5 + 2.3e4 - .7")
    assert tokenizer.get_tokens_as_string() == "1.5,+,2.3e4,-,.7,<EOF>"


def test_float_zero_formats_08():
    """Test 8: Different zero float formats"""
    tokenizer = Tokenizer("0.0 .0 0.")
    assert tokenizer.get_tokens_as_string() == "0.0,.0,0.,<EOF>"


def test_float_scientific_large_09():
    """Test 9: Large scientific notation"""
    tokenizer = Tokenizer("9.99999E+308")
    assert tokenizer.get_tokens_as_string() == "9.99999E+308,<EOF>"


def test_float_scientific_tiny_10():
    """Test 10: Tiny scientific notation"""
    tokenizer = Tokenizer("1e-100")
    assert tokenizer.get_tokens_as_string() == "1e-100,<EOF>"


# ========== SECTION 2: Integer Edge Cases (5 tests) ==========

def test_integer_zero_11():
    """Test 11: Zero is valid"""
    tokenizer = Tokenizer("0")
    assert tokenizer.get_tokens_as_string() == "0,<EOF>"


def test_integer_large_12():
    """Test 12: Large integer"""
    tokenizer = Tokenizer("02147483647")
    assert tokenizer.get_tokens_as_string() == "2147483647,<EOF>"


def test_integer_sequence_13():
    """Test 13: Multiple integers"""
    tokenizer = Tokenizer("1 22 333 4444")
    assert tokenizer.get_tokens_as_string() == "1,22,333,4444,<EOF>"


def test_integer_no_leading_zero_14():
    """Test 14: Leading zero creates multiple tokens (0 and number)"""
    # "007" should be parsed as "0" and "07" -> but "07" has leading zero
    # Actually based on spec, this should be 0, 0, 7 (three separate tokens)
    tokenizer = Tokenizer("007")
    assert tokenizer.get_tokens_as_string() == "0,0,7,<EOF>"


def test_integer_in_calculation_15():
    """Test 15: Integers in complex math"""
    tokenizer = Tokenizer("100 * 50 / 25 % 3")
    assert tokenizer.get_tokens_as_string() == "100,*,50,/,25,%,3,<EOF>"

# ========== SECTION 3: String Literal Valid Cases (10 tests) ==========

def test_string_empty_16():
    """Test 16: Empty string"""
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"


def test_string_with_spaces_17():
    """Test 17: String with spaces"""
    tokenizer = Tokenizer('"hello world"')
    assert tokenizer.get_tokens_as_string() == "hello world,<EOF>"


def test_string_with_tab_escape_18():
    """Test 18: String with tab escape"""
    tokenizer = Tokenizer('"hello\\tworld"')
    assert tokenizer.get_tokens_as_string() == "hello\\tworld,<EOF>"


def test_string_with_newline_escape_19():
    """Test 19: String with newline escape"""
    tokenizer = Tokenizer('"line1\\nline2"')
    assert tokenizer.get_tokens_as_string() == "line1\\nline2,<EOF>"


def test_string_with_quote_escape_20():
    """Test 20: String with escaped quotes"""
    tokenizer = Tokenizer('"He said \\\"Hello\\\""')
    assert tokenizer.get_tokens_as_string() == 'He said \\\"Hello\\\",<EOF>'


def test_string_with_backslash_escape_21():
    """Test 21: String with escaped backslash"""
    tokenizer = Tokenizer('"C:\\\\path\\\\file"')
    assert tokenizer.get_tokens_as_string() == "C:\\\\path\\\\file,<EOF>"


def test_string_all_escapes_22():
    """Test 22: String with all valid escapes"""
    tokenizer = Tokenizer('"\\b\\f\\r\\n\\t\\\"\\\\"')
    assert tokenizer.get_tokens_as_string() == '\\b\\f\\r\\n\\t\\\"\\\\,<EOF>'


def test_string_multiple_23():
    """Test 23: Multiple strings"""
    tokenizer = Tokenizer('"first" "second" "third"')
    assert tokenizer.get_tokens_as_string() == "first,second,third,<EOF>"


def test_string_in_function_call_24():
    """Test 24: String as function argument"""
    tokenizer = Tokenizer('printString("Hello, World!")')
    assert tokenizer.get_tokens_as_string() == "printString,(,Hello, World!,),<EOF>"


def test_string_concatenated_tokens_25():
    """Test 25: Strings separated by operators"""
    tokenizer = Tokenizer('"str1" + "str2"')
    assert tokenizer.get_tokens_as_string() == "str1,+,str2,<EOF>"

# ========== SECTION 4: ILLEGAL_ESCAPE Error Cases (15 tests) ==========

def test_illegal_escape_x_26():
    """Test 26: Illegal escape \\x"""
    tokenizer = Tokenizer('"hello\\x"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: hello\\x"

def test_illegal_escape_a_27():
    """Test 27: Illegal escape \\a"""
    tokenizer = Tokenizer('"test\\a"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: test\\a"


def test_illegal_escape_v_28():
    """Test 28: Illegal escape \\v"""
    tokenizer = Tokenizer('"\\vvertical"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\v"


def test_illegal_escape_digit_29():
    """Test 29: Illegal escape with digit \\1"""
    tokenizer = Tokenizer('"\\1"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\1"


def test_illegal_escape_space_30():
    """Test 30: Illegal escape with space"""
    tokenizer = Tokenizer('"\\ "')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\ "


def test_illegal_escape_at_start_31():
    """Test 31: Illegal escape at string start"""
    tokenizer = Tokenizer('"\\k"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\k"


def test_illegal_escape_after_valid_content_32():
    """Test 32: Illegal escape after valid text"""
    tokenizer = Tokenizer('"valid text\\z"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: valid text\\z"


def test_illegal_escape_multiple_chars_33():
    """Test 33: First illegal escape detected"""
    tokenizer = Tokenizer('"\\x\\y"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\x"


def test_illegal_escape_after_valid_escape_34():
    """Test 34: Illegal after valid escape"""
    tokenizer = Tokenizer('"\\n\\x"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\n\\x"


def test_illegal_escape_u_35():
    """Test 35: Illegal escape \\u (unicode not supported)"""
    tokenizer = Tokenizer('"\\u0041"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\u"


def test_illegal_escape_zero_36():
    """Test 36: Illegal escape \\0"""
    tokenizer = Tokenizer('"null\\0char"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: null\\0"


def test_illegal_escape_special_char_37():
    """Test 37: Illegal escape with special char \\@"""
    tokenizer = Tokenizer('"email\\@test"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: email\\@"


def test_illegal_escape_question_38():
    """Test 38: Illegal escape \\?"""
    tokenizer = Tokenizer('"what\\?"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: what\\?"


def test_illegal_escape_single_quote_39():
    """Test 39: Illegal escape \\' (only double quote valid)"""
    tokenizer = Tokenizer('"\\\'"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\'"


def test_illegal_escape_slash_40():
    """Test 40: Illegal escape \\/"""
    tokenizer = Tokenizer('"path\\/file"')
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: path\\/"

def test_illegal_escape_slash_401():
    """Test 40: Illegal escape \\/"""
    tokenizer = Tokenizer('"path \\t \t file"')
    assert tokenizer.get_tokens_as_string() == 'path \\t \t file,<EOF>'

# ========== SECTION 5: UNCLOSE_STRING Error Cases (15 tests) ==========

def test_unclose_string_eof_41():
    """Test 41: String not closed at EOF"""
    tokenizer = Tokenizer('"hello')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: hello"


def test_unclose_string_newline_42():
    """Test 42: String not closed before newline"""
    tokenizer = Tokenizer('"hello\n')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: hello"


def test_unclose_string_with_content_43():
    """Test 43: Unclosed string with valid content"""
    tokenizer = Tokenizer('"This is a long string without closing')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: This is a long string without closing"


def test_unclose_string_with_escape_44():
    """Test 44: Unclosed with valid escape"""
    tokenizer = Tokenizer('"text\\n')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: text\\n"


def test_unclose_string_empty_45():
    """Test 45: Unclosed empty string"""
    tokenizer = Tokenizer('"')
    assert tokenizer.get_tokens_as_string() == 'Unclosed String: '


def test_unclose_string_cr_46():
    """Test 46: String not closed before carriage return"""
    tokenizer = Tokenizer('"test\r')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: test"


def test_unclose_string_crlf_47():
    """Test 47: String unclosed before CRLF"""
    tokenizer = Tokenizer('"text\r\n')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: text"


def test_unclose_string_in_code_48():
    """Test 48: Unclosed string in variable assignment"""
    tokenizer = Tokenizer('auto msg = "hello')
    assert tokenizer.get_tokens_as_string() == "auto,msg,=,Unclosed String: hello"


def test_unclose_string_multiple_lines_attempt_49():
    """Test 49: Trying to span multiple lines"""
    tokenizer = Tokenizer('"line1\nline2"')
    assert tokenizer.get_tokens_as_string() == 'Unclosed String: line1'


def test_unclose_string_after_escape_51():
    """Test 51: Unclosed after escape sequence"""
    tokenizer = Tokenizer('"\\t\\n')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: \\t\\n"


def test_unclose_string_with_spaces_53():
    """Test 53: Unclosed string with trailing spaces"""
    tokenizer = Tokenizer('"hello world   ')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: hello world   "


def test_unclose_string_eof_after_escape_54():
    """Test 54: EOF after valid escape"""
    tokenizer = Tokenizer('"test\\\\"')
    # This is actually closed! Should be valid
    assert tokenizer.get_tokens_as_string() == "test\\\\,<EOF>"


def test_unclose_string_newline_in_middle_55():
    """Test 55: Newline appears directly in string"""
    tokenizer = Tokenizer('"before\nafter"')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: before"

# ========== SECTION 6: ERROR_CHAR Cases (10 tests) ==========

def test_error_char_at_sign_56():
    """Test 56: @ is not valid in TyC"""
    tokenizer = Tokenizer("@")
    assert tokenizer.get_tokens_as_string() == "Error Token @"


def test_error_char_hash_57():
    """Test 57: # is not valid (not a comment marker)"""
    tokenizer = Tokenizer("#")
    assert tokenizer.get_tokens_as_string() == "Error Token #"


def test_error_char_dollar_58():
    """Test 58: $ is not valid"""
    tokenizer = Tokenizer("$var")
    assert tokenizer.get_tokens_as_string() == "Error Token $"


def test_error_char_backtick_59():
    """Test 59: Backtick is not valid"""
    tokenizer = Tokenizer("`")
    assert tokenizer.get_tokens_as_string() == "Error Token `"


def test_error_char_tilde_60():
    """Test 60: ~ is not valid"""
    tokenizer = Tokenizer("~")
    assert tokenizer.get_tokens_as_string() == "Error Token ~"


def test_error_char_question_61():
    """Test 61: ? is not valid operator"""
    tokenizer = Tokenizer("a ? b")
    assert tokenizer.get_tokens_as_string() == "a,Error Token ?"


def test_error_char_pipe_62():
    """Test 62: Single pipe (|| is valid, but | alone is not)"""
    tokenizer = Tokenizer("a | b")
    assert tokenizer.get_tokens_as_string() == "a,Error Token |"


def test_error_char_ampersand_63():
    """Test 63: Single ampersand (&& is valid, but & alone is not)"""
    tokenizer = Tokenizer("a & b")
    assert tokenizer.get_tokens_as_string() == "a,Error Token &"


def test_error_char_caret_64():
    """Test 64: ^ is not valid"""
    tokenizer = Tokenizer("2^3")
    assert tokenizer.get_tokens_as_string() == "2,Error Token ^"


def test_error_char_bracket_65():
    """Test 65: Square brackets not valid"""
    tokenizer = Tokenizer("array[0]")
    assert tokenizer.get_tokens_as_string() == "array,Error Token ["


# ========== SECTION 7: Comment Edge Cases (5 tests) ==========

def test_comment_block_multiline_66():
    """Test 66: Block comment spanning lines"""
    tokenizer = Tokenizer("/* line1\nline2\nline3 */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_comment_line_before_code_67():
    """Test 67: Line comment before code"""
    tokenizer = Tokenizer("// comment\nint x")
    assert tokenizer.get_tokens_as_string() == "int,x,<EOF>"


def test_comment_block_with_slashes_68():
    """Test 68: Block comment containing //"""
    tokenizer = Tokenizer("/* // not a line comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_comment_line_with_block_markers_69():
    """Test 69: Line comment containing /* */"""
    tokenizer = Tokenizer("// /* not a block comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_comment_block_empty_70():
    """Test 70: Empty block comment"""
    tokenizer = Tokenizer("/**/")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


# ========== SECTION 8: Operator Combinations (10 tests) ==========

def test_operators_increment_decrement_71():
    """Test 71: Pre and post increment/decrement"""
    tokenizer = Tokenizer("++x-- y++ --z")
    assert tokenizer.get_tokens_as_string() == "++,x,--,y,++,--,z,<EOF>"


def test_operators_logical_72():
    """Test 72: Logical operators"""
    tokenizer = Tokenizer("a && b || !c")
    assert tokenizer.get_tokens_as_string() == "a,&&,b,||,!,c,<EOF>"


def test_operators_comparison_73():
    """Test 73: All comparison operators"""
    tokenizer = Tokenizer("a == b != c < d > e <= f >= g")
    assert tokenizer.get_tokens_as_string() == "a,==,b,!=,c,<,d,>,e,<=,f,>=,g,<EOF>"


def test_operators_arithmetic_all_74():
    """Test 74: All arithmetic operators"""
    tokenizer = Tokenizer("a + b - c * d / e % f")
    assert tokenizer.get_tokens_as_string() == "a,+,b,-,c,*,d,/,e,%,f,<EOF>"


def test_operators_assignment_chain_75():
    """Test 75: Chained assignments"""
    tokenizer = Tokenizer("x = y = z = 0")
    assert tokenizer.get_tokens_as_string() == "x,=,y,=,z,=,0,<EOF>"


def test_operators_member_access_76():
    """Test 76: Chained member access"""
    tokenizer = Tokenizer("obj.member.submember")
    assert tokenizer.get_tokens_as_string() == "obj,.,member,.,submember,<EOF>"


def test_operators_minus_ambiguity_77():
    """Test 77: Minus vs negative number"""
    tokenizer = Tokenizer("5-3")
    assert tokenizer.get_tokens_as_string() == "5,-,3,<EOF>"


def test_operators_plus_ambiguity_78():
    """Test 78: Plus vs positive"""
    tokenizer = Tokenizer("5+3")
    assert tokenizer.get_tokens_as_string() == "5,+,3,<EOF>"


def test_operators_division_79():
    """Test 79: Division not confused with comment"""
    tokenizer = Tokenizer("10/2")
    assert tokenizer.get_tokens_as_string() == "10,/,2,<EOF>"


def test_operators_not_equal_80():
    """Test 80: != as single token"""
    tokenizer = Tokenizer("5!=3")
    assert tokenizer.get_tokens_as_string() == "5,!=,3,<EOF>"


# ========== SECTION 9: Real Program Fragments (10 tests) ==========

def test_program_function_declaration_81():
    """Test 81: Simple function declaration"""
    tokenizer = Tokenizer("int add(int x, int y) {")
    assert tokenizer.get_tokens_as_string() == "int,add,(,int,x,,,int,y,),{,<EOF>"


def test_program_variable_declaration_82():
    """Test 82: Multiple variable declarations"""
    tokenizer = Tokenizer("auto x = 10; float y = 3.14;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,10,;,float,y,=,3.14,;,<EOF>"


def test_program_if_statement_83():
    """Test 83: If statement"""
    tokenizer = Tokenizer("if (x > 0) { return x; }")
    assert tokenizer.get_tokens_as_string() == "if,(,x,>,0,),{,return,x,;,},<EOF>"


def test_program_while_loop_84():
    """Test 84: While loop"""
    tokenizer = Tokenizer("while (i < 10) { i++; }")
    assert tokenizer.get_tokens_as_string() == "while,(,i,<,10,),{,i,++,;,},<EOF>"


def test_program_for_loop_85():
    """Test 85: For loop"""
    tokenizer = Tokenizer("for (auto i = 0; i < 10; ++i)")
    assert tokenizer.get_tokens_as_string() == "for,(,auto,i,=,0,;,i,<,10,;,++,i,),<EOF>"


def test_program_switch_case_86():
    """Test 86: Switch statement"""
    tokenizer = Tokenizer("switch (x) { case 1: break; default: }")
    assert tokenizer.get_tokens_as_string() == "switch,(,x,),{,case,1,:,break,;,default,:,},<EOF>"


def test_program_struct_definition_87():
    """Test 87: Struct definition"""
    tokenizer = Tokenizer("struct Point { int x; int y; };")
    assert tokenizer.get_tokens_as_string() == "struct,Point,{,int,x,;,int,y,;,},;,<EOF>"


def test_program_function_call_88():
    """Test 88: Function call with multiple args"""
    tokenizer = Tokenizer('printString("Value: "); printInt(result);')
    assert tokenizer.get_tokens_as_string() == "printString,(,Value: ,),;,printInt,(,result,),;,<EOF>"


def test_program_expression_complex_89():
    """Test 89: Complex expression"""
    tokenizer = Tokenizer("result = (a + b) * c - d / e % f")
    assert tokenizer.get_tokens_as_string() == "result,=,(,a,+,b,),*,c,-,d,/,e,%,f,<EOF>"


def test_program_array_initializer_like_90():
    """Test 90: Struct initializer (looks like array)"""
    tokenizer = Tokenizer("Point p = {10, 20};")
    assert tokenizer.get_tokens_as_string() == "Point,p,=,{,10,,,20,},;,<EOF>"


# ========== SECTION 10: Whitespace and Edge Cases (10 tests) ==========

def test_whitespace_all_types_91():
    """Test 91: All whitespace types"""
    tokenizer = Tokenizer("a \t\f\r\n b")
    assert tokenizer.get_tokens_as_string() == "a,b,<EOF>"


def test_whitespace_none_92():
    """Test 92: No whitespace between tokens"""
    tokenizer = Tokenizer("int x=5;")
    assert tokenizer.get_tokens_as_string() == "int,x,=,5,;,<EOF>"


def test_whitespace_excessive_93():
    """Test 93: Excessive whitespace"""
    tokenizer = Tokenizer("auto     x     =     10     ;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,10,;,<EOF>"


def test_identifier_with_digits_94():
    """Test 94: Identifier with numbers"""
    tokenizer = Tokenizer("var123 a1b2c3")
    assert tokenizer.get_tokens_as_string() == "var123,a1b2c3,<EOF>"


def test_identifier_with_underscores_95():
    """Test 95: Identifiers with underscores"""
    tokenizer = Tokenizer("_private __special my_var_123")
    assert tokenizer.get_tokens_as_string() == "_private,__special,my_var_123,<EOF>"


def test_keyword_as_part_of_identifier_96():
    """Test 96: Keywords within identifiers"""
    tokenizer = Tokenizer("automat integer_val")
    assert tokenizer.get_tokens_as_string() == "automat,integer_val,<EOF>"


def test_float_vs_member_access_97():
    """Test 97: Float decimal vs member access"""
    tokenizer = Tokenizer("3.14 obj.member")
    assert tokenizer.get_tokens_as_string() == "3.14,obj,.,member,<EOF>"


def test_multiple_dots_98():
    """Test 98: Multiple dots (member access chain)"""
    tokenizer = Tokenizer("a.b.c.d")
    assert tokenizer.get_tokens_as_string() == "a,.,b,.,c,.,d,<EOF>"


def test_string_with_numbers_99():
    """Test 99: String containing numbers"""
    tokenizer = Tokenizer('"Code: 12345"')
    assert tokenizer.get_tokens_as_string() == "Code: 12345,<EOF>"


def test_mixed_everything_100():
    """Test 100: Complex realistic code fragment"""
    tokenizer = Tokenizer('''
        // Calculate factorial
        int factorial(int n) {
            if (n <= 1) return 1;
            return n * factorial(n - 1);
        }
    ''')
    assert tokenizer.get_tokens_as_string() == "int,factorial,(,int,n,),{,if,(,n,<=,1,),return,1,;,return,n,*,factorial,(,n,-,1,),;,},<EOF>"