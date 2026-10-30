import re
import sys

def refactor_test_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into lines
    lines = content.splitlines()
    new_lines = []
    
    i = 0
    test_count = 0
    while i < len(lines):
        line = lines[i]
        
        # 1. Standardize test functions
        test_func_match = re.match(r'^def test_checker_(\d+)\(\):', line)
        if not test_func_match:
            test_func_match = re.match(r'^def test_(\d+)\(\):', line)
            
        if test_func_match:
            test_num = int(test_func_match.group(1))
            new_lines.append(line)
            i += 1
            
            # Skip docstrings
            if i < len(lines) and lines[i].strip().startswith('"""'):
                if lines[i].strip().count('"""') == 2:
                    i += 1 # skip single line docstring
                else:
                    i += 1
                    while i < len(lines) and '"""' not in lines[i]:
                        i += 1
                    i += 1 # skip closing docstring line
            
            # Process source block
            source_found = False
            while i < len(lines) and not re.match(r'^\s*def test_', lines[i]) and not re.match(r'^# ====', lines[i]):
                current_line = lines[i]
                
                # Format source string
                source_start = re.match(r'^(\s*)source = """', current_line)
                if source_start:
                    indent = source_start.group(1)
                    new_lines.append(f'{indent}source = """')
                    i += 1
                    source_lines = []
                    while i < len(lines) and '"""' not in lines[i]:
                        # Indent the source code by 4 spaces
                        source_lines.append("    " + lines[i] if lines[i].strip() else lines[i])
                        i += 1
                    
                    # Add indented lines
                    new_lines.extend(source_lines)
                    
                    # Closing triple quotes (aligned with source =)
                    if i < len(lines):
                        new_lines.append(f'{indent}"""')
                        i += 1
                    continue
                
                # Check for startswith assertions in tests >= 66
                if test_num >= 66:
                    # Look for result = ... and assert result.startswith(...)
                    res_match = re.match(r'^(\s*)result = Checker\(source\)\.check_from_source\(\)', current_line)
                    if res_match:
                        indent = res_match.group(1)
                        # Look ahead for startswith
                        next_line = ""
                        if i + 1 < len(lines):
                            next_line = lines[i+1]
                        
                        start_match = re.search(r'assert result\.startswith\("(.*?)"\)', next_line)
                        if start_match:
                            prefix = start_match.group(1)
                            # Check if 'expected' is already defined
                            # Search backwards in new_lines for expected = 
                            expected_found = False
                            for prev_line in reversed(new_lines):
                                if f'{indent}expected = ' in prev_line:
                                    expected_found = True
                                    break
                                if 'def test_' in prev_line:
                                    break
                            
                            if expected_found:
                                # Just change the assertion
                                new_lines.append(f'{indent}assert Checker(source).check_from_source() == expected')
                            else:
                                # We need an expected string. For now we use the prefix if we don't have better.
                                # But we should probably find the actual expected string if possible.
                                # For this task, I'll assume they want the one that was there or standard format.
                                new_lines.append(f'{indent}expected = "{prefix}(...)"')
                                new_lines.append(f'{indent}assert Checker(source).check_from_source() == expected')
                            
                            i += 2 # skip result line and assert line
                            continue
                
                new_lines.append(current_line)
                i += 1
            continue
        
        new_lines.append(line)
        i += 1
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))

if __name__ == "__main__":
    refactor_test_file(sys.argv[1])
