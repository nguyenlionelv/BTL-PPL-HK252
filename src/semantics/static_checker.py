"""
Static Semantic Checker for TyC Programming Language

This module implements a comprehensive static semantic checker using visitor pattern
for the TyC procedural programming language. It performs type checking,
scope management, type inference, and detects all semantic errors as
specified in the TyC language specification.
"""

from functools import reduce
from typing import (
    Dict,
    List,
    Set,
    Optional,
    Any,
    Tuple,
    NamedTuple,
    Union,
    TYPE_CHECKING,
)
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    ASTNode,
    Program,
    StructDecl,
    MemberDecl,
    FuncDecl,
    Param,
    VarDecl,
    IfStmt,
    WhileStmt,
    ForStmt,
    BreakStmt,
    ContinueStmt,
    ReturnStmt,
    BlockStmt,
    SwitchStmt,
    CaseStmt,
    DefaultStmt,
    Type,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    BinaryOp,
    PrefixOp,
    PostfixOp,
    AssignExpr,
    MemberAccess,
    FuncCall,
    Identifier,
    StructLiteral,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    ExprStmt,
    Expr,
    Stmt,
    Decl,
)

# Type aliases for better type hints
TyCType = Union[IntType, FloatType, StringType, VoidType, StructType]
from .static_error import (
    StaticError,
    Redeclared,
    UndeclaredIdentifier,
    UndeclaredFunction,
    UndeclaredStruct,
    TypeCannotBeInferred,
    TypeMismatchInStatement,
    TypeMismatchInExpression,
    MustInLoop,
)


# AutoType
class AutoType(Type):
    def __init__(self):
        super().__init__()
        self.resolved_type = None  # Will be filled in when type is inferred

    def __str__(self):
        return f"AutoType({self.resolved_type})" if self.resolved_type else "AutoType(Unknown)"

    def __eq__(self, other):
        return isinstance(other, AutoType) and self.resolved_type == other.resolved_type

    def accept(self, visitor, param=None):
        pass

def resolve_type(typ: Type) -> Type:
    if isinstance(typ, AutoType) and typ.resolved_type is not None:
        return typ.resolved_type
    return typ


def type_equivalent(t1: Type, t2: Type) -> bool:
    t1, t2 = resolve_type(t1), resolve_type(t2)
    if type(t1) is type(t2):
        if isinstance(t1, StructType):
            return t1.struct_name == t2.struct_name
        return True
    return False

class Symbol:
    def __init__(self, name: str, type: TyCType, kind: str, is_global: bool = False, params=None, members=None, node=None):
        self.name = name
        self.type = type
        self.kind = kind
        self.params = params if params is not None else []
        self.members = members if members is not None else []

class StaticChecker(ASTVisitor):
    def check_program(self, ast):
        return self.visit(ast)

    def visit_program(self, node: "Program", o: Any = None):

        builtin_funcs = [
            Symbol("readInt", IntType(), "func", params=[]),
            Symbol("printInt", VoidType(), "func", params=[IntType()]),
            Symbol("readFloat", FloatType(), "func", params=[]),
            Symbol("printFloat", VoidType(), "func", params=[FloatType()]),
            Symbol("readString", StringType(), "func", params=[]),
            Symbol("printString", VoidType(), "func", params=[StringType()]),
        ]

        # Global state for type checking
        self.loop_stack = 0      # how many enclosing loops we're in
        self.switch_stack = 0    # how many enclosing switch stmts we're in
        self.current_func_return_type = None  # return type of current function
        self.current_func_name = None         # name of current function (for inferred return update)
        self.current_params = []

        env = [builtin_funcs]
        env = reduce(lambda acc, decl: self.visit(decl, acc), node.decls, env)
        # main = [sym for sym in env[0] if sym.name == "main"]
        # if not main:
        #     raise UndeclaredFunction("main")
        
    def visit_struct_decl(self, node: "StructDecl", o: Any = None):
        # Check redeclared struct
        global_structs = [sym.name for sym in o[0] if sym.kind == "struct"]
        if node.name in global_structs:
            raise Redeclared("Struct", node.name)

        # Visit members with a new scope for the struct
        env = reduce(lambda acc, c: self.visit(c, acc), node.members, [[]] + o)

        # Add struct to global environment
        symbol = Symbol(node.name, StructType(node.name), "struct")
        symbol.members = env[0]
        return [o[0] + [symbol]] + o[1:]
        
        
    def visit_member_decl(self, node: "MemberDecl", o: Any = None):
        # Check redeclared member
        struct_scope = [sym.name for sym in o[0]]
        if node.name in struct_scope:
            raise Redeclared("Member", node.name)

        # Check undeclared struct
        if isinstance(node.member_type, StructType):
            global_structs = [sym.name for sym in o[-1] if sym.kind == "struct"]
            if node.member_type.struct_name not in global_structs:
                raise UndeclaredStruct(node.member_type.struct_name)

        symbol = Symbol(node.name, node.member_type, "member")
        return [o[0] + [symbol]] + o[1:]

    def visit_func_decl(self, node: "FuncDecl", o: Any = None):
        # Check redeclared function
        global_funcs = [sym.name for sym in o[0] if sym.kind == "func"]
        if node.name in global_funcs:
            raise Redeclared("Function", node.name)

        # Check UndeclaredStruct for return type
        if isinstance(node.return_type, StructType):
            global_structs = [sym.name for sym in o[-1] if sym.kind == "struct"]
            if node.return_type.struct_name not in global_structs:
                raise UndeclaredStruct(node.return_type.struct_name)

        # Lấy return type trước tên hàm
        return_typ = node.return_type if node.return_type is not None else AutoType()

        symbol = Symbol(node.name, return_typ, "func")
        new_o = [o[0] + [symbol]] + o[1:]

        # New scope for function parameters and body
        env = reduce(lambda acc, c: self.visit(c, acc), node.params, [[]] + new_o)
        symbol.params = [sym.type for sym in env[0]]  # store param types

        # Prevent parameter shadowing in nested blocks
        previous_params = self.current_params
        self.current_params = [sym.name for sym in env[0]]

        # Save and set function context for type checking
        previous_func_name = self.current_func_name
        previous_func_return_type = self.current_func_return_type
        self.current_func_name = node.name
        self.current_func_return_type = return_typ

        self.visit(node.body, env)

        # After visiting body, update the symbol's return type if it was inferred
        resolved_ret = resolve_type(self.current_func_return_type)
        if isinstance(resolved_ret, AutoType):
            resolved_ret = VoidType()
        symbol.type = resolved_ret

        # Restore context
        self.current_func_name = previous_func_name
        self.current_func_return_type = previous_func_return_type
        self.current_params = previous_params
        return new_o

    def visit_param(self, node: "Param", o: Any = None):
        # Check redeclared parameter
        names_in_scope = [sym.name for sym in o[0]]
        if node.name in names_in_scope:
            raise Redeclared("Parameter", node.name)
        # Check undeclared struct
        if isinstance(node.param_type, StructType):
            global_names = [sym.name for sym in o[-1] if sym.kind == "struct"]
            if node.param_type.struct_name not in global_names:
                raise UndeclaredStruct(node.param_type.struct_name)
        symbol = Symbol(node.name, node.param_type, "param")
        return [o[0] + [symbol]] + o[1:]

    # Type system
    def visit_int_type(self, node: "IntType", o: Any = None):
        return IntType()

    def visit_float_type(self, node: "FloatType", o: Any = None):
        return FloatType()

    def visit_string_type(self, node: "StringType", o: Any = None):
        return StringType()

    def visit_void_type(self, node: "VoidType", o: Any = None):
        return VoidType()

    def visit_struct_type(self, node: "StructType", o: Any = None):
        return StructType(node.struct_name)

    # Statements
    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        env = [[]] + o
        for stmt in node.statements:
            env = self.visit(stmt, env)

        # Check any auto variables that were never resolved
        for sym in env[0]:
            if sym.kind == "var":
                resolved = resolve_type(sym.type)
                if isinstance(resolved, AutoType):
                    for stmt in node.statements:
                        if isinstance(stmt, VarDecl) and stmt.name == sym.name and stmt.var_type is None:
                            raise TypeCannotBeInferred(node)
                    # raise TypeCannotBeInferred(node)

        return o  # block stmt doesn't affect outer environment

    def visit_var_decl(self, node: "VarDecl", o: Any = None):
        # Check redeclared var
        names_in_scope = [sym.name for sym in o[0]]
        if node.name in names_in_scope:
            raise Redeclared("Variable", node.name)

        # Check redelared param
        if node.name in self.current_params:
            raise Redeclared("Variable", node.name)

        # Check undeclared struct
        if isinstance(node.var_type, StructType):
            global_structs = [sym.name for sym in o[-1] if sym.kind == "struct"]
            if node.var_type.struct_name not in global_structs:
                raise UndeclaredStruct(node.var_type.struct_name)

        # Determine the symbol type — None means 'auto'
        if node.var_type is not None:
            sym_type = node.var_type
        else:
            sym_type = AutoType()  # will be inferred later

        symbol = Symbol(node.name, sym_type, "var")
        new_o = [o[0] + [symbol]] + o[1:]

        if node.var_type is not None:
            if node.init_value is not None:
                if isinstance(node.init_value, StructLiteral) and isinstance(node.var_type, StructType):
                    self._struct_literal_expected = node.var_type
                rhs_type = self.visit(node.init_value, o)
                rhs_type = resolve_type(rhs_type)
                if isinstance(rhs_type, AutoType):
                    rhs_type.resolved_type = node.var_type
                    rhs_type = node.var_type
                if not type_equivalent(node.var_type, rhs_type):
                    raise TypeMismatchInStatement(node)
            else:
                pass
        else:
            if node.init_value is not None:
                rhs_type = self.visit(node.init_value, o)
                rhs_type = resolve_type(rhs_type)
                if isinstance(rhs_type, AutoType):
                    raise TypeCannotBeInferred(node.init_value)
                symbol.type.resolved_type = rhs_type
        return new_o

    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        cond_ty = self.visit(node.condition, o)
        cond_ty = resolve_type(cond_ty)
        if isinstance(cond_ty, AutoType):
            raise TypeCannotBeInferred(node.condition)
        if not isinstance(cond_ty, IntType):
            raise TypeMismatchInStatement(node)
        self.visit(node.then_stmt, o)
        if node.else_stmt:
            self.visit(node.else_stmt, o)
        return o

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        cond_ty = self.visit(node.condition, o)
        cond_ty = resolve_type(cond_ty)
        if isinstance(cond_ty, AutoType):
            raise TypeCannotBeInferred(node.condition)
        if not isinstance(cond_ty, IntType):
            raise TypeMismatchInStatement(node)
        self.loop_stack += 1
        self.visit(node.body, o)
        self.loop_stack -= 1
        return o

    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        env = o
        if node.init:
            env = self.visit(node.init, env)

        if node.condition:
            cond_ty = self.visit(node.condition, env)
            cond_ty = resolve_type(cond_ty)
            if isinstance(cond_ty, AutoType):
                raise TypeCannotBeInferred(node.condition)
            if not isinstance(cond_ty, IntType):
                raise TypeMismatchInStatement(node)
        
        if node.update:
            self.visit(node.update, env)

        self.loop_stack += 1
        # Visit body. If it's a BlockStmt, its own visit_block_stmt will handle local scoping.
        self.visit(node.body, env)
        self.loop_stack -= 1

        return env

    def visit_switch_stmt(self, node: "SwitchStmt", o: Any = None):
        expr_ty = self.visit(node.expr, o)
        expr_ty = resolve_type(expr_ty)
        if isinstance(expr_ty, AutoType):
            raise TypeCannotBeInferred(node)
        if not isinstance(expr_ty, IntType):
            raise TypeMismatchInStatement(node)

        self.switch_stack += 1
        for case in node.cases:
            self.visit(case, o)
        if node.default_case:
            self.visit(node.default_case, o)
        self.switch_stack -= 1
        return o

    def visit_case_stmt(self, node: "CaseStmt", o: Any = None):
        case_ty = self.visit(node.expr, o)
        case_ty = resolve_type(case_ty)
        if isinstance(case_ty, AutoType):
            raise TypeCannotBeInferred(node.expr)
        if not isinstance(case_ty, IntType):
            raise TypeMismatchInStatement(node)

        env = [[]] + o
        for stmt in node.statements:
            env = self.visit(stmt, env)
        
        # Check any auto variables that were never resolved
        for sym in env[0]:
            if sym.kind == "var":
                resolved = resolve_type(sym.type)
                if isinstance(resolved, AutoType):
                    raise TypeCannotBeInferred(node)

        return o  # case body doesn't leak declarations into outer scope

    def visit_default_stmt(self, node: "DefaultStmt", o: Any = None):
        # Create a local scope for variables declared inside this default body
        env = [[]] + o
        for stmt in node.statements:
            env = self.visit(stmt, env)

        # Check any auto variables in the default scope that were never resolved
        for sym in env[0]:
            if sym.kind == "var":
                resolved = resolve_type(sym.type)
                if isinstance(resolved, AutoType):
                    raise TypeCannotBeInferred(node)

        return o  # default body doesn't leak declarations into outer scope

    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        if self.loop_stack == 0 and self.switch_stack == 0:
            raise MustInLoop(node)
        return o

    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        if self.loop_stack == 0:
            raise MustInLoop(node)
        return o

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        if node.expr:
            expected = self.current_func_return_type
            expected_for_visit = None if isinstance(resolve_type(expected), AutoType) else resolve_type(expected)
            if isinstance(node.expr, StructLiteral) and isinstance(expected_for_visit, StructType):
                self._struct_literal_expected = expected_for_visit
            
            expr_type = self.visit(node.expr, o)
            expr_type = resolve_type(expr_type)
            # nếu return có return type là auto
            if isinstance(expr_type, AutoType):
                # nếu trước tên hàm có return type
                if expected_for_visit is not None:
                    expr_type.resolved_type = expected_for_visit
                    expr_type = expected_for_visit
                # nếu trước tên hàm là auto và return stmt cũng auto
                else:
                    raise TypeCannotBeInferred(node)

            # Update inferred return type or check consistency
            current_ret = resolve_type(self.current_func_return_type)
            # nếu trước tên hàm là auto thì gán return type trong return stmt cho hàm
            if isinstance(current_ret, AutoType):
                # First time seeing a return: fix the inferred return type
                current_ret.resolved_type = expr_type
                self.current_func_return_type = expr_type
            else:
                # nếu trước tên hàm có return type và return stmt trả về return type khác nhau
                if not type_equivalent(expr_type, current_ret):
                    raise TypeMismatchInStatement(node)
        else:
            # return; (no expr)
            current_ret = resolve_type(self.current_func_return_type)
            if isinstance(current_ret, AutoType):
                # Treat as void return
                current_ret.resolved_type = VoidType()
                self.current_func_return_type = VoidType()
            else:
                if not isinstance(current_ret, VoidType):
                    raise TypeMismatchInStatement(node)
        return o

    def visit_expr_stmt(self, node: "ExprStmt", o: Any = None):
        try:
            self.visit(node.expr, o)
        except TypeMismatchInExpression as e:
            # Assignment at statement level -> TypeMismatchInStatement
            if isinstance(node.expr, AssignExpr):
                raise TypeMismatchInStatement(node.expr)
            raise
        return o

    # def help(self, name, typ, env):
    #     """Update AutoType for a variable in the environment."""
    #     for scope in env:
    #         for sym in scope:
    #             if sym.name == name and sym.kind in ["var", "param"]:
    #                 actual_type = resolve_type(sym.type)
    #                 if isinstance(actual_type, AutoType):
    #                     actual_type.resolved_type = typ
    #                     return typ
    #                 return actual_type
    #     return None
    # Expressions
    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        t1_raw = self.visit(node.left, o)
        t2_raw = self.visit(node.right, o)

        t1 = resolve_type(t1_raw)
        t2 = resolve_type(t2_raw)

        op = node.operator
        if isinstance(t1, AutoType) or isinstance(t2, AutoType):
            if not isinstance(node.right, (IntLiteral, FloatLiteral)) and not isinstance(node.left, (IntLiteral, FloatLiteral)):
                raise TypeCannotBeInferred(node)

        if op in ['+', '-', '*', '/']:
            if isinstance(t1, AutoType) and isinstance(node.right, (IntLiteral, FloatLiteral)):
                t1.resolved_type = IntType() if isinstance(node.right, IntLiteral) else FloatType()
                t1 = t1.resolved_type
            if isinstance(t2, AutoType) and isinstance(node.left, (IntLiteral, FloatLiteral)):
                t2.resolved_type = IntType() if isinstance(node.left, IntLiteral) else FloatType()
                t2 = t2.resolved_type
            if not isinstance(t1, (IntType, FloatType)) or not isinstance(t2, (IntType, FloatType)):
                raise TypeMismatchInExpression(node)
            if isinstance(t1, IntType) and isinstance(t2, IntType):
                return IntType()
            return FloatType()

        elif op in ['%', '&&', '||']:
            if isinstance(t1, AutoType) and isinstance(node.left, Identifier):
                t1.resolved_type = IntType()
                return t1
            elif isinstance(t2, AutoType) and isinstance(node.right, Identifier):
                t2.resolved_type = IntType()
                return t2
            elif not isinstance(t1, AutoType) and not isinstance(t2, AutoType):
                if not isinstance(t1, IntType) or not isinstance(t2, IntType):
                    raise TypeMismatchInExpression(node)
                return IntType()

        elif op in ['<', '>', '<=', '>=', '==', '!=']:
            if isinstance(t1, AutoType) and isinstance(node.left, Identifier):
                t1.resolved_type = IntType()
                return IntType()
            elif isinstance(t2, AutoType) and isinstance(node.right, Identifier):
                t2.resolved_type = IntType()
                return IntType()
            elif not isinstance(t1, AutoType) and not isinstance(t2, AutoType):
                if not isinstance(t1, (IntType, FloatType)) or not isinstance(t2, (IntType, FloatType)):
                    raise TypeMismatchInExpression(node)
                return IntType()
        

    def visit_prefix_op(self, node: "PrefixOp", o: Any = None):
        op = node.operator
        typ = self.visit(node.operand, o)
        typ = resolve_type(typ)

        if isinstance(typ, AutoType):
            raise TypeCannotBeInferred(node)

        if op in ['+', '-']:
            if not isinstance(typ, (IntType, FloatType)):
                raise TypeMismatchInExpression(node)
            return typ
        elif op == '!':
            if not isinstance(typ, IntType):
                raise TypeMismatchInExpression(node)
            return IntType()
        elif op in ['++', '--']:
            if not isinstance(node.operand, (Identifier, MemberAccess)):
                raise TypeMismatchInExpression(node)
            if not isinstance(typ, IntType):
                raise TypeMismatchInExpression(node)
            return IntType()
        raise TypeMismatchInExpression(node)

    def visit_postfix_op(self, node: "PostfixOp", o: Any = None):
        op = node.operator
        typ = self.visit(node.operand, o)
        typ = resolve_type(typ)

        if isinstance(typ, AutoType):
            raise TypeCannotBeInferred(node)

        if op in ['++', '--']:
            if not isinstance(node.operand, (Identifier, MemberAccess)):
                raise TypeMismatchInExpression(node)
            if not isinstance(typ, IntType):
                raise TypeMismatchInExpression(node)
            return IntType()
        raise TypeMismatchInExpression(node)

    def visit_assign_expr(self, node: "AssignExpr", o: Any = None):
        if not isinstance(node.lhs, (Identifier, MemberAccess)):
            self.visit(node.lhs, o)
            raise TypeMismatchInExpression(node)

        lhs_type = self.visit(node.lhs, o)
        lhs_type = resolve_type(lhs_type)
        if isinstance(lhs_type, StructType) and isinstance(node.rhs, StructLiteral):
            self._struct_literal_expected = lhs_type

        rhs_type = self.visit(node.rhs, o)
        rhs_type = resolve_type(rhs_type)

        lhs_type = resolve_type(lhs_type)

        if isinstance(lhs_type, AutoType) and not isinstance(rhs_type, AutoType):
            found_sym = None
            if isinstance(node.lhs, Identifier):
                for scope in o:
                    for sym in scope:
                        if sym.name == node.lhs.name and sym.kind in ["var", "param"]:
                            found_sym = sym
                            break
                    if found_sym:
                        break
            if found_sym is not None:
                auto_t = resolve_type(found_sym.type)
                if isinstance(auto_t, AutoType):
                    auto_t.resolved_type = rhs_type
            lhs_type = rhs_type

        if isinstance(lhs_type, AutoType) or isinstance(rhs_type, AutoType):
            raise TypeCannotBeInferred(node)

        if not type_equivalent(lhs_type, rhs_type):
            raise TypeMismatchInExpression(node)

        return lhs_type

    def visit_member_access(self, node: "MemberAccess", o: Any = None):
        obj_type = self.visit(node.obj, o)
        obj_type = resolve_type(obj_type)

        if isinstance(obj_type, AutoType):
            raise TypeCannotBeInferred(node)

        if not isinstance(obj_type, StructType):
            raise TypeMismatchInExpression(node)

        struct_sym = None
        for scope in o:
            for sym in scope:
                if sym.kind == "struct" and sym.name == obj_type.struct_name:
                    struct_sym = sym
                    break
            if struct_sym:
                break

        if struct_sym is None:
            raise UndeclaredStruct(obj_type.struct_name)
        for mem in struct_sym.members:
            if mem.name == node.member:
                return mem.type

        raise TypeMismatchInExpression(node)

    def visit_func_call(self, node: "FuncCall", o: Any = None):
        # Find the function symbol
        func_sym = None
        for scope in o:
            for sym in scope:
                if sym.name == node.name and sym.kind == "func":
                    func_sym = sym
                    break
            if func_sym:
                break

        if func_sym is None:
            raise UndeclaredFunction(node.name)

        # Check argument count
        if len(node.args) != len(func_sym.params):
            raise TypeMismatchInExpression(node)

        # Check argument types
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
                raise TypeMismatchInExpression(node)

        return resolve_type(func_sym.type)

    def visit_identifier(self, node: "Identifier", o: Any = None):
        found_sym = None
        for scope in o:
            for sym in scope:
                if sym.name == node.name and sym.kind in ["var", "param", "func"]:
                    found_sym = sym
                    break
            if found_sym:
                break

        if found_sym is None:
            raise UndeclaredIdentifier(node.name)

        typ = resolve_type(found_sym.type)
        return typ

    def visit_struct_literal(self, node: "StructLiteral", o: Any = None):
        expected = getattr(self, '_struct_literal_expected', None)
        self._struct_literal_expected = None  # reset

        if not isinstance(expected, StructType):
            raise TypeCannotBeInferred(node)

        struct_sym = None
        for scope in o:
            for sym in scope:
                if sym.kind == "struct" and sym.name == expected.struct_name:
                    struct_sym = sym
                    break
            if struct_sym:
                break

        if struct_sym is None:
            raise UndeclaredStruct(expected.struct_name)

        if len(node.values) != len(struct_sym.members):
            raise TypeMismatchInExpression(node)

        for val, mem in zip(node.values, struct_sym.members):
            if isinstance(val, StructLiteral) and isinstance(mem.type, StructType):
                self._struct_literal_expected = mem.type
            
            val_type = self.visit(val, o)
            val_type = resolve_type(val_type)
            if isinstance(val_type, AutoType):
                val_type.resolved_type = mem.type
                val_type = mem.type
            if not type_equivalent(val_type, mem.type):
                raise TypeMismatchInExpression(node)

        return expected

    def visit_int_literal(self, node: "IntLiteral", o: Any = None):
        return IntType()

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        return FloatType()

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        return StringType()
