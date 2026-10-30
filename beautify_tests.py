import re

def beautify_source(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(source = \"\"\")([\s\S]*?)(\s*\"\"\")'

    def replacer(match):
        header = match.group(1)
        code = match.group(2)
        footer = match.group(3)
        
        lines = code.splitlines()
        new_lines = []
        indent_level = 0
        
        # Clean up all leading/trailing whitespace lines
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
            
        for line in lines:
            stripped = line.strip()
            if not stripped:
                new_lines.append("")
                continue
            
            if stripped.startswith('}'):
                indent_level = max(0, indent_level - 1)
            
            new_lines.append(' ' * (8 + indent_level * 4) + stripped)
            
            if stripped.endswith('{'):
                indent_level += 1
            
        final_code = "\n" + "\n".join(new_lines) + "\n"
        return header + final_code + '    ' + footer.strip()

    new_content = re.sub(pattern, replacer, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    beautify_source(r'd:\Users\BuiTrongNguyen\[HK252] PPL\BTL-PPL-HK252\tests\test_checker.py')
    print("Beautified source indentation (strict whitespace cleanup).")
