# Generated from MyParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyParser import MyParser
else:
    from MyParser import MyParser

# This class defines a complete generic visitor for a parse tree produced by MyParser.

class MyParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyParser#sqlScript.
    def visitSqlScript(self, ctx:MyParser.SqlScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#statementList.
    def visitStatementList(self, ctx:MyParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#statement.
    def visitStatement(self, ctx:MyParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#goStatement.
    def visitGoStatement(self, ctx:MyParser.GoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#createTableStatement.
    def visitCreateTableStatement(self, ctx:MyParser.CreateTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#tableName.
    def visitTableName(self, ctx:MyParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#columnDefinitionList.
    def visitColumnDefinitionList(self, ctx:MyParser.ColumnDefinitionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#columnDefinition.
    def visitColumnDefinition(self, ctx:MyParser.ColumnDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#columnName.
    def visitColumnName(self, ctx:MyParser.ColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#dataType.
    def visitDataType(self, ctx:MyParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#columnConstraint.
    def visitColumnConstraint(self, ctx:MyParser.ColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#alterTableStatement.
    def visitAlterTableStatement(self, ctx:MyParser.AlterTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#addColumnClause.
    def visitAddColumnClause(self, ctx:MyParser.AddColumnClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#deleteStatement.
    def visitDeleteStatement(self, ctx:MyParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#dropConstraintClause.
    def visitDropConstraintClause(self, ctx:MyParser.DropConstraintClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#constraintName.
    def visitConstraintName(self, ctx:MyParser.ConstraintNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#updateStatement.
    def visitUpdateStatement(self, ctx:MyParser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#assignmentList.
    def visitAssignmentList(self, ctx:MyParser.AssignmentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#assignment.
    def visitAssignment(self, ctx:MyParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#whereClause.
    def visitWhereClause(self, ctx:MyParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#tryCatchStatement.
    def visitTryCatchStatement(self, ctx:MyParser.TryCatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#ifStatement.
    def visitIfStatement(self, ctx:MyParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#blockStatement.
    def visitBlockStatement(self, ctx:MyParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#declareStatement.
    def visitDeclareStatement(self, ctx:MyParser.DeclareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#setStatement.
    def visitSetStatement(self, ctx:MyParser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#execStatement.
    def visitExecStatement(self, ctx:MyParser.ExecStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#selectStatement.
    def visitSelectStatement(self, ctx:MyParser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#orderByClause.
    def visitOrderByClause(self, ctx:MyParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#orderByItem.
    def visitOrderByItem(self, ctx:MyParser.OrderByItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#selectList.
    def visitSelectList(self, ctx:MyParser.SelectListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#selectItem.
    def visitSelectItem(self, ctx:MyParser.SelectItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#fromClause.
    def visitFromClause(self, ctx:MyParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#tableSource.
    def visitTableSource(self, ctx:MyParser.TableSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#expression.
    def visitExpression(self, ctx:MyParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#expressionList.
    def visitExpressionList(self, ctx:MyParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#caseExpression.
    def visitCaseExpression(self, ctx:MyParser.CaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#whenClause.
    def visitWhenClause(self, ctx:MyParser.WhenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#elseClause.
    def visitElseClause(self, ctx:MyParser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#condition.
    def visitCondition(self, ctx:MyParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#columnReference.
    def visitColumnReference(self, ctx:MyParser.ColumnReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#functionCall.
    def visitFunctionCall(self, ctx:MyParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#literal.
    def visitLiteral(self, ctx:MyParser.LiteralContext):
        return self.visitChildren(ctx)



del MyParser