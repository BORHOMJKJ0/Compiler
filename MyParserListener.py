# Generated from MyParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyParser import MyParser
else:
    from MyParser import MyParser

# This class defines a complete listener for a parse tree produced by MyParser.
class MyParserListener(ParseTreeListener):

    # Enter a parse tree produced by MyParser#sqlScript.
    def enterSqlScript(self, ctx:MyParser.SqlScriptContext):
        pass

    # Exit a parse tree produced by MyParser#sqlScript.
    def exitSqlScript(self, ctx:MyParser.SqlScriptContext):
        pass


    # Enter a parse tree produced by MyParser#statementList.
    def enterStatementList(self, ctx:MyParser.StatementListContext):
        pass

    # Exit a parse tree produced by MyParser#statementList.
    def exitStatementList(self, ctx:MyParser.StatementListContext):
        pass


    # Enter a parse tree produced by MyParser#statement.
    def enterStatement(self, ctx:MyParser.StatementContext):
        pass

    # Exit a parse tree produced by MyParser#statement.
    def exitStatement(self, ctx:MyParser.StatementContext):
        pass


    # Enter a parse tree produced by MyParser#goStatement.
    def enterGoStatement(self, ctx:MyParser.GoStatementContext):
        pass

    # Exit a parse tree produced by MyParser#goStatement.
    def exitGoStatement(self, ctx:MyParser.GoStatementContext):
        pass


    # Enter a parse tree produced by MyParser#createTableStatement.
    def enterCreateTableStatement(self, ctx:MyParser.CreateTableStatementContext):
        pass

    # Exit a parse tree produced by MyParser#createTableStatement.
    def exitCreateTableStatement(self, ctx:MyParser.CreateTableStatementContext):
        pass


    # Enter a parse tree produced by MyParser#tableName.
    def enterTableName(self, ctx:MyParser.TableNameContext):
        pass

    # Exit a parse tree produced by MyParser#tableName.
    def exitTableName(self, ctx:MyParser.TableNameContext):
        pass


    # Enter a parse tree produced by MyParser#columnDefinitionList.
    def enterColumnDefinitionList(self, ctx:MyParser.ColumnDefinitionListContext):
        pass

    # Exit a parse tree produced by MyParser#columnDefinitionList.
    def exitColumnDefinitionList(self, ctx:MyParser.ColumnDefinitionListContext):
        pass


    # Enter a parse tree produced by MyParser#columnDefinition.
    def enterColumnDefinition(self, ctx:MyParser.ColumnDefinitionContext):
        pass

    # Exit a parse tree produced by MyParser#columnDefinition.
    def exitColumnDefinition(self, ctx:MyParser.ColumnDefinitionContext):
        pass


    # Enter a parse tree produced by MyParser#columnName.
    def enterColumnName(self, ctx:MyParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by MyParser#columnName.
    def exitColumnName(self, ctx:MyParser.ColumnNameContext):
        pass


    # Enter a parse tree produced by MyParser#dataType.
    def enterDataType(self, ctx:MyParser.DataTypeContext):
        pass

    # Exit a parse tree produced by MyParser#dataType.
    def exitDataType(self, ctx:MyParser.DataTypeContext):
        pass


    # Enter a parse tree produced by MyParser#columnConstraint.
    def enterColumnConstraint(self, ctx:MyParser.ColumnConstraintContext):
        pass

    # Exit a parse tree produced by MyParser#columnConstraint.
    def exitColumnConstraint(self, ctx:MyParser.ColumnConstraintContext):
        pass


    # Enter a parse tree produced by MyParser#alterTableStatement.
    def enterAlterTableStatement(self, ctx:MyParser.AlterTableStatementContext):
        pass

    # Exit a parse tree produced by MyParser#alterTableStatement.
    def exitAlterTableStatement(self, ctx:MyParser.AlterTableStatementContext):
        pass


    # Enter a parse tree produced by MyParser#addColumnClause.
    def enterAddColumnClause(self, ctx:MyParser.AddColumnClauseContext):
        pass

    # Exit a parse tree produced by MyParser#addColumnClause.
    def exitAddColumnClause(self, ctx:MyParser.AddColumnClauseContext):
        pass


    # Enter a parse tree produced by MyParser#dropConstraintClause.
    def enterDropConstraintClause(self, ctx:MyParser.DropConstraintClauseContext):
        pass

    # Exit a parse tree produced by MyParser#dropConstraintClause.
    def exitDropConstraintClause(self, ctx:MyParser.DropConstraintClauseContext):
        pass


    # Enter a parse tree produced by MyParser#constraintName.
    def enterConstraintName(self, ctx:MyParser.ConstraintNameContext):
        pass

    # Exit a parse tree produced by MyParser#constraintName.
    def exitConstraintName(self, ctx:MyParser.ConstraintNameContext):
        pass


    # Enter a parse tree produced by MyParser#updateStatement.
    def enterUpdateStatement(self, ctx:MyParser.UpdateStatementContext):
        pass

    # Exit a parse tree produced by MyParser#updateStatement.
    def exitUpdateStatement(self, ctx:MyParser.UpdateStatementContext):
        pass


    # Enter a parse tree produced by MyParser#assignmentList.
    def enterAssignmentList(self, ctx:MyParser.AssignmentListContext):
        pass

    # Exit a parse tree produced by MyParser#assignmentList.
    def exitAssignmentList(self, ctx:MyParser.AssignmentListContext):
        pass


    # Enter a parse tree produced by MyParser#assignment.
    def enterAssignment(self, ctx:MyParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MyParser#assignment.
    def exitAssignment(self, ctx:MyParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MyParser#whereClause.
    def enterWhereClause(self, ctx:MyParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by MyParser#whereClause.
    def exitWhereClause(self, ctx:MyParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by MyParser#selectStatement.
    def enterSelectStatement(self, ctx:MyParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by MyParser#selectStatement.
    def exitSelectStatement(self, ctx:MyParser.SelectStatementContext):
        pass


    # Enter a parse tree produced by MyParser#selectList.
    def enterSelectList(self, ctx:MyParser.SelectListContext):
        pass

    # Exit a parse tree produced by MyParser#selectList.
    def exitSelectList(self, ctx:MyParser.SelectListContext):
        pass


    # Enter a parse tree produced by MyParser#selectItem.
    def enterSelectItem(self, ctx:MyParser.SelectItemContext):
        pass

    # Exit a parse tree produced by MyParser#selectItem.
    def exitSelectItem(self, ctx:MyParser.SelectItemContext):
        pass


    # Enter a parse tree produced by MyParser#fromClause.
    def enterFromClause(self, ctx:MyParser.FromClauseContext):
        pass

    # Exit a parse tree produced by MyParser#fromClause.
    def exitFromClause(self, ctx:MyParser.FromClauseContext):
        pass


    # Enter a parse tree produced by MyParser#tableSource.
    def enterTableSource(self, ctx:MyParser.TableSourceContext):
        pass

    # Exit a parse tree produced by MyParser#tableSource.
    def exitTableSource(self, ctx:MyParser.TableSourceContext):
        pass


    # Enter a parse tree produced by MyParser#ifStatement.
    def enterIfStatement(self, ctx:MyParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MyParser#ifStatement.
    def exitIfStatement(self, ctx:MyParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MyParser#blockStatement.
    def enterBlockStatement(self, ctx:MyParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by MyParser#blockStatement.
    def exitBlockStatement(self, ctx:MyParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by MyParser#tryCatchStatement.
    def enterTryCatchStatement(self, ctx:MyParser.TryCatchStatementContext):
        pass

    # Exit a parse tree produced by MyParser#tryCatchStatement.
    def exitTryCatchStatement(self, ctx:MyParser.TryCatchStatementContext):
        pass


    # Enter a parse tree produced by MyParser#declareStatement.
    def enterDeclareStatement(self, ctx:MyParser.DeclareStatementContext):
        pass

    # Exit a parse tree produced by MyParser#declareStatement.
    def exitDeclareStatement(self, ctx:MyParser.DeclareStatementContext):
        pass


    # Enter a parse tree produced by MyParser#setStatement.
    def enterSetStatement(self, ctx:MyParser.SetStatementContext):
        pass

    # Exit a parse tree produced by MyParser#setStatement.
    def exitSetStatement(self, ctx:MyParser.SetStatementContext):
        pass


    # Enter a parse tree produced by MyParser#execStatement.
    def enterExecStatement(self, ctx:MyParser.ExecStatementContext):
        pass

    # Exit a parse tree produced by MyParser#execStatement.
    def exitExecStatement(self, ctx:MyParser.ExecStatementContext):
        pass


    # Enter a parse tree produced by MyParser#expression.
    def enterExpression(self, ctx:MyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MyParser#expression.
    def exitExpression(self, ctx:MyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MyParser#expressionList.
    def enterExpressionList(self, ctx:MyParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by MyParser#expressionList.
    def exitExpressionList(self, ctx:MyParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by MyParser#caseExpression.
    def enterCaseExpression(self, ctx:MyParser.CaseExpressionContext):
        pass

    # Exit a parse tree produced by MyParser#caseExpression.
    def exitCaseExpression(self, ctx:MyParser.CaseExpressionContext):
        pass


    # Enter a parse tree produced by MyParser#whenClause.
    def enterWhenClause(self, ctx:MyParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by MyParser#whenClause.
    def exitWhenClause(self, ctx:MyParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by MyParser#elseClause.
    def enterElseClause(self, ctx:MyParser.ElseClauseContext):
        pass

    # Exit a parse tree produced by MyParser#elseClause.
    def exitElseClause(self, ctx:MyParser.ElseClauseContext):
        pass


    # Enter a parse tree produced by MyParser#condition.
    def enterCondition(self, ctx:MyParser.ConditionContext):
        pass

    # Exit a parse tree produced by MyParser#condition.
    def exitCondition(self, ctx:MyParser.ConditionContext):
        pass


    # Enter a parse tree produced by MyParser#columnReference.
    def enterColumnReference(self, ctx:MyParser.ColumnReferenceContext):
        pass

    # Exit a parse tree produced by MyParser#columnReference.
    def exitColumnReference(self, ctx:MyParser.ColumnReferenceContext):
        pass


    # Enter a parse tree produced by MyParser#functionCall.
    def enterFunctionCall(self, ctx:MyParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MyParser#functionCall.
    def exitFunctionCall(self, ctx:MyParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MyParser#literal.
    def enterLiteral(self, ctx:MyParser.LiteralContext):
        pass

    # Exit a parse tree produced by MyParser#literal.
    def exitLiteral(self, ctx:MyParser.LiteralContext):
        pass



del MyParser