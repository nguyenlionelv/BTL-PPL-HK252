import re

def fix_indentation(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find source = \"\"\" ... \"\"\"
    # Group 1: header (source = \"\"\")
    # Group 2: code content
    # Group 3: footer (closing \"\"\")
    pattern = r'(source = \"\"\")([\s\S]*?)(\s*\"\"\")'

    def replacer(match):
        header = match.group(1)
        code = match.group(2)
        footer = match.group(3)
        
        lines = code.splitlines()
        new_lines = []
        for line in lines:
            if line.strip():
                # Apply 8 spaces of indentation to the code lines
                new_lines.append('        ' + line.lstrip())
            else:
                new_lines.append(line)
        
        return header + '\n'.join(new_lines) + footer

    new_content = re.sub(pattern, replacer, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    file_path = r'd:\Users\BuiTrongNguyen\[HK252] PPL\BTL-PPL-HK252\tests\test_checker.py'
    fix_indentation(file_path)
    print("Indentation adjusted to 8 spaces.")
