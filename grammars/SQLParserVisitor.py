# Generated from grammars/SQLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

# This class defines a complete generic visitor for a parse tree produced by SQLParser.

class SQLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SQLParser#parse.
    def visitParse(self, ctx:SQLParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#sqlScript.
    def visitSqlScript(self, ctx:SQLParser.SqlScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#batch.
    def visitBatch(self, ctx:SQLParser.BatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#statement.
    def visitStatement(self, ctx:SQLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#ddlStatement.
    def visitDdlStatement(self, ctx:SQLParser.DdlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#createTableStatement.
    def visitCreateTableStatement(self, ctx:SQLParser.CreateTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#columnDefinitionList.
    def visitColumnDefinitionList(self, ctx:SQLParser.ColumnDefinitionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#columnDefinition.
    def visitColumnDefinition(self, ctx:SQLParser.ColumnDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#dataType.
    def visitDataType(self, ctx:SQLParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#typeSize.
    def visitTypeSize(self, ctx:SQLParser.TypeSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#constraint.
    def visitConstraint(self, ctx:SQLParser.ConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#alterTableStatement.
    def visitAlterTableStatement(self, ctx:SQLParser.AlterTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#addColumnClause.
    def visitAddColumnClause(self, ctx:SQLParser.AddColumnClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#dropConstraintClause.
    def visitDropConstraintClause(self, ctx:SQLParser.DropConstraintClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#truncateStatement.
    def visitTruncateStatement(self, ctx:SQLParser.TruncateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#dmlStatement.
    def visitDmlStatement(self, ctx:SQLParser.DmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#selectStatement.
    def visitSelectStatement(self, ctx:SQLParser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#orderByList.
    def visitOrderByList(self, ctx:SQLParser.OrderByListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#orderByItem.
    def visitOrderByItem(self, ctx:SQLParser.OrderByItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#selectList.
    def visitSelectList(self, ctx:SQLParser.SelectListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#selectItem.
    def visitSelectItem(self, ctx:SQLParser.SelectItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#tableList.
    def visitTableList(self, ctx:SQLParser.TableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#joinClause.
    def visitJoinClause(self, ctx:SQLParser.JoinClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#joinType.
    def visitJoinType(self, ctx:SQLParser.JoinTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#tableRef.
    def visitTableRef(self, ctx:SQLParser.TableRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#insertStatement.
    def visitInsertStatement(self, ctx:SQLParser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#columnList.
    def visitColumnList(self, ctx:SQLParser.ColumnListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#insertValues.
    def visitInsertValues(self, ctx:SQLParser.InsertValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#updateStatement.
    def visitUpdateStatement(self, ctx:SQLParser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#assignments.
    def visitAssignments(self, ctx:SQLParser.AssignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#assignment.
    def visitAssignment(self, ctx:SQLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#deleteStatement.
    def visitDeleteStatement(self, ctx:SQLParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#controlFlowStatement.
    def visitControlFlowStatement(self, ctx:SQLParser.ControlFlowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#ifStatement.
    def visitIfStatement(self, ctx:SQLParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#thenBlock.
    def visitThenBlock(self, ctx:SQLParser.ThenBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#elseBlock.
    def visitElseBlock(self, ctx:SQLParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#blockStatement.
    def visitBlockStatement(self, ctx:SQLParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#tryCatchStatement.
    def visitTryCatchStatement(self, ctx:SQLParser.TryCatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#variableStatement.
    def visitVariableStatement(self, ctx:SQLParser.VariableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#declareStatement.
    def visitDeclareStatement(self, ctx:SQLParser.DeclareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#setStatement.
    def visitSetStatement(self, ctx:SQLParser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#execStatement.
    def visitExecStatement(self, ctx:SQLParser.ExecStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#expression.
    def visitExpression(self, ctx:SQLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#primary.
    def visitPrimary(self, ctx:SQLParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#binaryOp.
    def visitBinaryOp(self, ctx:SQLParser.BinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#expressionList.
    def visitExpressionList(self, ctx:SQLParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#literal.
    def visitLiteral(self, ctx:SQLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#identifier.
    def visitIdentifier(self, ctx:SQLParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#keywordAsIdentifier.
    def visitKeywordAsIdentifier(self, ctx:SQLParser.KeywordAsIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#functionCall.
    def visitFunctionCall(self, ctx:SQLParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#caseExpression.
    def visitCaseExpression(self, ctx:SQLParser.CaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#whenClause.
    def visitWhenClause(self, ctx:SQLParser.WhenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#elseClause.
    def visitElseClause(self, ctx:SQLParser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#condition.
    def visitCondition(self, ctx:SQLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#tableName.
    def visitTableName(self, ctx:SQLParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#columnName.
    def visitColumnName(self, ctx:SQLParser.ColumnNameContext):
        return self.visitChildren(ctx)



del SQLParser