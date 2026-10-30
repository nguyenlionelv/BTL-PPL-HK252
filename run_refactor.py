import re
import os

# Results captured from Checker execution
captured_results = {
    66: "TypeMismatchInStatement(IfStmt(if Identifier(x) then BlockStmt([ExprStmt(FuncCall(printInt, [IntLiteral(1)]))])))",
    67: "TypeMismatchInStatement(IfStmt(if Identifier(message) then BlockStmt([ExprStmt(FuncCall(printString, [Identifier(message)]))])))",
    68: "TypeMismatchInStatement(WhileStmt(while Identifier(f) do BlockStmt([ExprStmt(FuncCall(printFloat, [Identifier(f)]))])))",
    69: "TypeMismatchInStatement(AssignExpr(Identifier(x) = Identifier(text)))",
    70: "TypeMismatchInStatement(AssignExpr(Identifier(f) = Identifier(x)))",
    71: "TypeMismatchInStatement(ReturnStmt(return StringLiteral('invalid')))",
    72: "TypeMismatchInStatement(ReturnStmt(return IntLiteral(42)))",
    73: "TypeMismatchInStatement(ReturnStmt(return IntLiteral(10)))",
    74: "TypeMismatchInStatement(ReturnStmt(return))",
    75: "TypeMismatchInStatement(SwitchStmt(switch Identifier(f) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])]))",
    76: "TypeMismatchInStatement(AssignExpr(Identifier(p) = Identifier(person)))",
    77: "TypeMismatchInStatement(AssignExpr(Identifier(text) = Identifier(x)))",
    78: "TypeMismatchInStatement(ForStmt(for VarDecl(auto, i = IntLiteral(0)); Identifier(s); PrefixOp(++Identifier(i)) do BlockStmt([ExprStmt(FuncCall(printInt, [Identifier(i)]))])))",
    79: "TypeMismatchInStatement(ReturnStmt(return StringLiteral('oops')))",
    80: "TypeMismatchInExpression(BinaryOp(Identifier(x), +, Identifier(text)))",
    81: "TypeMismatchInExpression(BinaryOp(Identifier(f), %, Identifier(x)))",
    82: "TypeMismatchInExpression(BinaryOp(Identifier(x), %, Identifier(f)))",
    83: "TypeMismatchInExpression(BinaryOp(Identifier(x), <, Identifier(text)))",
    84: "TypeMismatchInExpression(BinaryOp(Identifier(f), &&, Identifier(x)))",
    85: "TypeMismatchInExpression(PrefixOp(!Identifier(f)))",
    86: "TypeMismatchInExpression(PrefixOp(++Identifier(f)))",
    87: "TypeMismatchInExpression(PostfixOp(Identifier(f)++))",
    88: "TypeMismatchInExpression(MemberAccess(Identifier(x).member))",
    89: "TypeMismatchInExpression(MemberAccess(Identifier(p).z))",
    90: "TypeMismatchInExpression(FuncCall(process, [Identifier(text)]))",
    91: "TypeMismatchInExpression(FuncCall(add, [IntLiteral(10)]))",
    92: "TypeMismatchInExpression(FuncCall(add, [IntLiteral(10), IntLiteral(20), IntLiteral(30)]))",
    93: "TypeMismatchInExpression(StructLiteral({IntLiteral(10), IntLiteral(20), IntLiteral(30)}))",
    94: "TypeMismatchInExpression(StructLiteral({IntLiteral(10), StringLiteral('hello')}))",
    95: "MustInLoop(BreakStmt())",
    96: "MustInLoop(ContinueStmt())",
    97: "MustInLoop(BreakStmt())",
    98: "MustInLoop(ContinueStmt())",
    99: "MustInLoop(ContinueStmt())",
    100: "MustInLoop(BreakStmt())",
}

def refactor_test_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split the file by test functions
    # Using a lookahead to keep the function header as part of the split
    parts = re.split(r'(def test_\d+\(\):)', content)
    
    new_content = [parts[0]] # The import section and header
    
    for i in range(1, len(parts), 2):
        header = parts[i]
        body = parts[i+1]
        
        # Extract test number
        tn_match = re.search(r'test_(\d+)', header)
        if not tn_match:
            new_content.extend([header, body])
            continue
        test_num = int(tn_match.group(1))
        
        # 1. Remove docstring
        # Look for triple quoted string at the start of the body
        body = re.sub(r'^\s*"""[\s\S]*?"""\s*', '\n', body)
        
        # 2. Indent source code
        # Find the source block
        source_match = re.search(r'(source = """)([\s\S]*?)(""")', body)
        if source_match:
            prefix = source_match.group(1)
            code = source_match.group(2)
            suffix = source_match.group(3)
            
            # Clean up leading/trailing newlines in code to standardize
            code_lines = [l for l in code.splitlines() if l.strip()]
            # Indent by 4 spaces
            indented_code = "\n" + "\n".join("    " + l for l in code_lines) + "\n"
            
            body = body.replace(source_match.group(0), f'    source = """{indented_code}    """')

        # 3. Update assertions for 66-100
        if test_num >= 66 and test_num in captured_results:
            # Replace the startswith logic
            # result = Checker(source).check_from_source()
            # assert result.startswith("...")
            
            # Find the assertion block
            assert_pattern = r'result = Checker\(source\)\.check_from_source\(\)\s*assert result\.startswith\(".*?"\)'
            # If not found exactly, maybe it has 'expected' defined already or result on different line
            if not re.search(assert_pattern, body):
               # Handle cases like test_066 where expected is defined
               body = re.sub(r'expected = ".*?"\s*result = Checker\(source\)\.check_from_source\(\)\s*assert result\.startswith\(".*?"\)',
                             f'expected = "{captured_results[test_num]}"\n    assert Checker(source).check_from_source() == expected',
                             body)
               # Handle case where result is already used but expected is NOT defined
               body = re.sub(r'result = Checker\(source\)\.check_from_source\(\)\s*assert result\.startswith\(".*?"\)',
                             f'expected = "{captured_results[test_num]}"\n    assert Checker(source).check_from_source() == expected',
                             body)
            else:
                 body = re.sub(assert_pattern,
                             f'expected = "{captured_results[test_num]}"\n    assert Checker(source).check_from_source() == expected',
                             body)

        new_content.append(header)
        new_content.append(body)

    # Join back and perform final cleanup on indentation
    final_output = "".join(new_content)
    
    # Fix potential double newlines or messy spacing from regex replacements
    final_output = re.sub(r'\n\n\n+', '\n\n', final_output)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_output)

if __name__ == "__main__":
    refactor_test_file(r'd:\Users\BuiTrongNguyen\[HK252] PPL\BTL-PPL-HK252\tests\test_checker.py')
