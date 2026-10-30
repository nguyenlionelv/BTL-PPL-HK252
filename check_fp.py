import ast
import sys

def check_strict_fp(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=file_path)
        
    violations = []
    class FPChecker(ast.NodeVisitor):
        def add_error(self, node, msg):
            violations.append(f"Line {getattr(node, 'lineno', '?')}: {msg}")
            
        def visit_For(self, node):
            self.add_error(node, "Found 'for' statement.")
            self.generic_visit(node)
            
        def visit_While(self, node):
            self.add_error(node, "Found 'while' statement.")
            self.generic_visit(node)
            
        def visit_ListComp(self, node):
            self.add_error(node, "Found List Comprehension.")
            self.generic_visit(node)
            
        def visit_SetComp(self, node):
            self.add_error(node, "Found Set Comprehension.")
            self.generic_visit(node)
            
        def visit_DictComp(self, node):
            self.add_error(node, "Found Dict Comprehension.")
            self.generic_visit(node)
            
        def visit_GeneratorExp(self, node):
            self.add_error(node, "Found Generator Expression.")
            self.generic_visit(node)

    FPChecker().visit(tree)
    if violations:
        print("FP Rule Violations Found:")
        for v in violations:
            print(v)
        sys.exit(1)
    else:
        print("No FP strictly forbidden loops/comprehensions found! Excellent!")
        sys.exit(0)

if __name__ == "__main__":
    check_strict_fp(sys.argv[1])
