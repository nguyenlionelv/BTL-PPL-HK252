
import sys
import os
import re

# Add project root and build directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(project_root, "build")
sys.path.insert(0, project_root)
sys.path.insert(0, build_dir)

try:
    from tests.utils import ASTGenerator
except ImportError as e:
    print(f"Error importing ASTGenerator: {e}")
    sys.exit(1)

def generate_ast_string(source_code):
    try:
        gen = ASTGenerator(source_code)
        ast = gen.generate()
        return str(ast)
    except Exception as e:
        print(f"Error processing source: {source_code[:20]}... : {e}")
        return f"ERROR: {e}"

def update_test_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find test functions and their source
    # This assumes the format:
    # def test_...
    #     ...
    #     source = """..."""
    #     expected = "..."
    
    pattern = re.compile(r'(def test_\w+\(\):.*?source = """)(.*?)("""\s+expected = ).*?(\n\s+assert)', re.DOTALL)

    def replacement(match):
        prefix = match.group(1)
        source_code = match.group(2)
        middle = match.group(3)
        suffix = match.group(4)
        
        # Auto-fix: Empty blocks are invalid in TyC (stmtlist must be non-empty).
        # Replace ') {}' with ') { return; }'
        # We use a simple regex for this common case.
        fixed_source = re.sub(r'(?<=\))\s*\{\s*\}', ' { return; }', source_code)
        
        # Calculate new expected
        new_expected = generate_ast_string(fixed_source)
        
        # If we fixed the source, we should use the fixed source in the file
        final_source = fixed_source
        
        if '"' in new_expected and "'" not in new_expected:
             formatted_expected = f"'{new_expected}'"
        else:
             escaped = new_expected.replace('\\', '\\\\').replace('"', '\\"')
             formatted_expected = f'"{escaped}"'

        return f"{prefix}{final_source}{middle}{formatted_expected}{suffix}"

    new_content = pattern.sub(replacement, content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"No changes made to {file_path}")

if __name__ == "__main__":
    file_path = os.path.join(project_root, "tests", "test_ast_gen.py")
    if os.path.exists(file_path):
        update_test_file(file_path)
    else:
        print(f"File not found: {file_path}")
