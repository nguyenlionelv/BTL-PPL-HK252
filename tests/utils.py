"""
Utility functions and classes for testing TyC compiler
"""

import os
import sys

# Add project root and build directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
build_dir = os.path.join(project_root, "build")
sys.path.insert(0, project_root)
sys.path.insert(0, build_dir)

from build.TyCLexer import TyCLexer
from build.TyCParser import TyCParser
from antlr4 import InputStream, CommonTokenStream
from src.utils.error_listener import NewErrorListener


class ASTGenerator:
    """Class to generate AST from TyC source code."""

    def __init__(self, input_string: str):
        self.input_string = input_string
        self.input_stream = InputStream(input_string)
        self.lexer = TyCLexer(self.input_stream)
        self.token_stream = CommonTokenStream(self.lexer)
        self.parser = TyCParser(self.token_stream)
        self.parser.removeErrorListeners()
        self.parser.addErrorListener(NewErrorListener.INSTANCE)
        # Import here to avoid circular dependency issues during build
        try:
            from src.astgen.ast_generation import ASTGeneration

            self.ast_generator = ASTGeneration()
        except ImportError:
            self.ast_generator = None

    def generate(self):
        """Generate AST from the input string."""
        if self.ast_generator is None:
            return "AST Generation Error: ASTGeneration class not found. Please implement src/astgen/ast_generation.py"
        try:
            # Parse the program starting from the entry point
            parse_tree = self.parser.program()

            # Generate AST using the visitor
            ast = self.ast_generator.visit(parse_tree)
            return ast
        except Exception as e:
            return f"AST Generation Error: {str(e)}"


class Tokenizer:
    """Lexer wrapper for testing"""

    def __init__(self, source_code: str):
        self.source_code = source_code

    def get_tokens_as_string(self) -> str:
        """Get tokens as comma-separated string (only token text)"""
        input_stream = InputStream(self.source_code)
        lexer = TyCLexer(input_stream)

        tokens = []
        try:
            while True:
                token = lexer.nextToken()
                if token.type == -1:  # EOF
                    tokens.append("<EOF>")
                    break
                tokens.append(token.text if token.text else "")
        except Exception as e:
            # If we already have some tokens, append error message
            if tokens:
                tokens.append(str(e))
            else:
                # If no tokens yet, just return error message
                return str(e)

        return ",".join(tokens)


class Parser:
    """Parser wrapper for testing"""

    def __init__(self, source_code: str):
        self.source_code = source_code

    def parse(self) -> str:
        """Parse source code and return result"""
        input_stream = InputStream(self.source_code)
        lexer = TyCLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = TyCParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(NewErrorListener.INSTANCE)

        try:
            tree = parser.program()
            return "success"
        except Exception as e:
            return str(e)
