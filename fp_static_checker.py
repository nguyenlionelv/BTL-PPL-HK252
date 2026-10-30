from functools import reduce
from typing import Any, Union
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    Program, StructDecl, MemberDecl, FuncDecl, Param, VarDecl,
    IfStmt, WhileStmt, ForStmt, BreakStmt, ContinueStmt, ReturnStmt,
    BlockStmt, SwitchStmt, CaseStmt, DefaultStmt,
    IntType, FloatType, StringType, VoidType, StructType,
    BinaryOp, PrefixOp, PostfixOp, AssignExpr, MemberAccess, FuncCall,
    Identifier, StructLiteral, ExprStmt
)
from .static_error import (
    Redeclared, UndeclaredIdentifier, UndeclaredFunction, UndeclaredStruct,
    TypeCannotBeInferred, TypeMismatchInStatement, TypeMismatchInExpression, MustInLoop
)

TyCType = Union[IntType, FloatType, StringType, VoidType, StructType]

class Symbol:
    def __init__(self, name: str, type: TyCType, kind: str):
        self.name = name
        self.type = type
        self.kind = kind
        self.members = {}
        self.params = []

class StaticChecker(ASTVisitor):
    def check_program(self, ast):
        return self.visit(ast, None)

    def flatten_env(self, env):
        return reduce(lambda acc, scope: acc + scope, env, [])

    def find_symbol(self, env, name=None, kind=None, kind_in=None):
        def match(sym):
            return ((name is None or sym.name == name) and 
                    (kind is None or sym.kind == kind) and 
                    (kind_in is None or sym.kind in kind_in))
        matches = list(filter(match, self.flatten_env(env)))
        return matches[0] if matches else None

    def find_symbol_in_scope(self, scope, name=None, kind=None, kind_in=None):
        def match(sym):
            return ((name is None or sym.name == name) and 
                    (kind is None or sym.kind == kind) and 
                    (kind_in is None or sym.kind in kind_in))
        matches = list(filter(match, scope))
        return matches[0] if matches else None

    def get_names_in_scope(self, scope, kind=None, kind_in=None):
        def match(sym):
            return ((kind is None or sym.kind == kind) and 
                    (kind_in is None or sym.kind in kind_in))
        return list(map(lambda s: s.name, filter(match, scope)))

    def visit_statements(self, statements, env):
        reduce(lambda acc, stmt: self.visit(stmt, acc) or acc, statements, env)

    def check_auto_variables(self, scope, error_node):
        def check_auto(sym):
            if sym.kind == 'var' and sym.type is None:
                raise TypeCannotBeInferred(error_node)
        list(map(check_auto, scope))

    def check_must_in_loop(self, env, error_node, allow_switch=False):
        valid_loop_names = ["@Loop", "@Switch"] if allow_switch else ["@Loop"]
        in_loop = list(filter(lambda sym: sym.name in valid_loop_names, self.flatten_env(env)))
        if not in_loop:
            raise MustInLoop(error_node)

    def is_type_match(self, t1, t2):
        if type(t1) is type(t2):
            if isinstance(t1, StructType):
                return t1.struct_name == t2.struct_name
            return True
        return False

    def can_coerce_to(self, target_type, src_type):
        if self.is_type_match(target_type, src_type):
            return True
        if isinstance(target_type, FloatType) and isinstance(src_type, IntType):
            return True
        return False

    def visit_program(self, node: "Program", o: Any = None):
        self.global_names = [
            Symbol("readInt", IntType(), "func"), 
            Symbol("printInt", VoidType(), "func"), 
            Symbol("readFloat", FloatType(), "func"), 
            Symbol("printFloat", VoidType(), "func"), 
            Symbol("readString", StringType(), "func"), 
            Symbol("printString", VoidType(), "func")
        ]
        self.global_names[0].params = []
        self.global_names[1].params = [IntType()]
        self.global_names[2].params = []
        self.global_names[3].params = [FloatType()]
        self.global_names[4].params = []
        self.global_names[5].params = [StringType()]
        
        env = [self.global_names]
        reduce(lambda acc, decl: self.visit(decl, acc) or acc, node.decls, env)

    def visit_struct_decl(self, node: "StructDecl", o: Any = None):
        structs_in_scope = self.get_names_in_scope(o[0], kind="struct")
        if node.name in structs_in_scope:
            raise Redeclared("Struct", node.name)
        
        symbol = Symbol(node.name, StructType(node.name), "struct")
        
        def add_member(acc, member):
            if member.name in acc:
                raise Redeclared("Member", member.name)
            if isinstance(member.member_type, StructType):
                global_names = self.get_names_in_scope(o[0], kind="struct")
                if member.member_type.struct_name not in global_names:
                    raise UndeclaredStruct(member.member_type.struct_name)
            acc[member.name] = member.member_type
            return acc
            
        symbol.members = reduce(add_member, node.members, {})
        return [o[0] + [symbol]] + o[1:]
        
    def visit_member_decl(self, node: "MemberDecl", o: Any = None):
        pass

    def visit_func_decl(self, node: "FuncDecl", o: Any = None):
        funcs_vars_in_scope = self.get_names_in_scope(o[0], kind_in=["func", "var", "param"])
        if node.name in funcs_vars_in_scope:
            raise Redeclared("Function", node.name)
            
        symbol = Symbol(node.name, node.return_type, "func")
        symbol.params = list(map(lambda p: p.param_type, node.params))
        new_o = [o[0] + [symbol]] + o[1:]
        
        env = [[]] + new_o
        env[0].append(Symbol("@Return", node.return_type, "return"))
        env[0].append(Symbol("@InsideFunc", VoidType(), "marker"))
        
        env = reduce(lambda acc, c: self.visit(c, acc) or acc, node.params, env)
        
        if isinstance(node.body, BlockStmt):
            self.visit_statements(node.body.statements, env)
        else:
            self.visit(node.body, env)
        
        ret_sym = self.find_symbol(env, name="@Return")
        if symbol.type is None:
            symbol.type = ret_sym.type if ret_sym.type is not None else VoidType()
            
        self.check_auto_variables(env[0], node.body)
        return new_o

    def visit_param(self, node: "Param", o: Any = None):
        names_in_scope = self.get_names_in_scope(o[0])
        if node.name in names_in_scope:
            raise Redeclared("Parameter", node.name)
            
        symbol = Symbol(node.name, node.param_type, "param")
        return [o[0] + [symbol]] + o[1:]

    def visit_int_type(self, node, o=None): return IntType()
    def visit_float_type(self, node, o=None): return FloatType()
    def visit_string_type(self, node, o=None): return StringType()
    def visit_void_type(self, node, o=None): return VoidType()
    def visit_struct_type(self, node, o=None): return StructType(node.struct_name)

    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        env = [[]] + o
        self.visit_statements(node.statements, env)
        self.check_auto_variables(env[0], node)
        return o

    def visit_var_decl(self, node: "VarDecl", o: Any = None):
        funcs_vars_in_scope = self.get_names_in_scope(o[0], kind_in=["func", "var", "param"])
        if node.name in funcs_vars_in_scope:
            raise Redeclared("Variable", node.name)
            
        if self.find_symbol(o, name="@InsideFunc"):
            if self.find_symbol(o, name=node.name, kind='param'):
                raise Redeclared("Variable", node.name)
            
        if isinstance(node.var_type, StructType):
            struct_names = list(map(lambda s: s.name, filter(lambda s: s.kind == "struct", self.flatten_env(o))))
            if node.var_type.struct_name not in struct_names:
                raise UndeclaredStruct(node.var_type.struct_name)
                
        actual_type = node.var_type
        if node.init_value:
            o[0].append(Symbol("@Target", actual_type, "target"))
            init_type = self.visit(node.init_value, o)
            o[0].pop()
            
            if actual_type is None:
                if init_type is None or isinstance(init_type, VoidType):
                    raise TypeCannotBeInferred(node)
                actual_type = init_type
            else:
                if init_type is None or not self.can_coerce_to(actual_type, init_type):
                    raise TypeMismatchInStatement(node)
            
        symbol = Symbol(node.name, actual_type, "var")
        o[0].append(symbol)
        return o

    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        cond_type = self.visit(node.condition, o)
        if cond_type is None or not isinstance(cond_type, IntType):
            raise TypeMismatchInStatement(node)
        self.visit(node.then_stmt, o)
        if node.else_stmt:
            self.visit(node.else_stmt, o)

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        cond_type = self.visit(node.condition, o)
        if cond_type is None or not isinstance(cond_type, IntType):
            raise TypeMismatchInStatement(node)
        
        loop_env = [[Symbol("@Loop", VoidType(), "loop")]] + o
        if isinstance(node.body, BlockStmt):
            self.visit_statements(node.body.statements, loop_env)
            self.check_auto_variables(loop_env[0], node.body)
        else:
            self.visit(node.body, loop_env)

    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        env = [[]] + o
        if node.init: self.visit(node.init, env)
        if node.condition:
            cond_type = self.visit(node.condition, env)
            if cond_type is None or not isinstance(cond_type, IntType):
                raise TypeMismatchInStatement(node)
        if node.update: self.visit(node.update, env)
            
        loop_env = [[Symbol("@Loop", VoidType(), "loop")]] + env
        if isinstance(node.body, BlockStmt):
            self.visit_statements(node.body.statements, loop_env)
            self.check_auto_variables(loop_env[0], node.body)
        else:
            self.visit(node.body, loop_env)

    def visit_switch_stmt(self, node: "SwitchStmt", o: Any = None):
        expr_type = self.visit(node.expr, o)
        if expr_type is None or not isinstance(expr_type, IntType):
            raise TypeMismatchInStatement(node)
            
        switch_env = [[Symbol("@Switch", VoidType(), "switch")]] + o
        reduce(lambda acc, c: self.visit(c, acc) or acc, node.cases, switch_env)
        if node.default_case:
            self.visit(node.default_case, switch_env)

    def visit_case_stmt(self, node: "CaseStmt", o: Any = None):
        expr_type = self.visit(node.expr, o)
        if expr_type is None or not isinstance(expr_type, IntType):
            raise TypeMismatchInStatement(node)
            
        env = [[]] + o
        self.visit_statements(node.statements, env)
        self.check_auto_variables(env[0], node)

    def visit_default_stmt(self, node: "DefaultStmt", o: Any = None):
        env = [[]] + o
        self.visit_statements(node.statements, env)
        self.check_auto_variables(env[0], node)

    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        self.check_must_in_loop(o, node, allow_switch=True)

    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        self.check_must_in_loop(o, node, allow_switch=False)

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        ret_sym = self.find_symbol(o, name="@Return")
        if node.expr:
            if ret_sym: o[0].append(Symbol("@Target", ret_sym.type, "target"))
            ret_type = self.visit(node.expr, o)
            if ret_sym: o[0].pop()
            
            if ret_sym and ret_sym.type is None:
                if ret_type is None or isinstance(ret_type, VoidType):
                    raise TypeCannotBeInferred(node)
                ret_sym.type = ret_type
            elif ret_sym:
                if ret_type is None or not self.can_coerce_to(ret_sym.type, ret_type):
                    raise TypeMismatchInStatement(node)
        else:
            if ret_sym and ret_sym.type is None:
                ret_sym.type = VoidType()
            elif ret_sym and not isinstance(ret_sym.type, VoidType):
                raise TypeMismatchInStatement(node)

    def visit_expr_stmt(self, node: "ExprStmt", o: Any = None):
        try:
            self.visit(node.expr, o)
        except TypeMismatchInExpression as e:
            if getattr(e, "expr", None) is node.expr and isinstance(node.expr, AssignExpr):
                raise TypeMismatchInStatement(node)
            raise e

    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        l_type = self.visit(node.left, o)
        r_type = self.visit(node.right, o)
        
        if l_type is None or r_type is None:
            raise TypeCannotBeInferred(node)
            
        if node.operator in ['+', '-', '*', '/']:
            if isinstance(l_type, FloatType) and isinstance(r_type, (IntType, FloatType)):
                return FloatType()
            if isinstance(r_type, FloatType) and isinstance(l_type, (IntType, FloatType)):
                return FloatType()
            if isinstance(l_type, IntType) and isinstance(r_type, IntType):
                return IntType()
            raise TypeMismatchInExpression(node)
            
        elif node.operator == '%':
            if isinstance(l_type, IntType) and isinstance(r_type, IntType):
                return IntType()
            raise TypeMismatchInExpression(node)
            
        elif node.operator in ['==', '!=']:
            if self.is_type_match(l_type, r_type) and not isinstance(l_type, StructType):
                return IntType()
            if isinstance(l_type, (IntType, FloatType)) and isinstance(r_type, (IntType, FloatType)):
                return IntType()
            raise TypeMismatchInExpression(node)
            
        elif node.operator in ['<', '<=', '>', '>=']:
            if isinstance(l_type, (IntType, FloatType)) and isinstance(r_type, (IntType, FloatType)):
                return IntType()
            raise TypeMismatchInExpression(node)
            
        elif node.operator in ['&&', '||']:
            if isinstance(l_type, IntType) and isinstance(r_type, IntType):
                return IntType()
            raise TypeMismatchInExpression(node)
            
        raise TypeMismatchInExpression(node)

    def visit_prefix_op(self, node: "PrefixOp", o: Any = None):
        op_type = self.visit(node.operand, o)
        if op_type is None:
            raise TypeCannotBeInferred(node)
            
        if node.operator in ['+', '-']:
            if isinstance(op_type, (IntType, FloatType)):
                return op_type
        elif node.operator == '!':
            if isinstance(op_type, IntType):
                return IntType()
        elif node.operator in ['++', '--']:
            if not isinstance(node.operand, (Identifier, MemberAccess)):
                raise TypeMismatchInExpression(node)
            if isinstance(op_type, IntType):
                return op_type
                
        raise TypeMismatchInExpression(node)

    def visit_postfix_op(self, node: "PostfixOp", o: Any = None):
        op_type = self.visit(node.operand, o)
        if op_type is None:
            raise TypeCannotBeInferred(node)
            
        if node.operator in ['++', '--']:
            if not isinstance(node.operand, (Identifier, MemberAccess)):
                raise TypeMismatchInExpression(node)
            if isinstance(op_type, IntType):
                return op_type
                
        raise TypeMismatchInExpression(node)

    def visit_assign_expr(self, node: "AssignExpr", o: Any = None):
        if not isinstance(node.lhs, (Identifier, MemberAccess)):
            raise TypeMismatchInExpression(node)
            
        l_sym = None
        if isinstance(node.lhs, Identifier):
            sym = self.find_symbol(o, name=node.lhs.name, kind_in=['var', 'param'])
            if sym is None:
                raise UndeclaredIdentifier(node.lhs.name)
            l_sym = sym
            
        l_type = getattr(l_sym, 'type', None)
        if l_sym is None:
            l_type = self.visit(node.lhs, o)
            
        o[0].append(Symbol("@Target", l_type, "target"))
        r_type = self.visit(node.rhs, o)
        o[0].pop()
        
        if r_type is None:
            raise TypeCannotBeInferred(node)
            
        if l_sym and l_sym.type is None:
            l_sym.type = r_type
            l_type = r_type
            
        if not self.can_coerce_to(l_type, r_type):
            raise TypeMismatchInExpression(node)
            
        return l_type

    def visit_member_access(self, node: "MemberAccess", o: Any = None):
        obj_type = self.visit(node.obj, o)
        if obj_type is None:
            raise TypeCannotBeInferred(node)
            
        if not isinstance(obj_type, StructType):
            raise TypeMismatchInExpression(node)
            
        struct_sym = self.find_symbol_in_scope(o[-1], name=obj_type.struct_name, kind="struct")
        if not struct_sym:
            raise UndeclaredStruct(obj_type.struct_name)
            
        if node.member not in struct_sym.members:
            raise UndeclaredIdentifier(node.member)
            
        return struct_sym.members[node.member]

    def visit_func_call(self, node: "FuncCall", o: Any = None):
        func_sym = self.find_symbol(o, name=node.name, kind="func")
        if not func_sym:
            raise UndeclaredFunction(node.name)
            
        if len(node.args) != len(func_sym.params):
            raise TypeMismatchInExpression(node)
            
        def check_arg(pair):
            arg, param_type = pair
            o[0].append(Symbol("@Target", param_type, "target"))
            arg_type = self.visit(arg, o)
            o[0].pop()
            if arg_type is None or not self.can_coerce_to(param_type, arg_type):
                raise TypeMismatchInExpression(node)
                
        list(map(check_arg, zip(node.args, func_sym.params)))
            
        if func_sym.type is None:
            return None
        return func_sym.type

    def visit_identifier(self, node: "Identifier", o: Any = None):
        sym = self.find_symbol(o, name=node.name, kind_in=['var', 'param'])
        if not sym:
            raise UndeclaredIdentifier(node.name)
        return sym.type

    def visit_struct_literal(self, node: "StructLiteral", o: Any = None):
        target_sym = self.find_symbol(o, name="@Target")
        if not target_sym or not isinstance(target_sym.type, StructType):
            raise TypeMismatchInExpression(node)
            
        struct_sym = self.find_symbol(o, name=target_sym.type.struct_name, kind="struct")
        if not struct_sym or len(node.values) != len(struct_sym.members):
            raise TypeMismatchInExpression(node)
            
        def check_val(pair):
            val, target_member_type = pair
            o[0].append(Symbol("@Target", target_member_type, "target"))
            val_type = self.visit(val, o)
            o[0].pop()
            if val_type is None or not self.can_coerce_to(target_member_type, val_type):
                raise TypeMismatchInExpression(node)
                
        list(map(check_val, zip(node.values, struct_sym.members.values())))
        return target_sym.type

    def visit_int_literal(self, node, o=None): return IntType()
    def visit_float_literal(self, node, o=None): return FloatType()
    def visit_string_literal(self, node, o=None): return StringType()
