"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser

def test_parser_024():
    """Function with multiple parameters"""
    parser = Parser("void main() { return x++.y; }")
    assert parser.parse() == "success"


def test_parser_025():
    """Function with struct parameter"""
    parser = Parser("""
        struct Point { int x; int y; };
        int getX(Point p) { return p(1,2).x; }
    """)
    assert parser.parse() == "success"