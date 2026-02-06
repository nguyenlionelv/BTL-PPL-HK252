"""
AST Generation module for TyC programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from functools import reduce
from build.TyCVisitor import TyCVisitor
from build.TyCParser import TyCParser
from src.utils.nodes import *


class ASTGeneration(TyCVisitor):
    """AST Generation visitor for TyC language."""

    # ========================================================================
    # Program and Declarations
    # ========================================================================

    def visitProgram(self, ctx: TyCParser.ProgramContext):
        # program: decl+ EOF;
        decls = [self.visit(d) for d in ctx.decl()]
        return Program(decls)

    def visitDecl(self, ctx: TyCParser.DeclContext):
        # decl: structdecl | funcdecl
        if ctx.structdecl():
            return self.visit(ctx.structdecl())
        return self.visit(ctx.funcdecl())

    def visitStructdecl(self, ctx: TyCParser.StructdeclContext):
        # structdecl: STRUCT ID LB structvarlist RB SEMI;
        name = ctx.ID().getText()
        members = self.visit(ctx.structvarlist())
        return StructDecl(name, members)

    def visitStructvarlist(self, ctx: TyCParser.StructvarlistContext):
        # structvarlist: stype ID SEMI structvarlist |;
        # Trường hợp rỗng
        if ctx.getChildCount() == 0:
            return []
        
        # Lấy member hiện tại
        varType = self.visit(ctx.stype())
        varName = ctx.ID().getText()
        currentMember = MemberDecl(varType, varName)
        
        # Nếu có structvarlist đệ quy, nối thêm vào
        if ctx.structvarlist():
            return [currentMember] + self.visit(ctx.structvarlist())
        return [currentMember]

    def visitFuncdecl(self, ctx: TyCParser.FuncdeclContext):
        # funcdecl: (ftype func) | func;
        funcContext = ctx.func()
        name = funcContext.ID().getText()
        params = self.visit(funcContext.paramlist())
        body = self.visit(funcContext.blockstmt())
        
        # Kiểm tra có return type không
        if ctx.ftype():
            returnType = self.visit(ctx.ftype())
        else:
            returnType = None  # Tự suy kiểu auto
        
        return FuncDecl(returnType, name, params, body)

    def visitParamlist(self, ctx: TyCParser.ParamlistContext):
        # paramlist: parameters |;
        if ctx.parameters():
            return self.visit(ctx.parameters())
        return []

    def visitParameters(self, ctx: TyCParser.ParametersContext):
        # parameters: param CM parameters | param;
        currentParam = self.visit(ctx.param())
        
        if ctx.parameters():
            return [currentParam] + self.visit(ctx.parameters())
        return [currentParam]

    def visitParam(self, ctx: TyCParser.ParamContext):
        # param: stype ID;
        paramType = self.visit(ctx.stype())
        name = ctx.ID().getText()
        return Param(paramType, name)

    # ========================================================================
    # Types
    # ========================================================================

    def visitStype(self, ctx: TyCParser.StypeContext):
        # stype: INTEGER | FLOAT | STRING | ID;
        if ctx.INTEGER():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.ID():
            return StructType(ctx.ID().getText())
        return None

    def visitVtype(self, ctx: TyCParser.VtypeContext):
        # vtype: INTEGER | FLOAT | STRING | AUTO | ID;
        if ctx.AUTO():
            return None  # None đại diện cho 'auto'
        if ctx.INTEGER():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.ID():
            return StructType(ctx.ID().getText())
        return None

    def visitFtype(self, ctx: TyCParser.FtypeContext):
        # ftype: INTEGER | FLOAT | STRING | VOID | ID;
        if ctx.VOID():
            return VoidType()
        if ctx.INTEGER():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.ID():
            return StructType(ctx.ID().getText())
        return None

    # ========================================================================
    # Statements
    # ========================================================================

    def visitBlockstmt(self, ctx: TyCParser.BlockstmtContext):
        # blockstmt: LB stmtlist RB;
        stmts = self.visit(ctx.stmtlist())
        return BlockStmt(stmts)

    def visitStmtlist(self, ctx: TyCParser.StmtlistContext):
        # stmtlist: stmt stmtlist | stmt;
        currentStmt = self.visit(ctx.stmt())
        
        # vardeclstmt có thể trả về list các VarDecl
        # Cần xử lý để làm phẳng (flatten)
        if not isinstance(currentStmt, list):
            currentStmt = [currentStmt]
        
        if ctx.stmtlist():
            return currentStmt + self.visit(ctx.stmtlist())
        return currentStmt

    def visitStmt(self, ctx: TyCParser.StmtContext):
        # stmt: (vardeclstmt SEMI)| ifstmt | whilestmt | forstmt | switchstmt | (controlstmt SEMI) | (exprstmt SEMI);
        if ctx.vardeclstmt():
            return self.visit(ctx.vardeclstmt())
        if ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        if ctx.whilestmt():
            return self.visit(ctx.whilestmt())
        if ctx.forstmt():
            return self.visit(ctx.forstmt())
        if ctx.switchstmt():
            return self.visit(ctx.switchstmt())
        if ctx.controlstmt():
            return self.visit(ctx.controlstmt())
        if ctx.exprstmt():
            return self.visit(ctx.exprstmt())
        return None

    def visitVardeclstmt(self, ctx: TyCParser.VardeclstmtContext):
        # vardeclstmt: vtype vardecl ;
        varType = self.visit(ctx.vtype())
        
        # visitVardecl trả về list các tuple (name, init_value)
        varList = self.visit(ctx.vardecl())
        
        # Tạo VarDecl cho từng biến
        result = []
        for varName, initValue in varList:
            result.append(VarDecl(varType, varName, initValue))
        
        return result

    def visitVardecl(self, ctx: TyCParser.VardeclContext):
        # vardecl: var CM vardecl | var ;
        currentVar = self.visit(ctx.var())
        
        if ctx.vardecl():
            return [currentVar] + self.visit(ctx.vardecl())
        return [currentVar]

    def visitVar(self, ctx: TyCParser.VarContext):
        # var: ID ASS expr | ID;
        varName = ctx.ID().getText()
        
        if ctx.expr():
            initValue = self.visit(ctx.expr())
            return (varName, initValue)
        return (varName, None)

    def visitIfstmt(self, ctx: TyCParser.IfstmtContext):
        # ifstmt: (IF LP expr RP (blockstmt | stmt) ELSE (blockstmt | stmt)) | (IF LP expr RP (blockstmt | stmt));
        condition = self.visit(ctx.expr())
        
        # Lấy then statement (child thứ 4)
        thenStmt = self.visit(ctx.getChild(4))
        
        # Kiểm tra có ELSE không
        elseStmt = None
        if ctx.ELSE():
            elseStmt = self.visit(ctx.getChild(6))
        
        return IfStmt(condition, thenStmt, elseStmt)

    def visitWhilestmt(self, ctx: TyCParser.WhilestmtContext):
        # whilestmt: WHILE LP expr RP (blockstmt | stmt);
        condition = self.visit(ctx.expr())
        body = self.visit(ctx.getChild(4))
        return WhileStmt(condition, body)

    def visitForstmt(self, ctx: TyCParser.ForstmtContext):
        # forstmt: FOR LP init SEMI condition SEMI update RP (blockstmt | stmt);
        init = self.visit(ctx.init())
        condition = self.visit(ctx.condition())
        update = self.visit(ctx.update())
        body = self.visit(ctx.getChild(8))
        
        return ForStmt(init, condition, update, body)

    def visitInit(self, ctx: TyCParser.InitContext):
        # init: (vardeclstmt | assignstmt) CM init | (vardeclstmt | assignstmt) |;
        if ctx.getChildCount() == 0:
            return None
        
        # Lấy statement đầu tiên
        firstChild = ctx.getChild(0)
        stmt = self.visit(firstChild)
        
        # Nếu là vardeclstmt, nó trả về list các VarDecl
        if isinstance(stmt, list):
            # Nếu chỉ có 1 biến, lấy ra
            if len(stmt) == 1:
                return stmt[0]
            # Nếu có nhiều biến, lấy biến đầu tiên
            # (Giới hạn của AST node - chỉ nhận 1 init)
            return stmt[0]
        
        # Nếu là assignstmt, trả về ExprStmt
        return stmt

    def visitCondition(self, ctx: TyCParser.ConditionContext):
        # condition: expr |;
        if ctx.expr():
            return self.visit(ctx.expr())
        return None

    def visitUpdate(self, ctx: TyCParser.UpdateContext):
        # update: expr |;
        if ctx.expr():
            return self.visit(ctx.expr())
        return None

    def visitSwitchstmt(self, ctx: TyCParser.SwitchstmtContext):
        # switchstmt: SWITCH LP expr RP LB casestmt defaultstmt RB;
        expr = self.visit(ctx.expr())
        cases = self.visit(ctx.casestmt())
        defaultCase = self.visit(ctx.defaultstmt())
        
        return SwitchStmt(expr, cases, defaultCase)

    def visitCasestmt(self, ctx: TyCParser.CasestmtContext):
        # casestmt: caselist |;
        if ctx.caselist():
            return self.visit(ctx.caselist())
        return []

    def visitCaselist(self, ctx: TyCParser.CaselistContext):
        # caselist: case caselist | case;
        currentCase = self.visit(ctx.case())
        
        if ctx.caselist():
            return [currentCase] + self.visit(ctx.caselist())
        return [currentCase]

    def visitCase(self, ctx: TyCParser.CaseContext):
        # case: CASE expr ':' stmtlist;
        caseExpr = self.visit(ctx.expr())
        stmts = self.visit(ctx.stmtlist())
        
        return CaseStmt(caseExpr, stmts)

    def visitDefaultstmt(self, ctx: TyCParser.DefaultstmtContext):
        # defaultstmt: (DEFAULT ':' stmtlist) |;
        if ctx.getChildCount() == 0:
            return None
        
        stmts = self.visit(ctx.stmtlist())
        return DefaultStmt(stmts)

    def visitControlstmt(self, ctx: TyCParser.ControlstmtContext):
        # controlstmt: breakstmt | continuestmt | returnstmt;
        return self.visit(ctx.getChild(0))

    def visitBreakstmt(self, ctx: TyCParser.BreakstmtContext):
        # breakstmt: BREAK;
        return BreakStmt()

    def visitContinuestmt(self, ctx: TyCParser.ContinuestmtContext):
        # continuestmt: CONTINUE;
        return ContinueStmt()

    def visitReturnstmt(self, ctx: TyCParser.ReturnstmtContext):
        # returnstmt: RETURN expr | RETURN;
        if ctx.expr():
            returnExpr = self.visit(ctx.expr())
            return ReturnStmt(returnExpr)
        return ReturnStmt(None)

    def visitExprstmt(self, ctx: TyCParser.ExprstmtContext):
        # exprstmt: assignstmt | callstmt | prefixstmt;
        expr = self.visit(ctx.getChild(0))
        return ExprStmt(expr)

    def visitAssignstmt(self, ctx: TyCParser.AssignstmtContext):
        # assignstmt: assignvar ASS expr;
        lhs = self.visit(ctx.assignvar())
        rhs = self.visit(ctx.expr())
        
        return AssignExpr(lhs, rhs)

    def visitAssignvar(self, ctx: TyCParser.AssignvarContext):
        # assignvar: ID DOT assignvar | ID;
        if ctx.assignvar():
            # Trường hợp ID DOT assignvar
            # Cần xây dựng MemberAccess từ right-recursive grammar
            # Thu thập tất cả IDs trong chuỗi a.b.c
            ids = [ctx.ID().getText()]
            current = ctx.assignvar()
            
            while current.assignvar():
                ids.append(current.ID().getText())
                current = current.assignvar()
            ids.append(current.ID().getText())
            
            # Xây dựng MemberAccess từ trái sang phải: MemberAccess(MemberAccess(a, b), c)
            result = Identifier(ids[0])
            for member in ids[1:]:
                result = MemberAccess(result, member)
            
            return result
        else:
            # Trường hợp chỉ có ID
            return Identifier(ctx.ID().getText())

    def visitCallstmt(self, ctx: TyCParser.CallstmtContext):
        # callstmt: ID LP callparam RP;
        funcName = ctx.ID().getText()
        args = self.visit(ctx.callparam())
        
        return FuncCall(funcName, args)

    def visitCallparam(self, ctx: TyCParser.CallparamContext):
        # callparam: callparameter |;
        if ctx.callparameter():
            return self.visit(ctx.callparameter())
        return []

    def visitCallparameter(self, ctx: TyCParser.CallparameterContext):
        # callparameter: expr CM callparameter | expr;
        currentExpr = self.visit(ctx.expr())
        
        if ctx.callparameter():
            return [currentExpr] + self.visit(ctx.callparameter())
        return [currentExpr]

    # ========================================================================
    # Expressions
    # ========================================================================

    def visitExpr(self, ctx: TyCParser.ExprContext):
        # expr: logicOR ASS expr| logicOR;
        if ctx.ASS():
            # Assignment expression
            lhs = self.visit(ctx.logicOR())
            rhs = self.visit(ctx.expr())
            return AssignExpr(lhs, rhs)
        return self.visit(ctx.logicOR())

    def visitLogicOR(self, ctx: TyCParser.LogicORContext):
        # logicOR: logicOR OR logicAND | logicAND;
        if ctx.OR():
            left = self.visit(ctx.logicOR())
            right = self.visit(ctx.logicAND())
            return BinaryOp(left, '||', right)
        return self.visit(ctx.logicAND())

    def visitLogicAND(self, ctx: TyCParser.LogicANDContext):
        # logicAND: logicAND AND eqcompare | eqcompare;
        if ctx.AND():
            left = self.visit(ctx.logicAND())
            right = self.visit(ctx.eqcompare())
            return BinaryOp(left, '&&', right)
        return self.visit(ctx.eqcompare())

    def visitEqcompare(self, ctx: TyCParser.EqcompareContext):
        # eqcompare: eqcompare (EQ|NEQ) relop | relop;
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.eqcompare())
            operator = ctx.getChild(1).getText()
            right = self.visit(ctx.relop())
            return BinaryOp(left, operator, right)
        return self.visit(ctx.relop())

    def visitRelop(self, ctx: TyCParser.RelopContext):
        # relop: relop (LETH|GRTH|LTE|GTE) additive | additive;
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.relop())
            operator = ctx.getChild(1).getText()
            right = self.visit(ctx.additive())
            return BinaryOp(left, operator, right)
        return self.visit(ctx.additive())

    def visitAdditive(self, ctx: TyCParser.AdditiveContext):
        # additive: additive (PLUS|MINUS) multiple | multiple;
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.additive())
            operator = ctx.getChild(1).getText()
            right = self.visit(ctx.multiple())
            return BinaryOp(left, operator, right)
        return self.visit(ctx.multiple())

    def visitMultiple(self, ctx: TyCParser.MultipleContext):
        # multiple: multiple (MUL|DIV|MOD) prefixstmt | prefixstmt;
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.multiple())
            operator = ctx.getChild(1).getText()
            right = self.visit(ctx.prefixstmt())
            return BinaryOp(left, operator, right)
        return self.visit(ctx.prefixstmt())

    def visitPrefixstmt(self, ctx: TyCParser.PrefixstmtContext):
        # prefixstmt: (INC | DEC | NOT | MINUS | PLUS) prefixstmt | postfix;
        if ctx.postfix():
            return self.visit(ctx.postfix())
        
        # Có prefix operator
        operator = ctx.getChild(0).getText()
        operand = self.visit(ctx.prefixstmt())
        
        return PrefixOp(operator, operand)

    def visitPostfix(self, ctx: TyCParser.PostfixContext):
        # postfix: postfix (INC|DEC) | memberaccess;
        if ctx.memberaccess():
            return self.visit(ctx.memberaccess())
        
        # Có postfix operator
        operator = ctx.getChild(1).getText()
        operand = self.visit(ctx.postfix())
        
        return PostfixOp(operator, operand)

    def visitMemberaccess(self, ctx: TyCParser.MemberaccessContext):
        # memberaccess: memberaccess DOT ID | primary;
        if ctx.primary():
            return self.visit(ctx.primary())
        
        # Trường hợp memberaccess DOT ID
        obj = self.visit(ctx.memberaccess())
        member = ctx.ID().getText()
        
        return MemberAccess(obj, member)

    def visitPrimary(self, ctx: TyCParser.PrimaryContext):
        # primary: LP expr RP | ID | INTLITERAL | FLOATLITERAL | STRINGLITERAL | LB exprlist RB | callstmt;
        
        # Parenthesized expression
        if ctx.LP():
            return self.visit(ctx.expr())
        
        # Identifier
        if ctx.ID():
            return Identifier(ctx.ID().getText())
        
        # Integer literal
        if ctx.INTLITERAL():
            value = int(ctx.INTLITERAL().getText())
            return IntLiteral(value)
        
        # Float literal
        if ctx.FLOATLITERAL():
            value = float(ctx.FLOATLITERAL().getText())
            return FloatLiteral(value)
        
        # String literal
        if ctx.STRINGLITERAL():
            value = ctx.STRINGLITERAL().getText()
            return StringLiteral(value)
        
        # Struct literal { expr, expr, ... }
        if ctx.LB():
            values = self.visit(ctx.exprlist())
            return StructLiteral(values)
        
        # Function call
        if ctx.callstmt():
            return self.visit(ctx.callstmt())
        
        return None

    def visitExprlist(self, ctx: TyCParser.ExprlistContext):
        # exprlist: nonemptyexprlist|;
        if ctx.nonemptyexprlist():
            return self.visit(ctx.nonemptyexprlist())
        return []

    def visitNonemptyexprlist(self, ctx: TyCParser.NonemptyexprlistContext):
        # nonemptyexprlist: expr CM nonemptyexprlist | expr;
        currentExpr = self.visit(ctx.expr())
        
        if ctx.nonemptyexprlist():
            return [currentExpr] + self.visit(ctx.nonemptyexprlist())
        return [currentExpr]