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

    def visitProgram(self, ctx: TyCParser.ProgramContext):
        # program: decl* EOF;
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
        if ctx.getChildCount() == 0:
            return []
        varType = self.visit(ctx.stype())
        varName = ctx.ID().getText()
        currentMember = MemberDecl(varType, varName)
        if ctx.structvarlist():
            return [currentMember] + self.visit(ctx.structvarlist())
        return [currentMember]

    def visitFuncdecl(self, ctx: TyCParser.FuncdeclContext):
        # funcdecl: ftype func;
        funcContext = ctx.func()
        name = funcContext.ID().getText()
        params = self.visit(funcContext.paramlist())
        body = self.visit(funcContext.blockstmt())
        if ctx.ftype():
            returnType = self.visit(ctx.ftype())
        else:
            returnType = None
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
            return None
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

    def visitBlockstmt(self, ctx: TyCParser.BlockstmtContext):
        # blockstmt: LB stmtlist RB;
        stmts = self.visit(ctx.stmtlist())
        return BlockStmt(stmts)

    def visitStmtlist(self, ctx: TyCParser.StmtlistContext):
        # stmtlist: stmt stmtlist | ;
        if ctx.getChildCount() == 0:
            return []
        currentStmt = self.visit(ctx.stmt())
        if not isinstance(currentStmt, list):
            currentStmt = [currentStmt]
        if ctx.stmtlist():
            return currentStmt + self.visit(ctx.stmtlist())
        return currentStmt

    def visitStmt(self, ctx: TyCParser.StmtContext):
        # stmt: (vardeclstmt SEMI)| ifstmt | whilestmt | forstmt | switchstmt | (controlstmt SEMI) | (exprstmt SEMI) | blockstmt;
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
        if ctx.blockstmt():
            return self.visit(ctx.blockstmt())
        return None

    def visitVardeclstmt(self, ctx: TyCParser.VardeclstmtContext):
        # vardeclstmt: vtype var;
        varType = self.visit(ctx.vtype())
        varName, initValue = self.visit(ctx.var())
        return VarDecl(varType, varName, initValue)

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
        thenStmt = self.visit(ctx.getChild(4))
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
        # init: vardeclstmt | assignstmt |;
        if ctx.getChildCount() == 0:
            return None
        if ctx.vardeclstmt():
            return self.visit(ctx.vardeclstmt())
        if ctx.assignstmt():
            return ExprStmt(self.visit(ctx.assignstmt()))
        return None

    def visitCondition(self, ctx: TyCParser.ConditionContext):
        # condition: expr |;
        if ctx.expr():
            return self.visit(ctx.expr())
        return None

    def visitUpdate(self, ctx: TyCParser.UpdateContext):
        # update: assignstmt | prefix | postfix |;
        if ctx.getChildCount() == 0:
            return None
        if ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        if ctx.prefix():
            return self.visit(ctx.prefix())
        if ctx.postfix():
            return self.visit(ctx.postfix())
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
        # case: CASE expr COLON stmtlist;
        caseExpr = self.visit(ctx.expr())
        stmts = self.visit(ctx.stmtlist())
        return CaseStmt(caseExpr, stmts)

    def visitDefaultstmt(self, ctx: TyCParser.DefaultstmtContext):
        # defaultstmt: (DEFAULT COLON stmtlist) |;
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
        # exprstmt: assignstmt | callstmt | expr;
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
            ids = [ctx.ID().getText()]
            current = ctx.assignvar()
            while current.assignvar():
                ids.append(current.ID().getText())
                current = current.assignvar()
            ids.append(current.ID().getText())
            result = Identifier(ids[0])
            for member in ids[1:]:
                result = MemberAccess(result, member)
            return result
        else:
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

    def visitExpr(self, ctx: TyCParser.ExprContext):
        # expr: logicOR ASS expr| logicOR;
        if ctx.ASS():
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
        # multiple: multiple (MUL|DIV|MOD) unary | unary;
        if ctx.getChildCount() > 1:
            left = self.visit(ctx.multiple())
            operator = ctx.getChild(1).getText()
            right = self.visit(ctx.unary())
            return BinaryOp(left, operator, right)
        return self.visit(ctx.unary())

    def visitUnary(self, ctx: TyCParser.UnaryContext):
        # unary: (NOT|MINUS|PLUS) unary | prefix;
        if ctx.prefix():
            return self.visit(ctx.prefix())
        operator = ctx.getChild(0).getText()
        operand = self.visit(ctx.unary())
        return PrefixOp(operator, operand)

    def visitPrefix(self, ctx: TyCParser.PrefixContext):
        # prefix: (INC|DEC) prefix | postfix;
        if ctx.postfix():
            return self.visit(ctx.postfix())
        operator = ctx.getChild(0).getText()
        operand = self.visit(ctx.prefix())
        return PrefixOp(operator, operand)

    def visitPostfix(self, ctx: TyCParser.PostfixContext):
        # postfix: postfix DOT ID | postfix ((LP callparam RP) | (INC|DEC)) | primary;
        if ctx.primary():
            return self.visit(ctx.primary())
        operand = self.visit(ctx.postfix())

        if ctx.DOT():
            member = ctx.ID().getText()
            return MemberAccess(operand, member)

        if ctx.LP():
            args = self.visit(ctx.callparam())
            if isinstance(operand, Identifier):
                return FuncCall(operand.name, args)
            return FuncCall(operand, args)

        if ctx.INC():
            return PostfixOp('++', operand)
        if ctx.DEC():
            return PostfixOp('--', operand)

        return None

    def visitPrimary(self, ctx: TyCParser.PrimaryContext):
        # primary: LP expr RP | ID | INTLITERAL | FLOATLITERAL | STRINGLITERAL | LB exprlist RB;
        if ctx.LP():
            return self.visit(ctx.expr())
        if ctx.ID():
            return Identifier(ctx.ID().getText())
        if ctx.INTLITERAL():
            value = int(ctx.INTLITERAL().getText())
            return IntLiteral(value)
        if ctx.FLOATLITERAL():
            value = float(ctx.FLOATLITERAL().getText())
            return FloatLiteral(value)
        if ctx.STRINGLITERAL():
            value = ctx.STRINGLITERAL().getText()
            return StringLiteral(value)
        if ctx.LB():
            values = self.visit(ctx.exprlist())
            return StructLiteral(values)
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