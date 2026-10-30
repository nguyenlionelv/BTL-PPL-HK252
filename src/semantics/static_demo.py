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


class AutoType(Type):
    def __init__(self):
        super().__init__()
        self.resolved_type = None
        
    def __str__(self):
        return f"AutoType({self.resolved_type})" if self.resolved_type else "AutoType(Unknown)"

    def __eq__(self, other):
        return isinstance(other, AutoType) and self.resolved_type == other.resolved_type

    def accept(self, visitor, param=None):
        pass


def resolve_type(typ: Type) -> Type:
    if isinstance(typ, AutoType):
        if typ.resolved_type is not None:
            return resolve_type(typ.resolved_type)
        return typ
    return typ


def type_equivalent(t1: Type, t2: Type) -> bool:
    t1 = resolve_type(t1)
    t2 = resolve_type(t2)
    if isinstance(t1, type(t2)) and isinstance(t2, type(t1)):
        if isinstance(t1, StructType) and isinstance(t2, StructType):
            return t1.struct_name == t2.struct_name
        return True
    return False


class Symbol:
    def __init__(self, name: str, typ: Type, kind: str):
        self.name = name
        self.typ = typ
        self.kind = kind


class StaticChecker(ASTVisitor):
    def check_program(self, ast):
        return self.visit(ast)

    def lookup(self, name: str) -> Optional[Symbol]:
        for scope in reversed(self.env_stack):
            if name in scope:
                return scope[name]
        return None

    def visit_program(self, node: "Program", o: Any = None):
        self.global_funcs = {
            "readInt": (IntType(), [], None),
            "readFloat": (FloatType(), [], None),
            "readString": (StringType(), [], None),
            "printInt": (VoidType(), [IntType()], None),
            "printFloat": (VoidType(), [FloatType()], None),
            "printString": (VoidType(), [StringType()], None),
        }
        self.global_structs = {}
        self.env_stack = []
        self.loop_stack = 0
        self.switch_stack = 0
        
        for decl in node.decls:
            self.visit(decl)
            
        return "Static checking passed"

    def visit_struct_decl(self, node: "StructDecl", o: Any = None):
        if node.name in self.global_structs:
            raise Redeclared("Struct", node.name)
            
        member_names = set()
        for member in node.members:
            if member.name in member_names:
                raise Redeclared("Member", member.name)
            member_names.add(member.name)
            if isinstance(member.member_type, StructType):
                if member.member_type.struct_name not in self.global_structs:
                    raise UndeclaredStruct(member.member_type.struct_name)
                    
        self.global_structs[node.name] = node

    def visit_member_decl(self, node: "MemberDecl", o: Any = None):
        pass

    def visit_func_decl(self, node: "FuncDecl", o: Any = None):
        if node.name in self.global_funcs:
            raise Redeclared("Function", node.name)
            
        self.current_func_name = node.name
        self.current_func_params = set()
        self.current_func_return_type = node.return_type
        
        ret_ty = node.return_type if node.return_type else AutoType()
        self.global_funcs[node.name] = (ret_ty, [p.param_type for p in node.params], node)
        
        self.env_stack.append({})
        
        for param in node.params:
            if param.name in self.current_func_params:
                raise Redeclared("Parameter", param.name)
            if isinstance(param.param_type, StructType):
                if param.param_type.struct_name not in self.global_structs:
                    raise UndeclaredStruct(param.param_type.struct_name)
            self.current_func_params.add(param.name)
            self.env_stack[-1][param.name] = Symbol(param.name, param.param_type, "Parameter")
            
        if isinstance(node.body, BlockStmt):
            self.visit(node.body)
        else:
            for stmt in node.body:
                self.visit(stmt)
                
        self.env_stack.pop()
        self.current_func_params = set()
        
        if self.current_func_return_type is None or isinstance(self.current_func_return_type, AutoType):
            self.current_func_return_type = VoidType()
            
        orig = self.global_funcs[node.name]
        self.global_funcs[node.name] = (self.current_func_return_type, orig[1], orig[2])

    def visit_param(self, node: "Param", o: Any = None):
        pass

    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        self.env_stack.append({})
        for stmt in node.statements:
            self.visit(stmt)
            
        for var_name, sym in self.env_stack[-1].items():
            typ = resolve_type(sym.typ)
            if isinstance(typ, AutoType):
                raise TypeCannotBeInferred(node)
                
        self.env_stack.pop()

    def visit_var_decl(self, node: "VarDecl", o: Any = None):
        if node.name in self.env_stack[-1]:
            raise Redeclared("Variable", node.name)
        if hasattr(self, "current_func_params") and node.name in self.current_func_params:
            raise Redeclared("Variable", node.name)
            
        if node.var_type:
            if isinstance(node.var_type, StructType):
                if node.var_type.struct_name not in self.global_structs:
                    raise UndeclaredStruct(node.var_type.struct_name)
            sym = Symbol(node.name, node.var_type, "Variable")
        else:
            sym = Symbol(node.name, AutoType(), "Variable")
            
        self.env_stack[-1][node.name] = sym
            
        if node.init_value:
            if node.var_type:
                expected = node.var_type
                rhs_ty = self.visit(node.init_value, o=expected)
                rhs_ty = resolve_type(rhs_ty)
                if isinstance(rhs_ty, AutoType):
                    rhs_ty.resolved_type = expected
                    rhs_ty = expected
                if not type_equivalent(expected, rhs_ty):
                    raise TypeMismatchInStatement(node)
            else:
                rhs_ty = self.visit(node.init_value)
                rhs_ty = resolve_type(rhs_ty)
                if isinstance(rhs_ty, AutoType):
                    raise TypeCannotBeInferred(node)
                sym.typ = rhs_ty


    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        cond_ty = self.visit(node.condition)
        cond_ty = resolve_type(cond_ty)
        if isinstance(cond_ty, AutoType):
            raise TypeCannotBeInferred(node.condition)
        if not isinstance(cond_ty, IntType):
            raise TypeMismatchInStatement(node)
            
        self.visit(node.then_stmt)
        if node.else_stmt:
            self.visit(node.else_stmt)

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        cond_ty = self.visit(node.condition)
        cond_ty = resolve_type(cond_ty)
        if isinstance(cond_ty, AutoType):
            raise TypeCannotBeInferred(node.condition)
        if not isinstance(cond_ty, IntType):
            raise TypeMismatchInStatement(node)
            
        self.loop_stack += 1
        self.visit(node.body)
        self.loop_stack -= 1

    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        if node.init:
            self.visit(node.init)
            
        if node.condition:
            cond_ty = self.visit(node.condition)
            cond_ty = resolve_type(cond_ty)
            if isinstance(cond_ty, AutoType):
                raise TypeCannotBeInferred(node.condition)
            if not isinstance(cond_ty, IntType):
                raise TypeMismatchInStatement(node)
                
        if node.update:
            self.visit(node.update)
            
        self.loop_stack += 1
        self.env_stack.append({})
        if isinstance(node.body, BlockStmt):
            for stmt in node.body.statements:
                self.visit(stmt)
            for var_name, sym in self.env_stack[-1].items():
                typ = resolve_type(sym.typ)
                if isinstance(typ, AutoType):
                    raise TypeCannotBeInferred(node.body)
        else:
            self.visit(node.body)
            for var_name, sym in self.env_stack[-1].items():
                typ = resolve_type(sym.typ)
                if isinstance(typ, AutoType):
                    raise TypeCannotBeInferred(node.body)
        self.env_stack.pop()
        self.loop_stack -= 1

    def visit_switch_stmt(self, node: "SwitchStmt", o: Any = None):
        expr_ty = self.visit(node.expr)
        expr_ty = resolve_type(expr_ty)
        if isinstance(expr_ty, AutoType):
            raise TypeCannotBeInferred(node.expr)
        if not isinstance(expr_ty, IntType):
            raise TypeMismatchInStatement(node)
            
        self.switch_stack += 1
        for case in node.cases:
            self.visit(case)
        if node.default_case:
            self.visit(node.default_case)
        self.switch_stack -= 1

    def visit_case_stmt(self, node: "CaseStmt", o: Any = None):
        cty = self.visit(node.expr)
        cty = resolve_type(cty)
        if isinstance(cty, AutoType):
            raise TypeCannotBeInferred(node.expr)
        if not isinstance(cty, IntType):
            raise TypeMismatchInStatement(node)
            
        for stmt in node.statements:
            self.visit(stmt)

    def visit_default_stmt(self, node: "DefaultStmt", o: Any = None):
        for stmt in node.statements:
            self.visit(stmt)

    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        if self.loop_stack == 0 and self.switch_stack == 0:
            raise MustInLoop(node)

    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        if self.loop_stack == 0:
            raise MustInLoop(node)

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        if node.expr:
            expected = self.current_func_return_type
            if isinstance(expected, AutoType):
                expected = None
            expr_type = self.visit(node.expr, o=expected)
            expr_type = resolve_type(expr_type)
            
            if isinstance(expr_type, AutoType):
                if expected and not isinstance(expected, AutoType):
                    expr_type.resolved_type = expected
                    expr_type = expected
                else:
                    raise TypeCannotBeInferred(node)
                    
            if self.current_func_return_type is None or isinstance(self.current_func_return_type, AutoType):
                self.current_func_return_type = expr_type
                orig = self.global_funcs[self.current_func_name]
                self.global_funcs[self.current_func_name] = (expr_type, orig[1], orig[2])
            else:
                if not type_equivalent(expr_type, self.current_func_return_type):
                    raise TypeMismatchInStatement(node)
        else:
            if self.current_func_return_type is None or isinstance(self.current_func_return_type, AutoType):
                self.current_func_return_type = VoidType()
                orig = self.global_funcs[self.current_func_name]
                self.global_funcs[self.current_func_name] = (VoidType(), orig[1], orig[2])
            else:
                if not isinstance(self.current_func_return_type, VoidType):
                    raise TypeMismatchInStatement(node)

    def visit_expr_stmt(self, node: "ExprStmt", o: Any = None):
        try:
            val = self.visit(node.expr, o)
            return val
        except TypeMismatchInExpression as e:
            if hasattr(e, 'expr') and e.expr is node.expr and isinstance(node.expr, AssignExpr):
                raise TypeMismatchInStatement(node)
            raise e
        except TypeCannotBeInferred as e:
            if hasattr(e, 'ctx') and e.ctx is node.expr and isinstance(node.expr, AssignExpr):
                raise TypeCannotBeInferred(node.expr)
            raise e

    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        left_ty = self.visit(node.left)
        right_ty = self.visit(node.right)
        
        left_ty = resolve_type(left_ty)
        right_ty = resolve_type(right_ty)
        
        op = node.operator
        
        if op in ('+', '-', '*', '/'):
            if isinstance(left_ty, AutoType) and isinstance(node.right, IntLiteral):
                left_ty.resolved_type = IntType()
                left_ty = IntType()
            elif isinstance(right_ty, AutoType) and isinstance(node.left, IntLiteral):
                right_ty.resolved_type = IntType()
                right_ty = IntType()
                
        if isinstance(left_ty, AutoType) or isinstance(right_ty, AutoType):
            raise TypeCannotBeInferred(node)
            
        if op in ('+', '-', '*', '/'):
            if not isinstance(left_ty, (IntType, FloatType)) or not isinstance(right_ty, (IntType, FloatType)):
                raise TypeMismatchInExpression(node)
            if isinstance(left_ty, IntType) and isinstance(right_ty, IntType):
                return IntType()
            return FloatType()
        elif op == '%':
            if not isinstance(left_ty, IntType) or not isinstance(right_ty, IntType):
                raise TypeMismatchInExpression(node)
            return IntType()
        elif op in ('==', '!=', '<', '<=', '>', '>='):
            if not isinstance(left_ty, (IntType, FloatType)) or not isinstance(right_ty, (IntType, FloatType)):
                raise TypeMismatchInExpression(node)
            return IntType()
        elif op in ('&&', '||'):
            if not isinstance(left_ty, IntType) or not isinstance(right_ty, IntType):
                raise TypeMismatchInExpression(node)
            return IntType()
        raise TypeMismatchInExpression(node)

    def visit_prefix_op(self, node: "PrefixOp", o: Any = None):
        op = node.operator
        typ = self.visit(node.operand)
        typ = resolve_type(typ)
        
        if isinstance(typ, AutoType):
            raise TypeCannotBeInferred(node)
            
        if op in ('+', '-'):
            if not isinstance(typ, (IntType, FloatType)):
                raise TypeMismatchInExpression(node)
            return typ
        elif op == '!':
            if not isinstance(typ, IntType):
                raise TypeMismatchInExpression(node)
            return IntType()
        elif op in ('++', '--'):
            if not isinstance(typ, IntType):
                raise TypeMismatchInExpression(node)
            if not isinstance(node.operand, (Identifier, MemberAccess)):
                raise TypeMismatchInExpression(node)
            return IntType()
        raise TypeMismatchInExpression(node)

    def visit_postfix_op(self, node: "PostfixOp", o: Any = None):
        op = node.operator
        typ = self.visit(node.operand)
        typ = resolve_type(typ)
        
        if isinstance(typ, AutoType):
            raise TypeCannotBeInferred(node)
            
        if op in ('++', '--'):
            if not isinstance(typ, IntType):
                raise TypeMismatchInExpression(node)
            if not isinstance(node.operand, (Identifier, MemberAccess)):
                raise TypeMismatchInExpression(node)
            return IntType()
        raise TypeMismatchInExpression(node)

    def visit_assign_expr(self, node: "AssignExpr", o: Any = None):
        lhs_ty = self.visit(node.lhs)
        lhs_ty_resolved = resolve_type(lhs_ty)
        
        expected = lhs_ty_resolved
        if isinstance(expected, AutoType):
            expected = None
            
        rhs_ty = self.visit(node.rhs, o=expected)
        
        lhs_ty = resolve_type(lhs_ty)
        rhs_ty = resolve_type(rhs_ty)
        
        if isinstance(lhs_ty, AutoType) and not isinstance(rhs_ty, AutoType):
            lhs_ty.resolved_type = rhs_ty
            lhs_ty = rhs_ty
            
        if isinstance(lhs_ty, AutoType) or isinstance(rhs_ty, AutoType):
            raise TypeCannotBeInferred(node)
            
        if not type_equivalent(lhs_ty, rhs_ty):
            raise TypeMismatchInExpression(node)
            
        if not isinstance(node.lhs, (Identifier, MemberAccess)):
            raise TypeMismatchInExpression(node)
            
        return lhs_ty

    def visit_member_access(self, node: "MemberAccess", o: Any = None):
        obj_ty = self.visit(node.obj)
        obj_ty = resolve_type(obj_ty)
        
        if isinstance(obj_ty, AutoType):
            raise TypeCannotBeInferred(node)
            
        if not isinstance(obj_ty, StructType):
            raise TypeMismatchInExpression(node)
            
        struct_decl = self.global_structs.get(obj_ty.struct_name)
        if not struct_decl:
            raise UndeclaredStruct(obj_ty.struct_name)
            
        for member in struct_decl.members:
            if member.name == node.member:
                mdl = member.member_type
                return mdl
                
        raise TypeMismatchInExpression(node)

    def visit_func_call(self, node: "FuncCall", o: Any = None):
        if node.name not in self.global_funcs:
            raise UndeclaredFunction(node.name)
            
        ret_ty, param_types, func_decl = self.global_funcs[node.name]
        
        if len(node.args) != len(param_types):
            raise TypeMismatchInExpression(node)
            
        for i in range(len(node.args)):
            arg_expected = param_types[i]
            arg_ty = self.visit(node.args[i], o=arg_expected)
            arg_ty = resolve_type(arg_ty)
            
            if isinstance(arg_ty, AutoType):
                arg_ty.resolved_type = arg_expected
                arg_ty = arg_expected
                
            if not type_equivalent(arg_ty, arg_expected):
                raise TypeMismatchInExpression(node)
                
        return ret_ty

    def visit_identifier(self, node: "Identifier", o: Any = None):
        sym = self.lookup(node.name)
        if not sym:
            raise UndeclaredIdentifier(node.name)
            
        typ = resolve_type(sym.typ)
        if isinstance(typ, AutoType):
            if o is not None and not isinstance(o, AutoType):
                typ.resolved_type = o
                return o
        return typ

    def visit_struct_literal(self, node: "StructLiteral", o: Any = None):
        if not isinstance(o, StructType):
            raise TypeCannotBeInferred(node)
            
        struct_decl = self.global_structs.get(o.struct_name)
        if struct_decl is None:
            raise UndeclaredStruct(o.struct_name)
            
        if len(node.values) != len(struct_decl.members):
            raise TypeMismatchInExpression(node)
            
        for i in range(len(node.values)):
            expected_type = struct_decl.members[i].member_type
            val_type = self.visit(node.values[i], o=expected_type)
            val_type = resolve_type(val_type)
            
            if isinstance(val_type, AutoType):
                val_type.resolved_type = expected_type
                val_type = expected_type
                
            if not type_equivalent(val_type, expected_type):
                raise TypeMismatchInExpression(node)
                
        return o

    def visit_int_literal(self, node: "IntLiteral", o: Any = None):
        return IntType()

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        return FloatType()

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        return StringType()

    def visit_int_type(self, node: "IntType", o: Any = None):
        return IntType()

    def visit_float_type(self, node: "FloatType", o: Any = None):
        return FloatType()

    def visit_string_type(self, node: "StringType", o: Any = None):
        return StringType()

    def visit_void_type(self, node: "VoidType", o: Any = None):
        return VoidType()

    def visit_struct_type(self, node: "StructType", o: Any = None):
        return node
