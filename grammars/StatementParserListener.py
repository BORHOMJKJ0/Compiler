# Generated from grammars/StatementParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .StatementParser import StatementParser
else:
    from StatementParser import StatementParser

# This class defines a complete listener for a parse tree produced by StatementParser.
class StatementParserListener(ParseTreeListener):

    # Enter a parse tree produced by StatementParser#sqlScript.
    def enterSqlScript(self, ctx:StatementParser.SqlScriptContext):
        pass

    # Exit a parse tree produced by StatementParser#sqlScript.
    def exitSqlScript(self, ctx:StatementParser.SqlScriptContext):
        pass


    # Enter a parse tree produced by StatementParser#batch.
    def enterBatch(self, ctx:StatementParser.BatchContext):
        pass

    # Exit a parse tree produced by StatementParser#batch.
    def exitBatch(self, ctx:StatementParser.BatchContext):
        pass


    # Enter a parse tree produced by StatementParser#statement.
    def enterStatement(self, ctx:StatementParser.StatementContext):
        pass

    # Exit a parse tree produced by StatementParser#statement.
    def exitStatement(self, ctx:StatementParser.StatementContext):
        pass


    # Enter a parse tree produced by StatementParser#ddlStatement.
    def enterDdlStatement(self, ctx:StatementParser.DdlStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#ddlStatement.
    def exitDdlStatement(self, ctx:StatementParser.DdlStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#createTableStatement.
    def enterCreateTableStatement(self, ctx:StatementParser.CreateTableStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#createTableStatement.
    def exitCreateTableStatement(self, ctx:StatementParser.CreateTableStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#columnDefinitionList.
    def enterColumnDefinitionList(self, ctx:StatementParser.ColumnDefinitionListContext):
        pass

    # Exit a parse tree produced by StatementParser#columnDefinitionList.
    def exitColumnDefinitionList(self, ctx:StatementParser.ColumnDefinitionListContext):
        pass


    # Enter a parse tree produced by StatementParser#columnDefinition.
    def enterColumnDefinition(self, ctx:StatementParser.ColumnDefinitionContext):
        pass

    # Exit a parse tree produced by StatementParser#columnDefinition.
    def exitColumnDefinition(self, ctx:StatementParser.ColumnDefinitionContext):
        pass


    # Enter a parse tree produced by StatementParser#dataType.
    def enterDataType(self, ctx:StatementParser.DataTypeContext):
        pass

    # Exit a parse tree produced by StatementParser#dataType.
    def exitDataType(self, ctx:StatementParser.DataTypeContext):
        pass


    # Enter a parse tree produced by StatementParser#typeSize.
    def enterTypeSize(self, ctx:StatementParser.TypeSizeContext):
        pass

    # Exit a parse tree produced by StatementParser#typeSize.
    def exitTypeSize(self, ctx:StatementParser.TypeSizeContext):
        pass


    # Enter a parse tree produced by StatementParser#constraint.
    def enterConstraint(self, ctx:StatementParser.ConstraintContext):
        pass

    # Exit a parse tree produced by StatementParser#constraint.
    def exitConstraint(self, ctx:StatementParser.ConstraintContext):
        pass


    # Enter a parse tree produced by StatementParser#alterTableStatement.
    def enterAlterTableStatement(self, ctx:StatementParser.AlterTableStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#alterTableStatement.
    def exitAlterTableStatement(self, ctx:StatementParser.AlterTableStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#addColumnClause.
    def enterAddColumnClause(self, ctx:StatementParser.AddColumnClauseContext):
        pass

    # Exit a parse tree produced by StatementParser#addColumnClause.
    def exitAddColumnClause(self, ctx:StatementParser.AddColumnClauseContext):
        pass


    # Enter a parse tree produced by StatementParser#dropConstraintClause.
    def enterDropConstraintClause(self, ctx:StatementParser.DropConstraintClauseContext):
        pass

    # Exit a parse tree produced by StatementParser#dropConstraintClause.
    def exitDropConstraintClause(self, ctx:StatementParser.DropConstraintClauseContext):
        pass


    # Enter a parse tree produced by StatementParser#truncateStatement.
    def enterTruncateStatement(self, ctx:StatementParser.TruncateStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#truncateStatement.
    def exitTruncateStatement(self, ctx:StatementParser.TruncateStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#dmlStatement.
    def enterDmlStatement(self, ctx:StatementParser.DmlStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#dmlStatement.
    def exitDmlStatement(self, ctx:StatementParser.DmlStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#selectStatement.
    def enterSelectStatement(self, ctx:StatementParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#selectStatement.
    def exitSelectStatement(self, ctx:StatementParser.SelectStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#orderByList.
    def enterOrderByList(self, ctx:StatementParser.OrderByListContext):
        pass

    # Exit a parse tree produced by StatementParser#orderByList.
    def exitOrderByList(self, ctx:StatementParser.OrderByListContext):
        pass


    # Enter a parse tree produced by StatementParser#orderByItem.
    def enterOrderByItem(self, ctx:StatementParser.OrderByItemContext):
        pass

    # Exit a parse tree produced by StatementParser#orderByItem.
    def exitOrderByItem(self, ctx:StatementParser.OrderByItemContext):
        pass


    # Enter a parse tree produced by StatementParser#selectList.
    def enterSelectList(self, ctx:StatementParser.SelectListContext):
        pass

    # Exit a parse tree produced by StatementParser#selectList.
    def exitSelectList(self, ctx:StatementParser.SelectListContext):
        pass


    # Enter a parse tree produced by StatementParser#selectItem.
    def enterSelectItem(self, ctx:StatementParser.SelectItemContext):
        pass

    # Exit a parse tree produced by StatementParser#selectItem.
    def exitSelectItem(self, ctx:StatementParser.SelectItemContext):
        pass


    # Enter a parse tree produced by StatementParser#tableList.
    def enterTableList(self, ctx:StatementParser.TableListContext):
        pass

    # Exit a parse tree produced by StatementParser#tableList.
    def exitTableList(self, ctx:StatementParser.TableListContext):
        pass


    # Enter a parse tree produced by StatementParser#joinClause.
    def enterJoinClause(self, ctx:StatementParser.JoinClauseContext):
        pass

    # Exit a parse tree produced by StatementParser#joinClause.
    def exitJoinClause(self, ctx:StatementParser.JoinClauseContext):
        pass


    # Enter a parse tree produced by StatementParser#joinType.
    def enterJoinType(self, ctx:StatementParser.JoinTypeContext):
        pass

    # Exit a parse tree produced by StatementParser#joinType.
    def exitJoinType(self, ctx:StatementParser.JoinTypeContext):
        pass


    # Enter a parse tree produced by StatementParser#tableRef.
    def enterTableRef(self, ctx:StatementParser.TableRefContext):
        pass

    # Exit a parse tree produced by StatementParser#tableRef.
    def exitTableRef(self, ctx:StatementParser.TableRefContext):
        pass


    # Enter a parse tree produced by StatementParser#insertStatement.
    def enterInsertStatement(self, ctx:StatementParser.InsertStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#insertStatement.
    def exitInsertStatement(self, ctx:StatementParser.InsertStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#columnList.
    def enterColumnList(self, ctx:StatementParser.ColumnListContext):
        pass

    # Exit a parse tree produced by StatementParser#columnList.
    def exitColumnList(self, ctx:StatementParser.ColumnListContext):
        pass


    # Enter a parse tree produced by StatementParser#insertValues.
    def enterInsertValues(self, ctx:StatementParser.InsertValuesContext):
        pass

    # Exit a parse tree produced by StatementParser#insertValues.
    def exitInsertValues(self, ctx:StatementParser.InsertValuesContext):
        pass


    # Enter a parse tree produced by StatementParser#updateStatement.
    def enterUpdateStatement(self, ctx:StatementParser.UpdateStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#updateStatement.
    def exitUpdateStatement(self, ctx:StatementParser.UpdateStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#assignments.
    def enterAssignments(self, ctx:StatementParser.AssignmentsContext):
        pass

    # Exit a parse tree produced by StatementParser#assignments.
    def exitAssignments(self, ctx:StatementParser.AssignmentsContext):
        pass


    # Enter a parse tree produced by StatementParser#assignment.
    def enterAssignment(self, ctx:StatementParser.AssignmentContext):
        pass

    # Exit a parse tree produced by StatementParser#assignment.
    def exitAssignment(self, ctx:StatementParser.AssignmentContext):
        pass


    # Enter a parse tree produced by StatementParser#deleteStatement.
    def enterDeleteStatement(self, ctx:StatementParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#deleteStatement.
    def exitDeleteStatement(self, ctx:StatementParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#controlFlowStatement.
    def enterControlFlowStatement(self, ctx:StatementParser.ControlFlowStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#controlFlowStatement.
    def exitControlFlowStatement(self, ctx:StatementParser.ControlFlowStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#ifStatement.
    def enterIfStatement(self, ctx:StatementParser.IfStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#ifStatement.
    def exitIfStatement(self, ctx:StatementParser.IfStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#thenBlock.
    def enterThenBlock(self, ctx:StatementParser.ThenBlockContext):
        pass

    # Exit a parse tree produced by StatementParser#thenBlock.
    def exitThenBlock(self, ctx:StatementParser.ThenBlockContext):
        pass


    # Enter a parse tree produced by StatementParser#elseBlock.
    def enterElseBlock(self, ctx:StatementParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by StatementParser#elseBlock.
    def exitElseBlock(self, ctx:StatementParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by StatementParser#blockStatement.
    def enterBlockStatement(self, ctx:StatementParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#blockStatement.
    def exitBlockStatement(self, ctx:StatementParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#tryCatchStatement.
    def enterTryCatchStatement(self, ctx:StatementParser.TryCatchStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#tryCatchStatement.
    def exitTryCatchStatement(self, ctx:StatementParser.TryCatchStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#variableStatement.
    def enterVariableStatement(self, ctx:StatementParser.VariableStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#variableStatement.
    def exitVariableStatement(self, ctx:StatementParser.VariableStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#declareStatement.
    def enterDeclareStatement(self, ctx:StatementParser.DeclareStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#declareStatement.
    def exitDeclareStatement(self, ctx:StatementParser.DeclareStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#setStatement.
    def enterSetStatement(self, ctx:StatementParser.SetStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#setStatement.
    def exitSetStatement(self, ctx:StatementParser.SetStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#execStatement.
    def enterExecStatement(self, ctx:StatementParser.ExecStatementContext):
        pass

    # Exit a parse tree produced by StatementParser#execStatement.
    def exitExecStatement(self, ctx:StatementParser.ExecStatementContext):
        pass


    # Enter a parse tree produced by StatementParser#expression.
    def enterExpression(self, ctx:StatementParser.ExpressionContext):
        pass

    # Exit a parse tree produced by StatementParser#expression.
    def exitExpression(self, ctx:StatementParser.ExpressionContext):
        pass


    # Enter a parse tree produced by StatementParser#primary.
    def enterPrimary(self, ctx:StatementParser.PrimaryContext):
        pass

    # Exit a parse tree produced by StatementParser#primary.
    def exitPrimary(self, ctx:StatementParser.PrimaryContext):
        pass


    # Enter a parse tree produced by StatementParser#binaryOp.
    def enterBinaryOp(self, ctx:StatementParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by StatementParser#binaryOp.
    def exitBinaryOp(self, ctx:StatementParser.BinaryOpContext):
        pass


    # Enter a parse tree produced by StatementParser#expressionList.
    def enterExpressionList(self, ctx:StatementParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by StatementParser#expressionList.
    def exitExpressionList(self, ctx:StatementParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by StatementParser#literal.
    def enterLiteral(self, ctx:StatementParser.LiteralContext):
        pass

    # Exit a parse tree produced by StatementParser#literal.
    def exitLiteral(self, ctx:StatementParser.LiteralContext):
        pass


    # Enter a parse tree produced by StatementParser#identifier.
    def enterIdentifier(self, ctx:StatementParser.IdentifierContext):
        pass

    # Exit a parse tree produced by StatementParser#identifier.
    def exitIdentifier(self, ctx:StatementParser.IdentifierContext):
        pass


    # Enter a parse tree produced by StatementParser#keywordAsIdentifier.
    def enterKeywordAsIdentifier(self, ctx:StatementParser.KeywordAsIdentifierContext):
        pass

    # Exit a parse tree produced by StatementParser#keywordAsIdentifier.
    def exitKeywordAsIdentifier(self, ctx:StatementParser.KeywordAsIdentifierContext):
        pass


    # Enter a parse tree produced by StatementParser#functionCall.
    def enterFunctionCall(self, ctx:StatementParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by StatementParser#functionCall.
    def exitFunctionCall(self, ctx:StatementParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by StatementParser#caseExpression.
    def enterCaseExpression(self, ctx:StatementParser.CaseExpressionContext):
        pass

    # Exit a parse tree produced by StatementParser#caseExpression.
    def exitCaseExpression(self, ctx:StatementParser.CaseExpressionContext):
        pass


    # Enter a parse tree produced by StatementParser#whenClause.
    def enterWhenClause(self, ctx:StatementParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by StatementParser#whenClause.
    def exitWhenClause(self, ctx:StatementParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by StatementParser#elseClause.
    def enterElseClause(self, ctx:StatementParser.ElseClauseContext):
        pass

    # Exit a parse tree produced by StatementParser#elseClause.
    def exitElseClause(self, ctx:StatementParser.ElseClauseContext):
        pass


    # Enter a parse tree produced by StatementParser#condition.
    def enterCondition(self, ctx:StatementParser.ConditionContext):
        pass

    # Exit a parse tree produced by StatementParser#condition.
    def exitCondition(self, ctx:StatementParser.ConditionContext):
        pass


    # Enter a parse tree produced by StatementParser#tableName.
    def enterTableName(self, ctx:StatementParser.TableNameContext):
        pass

    # Exit a parse tree produced by StatementParser#tableName.
    def exitTableName(self, ctx:StatementParser.TableNameContext):
        pass


    # Enter a parse tree produced by StatementParser#columnName.
    def enterColumnName(self, ctx:StatementParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by StatementParser#columnName.
    def exitColumnName(self, ctx:StatementParser.ColumnNameContext):
        pass



del StatementParser