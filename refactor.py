import os

file_path = r'd:\Users\BuiTrongNguyen\[HK252] PPL\BTL-PPL-HK252\src\semantics\static_checker.py'
with open(file_path, 'r', encoding='utf-8') as f:
    code = f.read()

replacements = [
    ('main = [sym for sym in env[0] if sym.name == "main"]', 'main = list(filter(lambda sym: sym.name == "main", env[0]))'),
    ('global_structs = [sym.name for sym in o[0] if sym.kind == "struct"]', 'global_structs = list(map(lambda sym: sym.name, filter(lambda sym: sym.kind == "struct", o[0])))'),
    ('struct_scope = [sym.name for sym in o[0]]', 'struct_scope = list(map(lambda sym: sym.name, o[0]))'),
    ('global_structs = [sym.name for sym in o[-1] if sym.kind == "struct"]', 'global_structs = list(map(lambda sym: sym.name, filter(lambda sym: sym.kind == "struct", o[-1])))'),
    ('global_funcs = [sym.name for sym in o[0] if sym.kind == "func"]', 'global_funcs = list(map(lambda sym: sym.name, filter(lambda sym: sym.kind == "func", o[0])))'),
    ('symbol.params = [sym.type for sym in env[0]]  # store param types', 'symbol.params = list(map(lambda sym: sym.type, env[0]))  # store param types'),
    ('self.current_params = [sym.name for sym in env[0]]', 'self.current_params = list(map(lambda sym: sym.name, env[0]))'),
    ('names_in_scope = [sym.name for sym in o[0]]', 'names_in_scope = list(map(lambda sym: sym.name, o[0]))'),
    ('global_names = [sym.name for sym in o[-1] if sym.kind == "struct"]', 'global_names = list(map(lambda sym: sym.name, filter(lambda sym: sym.kind == "struct", o[-1])))'),
]

for old, new in replacements:
    code = code.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(code)
