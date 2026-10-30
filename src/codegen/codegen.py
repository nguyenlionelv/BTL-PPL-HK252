"""
Code generator for TyC.
"""

from typing import Any

from ..utils.nodes import *
from ..utils.visitor import BaseVisitor
from .emitter import *
from .frame import *
from .io import IO_SYMBOL_LIST
from .utils import *


class StringArrayType:
    """Marker type for JVM main(String[] args)."""
    pass


class CodeGenerator(BaseVisitor):
    """Minimal AST -> Jasmin code generator."""

    def __init__(self):
        self.emit = None
        self.functions = {}
        self.structs = {} # Map struct name to StructDecl
        self.current_return_type = VoidType()
        self.class_name = "TyC"
        self.expected_type = None

    def _lookup_symbol(self, name: str, sym_list: list[Symbol]) -> Symbol:
        for sym in reversed(sym_list):
            if sym.name == name:
                return sym
        raise RuntimeError(f"Undeclared symbol: {name}")

    def _infer_type(self, node: Expr, o: Access):
        if isinstance(node, IntLiteral):
            return IntType()
        if isinstance(node, FloatLiteral):
            return FloatType()
        if isinstance(node, StringLiteral):
            return StringType()
        if isinstance(node, Identifier):
            sym = self._lookup_symbol(node.name, o.sym)
            return sym.type
        if isinstance(node, AssignExpr):
            return self._infer_type(node.rhs, o)
        if isinstance(node, FuncCall):
            return self.functions[node.name].type.return_type
        if isinstance(node, MemberAccess):
            obj_type = self._infer_type(node.obj, o)
            if is_struct_type(obj_type):
                struct_decl = self.structs.get(obj_type.struct_name)
                if struct_decl:
                    for member in struct_decl.members:
                        if member.name == node.member:
                            return member.member_type
            return IntType()
        if isinstance(node, StructLiteral):
            if hasattr(node, "struct_name"):
                return StructType(node.struct_name)
            if self.expected_type and is_struct_type(self.expected_type):
                return self.expected_type
            return IntType()
        if isinstance(node, BinaryOp):
            if node.operator in ["+", "-", "*", "/", "%"]:
                left_type = self._infer_type(node.left, o)
                right_type = self._infer_type(node.right, o)
                if is_float_type(left_type) or is_float_type(right_type):
                    return FloatType()
                return IntType()
            if node.operator in ["<", "<=", ">", ">=", "==", "!="]:
                return IntType()
            if node.operator in ["&&", "||"]:
                return IntType()
        if isinstance(node, PrefixOp):
            return self._infer_type(node.operand, o)
        return IntType()

    def _infer_func_return_type(self, body):
        """Scan function body for the first ReturnStmt with an expression to infer return type."""
        if isinstance(body, BlockStmt):
            for stmt in body.statements:
                if isinstance(stmt, ReturnStmt) and stmt.expr is not None:
                    if isinstance(stmt.expr, IntLiteral):
                        return IntType()
                    if isinstance(stmt.expr, FloatLiteral):
                        return FloatType()
                    if isinstance(stmt.expr, StringLiteral):
                        return StringType()
                    if isinstance(stmt.expr, StructLiteral):
                        return StructType(getattr(stmt.expr, 'struct_name', None) or 'Unknown')
                result = self._infer_func_return_type(stmt)
                if result is not None:
                    return result
        elif isinstance(body, ReturnStmt) and body.expr is not None:
            if isinstance(body.expr, IntLiteral):
                return IntType()
            if isinstance(body.expr, FloatLiteral):
                return FloatType()
            if isinstance(body.expr, StringLiteral):
                return StringType()
        elif isinstance(body, IfStmt):
            r = self._infer_func_return_type(body.then_stmt)
            if r is not None:
                return r
            if body.else_stmt:
                return self._infer_func_return_type(body.else_stmt)
        elif isinstance(body, WhileStmt):
            return self._infer_func_return_type(body.body)
        elif isinstance(body, ForStmt):
            return self._infer_func_return_type(body.body)
        return None

    def visit_program(self, node: Program, o: Any = None):
        self.emit = Emitter(f"{self.class_name}.j")
        self.emit.print_out(self.emit.emit_prolog(self.class_name))

        for io_sym in IO_SYMBOL_LIST:
            self.functions[io_sym.name] = io_sym

        for decl in node.decls:
            if isinstance(decl, StructDecl):
                self.structs[decl.name] = decl
                self.visit(decl)
            elif isinstance(decl, FuncDecl):
                if decl.return_type is not None:
                    return_type = decl.return_type
                else:
                    # Infer return type from body
                    inferred = self._infer_func_return_type(decl.body)
                    return_type = inferred if inferred is not None else VoidType()
                param_types = [p.param_type for p in decl.params]
                self.functions[decl.name] = Symbol(
                    decl.name, FunctionType(param_types, return_type), CName(self.class_name)
                )

        for decl in node.decls:
            if isinstance(decl, FuncDecl):
                self.visit(decl, None)

        # Default constructor for TyC class
        self.emit.print_out(".method public <init>()V\n")
        self.emit.print_out("    aload_0\n")
        self.emit.print_out("    invokespecial java/lang/Object/<init>()V\n")
        self.emit.print_out("    return\n")
        self.emit.print_out(".end method\n")

        self.emit.emit_epilog()

    def visit_func_decl(self, node: FuncDecl, o: Any = None):
        if node.return_type is not None:
            self.current_return_type = node.return_type
        else:
            fn_sym = self.functions.get(node.name)
            if fn_sym and hasattr(fn_sym, 'type') and hasattr(fn_sym.type, 'return_type'):
                self.current_return_type = fn_sym.type.return_type
            else:
                self.current_return_type = VoidType()
        frame = Frame(node.name, self.current_return_type)
        frame.enter_scope(True)

        if node.name == "main":
            mtype = FunctionType([StringArrayType()], VoidType())
        else:
            mtype = FunctionType([p.param_type for p in node.params], self.current_return_type)

        self.emit.print_out(self.emit.emit_method(node.name, mtype, True))

        start_label = frame.get_start_label()
        end_label = frame.get_end_label()
        self.emit.print_out(self.emit.emit_label(start_label, frame))

        local_syms: list[Symbol] = []
        if node.name == "main":
            args_idx = frame.get_new_index()
            self.emit.print_out(
                self.emit.emit_var(
                    args_idx, "args", StringArrayType(), start_label, end_label
                )
            )

        for param in node.params:
            idx = frame.get_new_index()
            self.emit.print_out(
                self.emit.emit_var(idx, param.name, param.param_type, start_label, end_label)
            )
            local_syms.append(Symbol(param.name, param.param_type, Index(idx)))

        sub_body = SubBody(frame, local_syms)
        self.visit(node.body, sub_body)

        if is_void_type(self.current_return_type):
            self.emit.print_out(self.emit.emit_return(VoidType(), frame))

        self.emit.print_out(self.emit.emit_label(end_label, frame))
        frame.exit_scope()
        self.emit.print_out(self.emit.emit_end_method(frame))
        # self.current_return_type = node.return_type if node.return_type else VoidType()
        # frame = Frame(node.name, self.current_return_type)
        # frame.enter_scope(True)

        # if node.name == "main":
        #     mtype = FunctionType([StringArrayType()], VoidType())
        # else:
        #     mtype = FunctionType([p.param_type for p in node.params], self.current_return_type)

        # self.emit.print_out(self.emit.emit_method(node.name, mtype, True))

        # start_label = frame.get_start_label()
        # end_label = frame.get_end_label()
        # self.emit.print_out(self.emit.emit_label(start_label, frame))

        # local_syms: list[Symbol] = []
        # if node.name == "main":
        #     args_idx = frame.get_new_index()
        #     self.emit.print_out(
        #         self.emit.emit_var(
        #             args_idx, "args", StringArrayType(), start_label, end_label
        #         )
        #     )

        # for param in node.params:
        #     idx = frame.get_new_index()
        #     self.emit.print_out(
        #         self.emit.emit_var(idx, param.name, param.param_type, start_label, end_label)
        #     )
        #     local_syms.append(Symbol(param.name, param.param_type, Index(idx)))

        # sub_body = SubBody(frame, local_syms)
        # self.visit(node.body, sub_body)

        # if is_void_type(self.current_return_type):
        #     self.emit.print_out(self.emit.emit_return(VoidType(), frame))

        # self.emit.print_out(self.emit.emit_label(end_label, frame))
        # frame.exit_scope()
        # self.emit.print_out(self.emit.emit_end_method(frame))

    def visit_block_stmt(self, node: BlockStmt, o: SubBody = None):
        o.frame.enter_scope(False)
        start_label = o.frame.get_start_label()
        end_label = o.frame.get_end_label()
        self.emit.print_out(self.emit.emit_label(start_label, o.frame))
        
        new_o = SubBody(o.frame, list(o.sym))
        for stmt in node.statements:
            new_o = self.visit(stmt, new_o)
            
        self.emit.print_out(self.emit.emit_label(end_label, o.frame))
        o.frame.exit_scope()
        return o # Return o because block scope ended

    def visit_var_decl(self, node: VarDecl, o: SubBody = None):
        frame = o.frame
        idx = frame.get_new_index()
        var_type = node.var_type if node.var_type else self._infer_type(node.init_value, Access(frame, o.sym))
        self.emit.print_out(
            self.emit.emit_var(
                idx, node.name, var_type, frame.get_start_label(), frame.get_end_label()
            )
        )
        if node.init_value is not None:
            old_expected = self.expected_type
            self.expected_type = var_type
            rhs_code, rhs_type = self.visit(node.init_value, Access(frame, o.sym))
            self.expected_type = old_expected

            if is_struct_type(var_type) and is_struct_type(rhs_type):
                struct_name = var_type.struct_name
                struct_decl = self.structs.get(struct_name)
                if struct_decl and isinstance(node.init_value, Identifier):
                    tmp_idx = frame.get_new_index()
                    self.emit.print_out(rhs_code)
                    self.emit.print_out(self.emit.emit_write_var("__tmp__", rhs_type, tmp_idx, frame))
                    copy_code = self.emit.emit_new_instance(struct_name, frame)
                    
                    # For each field, load src field and store in dest
                    for member in struct_decl.members:
                        mtype = member.member_type
                        field_desc = f"{struct_name}/{member.name}"
                        copy_code += self.emit.emit_dup(frame)
                        copy_code += self.emit.emit_read_var("__tmp__", rhs_type, tmp_idx, frame)
                        copy_code += self.emit.emit_get_field(field_desc, mtype, frame)
                        copy_code += self.emit.emit_put_field(field_desc, mtype, frame)
                    self.emit.print_out(copy_code)
                    self.emit.print_out(self.emit.emit_write_var(node.name, var_type, idx, frame))
                    o.sym.append(Symbol(node.name, var_type, Index(idx)))
                    return o
            self.emit.print_out(rhs_code)
            if is_float_type(var_type) and is_int_type(rhs_type):
                self.emit.print_out(self.emit.emit_i2f(frame))
            self.emit.print_out(self.emit.emit_write_var(node.name, var_type, idx, frame))
        else:

            if is_int_type(var_type):
                self.emit.print_out(self.emit.emit_push_iconst(0, frame))
            elif is_float_type(var_type):
                self.emit.print_out(self.emit.emit_push_fconst("0.0", frame))
            elif is_string_type(var_type):
                self.emit.print_out(self.emit.emit_push_const("", StringType(), frame))
            elif is_struct_type(var_type):
                self.emit.print_out(self.emit.emit_new_instance(var_type.struct_name, frame))
            else:

                self.emit.print_out(self.emit.emit_push_iconst(0, frame))
            self.emit.print_out(self.emit.emit_write_var(node.name, var_type, idx, frame))

        o.sym.append(Symbol(node.name, var_type, Index(idx)))
        return o

    def visit_expr_stmt(self, node: ExprStmt, o: SubBody = None):
        code, expr_type = self.visit(node.expr, Access(o.frame, o.sym))
        self.emit.print_out(code)
        if not is_void_type(expr_type):
            self.emit.print_out(self.emit.emit_pop(o.frame))
        return o

    def visit_if_stmt(self, node: IfStmt, o: SubBody = None):
        frame = o.frame
        cond_code, _ = self.visit(node.condition, Access(frame, o.sym))
        self.emit.print_out(cond_code)
        
        else_label = frame.get_new_label()
        end_label = frame.get_new_label()
        
        self.emit.print_out(self.emit.emit_if_false(else_label, frame))
        if node.then_stmt:
            self.visit(node.then_stmt, o)
        self.emit.print_out(self.emit.emit_goto(end_label, frame))
        self.emit.print_out(self.emit.emit_label(else_label, frame))
        if node.else_stmt:
            self.visit(node.else_stmt, o)
        self.emit.print_out(self.emit.emit_label(end_label, frame))
        return o

    def visit_while_stmt(self, node: WhileStmt, o: SubBody = None):
        o.frame.enter_loop()
        frame = o.frame
        start_label = frame.get_continue_label()
        end_label = frame.get_break_label()
        
        self.emit.print_out(self.emit.emit_label(start_label, frame))
        cond_code, _ = self.visit(node.condition, Access(frame, o.sym))
        self.emit.print_out(cond_code)
        self.emit.print_out(self.emit.emit_if_false(end_label, frame))
        self.visit(node.body, o)
        self.emit.print_out(self.emit.emit_goto(start_label, frame))
        self.emit.print_out(self.emit.emit_label(end_label, frame))
        
        o.frame.exit_loop()
        return o

    def visit_for_stmt(self, node: ForStmt, o: SubBody = None):
        frame = o.frame
        # New scope forloop if init is VarDecl
        frame.enter_scope(False)
        start_label_scope = frame.get_start_label()
        end_label_scope = frame.get_end_label()
        self.emit.print_out(self.emit.emit_label(start_label_scope, frame))
        
        # Copy symbols for the forloop scope
        new_o = SubBody(frame, list(o.sym))
        
        if node.init:
            new_o = self.visit(node.init, new_o)
            
        frame.enter_loop()
        update_label = frame.get_continue_label()
        end_label = frame.get_break_label()
        start_label = frame.get_new_label()
        
        self.emit.print_out(self.emit.emit_label(start_label, frame))
        if node.condition:
            cond_code, _ = self.visit(node.condition, Access(frame, new_o.sym))
            self.emit.print_out(cond_code)
            self.emit.print_out(self.emit.emit_if_false(end_label, frame))
            
        self.visit(node.body, new_o)
        
        self.emit.print_out(self.emit.emit_label(update_label, frame))
        if node.update:
            update_code, _ = self.visit(node.update, Access(frame, new_o.sym))
            self.emit.print_out(update_code)
            self.emit.print_out(self.emit.emit_pop(frame))
            
        self.emit.print_out(self.emit.emit_goto(start_label, frame))
        self.emit.print_out(self.emit.emit_label(end_label, frame))
        
        frame.exit_loop()
        self.emit.print_out(self.emit.emit_label(end_label_scope, frame))
        frame.exit_scope()
        return o

    def visit_break_stmt(self, node: BreakStmt, o: SubBody = None):
        break_label = o.frame.get_break_label()
        self.emit.print_out(self.emit.emit_goto(break_label, o.frame))
        return o

    def visit_continue_stmt(self, node: ContinueStmt, o: SubBody = None):
        continue_label = o.frame.get_continue_label()
        self.emit.print_out(self.emit.emit_goto(continue_label, o.frame))
        return o

    def visit_return_stmt(self, node: ReturnStmt, o: SubBody = None):
        if node.expr is None:
            self.emit.print_out(self.emit.emit_return(VoidType(), o.frame))
            return o
        old_expected = self.expected_type
        self.expected_type = self.current_return_type
        code, ret_type = self.visit(node.expr, Access(o.frame, o.sym))
        self.expected_type = old_expected
        self.emit.print_out(code)
        self.emit.print_out(self.emit.emit_return(ret_type, o.frame))
        return o

    def visit_binary_op(self, node: BinaryOp, o: Access = None):
        left_code, left_type = self.visit(node.left, o)
        right_code, right_type = self.visit(node.right, o)
        frame = o.frame

        if node.operator in ["+", "-"]:
            result_type = FloatType() if is_float_type(left_type) or is_float_type(right_type) else IntType()
            if is_float_type(result_type) and is_int_type(left_type):
                left_code += self.emit.emit_i2f(frame)
            # code += right_code
            if is_float_type(result_type) and is_int_type(right_type):
                right_code += self.emit.emit_i2f(frame)
            op_code = self.emit.emit_add_op(node.operator, result_type, frame)
            return left_code + right_code + op_code, result_type
            
        if node.operator in ["*", "/"]:
            result_type = FloatType() if is_float_type(left_type) or is_float_type(right_type) else IntType()
            # code = left_code
            if is_float_type(result_type) and is_int_type(left_type):
                left_code += self.emit.emit_i2f(frame)
            # code += right_code
            if is_float_type(result_type) and is_int_type(right_type):
                right_code += self.emit.emit_i2f(frame)
            op_code = self.emit.emit_mul_op(node.operator, result_type, frame)
            return left_code + right_code + op_code, result_type
        
        if node.operator == "%":
            return left_code + right_code + self.emit.emit_mod(frame), IntType()
        
        if node.operator == "&&":
            label_false = frame.get_new_label()
            label_end = frame.get_new_label()
            # Push left, if false go to label_false
            code = left_code + self.emit.emit_if_false(label_false, frame)
            # Push right, if false go to label_false
            code += right_code + self.emit.emit_if_false(label_false, frame)
            # Both true
            code += self.emit.emit_push_iconst(1, frame) + self.emit.emit_goto(label_end, frame)
            
            # False case
            code += self.emit.emit_label(label_false, frame)
            code += self.emit.emit_push_iconst(0, frame)
            
            # End
            code += self.emit.emit_label(label_end, frame)
            return code, IntType()

        if node.operator == "||":
            label_true = frame.get_new_label()
            label_end = frame.get_new_label()
            # Push left, if true go to label_true
            code = left_code + self.emit.emit_if_true(label_true, frame)
            # Push right, if true go to label_true
            code += right_code + self.emit.emit_if_true(label_true, frame)
            
            # Both false
            code += self.emit.emit_push_iconst(0, frame) + self.emit.emit_goto(label_end, frame)
            
            # True label
            code += self.emit.emit_label(label_true, frame)
            code += self.emit.emit_push_iconst(1, frame)
            
            # End label
            code += self.emit.emit_label(label_end, frame)
            return code, IntType()

        if node.operator in ["<", "<=", ">", ">=", "==", "!="]:
            op_type = FloatType() if is_float_type(left_type) or is_float_type(right_type) else IntType()            
            code = left_code
            if is_float_type(op_type) and is_int_type(left_type):
                code += self.emit.emit_i2f(frame)
            code += right_code
            if is_float_type(op_type) and is_int_type(right_type):
                code += self.emit.emit_i2f(frame)
            return code + self.emit.emit_re_op(node.operator, op_type, frame), IntType()
        raise RuntimeError(f"Unsupported operator: {node.operator}")

    def visit_assign_expr(self, node: AssignExpr, o: Access = None):
        if isinstance(node.lhs, Identifier):
            lhs_sym = self._lookup_symbol(node.lhs.name, o.sym)
            old_expected = self.expected_type
            self.expected_type = lhs_sym.type
            # rhs_code, rhs_type = self.visit(node.rhs, Access(o.frame, o.sym))
            rhs_code, rhs_type = self.visit(node.rhs, o)
            self.expected_type = old_expected
            idx = lhs_sym.value.value
            code = rhs_code
            # if is_float_type(lhs_sym.type) and is_int_type(rhs_type):
            #     code += self.emit.emit_i2f(o.frame)
            code += self.emit.emit_dup(o.frame) + self.emit.emit_write_var(
                node.lhs.name, lhs_sym.type, idx, o.frame
            )
            return code, lhs_sym.type
        elif isinstance(node.lhs, MemberAccess):
            # obj.member = rhs
            obj_code, obj_type = self.visit(node.lhs.obj, o)
            
            struct_name = obj_type.struct_name
            # Find field type
            field_type = IntType()
            struct_decl = self.structs.get(struct_name)
            if struct_decl:
                for member in struct_decl.members:
                    if member.name == node.lhs.member:
                        field_type = member.member_type
                        break
            
            old_expected = self.expected_type
            self.expected_type = field_type
            rhs_code, rhs_type = self.visit(node.rhs, Access(o.frame, o.sym))
            self.expected_type = old_expected
            code = obj_code
            code += rhs_code
            if is_float_type(field_type) and is_int_type(rhs_type):
                code += self.emit.emit_i2f(o.frame)
            # Stack: [.., objref, value]
            # dup_x1 -> [.., value, objref, value]
            code += self.emit.emit_dup_x1(o.frame)

            code += self.emit.emit_put_field(f"{struct_name}/{node.lhs.member}", field_type, o.frame)
            return code, field_type
            
        raise RuntimeError("Unsupported assignment LHS")

    def visit_func_call(self, node: FuncCall, o: Access = None):
        frame = o.frame
        fn_sym = self.functions[node.name]
        fn_type = fn_sym.type
        code = ""
        for i, arg in enumerate(node.args):
            old_expected = self.expected_type
            if i < len(fn_type.param_types):
                self.expected_type = fn_type.param_types[i]
            arg_code, _ = self.visit(arg, o)
            self.expected_type = old_expected
            code += arg_code
        # for arg in node.args:
        #     arg_code, _ = self.visit(arg, o)
        #     code += arg_code
        code += self.emit.emit_invoke_static(f"{fn_sym.value.value}/{node.name}", fn_type, frame)
        return code, fn_type.return_type

    def visit_identifier(self, node: Identifier, o: Access = None):
        sym = self._lookup_symbol(node.name, o.sym)
        return self.emit.emit_read_var(node.name, sym.type, sym.value.value, o.frame), sym.type

    def visit_int_literal(self, node: IntLiteral, o: Access = None):
        return self.emit.emit_push_iconst(node.value, o.frame), IntType()

    def visit_float_literal(self, node: FloatLiteral, o: Access = None):
        return self.emit.emit_push_fconst(str(node.value), o.frame), FloatType()

    def visit_string_literal(self, node: StringLiteral, o: Access = None):
        return self.emit.emit_push_const(node.value, StringType(), o.frame), StringType()

    def visit_struct_decl(self, node: StructDecl, o: Any = None):
        # Generate a separate .j file for the struct
        struct_emitter = Emitter(f"{node.name}.j")
        struct_emitter.print_out(struct_emitter.jvm.emitSOURCE(f"{node.name}.java"))
        struct_emitter.print_out(struct_emitter.jvm.emitCLASS(f"public {node.name}"))
        struct_emitter.print_out(struct_emitter.jvm.emitSUPER("java/lang/Object"))
        
        # Fields
        for member in node.members:
            field_name = member.name
            field_type = self.emit.get_jvm_type(member.member_type)
            struct_emitter.print_out(f".field public {field_name} {field_type}\n")
            
        # Default constructor
        frame = Frame("<init>", VoidType())
        frame.enter_scope(True)
        # aload_0 for this
        frame.get_new_index()
        
        struct_emitter.print_out(".method public <init>()V\n")
        struct_emitter.print_out("    aload_0\n")
        frame.push()
        struct_emitter.print_out("    invokespecial java/lang/Object/<init>()V\n")
        frame.pop()
        
        for member in node.members:
            struct_emitter.print_out("    aload_0\n")
            frame.push()
            if is_int_type(member.member_type):
                struct_emitter.print_out("    iconst_0\n")
                frame.push()
            elif is_float_type(member.member_type):
                struct_emitter.print_out("    fconst_0\n")
                frame.push()
            elif is_string_type(member.member_type):
                struct_emitter.print_out("    ldc \"\"\n")
                frame.push()
            elif is_struct_type(member.member_type):
                struct_emitter.print_out(f"    new {member.member_type.struct_name}\n")
                frame.push()
                struct_emitter.print_out("    dup\n")
                frame.push()
                struct_emitter.print_out(f"    invokespecial {member.member_type.struct_name}/<init>()V\n")
                frame.pop()
            else:
                struct_emitter.print_out("    iconst_0\n")
                frame.push()
            
            field_type = self.emit.get_jvm_type(member.member_type)
            struct_emitter.print_out(f"    putfield {node.name}/{member.name} {field_type}\n")
            frame.pop() # value
            frame.pop() # objectref
            
        struct_emitter.print_out("    return\n")
        struct_emitter.print_out(f"    .limit stack {frame.get_max_op_stack_size()}\n")
        struct_emitter.print_out(f"    .limit locals {frame.get_max_index()}\n")
        struct_emitter.print_out(".end method\n")
        
        struct_emitter.emit_epilog()
        return None

    def visit_switch_stmt(self, node: SwitchStmt, o: SubBody = None):
        o.frame.enter_loop()
        frame = o.frame
        expr_code, expr_type = self.visit(node.expr, Access(frame, o.sym))
        self.emit.print_out(expr_code)
        
        end_label = frame.get_break_label()
        next_case_label = frame.get_new_label()
        
        case_labels = [frame.get_new_label() for _ in node.cases]
        default_label = frame.get_new_label()
        
        for i, case in enumerate(node.cases):
            self.emit.print_out(self.emit.emit_label(next_case_label, frame))
            next_case_label = frame.get_new_label()
            
            # Case expression
            val_code, _ = self.visit(case.expr, Access(frame, o.sym))
            self.emit.print_out(self.emit.emit_dup(frame)) # Dup switch expr value
            self.emit.print_out(val_code)
            self.emit.print_out(self.emit.emit_re_op("==", IntType(), frame))
            self.emit.print_out(self.emit.emit_if_true(case_labels[i], frame))
            
        self.emit.print_out(self.emit.emit_goto(default_label, frame))
            
        for i, case in enumerate(node.cases):
            self.emit.print_out(self.emit.emit_label(case_labels[i], frame))
            for stmt in case.statements:
                self.visit(stmt, o)
            
        # Default
        self.emit.print_out(self.emit.emit_label(default_label, frame))
        if node.default_case:
            for stmt in node.default_case.statements:
                self.visit(stmt, o)
                
        self.emit.print_out(self.emit.emit_label(end_label, frame))
        self.emit.print_out(self.emit.emit_pop(frame)) # Pop the switch expr value
        o.frame.exit_loop()
        return o

    def visit_member_access(self, node: MemberAccess, o: Access = None):
        frame = o.frame
        obj_code, obj_type = self.visit(node.obj, o)
        if not is_struct_type(obj_type):
            raise RuntimeError("Member access on non-struct type")
        
        struct_name = obj_type.struct_name
        field_type = IntType()
        struct_decl = self.structs.get(struct_name)
        if struct_decl:
            for member in struct_decl.members:
                if member.name == node.member:
                    field_type = member.member_type
                    break
        
        code = obj_code + self.emit.emit_get_field(f"{struct_name}/{node.member}", field_type, frame)
        return code, field_type

    def visit_struct_literal(self, node: StructLiteral, o: Access = None):
        frame = o.frame

        struct_name = node.struct_name if hasattr(node, "struct_name") else self.expected_type.struct_name
        code = self.emit.emit_new_instance(struct_name, frame)
        
        struct_decl = self.structs.get(struct_name)
        if struct_decl and node.values:
            for i, expr in enumerate(node.values):
                if i < len(struct_decl.members):
                    member = struct_decl.members[i]

                    code += self.emit.emit_dup(frame)
                    old_expected = self.expected_type
                    self.expected_type = member.member_type
                    val_code, val_type = self.visit(expr, Access(frame, o.sym))
                    self.expected_type = old_expected
                    code += val_code
                    if is_float_type(member.member_type) and is_int_type(val_type):
                        code += self.emit.emit_i2f(frame)
                    code += self.emit.emit_put_field(f"{struct_name}/{member.name}", member.member_type, frame)
                    
        return code, StructType(struct_name)

    def visit_prefix_op(self, node: PrefixOp, o: Access = None):
        if node.operator == "!":
            operand_code, _ = self.visit(node.operand, o)
            label_true = o.frame.get_new_label()
            label_end = o.frame.get_new_label()
            code = operand_code
            code += self.emit.emit_if_true(label_true, o.frame)
            # If not true, push 1
            code += self.emit.emit_push_iconst(1, o.frame)
            code += self.emit.emit_goto(label_end, o.frame)
            # If true, push 0
            code += self.emit.emit_label(label_true, o.frame)
            code += self.emit.emit_push_iconst(0, o.frame)
            code += self.emit.emit_label(label_end, o.frame)
            return code, IntType()
            
        if node.operator in ["+", "-"]:
            operand_code, operand_type = self.visit(node.operand, o)
            if node.operator == "-":
                return operand_code + self.emit.emit_neg_op(operand_type, o.frame), operand_type
            return operand_code, operand_type
            
        if node.operator in ["++", "--"]:
            if isinstance(node.operand, Identifier):
                sym = self._lookup_symbol(node.operand.name, o.sym)
                idx = sym.value.value
                code = self.emit.emit_read_var(node.operand.name, sym.type, idx, o.frame)
                code += self.emit.emit_push_iconst(1, o.frame)
                code += self.emit.emit_add_op("+" if node.operator == "++" else "-", sym.type, o.frame)
                code += self.emit.emit_dup(o.frame)
                code += self.emit.emit_write_var(node.operand.name, sym.type, idx, o.frame)
                return code, sym.type
            elif isinstance(node.operand, MemberAccess):

                obj_code, obj_type = self.visit(node.operand.obj, o)
                struct_name = obj_type.struct_name

                field_type = IntType()
                struct_decl = self.structs.get(struct_name)
                if struct_decl:
                    for member in struct_decl.members:
                        if member.name == node.operand.member:
                            field_type = member.member_type
                            break
                            
                code = obj_code + self.emit.emit_dup(o.frame) 
                code += self.emit.emit_get_field(f"{struct_name}/{node.operand.member}", field_type, o.frame)
                code += self.emit.emit_push_iconst(1, o.frame)
                code += self.emit.emit_add_op("+" if node.operator == "++" else "-", field_type, o.frame)
                code += self.emit.emit_dup_x1(o.frame) #  stack = [obj, value] -> [value, obj, value]
                code += self.emit.emit_put_field(f"{struct_name}/{node.operand.member}", field_type, o.frame)
                return code, field_type
                
        raise RuntimeError(f"Unsupported prefix operator: {node.operator}")

    def visit_postfix_op(self, node: PostfixOp, o: Access = None):
        if node.operator in ["++", "--"]:
            if isinstance(node.operand, Identifier):
                sym = self._lookup_symbol(node.operand.name, o.sym)
                idx = sym.value.value
                code = self.emit.emit_read_var(node.operand.name, sym.type, idx, o.frame)
                code += self.emit.emit_dup(o.frame) # Val for expression
                code += self.emit.emit_push_iconst(1, o.frame)
                code += self.emit.emit_add_op("+" if node.operator == "++" else "-", sym.type, o.frame)
                code += self.emit.emit_write_var(node.operand.name, sym.type, idx, o.frame)
                return code, sym.type
            elif isinstance(node.operand, MemberAccess):
                obj_code, obj_type = self.visit(node.operand.obj, o)
                struct_name = obj_type.struct_name
                # Find field type
                field_type = IntType()
                struct_decl = self.structs.get(struct_name)
                if struct_decl:
                    for member in struct_decl.members:
                        if member.name == node.operand.member:
                            field_type = member.member_type
                            break
                            
                code = obj_code + self.emit.emit_dup(o.frame) # [obj, obj]
                code += self.emit.emit_get_field(f"{struct_name}/{node.operand.member}", field_type, o.frame) # [obj, val]
                code += self.emit.emit_dup_x1(o.frame) # [val, obj, val]
                code += self.emit.emit_push_iconst(1, o.frame) # [val, obj, val, 1]
                code += self.emit.emit_add_op("+" if node.operator == "++" else "-", field_type, o.frame) # [val, obj, val_new]
                code += self.emit.emit_put_field(f"{struct_name}/{node.operand.member}", field_type, o.frame) # [val]
                return code, field_type
                
        raise RuntimeError(f"Unsupported postfix operator: {node.operator}")

