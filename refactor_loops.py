import os

file_path = r'd:\Users\BuiTrongNguyen\[HK252] PPL\BTL-PPL-HK252\src\semantics\static_checker.py'
with open(file_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Lines 261-274
block_old = '''        env = [[]] + o
        for stmt in node.statements:
            env = self.visit(stmt, env)

        # Check any auto variables that were never resolved
        for sym in env[0]:
            if sym.kind == "var":
                resolved = resolve_type(sym.type)
                if isinstance(resolved, AutoType):
                    # Find the matching VarDecl node from the statement list
                    for stmt in node.statements:
                        if isinstance(stmt, VarDecl) and stmt.name == sym.name and stmt.var_type is None:
                            raise TypeCannotBeInferred(node)
                    raise TypeCannotBeInferred(node)'''

block_new = '''        env = reduce(lambda acc, stmt: self.visit(stmt, acc), node.statements, [[]] + o)

        def check_auto(sym):
            if sym.kind == "var" and isinstance(resolve_type(sym.type), AutoType):
                raise TypeCannotBeInferred(node)
        list(map(check_auto, env[0]))'''
code = code.replace(block_old, block_new)

# Lines 414-415
switch_old = '''        self.switch_stack += 1
        for case in node.cases:
            self.visit(case, o)'''
switch_new = '''        self.switch_stack += 1
        list(map(lambda case: self.visit(case, o), node.cases))'''
code = code.replace(switch_old, switch_new)

# case default old
case_old = '''        # Create a local scope for variables declared inside this case body
        env = [[]] + o
        for stmt in node.statements:
            env = self.visit(stmt, env)

        # Check any auto variables in the case scope that were never resolved
        for sym in env[0]:
            if sym.kind == "var":
                resolved = resolve_type(sym.type)
                if isinstance(resolved, AutoType):
                    raise TypeCannotBeInferred(node)'''
case_new = '''        # Create a local scope for variables declared inside this case body
        env = reduce(lambda acc, stmt: self.visit(stmt, acc), node.statements, [[]] + o)

        def check_case_unresolved(sym):
            if sym.kind == "var" and isinstance(resolve_type(sym.type), AutoType):
                raise TypeCannotBeInferred(node)
        list(map(check_case_unresolved, env[0]))'''
code = code.replace(case_old, case_new)

default_old = '''        # Create a local scope for variables declared inside this default body
        env = [[]] + o
        for stmt in node.statements:
            env = self.visit(stmt, env)

        # Check any auto variables in the default scope that were never resolved
        for sym in env[0]:
            if sym.kind == "var":
                resolved = resolve_type(sym.type)
                if isinstance(resolved, AutoType):
                    raise TypeCannotBeInferred(node)'''
default_new = '''        # Create a local scope for variables declared inside this default body
        env = reduce(lambda acc, stmt: self.visit(stmt, acc), node.statements, [[]] + o)

        def check_default_unresolved(sym):
            if sym.kind == "var" and isinstance(resolve_type(sym.type), AutoType):
                raise TypeCannotBeInferred(node)
        list(map(check_default_unresolved, env[0]))'''
code = code.replace(default_old, default_new)

help_old = '''    def help(self, name, typ, env):
        """Update AutoType for a variable in the environment."""
        for scope in env:
            for sym in scope:
                if sym.name == name and sym.kind in ["var", "param"]:
                    actual_type = resolve_type(sym.type)
                    if isinstance(actual_type, AutoType):
                        actual_type.resolved_type = typ
                        return typ
                    return actual_type
        return None'''
help_new = '''    def help(self, name, typ, env):
        """Update AutoType for a variable in the environment."""
        flat_syms = reduce(lambda acc, scope: acc + scope, env, [])
        matches = list(filter(lambda sym: sym.name == name and sym.kind in ["var", "param"], flat_syms))
        if matches:
            actual_type = resolve_type(matches[0].type)
            if isinstance(actual_type, AutoType):
                actual_type.resolved_type = typ
                return typ
            return actual_type
        return None'''
code = code.replace(help_old, help_new)

assign_old = '''            found_sym = None
            if isinstance(node.lhs, Identifier):
                for scope in o:
                    for sym in scope:
                        if sym.name == node.lhs.name and sym.kind in ["var", "param"]:
                            found_sym = sym
                            break
                    if found_sym:
                        break'''
assign_new = '''            found_sym = None
            if isinstance(node.lhs, Identifier):
                flat_syms = reduce(lambda acc, scope: acc + scope, o, [])
                matches = list(filter(lambda sym: sym.name == node.lhs.name and sym.kind in ["var", "param"], flat_syms))
                if matches:
                    found_sym = matches[0]'''
code = code.replace(assign_old, assign_new)

mem1_old = '''        struct_sym = None
        for scope in o:
            for sym in scope:
                if sym.kind == "struct" and sym.name == obj_ty.struct_name:
                    struct_sym = sym
                    break
            if struct_sym:
                break'''
mem1_new = '''        struct_sym = None
        flat_syms = reduce(lambda acc, scope: acc + scope, o, [])
        matches = list(filter(lambda sym: sym.kind == "struct" and sym.name == obj_ty.struct_name, flat_syms))
        if matches:
            struct_sym = matches[0]'''
code = code.replace(mem1_old, mem1_new)

mem2_old = '''        # Find the member
        for mem in struct_sym.members:
            if mem.name == node.member:
                return mem.type'''
mem2_new = '''        # Find the member
        mem_matches = list(filter(lambda mem: mem.name == node.member, struct_sym.members))
        if mem_matches:
            return mem_matches[0].type'''
code = code.replace(mem2_old, mem2_new)

func1_old = '''        # Find the function symbol
        func_sym = None
        for scope in o:
            for sym in scope:
                if sym.name == node.name and sym.kind == "func":
                    func_sym = sym
                    break
            if func_sym:
                break'''
func1_new = '''        # Find the function symbol
        func_sym = None
        flat_syms = reduce(lambda acc, scope: acc + scope, o, [])
        matches = list(filter(lambda sym: sym.name == node.name and sym.kind == "func", flat_syms))
        if matches:
            func_sym = matches[0]'''
code = code.replace(func1_old, func1_new)

func2_old = '''        # Check argument types
        for i, (arg, param_type) in enumerate(zip(node.args, func_sym.params)):
            # If arg is a struct literal, tell it what type to expect
            if isinstance(arg, StructLiteral) and isinstance(param_type, StructType):
                self._struct_literal_expected = param_type
            
            arg_ty = self.visit(arg, o)
            arg_ty = resolve_type(arg_ty)

            # If arg is auto and param_type is concrete, assign the param type
            if isinstance(arg_ty, AutoType) and not isinstance(param_type, AutoType):
                arg_ty_obj = self.visit(arg, o)
                arg_ty_obj = resolve_type(arg_ty_obj)
                if isinstance(arg_ty_obj, AutoType):
                    arg_ty_obj.resolved_type = param_type
                arg_ty = param_type

            if isinstance(arg_ty, AutoType):
                raise TypeCannotBeInferred(node)  # cannot infer arg type

            if not type_equivalent(arg_ty, param_type):
                raise TypeMismatchInExpression(node)'''
func2_new = '''        # Check argument types
        def check_arg(arg_tuple):
            arg, param_type = arg_tuple
            if isinstance(arg, StructLiteral) and isinstance(param_type, StructType):
                self._struct_literal_expected = param_type
            
            arg_ty = self.visit(arg, o)
            arg_ty = resolve_type(arg_ty)

            if isinstance(arg_ty, AutoType) and not isinstance(param_type, AutoType):
                arg_ty_obj = self.visit(arg, o)
                arg_ty_obj = resolve_type(arg_ty_obj)
                if isinstance(arg_ty_obj, AutoType):
                    arg_ty_obj.resolved_type = param_type
                arg_ty = param_type

            if isinstance(arg_ty, AutoType):
                raise TypeCannotBeInferred(node)

            if not type_equivalent(arg_ty, param_type):
                raise TypeMismatchInExpression(node)
        list(map(check_arg, zip(node.args, func_sym.params)))'''
code = code.replace(func2_old, func2_new)

id_old = '''        found_sym = None
        for scope in o:
            for sym in scope:
                if sym.name == node.name and sym.kind in ["var", "param", "func"]:
                    found_sym = sym
                    break
            if found_sym:
                break'''
id_new = '''        found_sym = None
        flat_syms = reduce(lambda acc, scope: acc + scope, o, [])
        matches = list(filter(lambda sym: sym.name == node.name and sym.kind in ["var", "param", "func"], flat_syms))
        if matches:
            found_sym = matches[0]'''
code = code.replace(id_old, id_new)

structliteral1_old = '''        # Find the struct declaration
        struct_sym = None
        for scope in o:
            for sym in scope:
                if sym.kind == "struct" and sym.name == expected.struct_name:
                    struct_sym = sym
                    break
            if struct_sym:
                break'''
structliteral1_new = '''        # Find the struct declaration
        struct_sym = None
        flat_syms = reduce(lambda acc, scope: acc + scope, o, [])
        matches = list(filter(lambda sym: sym.kind == "struct" and sym.name == expected.struct_name, flat_syms))
        if matches:
            struct_sym = matches[0]'''
code = code.replace(structliteral1_old, structliteral1_new)

structliteral2_old = '''        # Check each field
        for val, mem in zip(node.values, struct_sym.members):
            # Pass expected type if field is a struct literal
            if isinstance(val, StructLiteral) and isinstance(mem.type, StructType):
                self._struct_literal_expected = mem.type
            
            val_ty = self.visit(val, o)
            val_ty = resolve_type(val_ty)
            if isinstance(val_ty, AutoType):
                val_ty.resolved_type = mem.type
                val_ty = mem.type
            if not type_equivalent(val_ty, mem.type):
                raise TypeMismatchInExpression(node)'''
structliteral2_new = '''        # Check each field
        def check_field(field_tuple):
            val, mem = field_tuple
            if isinstance(val, StructLiteral) and isinstance(mem.type, StructType):
                self._struct_literal_expected = mem.type
            
            val_ty = self.visit(val, o)
            val_ty = resolve_type(val_ty)
            if isinstance(val_ty, AutoType):
                val_ty.resolved_type = mem.type
                val_ty = mem.type
            if not type_equivalent(val_ty, mem.type):
                raise TypeMismatchInExpression(node)
        list(map(check_field, zip(node.values, struct_sym.members)))'''
code = code.replace(structliteral2_old, structliteral2_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(code)
