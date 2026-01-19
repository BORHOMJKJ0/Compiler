# Generated from grammars/SQLParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

# This class defines a complete listener for a parse tree produced by SQLParser.
class SQLParserListener(ParseTreeListener):

    # Enter a parse tree produced by SQLParser#parse.
    def enterParse(self, ctx:SQLParser.ParseContext):
        pass

    # Exit a parse tree produced by SQLParser#parse.
    def exitParse(self, ctx:SQLParser.ParseContext):
        pass


    # Enter a parse tree produced by SQLParser#sqlScript.
    def enterSqlScript(self, ctx:SQLParser.SqlScriptContext):
        pass

    # Exit a parse tree produced by SQLParser#sqlScript.
    def exitSqlScript(self, ctx:SQLParser.SqlScriptContext):
        pass


    # Enter a parse tree produced by SQLParser#batch.
    def enterBatch(self, ctx:SQLParser.BatchContext):
        pass

    # Exit a parse tree produced by SQLParser#batch.
    def exitBatch(self, ctx:SQLParser.BatchContext):
        pass


    # Enter a parse tree produced by SQLParser#statement.
    def enterStatement(self, ctx:SQLParser.StatementContext):
        pass

    # Exit a parse tree produced by SQLParser#statement.
    def exitStatement(self, ctx:SQLParser.StatementContext):
        pass


    # Enter a parse tree produced by SQLParser#ddlStatement.
    def enterDdlStatement(self, ctx:SQLParser.DdlStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#ddlStatement.
    def exitDdlStatement(self, ctx:SQLParser.DdlStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#createTableStatement.
    def enterCreateTableStatement(self, ctx:SQLParser.CreateTableStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#createTableStatement.
    def exitCreateTableStatement(self, ctx:SQLParser.CreateTableStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#columnDefinitionList.
    def enterColumnDefinitionList(self, ctx:SQLParser.ColumnDefinitionListContext):
        pass

    # Exit a parse tree produced by SQLParser#columnDefinitionList.
    def exitColumnDefinitionList(self, ctx:SQLParser.ColumnDefinitionListContext):
        pass


    # Enter a parse tree produced by SQLParser#columnDefinition.
    def enterColumnDefinition(self, ctx:SQLParser.ColumnDefinitionContext):
        pass

    # Exit a parse tree produced by SQLParser#columnDefinition.
    def exitColumnDefinition(self, ctx:SQLParser.ColumnDefinitionContext):
        pass


    # Enter a parse tree produced by SQLParser#dataType.
    def enterDataType(self, ctx:SQLParser.DataTypeContext):
        pass

    # Exit a parse tree produced by SQLParser#dataType.
    def exitDataType(self, ctx:SQLParser.DataTypeContext):
        pass


    # Enter a parse tree produced by SQLParser#typeSize.
    def enterTypeSize(self, ctx:SQLParser.TypeSizeContext):
        pass

    # Exit a parse tree produced by SQLParser#typeSize.
    def exitTypeSize(self, ctx:SQLParser.TypeSizeContext):
        pass


    # Enter a parse tree produced by SQLParser#constraint.
    def enterConstraint(self, ctx:SQLParser.ConstraintContext):
        pass

    # Exit a parse tree produced by SQLParser#constraint.
    def exitConstraint(self, ctx:SQLParser.ConstraintContext):
        pass


    # Enter a parse tree produced by SQLParser#alterTableStatement.
    def enterAlterTableStatement(self, ctx:SQLParser.AlterTableStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#alterTableStatement.
    def exitAlterTableStatement(self, ctx:SQLParser.AlterTableStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#addColumnClause.
    def enterAddColumnClause(self, ctx:SQLParser.AddColumnClauseContext):
        pass

    # Exit a parse tree produced by SQLParser#addColumnClause.
    def exitAddColumnClause(self, ctx:SQLParser.AddColumnClauseContext):
        pass


    # Enter a parse tree produced by SQLParser#dropConstraintClause.
    def enterDropConstraintClause(self, ctx:SQLParser.DropConstraintClauseContext):
        pass

    # Exit a parse tree produced by SQLParser#dropConstraintClause.
    def exitDropConstraintClause(self, ctx:SQLParser.DropConstraintClauseContext):
        pass


    # Enter a parse tree produced by SQLParser#truncateStatement.
    def enterTruncateStatement(self, ctx:SQLParser.TruncateStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#truncateStatement.
    def exitTruncateStatement(self, ctx:SQLParser.TruncateStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#dmlStatement.
    def enterDmlStatement(self, ctx:SQLParser.DmlStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#dmlStatement.
    def exitDmlStatement(self, ctx:SQLParser.DmlStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#selectStatement.
    def enterSelectStatement(self, ctx:SQLParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#selectStatement.
    def exitSelectStatement(self, ctx:SQLParser.SelectStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#orderByList.
    def enterOrderByList(self, ctx:SQLParser.OrderByListContext):
        pass

    # Exit a parse tree produced by SQLParser#orderByList.
    def exitOrderByList(self, ctx:SQLParser.OrderByListContext):
        pass


    # Enter a parse tree produced by SQLParser#orderByItem.
    def enterOrderByItem(self, ctx:SQLParser.OrderByItemContext):
        pass

    # Exit a parse tree produced by SQLParser#orderByItem.
    def exitOrderByItem(self, ctx:SQLParser.OrderByItemContext):
        pass


    # Enter a parse tree produced by SQLParser#selectList.
    def enterSelectList(self, ctx:SQLParser.SelectListContext):
        pass

    # Exit a parse tree produced by SQLParser#selectList.
    def exitSelectList(self, ctx:SQLParser.SelectListContext):
        pass


    # Enter a parse tree produced by SQLParser#selectItem.
    def enterSelectItem(self, ctx:SQLParser.SelectItemContext):
        pass

    # Exit a parse tree produced by SQLParser#selectItem.
    def exitSelectItem(self, ctx:SQLParser.SelectItemContext):
        pass


    # Enter a parse tree produced by SQLParser#tableList.
    def enterTableList(self, ctx:SQLParser.TableListContext):
        pass

    # Exit a parse tree produced by SQLParser#tableList.
    def exitTableList(self, ctx:SQLParser.TableListContext):
        pass


    # Enter a parse tree produced by SQLParser#joinClause.
    def enterJoinClause(self, ctx:SQLParser.JoinClauseContext):
        pass

    # Exit a parse tree produced by SQLParser#joinClause.
    def exitJoinClause(self, ctx:SQLParser.JoinClauseContext):
        pass


    # Enter a parse tree produced by SQLParser#joinType.
    def enterJoinType(self, ctx:SQLParser.JoinTypeContext):
        pass

    # Exit a parse tree produced by SQLParser#joinType.
    def exitJoinType(self, ctx:SQLParser.JoinTypeContext):
        pass


    # Enter a parse tree produced by SQLParser#tableRef.
    def enterTableRef(self, ctx:SQLParser.TableRefContext):
        pass

    # Exit a parse tree produced by SQLParser#tableRef.
    def exitTableRef(self, ctx:SQLParser.TableRefContext):
        pass


    # Enter a parse tree produced by SQLParser#insertStatement.
    def enterInsertStatement(self, ctx:SQLParser.InsertStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#insertStatement.
    def exitInsertStatement(self, ctx:SQLParser.InsertStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#columnList.
    def enterColumnList(self, ctx:SQLParser.ColumnListContext):
        pass

    # Exit a parse tree produced by SQLParser#columnList.
    def exitColumnList(self, ctx:SQLParser.ColumnListContext):
        pass


    # Enter a parse tree produced by SQLParser#insertValues.
    def enterInsertValues(self, ctx:SQLParser.InsertValuesContext):
        pass

    # Exit a parse tree produced by SQLParser#insertValues.
    def exitInsertValues(self, ctx:SQLParser.InsertValuesContext):
        pass


    # Enter a parse tree produced by SQLParser#updateStatement.
    def enterUpdateStatement(self, ctx:SQLParser.UpdateStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#updateStatement.
    def exitUpdateStatement(self, ctx:SQLParser.UpdateStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#assignments.
    def enterAssignments(self, ctx:SQLParser.AssignmentsContext):
        pass

    # Exit a parse tree produced by SQLParser#assignments.
    def exitAssignments(self, ctx:SQLParser.AssignmentsContext):
        pass


    # Enter a parse tree produced by SQLParser#assignment.
    def enterAssignment(self, ctx:SQLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SQLParser#assignment.
    def exitAssignment(self, ctx:SQLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SQLParser#deleteStatement.
    def enterDeleteStatement(self, ctx:SQLParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#deleteStatement.
    def exitDeleteStatement(self, ctx:SQLParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#controlFlowStatement.
    def enterControlFlowStatement(self, ctx:SQLParser.ControlFlowStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#controlFlowStatement.
    def exitControlFlowStatement(self, ctx:SQLParser.ControlFlowStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#ifStatement.
    def enterIfStatement(self, ctx:SQLParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#ifStatement.
    def exitIfStatement(self, ctx:SQLParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#thenBlock.
    def enterThenBlock(self, ctx:SQLParser.ThenBlockContext):
        pass

    # Exit a parse tree produced by SQLParser#thenBlock.
    def exitThenBlock(self, ctx:SQLParser.ThenBlockContext):
        pass


    # Enter a parse tree produced by SQLParser#elseBlock.
    def enterElseBlock(self, ctx:SQLParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by SQLParser#elseBlock.
    def exitElseBlock(self, ctx:SQLParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by SQLParser#blockStatement.
    def enterBlockStatement(self, ctx:SQLParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#blockStatement.
    def exitBlockStatement(self, ctx:SQLParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#tryCatchStatement.
    def enterTryCatchStatement(self, ctx:SQLParser.TryCatchStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#tryCatchStatement.
    def exitTryCatchStatement(self, ctx:SQLParser.TryCatchStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#variableStatement.
    def enterVariableStatement(self, ctx:SQLParser.VariableStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#variableStatement.
    def exitVariableStatement(self, ctx:SQLParser.VariableStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#declareStatement.
    def enterDeclareStatement(self, ctx:SQLParser.DeclareStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#declareStatement.
    def exitDeclareStatement(self, ctx:SQLParser.DeclareStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#setStatement.
    def enterSetStatement(self, ctx:SQLParser.SetStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#setStatement.
    def exitSetStatement(self, ctx:SQLParser.SetStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#execStatement.
    def enterExecStatement(self, ctx:SQLParser.ExecStatementContext):
        pass

    # Exit a parse tree produced by SQLParser#execStatement.
    def exitExecStatement(self, ctx:SQLParser.ExecStatementContext):
        pass


    # Enter a parse tree produced by SQLParser#expression.
    def enterExpression(self, ctx:SQLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SQLParser#expression.
    def exitExpression(self, ctx:SQLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SQLParser#primary.
    def enterPrimary(self, ctx:SQLParser.PrimaryContext):
        pass

    # Exit a parse tree produced by SQLParser#primary.
    def exitPrimary(self, ctx:SQLParser.PrimaryContext):
        pass


    # Enter a parse tree produced by SQLParser#binaryOp.
    def enterBinaryOp(self, ctx:SQLParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by SQLParser#binaryOp.
    def exitBinaryOp(self, ctx:SQLParser.BinaryOpContext):
        pass


    # Enter a parse tree produced by SQLParser#expressionList.
    def enterExpressionList(self, ctx:SQLParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by SQLParser#expressionList.
    def exitExpressionList(self, ctx:SQLParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by SQLParser#literal.
    def enterLiteral(self, ctx:SQLParser.LiteralContext):
        pass

    # Exit a parse tree produced by SQLParser#literal.
    def exitLiteral(self, ctx:SQLParser.LiteralContext):
        pass


    # Enter a parse tree produced by SQLParser#identifier.
    def enterIdentifier(self, ctx:SQLParser.IdentifierContext):
        pass

    # Exit a parse tree produced by SQLParser#identifier.
    def exitIdentifier(self, ctx:SQLParser.IdentifierContext):
        pass


    # Enter a parse tree produced by SQLParser#keywordAsIdentifier.
    def enterKeywordAsIdentifier(self, ctx:SQLParser.KeywordAsIdentifierContext):
        pass

    # Exit a parse tree produced by SQLParser#keywordAsIdentifier.
    def exitKeywordAsIdentifier(self, ctx:SQLParser.KeywordAsIdentifierContext):
        pass


    # Enter a parse tree produced by SQLParser#functionCall.
    def enterFunctionCall(self, ctx:SQLParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SQLParser#functionCall.
    def exitFunctionCall(self, ctx:SQLParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SQLParser#caseExpression.
    def enterCaseExpression(self, ctx:SQLParser.CaseExpressionContext):
        pass

    # Exit a parse tree produced by SQLParser#caseExpression.
    def exitCaseExpression(self, ctx:SQLParser.CaseExpressionContext):
        pass


    # Enter a parse tree produced by SQLParser#whenClause.
    def enterWhenClause(self, ctx:SQLParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by SQLParser#whenClause.
    def exitWhenClause(self, ctx:SQLParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by SQLParser#elseClause.
    def enterElseClause(self, ctx:SQLParser.ElseClauseContext):
        pass

    # Exit a parse tree produced by SQLParser#elseClause.
    def exitElseClause(self, ctx:SQLParser.ElseClauseContext):
        pass


    # Enter a parse tree produced by SQLParser#condition.
    def enterCondition(self, ctx:SQLParser.ConditionContext):
        pass

    # Exit a parse tree produced by SQLParser#condition.
    def exitCondition(self, ctx:SQLParser.ConditionContext):
        pass


    # Enter a parse tree produced by SQLParser#tableName.
    def enterTableName(self, ctx:SQLParser.TableNameContext):
        pass

    # Exit a parse tree produced by SQLParser#tableName.
    def exitTableName(self, ctx:SQLParser.TableNameContext):
        pass


    # Enter a parse tree produced by SQLParser#columnName.
    def enterColumnName(self, ctx:SQLParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by SQLParser#columnName.
    def exitColumnName(self, ctx:SQLParser.ColumnNameContext):
        pass



del SQLParser