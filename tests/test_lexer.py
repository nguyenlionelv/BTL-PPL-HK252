"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer
from tests.grammar_config import get_token_name as T, set_grammar


# ============================================================================
# EXAMPLE: Grammar-Agnostic Tests
# ============================================================================

def test_keywords_type_keywords_flexible():
    """Test all type keywords - works with any grammar"""
    sources = ["auto", "int", "float", "string", "void"]
    
    # Build expected results using grammar configuration
    expected = [
        f"{T('keyword_auto')},auto,EOF",
        f"{T('keyword_int')},int,EOF",
        f"{T('keyword_float')},float,EOF",
        f"{T('keyword_string')},string,EOF",
        f"{T('keyword_void')},void,EOF"
    ]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected
def test_keywords_control_flow_flexible():
    """Test control flow keywords - works with any grammar"""
    sources = ["if", "else", "while", "for", "break", "continue", "return"]
    
    expected = [
        f"{T('keyword_if')},if,EOF",
        f"{T('keyword_else')},else,EOF",
        f"{T('keyword_while')},while,EOF",
        f"{T('keyword_for')},for,EOF",
        f"{T('keyword_break')},break,EOF",
        f"{T('keyword_continue')},continue,EOF",
        f"{T('keyword_return')},return,EOF"
    ]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_identifiers_valid_flexible():
    """Test valid identifiers - works with any grammar"""
    sources = ["x", "abc", "test123", "my_var", "_test"]
    
    id_token = T('identifier')
    expected = [
        f"{id_token},x,EOF",
        f"{id_token},abc,EOF",
        f"{id_token},test123,EOF",
        f"{id_token},my_var,EOF",
        f"{id_token},_test,EOF"
    ]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_operators_arithmetic_flexible():
    """Test arithmetic operators - works with any grammar"""
    sources = ["+", "-", "*", "/", "%"]
    
    expected = [
        f"{T('op_plus')},+,EOF",
        f"{T('op_minus')},-,EOF",
        f"{T('op_mul')},*,EOF",
        f"{T('op_div')},/,EOF",
        f"{T('op_mod')},%,EOF"
    ]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected


def test_operators_relational_flexible():
    """Test relational operators - works with any grammar"""
    sources = ["<", ">", "<=", ">=", "==", "!="]
    
    expected = [
        f"{T('op_lt')},<,EOF",
        f"{T('op_gt')},>,EOF",
        f"{T('op_lte')},<=,EOF",
        f"{T('op_gte')},>=,EOF",
        f"{T('op_eq')},==,EOF",
        f"{T('op_neq')},!=,EOF"
    ]
    
    results = [Tokenizer(src).get_tokens_as_string() for src in sources]
    assert results == expected
    
def test_lexer_placeholder():
    """Placeholder test - replace with actual test cases"""
    source = "// This is a placeholder test"
    tokenizer = Tokenizer(source)
    # TODO: Add actual test assertions
    assert True

# TEST KEYWORD (10 valid - 10 invalid)
def test_1():
    sources = ["int",
              "string",
              'auto',
              'break',
              'struct',
              'return',
              'if',
              'while',
              'for',
              'default',]
    result = []
    for source in sources:
        tokenizer = Tokenizer(source)
        result.append(tokenizer.get_tokens_as_string())
    assert result == ["INTEGER,int,EOF", 
                      "STRING,string,EOF", 
                      "AUTO,auto,EOF", 
                      "BREAK,break,EOF",
                      "STRUCT,struct,EOF",
                      "RETURN,return,EOF",
                      "IF,if,EOF",
                      "WHILE,while,EOF",
                      "FOR,for,EOF",
                      "DEFAULT,default,EOF",
                      ]
def test_1_1():
    sources = [
        "INT",
        "String",
        'AUTO',
        'class',
        'strut',
        'elif',
        'then',
        'do',
        'continued',
        'SWITCH',
    ]
    results = []
    for source in sources:
        tokenizer = Tokenizer(source)
        try:
            valid = tokenizer.get_tokens_as_string()
            results.append(valid)
        except Exception as e:
            output = str(e)
            results.append(output)
            print(f"\n'{source}' -> {output}")
    
    assert results == [
        "ID,INT,EOF",
        'ID,String,EOF',
        'ID,AUTO,EOF',
        'ID,class,EOF',
        'ID,strut,EOF',
        'ID,elif,EOF',
        'ID,then,EOF',
        'ID,do,EOF',
        'ID,continued,EOF',
        'ID,SWITCH,EOF',
    ]

# TEST OPERATOR (10 valid - 10 invalid)
def test_2():
    sources = ["==",
              "!=",
              "+",
              "-",
              "*",
              "/",
              "<",
              ">",
              "<=",
              ">=",]
    result = []
    for source in sources:
        tokenizer = Tokenizer(source)
        result.append(tokenizer.get_tokens_as_string())
    assert result == ["EQ,==,EOF", 
                      "NEQ,!=,EOF", 
                      "PLUS,+,EOF", 
                      "MINUS,-,EOF",
                      "MUL,*,EOF",
                      "DIV,/,EOF",
                      "LETH,<,EOF",
                      "GRTH,>,EOF",
                      "LTE,<=,EOF",
                      "GTE,>=,EOF",
                      ]

# TEST IDENTIFIER (10 valid - 10 invalid)
def test_3():
    sources = [
        'helokItTy',
        'a_123',
        'toilaBan',
        'b176534252',
        'sources',
    ]
    result = []
    for source in sources:
        tokenizer = Tokenizer(source)
        result.append(tokenizer.get_tokens_as_string())
    assert result == [
        "ID,helokItTy,EOF",
        "ID,a_123,EOF",
        "ID,toilaBan,EOF",
        "ID,b176534252,EOF",
        "ID,sources,EOF",
    ]

def test_3_1():
    sources = [
        'phomaiQue$2',
    ]
    results = []
    for source in sources:
        tokenizer = Tokenizer(source)
        try:
            valid = tokenizer.get_tokens_as_string()
            results.append(valid)
        except Exception as e:
            output = str(e)
            results.append(output)
            print(f"\n'{source}' -> {output}")
    
    assert results == [
        'Error Token $',
    ]
# TEST LITERAL (15 valid - 15 invalid)
def test_4():
    sources = [
        '123',
        '1234567890',
        '0',
        '100',
        '-45',
        '-1920',
        '-10',
        '123.456',
        '123.456e789',
        '123.456E-789',
        '0.0',
        '-123.456e1',
    ]
    result = []
    for source in sources:
        tokenizer = Tokenizer(source)
        result.append(tokenizer.get_tokens_as_string())
    assert result == [
        "INTLITERAL,123,EOF",
        "INTLITERAL,1234567890,EOF",
        "INTLITERAL,0,EOF",
        "INTLITERAL,100,EOF",
        "MINUS,-,INTLITERAL,45,EOF",
        "MINUS,-,INTLITERAL,1920,EOF",
        "MINUS,-,INTLITERAL,10,EOF",
        "FLOATLITERAL,123.456,EOF",
        "FLOATLITERAL,123.456e789,EOF",
        "FLOATLITERAL,123.456E-789,EOF",
        "FLOATLITERAL,0.0,EOF",
        "MINUS,-,FLOATLITERAL,123.456e1,EOF",
    ]
# TEST SEPARATOR + COMMENT (10)

# TEST ERROR (10)

# TEST ALL (40)
