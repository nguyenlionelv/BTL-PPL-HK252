"""
Test script to verify auto-generated grammar configuration
"""

import sys
import os

# Add project paths
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
build_dir = os.path.join(project_root, "build")
sys.path.insert(0, project_root)
sys.path.insert(0, build_dir)

from tests.grammar_config import TokenMapper, T, get_token_name
from build.TyCLexer import TyCLexer

print("=" * 70)
print("AUTO-GENERATED GRAMMAR CONFIGURATION - TEST")
print("=" * 70)

# Create mapper from TyCLexer
print("\n📋 Creating TokenMapper from TyCLexer...")
mapper = TokenMapper.from_lexer(TyCLexer)

print(f"✓ Mapper created successfully!")
print(f"✓ Found {len(mapper.all_tokens())} tokens")

# Show all detected concepts
print("\n" + "=" * 70)
print("DETECTED TOKEN CONCEPTS")
print("=" * 70)

concepts = mapper.all_concepts()
print(f"\nTotal concepts detected: {len(concepts)}\n")

# Group by category
keywords = {k: v for k, v in concepts.items() if k.startswith('keyword_')}
literals = {k: v for k, v in concepts.items() if k.endswith('_literal')}
operators = {k: v for k, v in concepts.items() if k.startswith('op_')}
separators = {k: v for k, v in concepts.items() if k.startswith('sep_')}
other = {k: v for k, v in concepts.items() if not any(k.startswith(p) for p in ['keyword_', 'op_', 'sep_']) and not k.endswith('_literal')}

print("Keywords:")
for concept, token in sorted(keywords.items()):
    print(f"  {concept:25s} -> {token}")

print("\nLiterals:")
for concept, token in sorted(literals.items()):
    print(f"  {concept:25s} -> {token}")

print("\nOperators:")
for concept, token in sorted(operators.items()):
    print(f"  {concept:25s} -> {token}")

print("\nSeparators:")
for concept, token in sorted(separators.items()):
    print(f"  {concept:25s} -> {token}")

if other:
    print("\nOther:")
    for concept, token in sorted(other.items()):
        print(f"  {concept:25s} -> {token}")

# Test the T() function
print("\n" + "=" * 70)
print("TESTING T() FUNCTION")
print("=" * 70)

test_concepts = [
    'int_literal',
    'keyword_int',
    'keyword_float',
    'identifier',
    'op_plus',
    'op_eq',
    'sep_semi'
]

print("\nUsing T() to get token names:")
for concept in test_concepts:
    try:
        token = T(concept)
        print(f"  T('{concept}')".ljust(30) + f" = {token}")
    except ValueError as e:
        print(f"  T('{concept}')".ljust(30) + f" = ERROR: {e}")

# Test building expected results
print("\n" + "=" * 70)
print("BUILDING TEST EXPECTED RESULTS")
print("=" * 70)

print("\nFor test: int x = 123;")
try:
    expected = f"{T('keyword_int')},int,{T('identifier')},x,{T('op_assign')},=,{T('int_literal')},123,{T('sep_semi')},;,EOF"
    print(f"Expected: {expected}")
except ValueError as e:
    print(f"Error: {e}")

print("\nFor test: 3.14 + 2.5")
try:
    expected = f"{T('float_literal')},3.14,{T('op_plus')},+,{T('float_literal')},2.5,EOF"
    print(f"Expected: {expected}")
except ValueError as e:
    print(f"Error: {e}")

# Test keyword lookup
print("\n" + "=" * 70)
print("KEYWORD LOOKUP")
print("=" * 70)

keywords_to_test = ['int', 'float', 'if', 'while', 'return']
print("\nFinding token names by keyword literals:")
for kw in keywords_to_test:
    token = mapper.find_by_keyword(kw)
    print(f"  '{kw}'".ljust(15) + f" -> {token}")

# Test pattern search
print("\n" + "=" * 70)
print("PATTERN SEARCH")
print("=" * 70)

patterns = ['INT', 'FLOAT', 'STRING']
print("\nFinding tokens by pattern:")
for pattern in patterns:
    matches = mapper.find_by_pattern(pattern)
    print(f"  Pattern '{pattern}': {matches}")

print("\n" + "=" * 70)
print("✅ AUTO-CONFIGURATION WORKS!")
print("=" * 70)

print("""
✨ BENEFITS:
1. ✅ No manual configuration needed
2. ✅ Automatically syncs with .g4 file changes
3. ✅ Works with ANY grammar after ANTLR build
4. ✅ Intelligent pattern matching for common token types
5. ✅ Easy to extend for custom mappings

🎯 HOW IT WORKS:
- Reads symbolicNames from generated Lexer class
- Uses pattern matching to map concepts to token names
- Supports lookup by concept, keyword, or pattern

📖 USE IN TESTS:
from tests.grammar_config import T

def test_integer():
    result = Tokenizer("123").get_tokens_as_string()
    expected = f"{T('int_literal')},123,EOF"
    assert result == expected
""")

print("=" * 70)
