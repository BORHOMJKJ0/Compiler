# Generated from grammars/StatementParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .StatementParser import StatementParser
else:
    from StatementParser import StatementParser

# This class defines a complete generic visitor for a parse tree produced by StatementParser.

class StatementParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by StatementParser#sqlScript.
    def visitSqlScript(self, ctx:StatementParser.SqlScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#batch.
    def visitBatch(self, ctx:StatementParser.BatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#statement.
    def visitStatement(self, ctx:StatementParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#ddlStatement.
    def visitDdlStatement(self, ctx:StatementParser.DdlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#createTableStatement.
    def visitCreateTableStatement(self, ctx:StatementParser.CreateTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#columnDefinitionList.
    def visitColumnDefinitionList(self, ctx:StatementParser.ColumnDefinitionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#columnDefinition.
    def visitColumnDefinition(self, ctx:StatementParser.ColumnDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#dataType.
    def visitDataType(self, ctx:StatementParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#typeSize.
    def visitTypeSize(self, ctx:StatementParser.TypeSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#constraint.
    def visitConstraint(self, ctx:StatementParser.ConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#alterTableStatement.
    def visitAlterTableStatement(self, ctx:StatementParser.AlterTableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#addColumnClause.
    def visitAddColumnClause(self, ctx:StatementParser.AddColumnClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#dropConstraintClause.
    def visitDropConstraintClause(self, ctx:StatementParser.DropConstraintClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#dropStatement.
    def visitDropStatement(self, ctx:StatementParser.DropStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#truncateStatement.
    def visitTruncateStatement(self, ctx:StatementParser.TruncateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#useStatement.
    def visitUseStatement(self, ctx:StatementParser.UseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#dmlStatement.
    def visitDmlStatement(self, ctx:StatementParser.DmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#cteStatement.
    def visitCteStatement(self, ctx:StatementParser.CteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#cteList.
    def visitCteList(self, ctx:StatementParser.CteListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#cteDefinition.
    def visitCteDefinition(self, ctx:StatementParser.CteDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#selectStatement.
    def visitSelectStatement(self, ctx:StatementParser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#orderByList.
    def visitOrderByList(self, ctx:StatementParser.OrderByListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#orderByItem.
    def visitOrderByItem(self, ctx:StatementParser.OrderByItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#selectList.
    def visitSelectList(self, ctx:StatementParser.SelectListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#selectItem.
    def visitSelectItem(self, ctx:StatementParser.SelectItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#tableList.
    def visitTableList(self, ctx:StatementParser.TableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#joinClause.
    def visitJoinClause(self, ctx:StatementParser.JoinClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#joinType.
    def visitJoinType(self, ctx:StatementParser.JoinTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#tableRef.
    def visitTableRef(self, ctx:StatementParser.TableRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#insertStatement.
    def visitInsertStatement(self, ctx:StatementParser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#columnList.
    def visitColumnList(self, ctx:StatementParser.ColumnListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#insertValues.
    def visitInsertValues(self, ctx:StatementParser.InsertValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#updateStatement.
    def visitUpdateStatement(self, ctx:StatementParser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#assignments.
    def visitAssignments(self, ctx:StatementParser.AssignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#assignment.
    def visitAssignment(self, ctx:StatementParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#deleteStatement.
    def visitDeleteStatement(self, ctx:StatementParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#controlFlowStatement.
    def visitControlFlowStatement(self, ctx:StatementParser.ControlFlowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#ifStatement.
    def visitIfStatement(self, ctx:StatementParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#thenBlock.
    def visitThenBlock(self, ctx:StatementParser.ThenBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#elseBlock.
    def visitElseBlock(self, ctx:StatementParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#blockStatement.
    def visitBlockStatement(self, ctx:StatementParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#tryCatchStatement.
    def visitTryCatchStatement(self, ctx:StatementParser.TryCatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#variableStatement.
    def visitVariableStatement(self, ctx:StatementParser.VariableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#declareStatement.
    def visitDeclareStatement(self, ctx:StatementParser.DeclareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#setStatement.
    def visitSetStatement(self, ctx:StatementParser.SetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#execStatement.
    def visitExecStatement(self, ctx:StatementParser.ExecStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#cursorStatement.
    def visitCursorStatement(self, ctx:StatementParser.CursorStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#declareCursorStatement.
    def visitDeclareCursorStatement(self, ctx:StatementParser.DeclareCursorStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#cursorOptions.
    def visitCursorOptions(self, ctx:StatementParser.CursorOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#openCursorStatement.
    def visitOpenCursorStatement(self, ctx:StatementParser.OpenCursorStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#fetchCursorStatement.
    def visitFetchCursorStatement(self, ctx:StatementParser.FetchCursorStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#variableList.
    def visitVariableList(self, ctx:StatementParser.VariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#closeCursorStatement.
    def visitCloseCursorStatement(self, ctx:StatementParser.CloseCursorStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#deallocateCursorStatement.
    def visitDeallocateCursorStatement(self, ctx:StatementParser.DeallocateCursorStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#expression.
    def visitExpression(self, ctx:StatementParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#primary.
    def visitPrimary(self, ctx:StatementParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#binaryOp.
    def visitBinaryOp(self, ctx:StatementParser.BinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#columnReference.
    def visitColumnReference(self, ctx:StatementParser.ColumnReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#expressionList.
    def visitExpressionList(self, ctx:StatementParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#literal.
    def visitLiteral(self, ctx:StatementParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#identifier.
    def visitIdentifier(self, ctx:StatementParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#keywordAsIdentifier.
    def visitKeywordAsIdentifier(self, ctx:StatementParser.KeywordAsIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#functionCall.
    def visitFunctionCall(self, ctx:StatementParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#caseExpression.
    def visitCaseExpression(self, ctx:StatementParser.CaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#whenClause.
    def visitWhenClause(self, ctx:StatementParser.WhenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#elseClause.
    def visitElseClause(self, ctx:StatementParser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#condition.
    def visitCondition(self, ctx:StatementParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#tableName.
    def visitTableName(self, ctx:StatementParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by StatementParser#columnName.
    def visitColumnName(self, ctx:StatementParser.ColumnNameContext):
        return self.visitChildren(ctx)



del StatementParser