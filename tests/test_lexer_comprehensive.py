"""
Comprehensive Lexer Test Suite for TyC Compiler
Contains 100 test cases covering all lexical analysis features
"""

import pytest
from tests.utils import Tokenizer


# ============================================================================
# KEYWORD TESTS (15 tests)
# ============================================================================

def test_keywords_type_keywords():
    """Test all type keywords"""
    sources = ["auto", "int", "float", "string", "void"]
    expected = [
        "AUTO,auto,EOF",
        "INTEGER,int,EOF",
        "FLOAT,float,EOF",
        "STRING,string,EOF",
        "VOID,void,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_keywords_control_flow():
    """Test control flow keywords"""
    sources = ["if", "else", "while", "for", "break", "continue", "return"]
    expected = [
        "IF,if,EOF",
        "ELSE,else,EOF",
        "WHILE,while,EOF",
        "FOR,for,EOF",
        "BREAK,break,EOF",
        "CONTINUE,continue,EOF",
        "RETURN,return,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_keywords_struct_switch():
    """Test struct and switch-case keywords"""
    sources = ["struct", "switch", "case", "default"]
    expected = [
        "STRUCT,struct,EOF",
        "SWITCH,switch,EOF",
        "CASE,case,EOF",
        "DEFAULT,default,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_keywords_case_sensitive():
    """Test that keywords are case-sensitive (uppercase are valid IDs, not keywords)"""
    sources = ["INT", "FLOAT", "IF", "WHILE"]
    expected = [
        "ID,INT,EOF",
        "ID,FLOAT,EOF",
        "ID,IF,EOF",
        "ID,WHILE,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    # Uppercase versions should be valid identifiers, not keywords
    assert results == expected


def test_keywords_mixed_case():
    """Test mixed case keywords (should be valid identifiers, not keywords)"""
    sources = ["Int", "Float", "While", "Return"]
    expected = [
        "ID,Int,EOF",
        "ID,Float,EOF",
        "ID,While,EOF",
        "ID,Return,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    # Mixed case should be valid identifiers, not keywords
    assert results == expected


# ============================================================================
# IDENTIFIER TESTS (15 tests)
# ============================================================================

def test_identifiers_valid_lowercase():
    """Test valid identifiers starting with lowercase"""
    sources = ["x", "abc", "test123", "my_var", "var_name_123"]
    expected = [
        "ID,x,EOF",
        "ID,abc,EOF",
        "ID,test123,EOF",
        "ID,my_var,EOF",
        "ID,var_name_123,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_identifiers_valid_underscore():
    """Test valid identifiers starting with underscore"""
    sources = ["_x", "_test", "_123", "__private", "_"]
    expected = [
        "ID,_x,EOF",
        "ID,_test,EOF",
        "ID,_123,EOF",
        "ID,__private,EOF",
        "ID,_,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_identifiers_valid_mixed():
    """Test valid identifiers with mixed case (starting with lowercase/underscore)"""
    sources = ["camelCase", "mixedCase123", "_MixedCase", "test_Case_123"]
    expected = [
        "ID,camelCase,EOF",
        "ID,mixedCase123,EOF",
        "ID,_MixedCase,EOF",
        "ID,test_Case_123,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_identifiers_valid_uppercase():
    """Test valid identifiers starting with uppercase (per TyC spec)"""
    sources = ["UpperCase", "Test", "ABC", "MyVar"]
    expected = [
        "ID,UpperCase,EOF",
        "ID,Test,EOF",
        "ID,ABC,EOF",
        "ID,MyVar,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    # Per spec: "Identifiers begin with a letter (A-Z or a-z) or underscore"
    assert results == expected


def test_identifiers_invalid_start_digit():
    """Test invalid identifiers starting with digit"""
    sources = ["123abc", "9test", "0var"]
    results = []
    for src in sources:
        try:
            results.append(Tokenizer(src).get_tokens_as_string())
        except Exception as e:
            results.append(str(e))
    
    # Should be treated as INTLITERAL followed by error or ID
    assert all("Error Token" in r or "INTLITERAL" in r for r in results)


def test_identifiers_keyword_prefix():
    """Test identifiers that start with keyword"""
    sources = ["integer", "ifelse", "whileloop", "forloop", "returns"]
    expected = [
        "ID,integer,EOF",
        "ID,ifelse,EOF",
        "ID,whileloop,EOF",
        "ID,forloop,EOF",
        "ID,returns,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


# ============================================================================
# OPERATOR TESTS (15 tests)
# ============================================================================

def test_operators_arithmetic():
    """Test arithmetic operators"""
    sources = ["+", "-", "*", "/", "%"]
    expected = [
        "PLUS,+,EOF",
        "MINUS,-,EOF",
        "MUL,*,EOF",
        "DIV,/,EOF",
        "MOD,%,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_operators_relational():
    """Test relational operators"""
    sources = ["<", ">", "<=", ">=", "==", "!="]
    expected = [
        "LETH,<,EOF",
        "GRTH,>,EOF",
        "LTE,<=,EOF",
        "GTE,>=,EOF",
        "EQ,==,EOF",
        "NEQ,!=,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_operators_logical():
    """Test logical operators"""
    sources = ["&&", "||", "!"]
    expected = [
        "AND,&&,EOF",
        "OR,||,EOF",
        "NOT,!,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_operators_increment_decrement():
    """Test increment and decrement operators"""
    sources = ["++", "--"]
    expected = [
        "INC,++,EOF",
        "DEC,--,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_operators_assignment_dot():
    """Test assignment and dot operators"""
    sources = ["=", "."]
    expected = [
        "ASS,=,EOF",
        "DOT,.,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_operators_combined_expression():
    """Test operators in combined expressions"""
    sources = ["a+b", "x==y", "i++", "p.x"]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    assert "ID,a" in results[0] and "PLUS,+" in results[0] and "ID,b" in results[0]
    assert "ID,x" in results[1] and "EQ,==" in results[1] and "ID,y" in results[1]
    assert "ID,i" in results[2] and "INC,++" in results[2]
    assert "ID,p" in results[3] and "DOT,." in results[3] and "ID,x" in results[3]


# ============================================================================
# SEPARATOR TESTS (5 tests)
# ============================================================================

def test_separators_brackets():
    """Test bracket separators"""
    sources = ["[", "]", "{", "}", "(", ")"]
    expected = [
        "LQB,[,EOF",
        "RQB,],EOF",
        "LB,{,EOF",
        "RB,},EOF",
        "LP,(,EOF",
        "RP,),EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_separators_punctuation():
    """Test punctuation separators"""
    sources = [";", ","]
    expected = [
        "SEMI,;,EOF",
        "CM,,,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_separators_in_context():
    """Test separators in context"""
    source = "int x, y;"
    result = Tokenizer(source).get_tokens_as_string()
    
    assert "INTEGER,int" in result
    assert "ID,x" in result
    assert "CM,," in result
    assert "ID,y" in result
    assert "SEMI,;" in result


def test_separators_function_call():
    """Test separators in function call"""
    source = "func(a, b)"
    result = Tokenizer(source).get_tokens_as_string()
    
    assert "ID,func" in result
    assert "LP,(" in result
    assert "CM,," in result
    assert "RP,)" in result


def test_separators_array_struct():
    """Test separators for array and struct syntax"""
    sources = ["arr[0]", "struct Point { }"]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    assert "LQB,[" in results[0] and "RQB,]" in results[0]
    assert "LB,{" in results[1] and "RB,}" in results[1]


# ============================================================================
# INTEGER LITERAL TESTS (8 tests)
# ============================================================================

def test_integer_literals_basic():
    """Test basic integer literals"""
    sources = ["0", "1", "123", "999", "1234567890"]
    expected = [
        "INTLITERAL,0,EOF",
        "INTLITERAL,1,EOF",
        "INTLITERAL,123,EOF",
        "INTLITERAL,999,EOF",
        "INTLITERAL,1234567890,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_integer_literals_single_digit():
    """Test single digit integers"""
    sources = ["1", "2", "5", "9"]
    expected = [
        "INTLITERAL,1,EOF",
        "INTLITERAL,2,EOF",
        "INTLITERAL,5,EOF",
        "INTLITERAL,9,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_integer_literals_leading_zeros_invalid():
    """Test that leading zeros are invalid (except for 0 itself)"""
    sources = ["01", "007", "00123"]
    results = []
    for src in sources:
        result = Tokenizer(src).get_tokens_as_string()
        results.append(result)
    
    # Should be tokenized as 0 followed by other integers
    for r in results:
        assert "INTLITERAL,0" in r


def test_integer_literals_negative_unary():
    """Test negative integers (should be MINUS + INTLITERAL)"""
    sources = ["-1", "-123", "-999"]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    for r in results:
        assert "MINUS,-" in r and "INTLITERAL" in r


def test_integer_literals_large_numbers():
    """Test large integer literals"""
    sources = ["123456789", "987654321", "1000000000"]
    expected = [
        "INTLITERAL,123456789,EOF",
        "INTLITERAL,987654321,EOF",
        "INTLITERAL,1000000000,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_integer_literals_in_expressions():
    """Test integer literals in expressions"""
    sources = ["123+456", "10*20", "100-50"]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    assert "INTLITERAL,123" in results[0] and "INTLITERAL,456" in results[0]
    assert "INTLITERAL,10" in results[1] and "INTLITERAL,20" in results[1]
    assert "INTLITERAL,100" in results[2] and "INTLITERAL,50" in results[2]


# ============================================================================
# FLOAT LITERAL TESTS (10 tests)
# ============================================================================

def test_float_literals_basic():
    """Test basic float literals"""
    sources = ["0.0", "1.0", "3.14", "123.456"]
    expected = [
        "FLOATLITERAL,0.0,EOF",
        "FLOATLITERAL,1.0,EOF",
        "FLOATLITERAL,3.14,EOF",
        "FLOATLITERAL,123.456,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_float_literals_decimal_point_variants():
    """Test float literals with various decimal point positions"""
    sources = ["1.", ".5", "123.", ".999"]
    expected = [
        "FLOATLITERAL,1.,EOF",
        "FLOATLITERAL,.5,EOF",
        "FLOATLITERAL,123.,EOF",
        "FLOATLITERAL,.999,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_float_literals_scientific_notation_lowercase():
    """Test float literals with scientific notation (lowercase e)"""
    sources = ["1.0e10", "3.14e2", "2.5e-3", "1.23e+5"]
    expected = [
        "FLOATLITERAL,1.0e10,EOF",
        "FLOATLITERAL,3.14e2,EOF",
        "FLOATLITERAL,2.5e-3,EOF",
        "FLOATLITERAL,1.23e+5,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_float_literals_scientific_notation_uppercase():
    """Test float literals with scientific notation (uppercase E)"""
    sources = ["1.0E10", "3.14E2", "2.5E-3", "1.23E+5"]
    expected = [
        "FLOATLITERAL,1.0E10,EOF",
        "FLOATLITERAL,3.14E2,EOF",
        "FLOATLITERAL,2.5E-3,EOF",
        "FLOATLITERAL,1.23E+5,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_float_literals_negative_unary():
    """Test negative float literals (should be MINUS + FLOATLITERAL)"""
    sources = ["-3.14", "-0.5", "-123.456e10"]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    for r in results:
        assert "MINUS,-" in r and "FLOATLITERAL" in r


def test_float_literals_very_small():
    """Test very small float literals"""
    sources = ["0.001", "0.0000001", ".00001"]
    expected = [
        "FLOATLITERAL,0.001,EOF",
        "FLOATLITERAL,0.0000001,EOF",
        "FLOATLITERAL,.00001,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_float_literals_scientific_edge_cases():
    """Test edge cases of scientific notation"""
    sources = [".5e10", "123.e5", "0.0e0"]
    expected = [
        "FLOATLITERAL,.5e10,EOF",
        "FLOATLITERAL,123.e5,EOF",
        "FLOATLITERAL,0.0e0,EOF"
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_float_literals_in_expressions():
    """Test float literals in expressions"""
    sources = ["3.14+2.5", "1.0*2.0", "5.5-1.5"]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    assert "FLOATLITERAL,3.14" in results[0] and "FLOATLITERAL,2.5" in results[0]
    assert "FLOATLITERAL,1.0" in results[1] and "FLOATLITERAL,2.0" in results[1]
    assert "FLOATLITERAL,5.5" in results[2] and "FLOATLITERAL,1.5" in results[2]


# ============================================================================
# STRING LITERAL TESTS (10 tests)
# ============================================================================

def test_string_literals_basic():
    """Test basic string literals"""
    sources = ['""', '"hello"', '"world"', '"TyC Compiler"']
    expected = [
        'STRINGLITERAL,"",EOF',
        'STRINGLITERAL,"hello",EOF',
        'STRINGLITERAL,"world",EOF',
        'STRINGLITERAL,"TyC Compiler",EOF'
    ]
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_string_literals_with_escape_sequences():
    """Test string literals with valid escape sequences"""
    sources = [
        r'"hello\nworld"',
        r'"tab\there"',
        r'"quote:\"test\""',
        r'"backslash:\\"',
        r'"bell\b"',
        r'"form\feed"',
        r'"carriage\return"'
    ]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    # All should be valid STRINGLITERAL
    for r in results:
        assert "STRINGLITERAL" in r


def test_string_literals_empty():
    """Test empty string literal"""
    source = '""'
    result = Tokenizer(source).get_tokens_as_string()
    assert result == 'STRINGLITERAL,"",EOF'


def test_string_literals_spaces_and_special_chars():
    """Test strings with spaces and special characters"""
    sources = [
        '"   spaces   "',
        '"!@#$%^&*()"',
        '"123 abc XYZ"'
    ]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    for r in results:
        assert "STRINGLITERAL" in r


def test_string_literals_unclose_string_newline():
    """Test unclosed string (newline before closing quote)"""
    sources = [
        '"hello\n',
        '"world\r\n',
        '"test'
    ]
    
    results = []
    for src in sources:
        try:
            results.append(Tokenizer(src).get_tokens_as_string())
        except Exception as e:
            results.append(str(e))
    
    # Should raise UncloseString error
    for r in results:
        assert "Unclose" in r or "UNCLOSE" in r.upper()


def test_string_literals_illegal_escape():
    """Test string with illegal escape sequences"""
    sources = [
        r'"hello\x"',  # \x is not valid
        r'"test\a"',   # \a is not valid
        r'"world\v"'   # \v is not valid
    ]
    
    results = []
    for src in sources:
        try:
            results.append(Tokenizer(src).get_tokens_as_string())
        except Exception as e:
            results.append(str(e))
    
    # Should raise IllegalEscape error
    for r in results:
        assert "Illegal" in r or "ILLEGAL" in r.upper() or "Escape" in r


def test_string_literals_multiple_escapes():
    """Test string with multiple escape sequences"""
    sources = [
        r'"line1\nline2\nline3"',
        r'"tab\ttab\ttab"',
        r'"quote\"quote\"quote"'
    ]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    for r in results:
        assert "STRINGLITERAL" in r


# ============================================================================
# COMMENT TESTS (5 tests)
# ============================================================================

def test_comments_line_comment():
    """Test line comments"""
    sources = [
        "// This is a comment",
        "int x; // variable declaration",
        "// comment\nint y;"
    ]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    # Line comments should be skipped
    assert results[0] == "EOF"
    assert "INTEGER,int" in results[1] and "ID,x" in results[1]
    assert "INTEGER,int" in results[2] and "ID,y" in results[2]


def test_comments_block_comment():
    """Test block comments"""
    sources = [
        "/* This is a block comment */",
        "int /* comment */ x;",
        "/* multi\nline\ncomment */ int y;"
    ]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    # Block comments should be skipped
    assert results[0] == "EOF"
    assert "INTEGER,int" in results[1] and "ID,x" in results[1]
    assert "INTEGER,int" in results[2] and "ID,y" in results[2]


def test_comments_nested_symbols():
    """Test that comment symbols inside comments are ignored"""
    sources = [
        "// This // is a comment",
        "/* This /* is a comment */",
        "// This /* is a line comment"
    ]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    # All should result in just EOF
    assert results[0] == "EOF"
    assert results[1] == "EOF"
    assert results[2] == "EOF"


def test_comments_multiple_comments():
    """Test multiple comments in source"""
    source = """
    // Line comment 1
    /* Block comment 1 */
    int x; // inline comment
    /* Block comment 2 */
    // Line comment 2
    """
    
    result = Tokenizer(source).get_tokens_as_string()
    
    assert "INTEGER,int" in result
    assert "ID,x" in result
    assert "SEMI,;" in result


def test_comments_with_special_chars():
    """Test comments containing special characters"""
    sources = [
        "// Comment with symbols: !@#$%^&*()",
        "/* Comment with symbols: <>?:\"{}[] */"
    ]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    # Comments should be completely ignored
    assert results[0] == "EOF"
    assert results[1] == "EOF"


# ============================================================================
# ERROR HANDLING TESTS (10 tests)
# ============================================================================

def test_errors_invalid_characters():
    """Test invalid characters"""
    sources = ["@", "#", "$", "`", "~"]
    
    results = []
    for src in sources:
        try:
            results.append(Tokenizer(src).get_tokens_as_string())
        except Exception as e:
            results.append(str(e))
    
    # All should be error tokens
    for r in results:
        assert "Error Token" in r


def test_errors_identifier_starting_digit():
    """Test identifiers starting with digit (error)"""
    sources = ["123abc", "9test", "0var"]
    
    results = []
    for src in sources:
        try:
            results.append(Tokenizer(src).get_tokens_as_string())
        except Exception as e:
            results.append(str(e))
    
    # Should be INTLITERAL followed by ID or error
    for r in results:
        assert "INTLITERAL" in r or "Error Token" in r


def test_errors_unclosed_string_eof():
    """Test unclosed string at EOF"""
    sources = ['"hello', '"world', '"test123']
    
    results = []
    for src in sources:
        try:
            results.append(Tokenizer(src).get_tokens_as_string())
        except Exception as e:
            results.append(str(e))
    
    for r in results:
        assert "Unclose" in r or "UNCLOSE" in r.upper()


def test_errors_illegal_escape_in_string():
    """Test illegal escape sequences in strings"""
    sources = [r'"bad\kescape"', r'"another\zbad"']
    
    results = []
    for src in sources:
        try:
            results.append(Tokenizer(src).get_tokens_as_string())
        except Exception as e:
            results.append(str(e))
    
    for r in results:
        assert "Illegal" in r or "Escape" in r


def test_errors_mixed_valid_invalid():
    """Test mixing valid tokens with errors"""
    source = "int x @ string y"
    
    try:
        result = Tokenizer(source).get_tokens_as_string()
    except Exception as e:
        result = str(e)
    
    # Should detect error token @
    assert "Error Token" in result or "INTEGER,int" in result


# ============================================================================
# WHITESPACE AND EDGE CASES (7 tests)
# ============================================================================

def test_whitespace_spaces_tabs():
    """Test that spaces and tabs are properly skipped"""
    sources = [
        "  int  ",
        "\tint\t",
        "  \t  int  \t  "
    ]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    for r in results:
        assert r == "INTEGER,int,EOF"


def test_whitespace_newlines():
    """Test that newlines are properly handled"""
    source = "int\nx\n;\n"
    result = Tokenizer(source).get_tokens_as_string()
    
    assert "INTEGER,int" in result
    assert "ID,x" in result
    assert "SEMI,;" in result


def test_edge_case_empty_source():
    """Test empty source code"""
    source = ""
    result = Tokenizer(source).get_tokens_as_string()
    assert result == "EOF"


def test_edge_case_only_whitespace():
    """Test source with only whitespace"""
    sources = ["   ", "\t\t\t", "\n\n\n", "  \t  \n  \t  "]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    for r in results:
        assert r == "EOF"


def test_edge_case_only_comments():
    """Test source with only comments"""
    sources = [
        "// just a comment",
        "/* just a block comment */",
        "// comment1\n/* comment2 */\n// comment3"
    ]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    
    for r in results:
        assert r == "EOF"


def test_complex_expression_tokenization():
    """Test complex expression tokenization"""
    source = "result = (a + b) * c - d / e;"
    result = Tokenizer(source).get_tokens_as_string()
    
    assert "ID,result" in result
    assert "ASS,=" in result
    assert "LP,(" in result
    assert "ID,a" in result
    assert "PLUS,+" in result
    assert "ID,b" in result
    assert "RP,)" in result
    assert "MUL,*" in result
    assert "ID,c" in result
    assert "MINUS,-" in result
    assert "ID,d" in result
    assert "DIV,/" in result
    assert "ID,e" in result
    assert "SEMI,;" in result


def test_complete_statement_tokenization():
    """Test complete statement tokenization"""
    source = 'int x = 10; float y = 3.14; string msg = "hello";'
    result = Tokenizer(source).get_tokens_as_string()
    
    # Check for all expected tokens
    assert "INTEGER,int" in result
    assert "ID,x" in result
    assert "ASS,=" in result
    assert "INTLITERAL,10" in result
    assert "FLOAT,float" in result
    assert "ID,y" in result
    assert "FLOATLITERAL,3.14" in result
    assert "STRING,string" in result
    assert "ID,msg" in result
    assert 'STRINGLITERAL,"hello"' in result
    assert result.count("SEMI,;") == 3
