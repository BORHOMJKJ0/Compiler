# Generated from grammars/ExpressionParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpressionParser import ExpressionParser
else:
    from ExpressionParser import ExpressionParser

# This class defines a complete listener for a parse tree produced by ExpressionParser.
class ExpressionParserListener(ParseTreeListener):

    # Enter a parse tree produced by ExpressionParser#expression.
    def enterExpression(self, ctx:ExpressionParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExpressionParser#expression.
    def exitExpression(self, ctx:ExpressionParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExpressionParser#primary.
    def enterPrimary(self, ctx:ExpressionParser.PrimaryContext):
        pass

    # Exit a parse tree produced by ExpressionParser#primary.
    def exitPrimary(self, ctx:ExpressionParser.PrimaryContext):
        pass


    # Enter a parse tree produced by ExpressionParser#binaryOp.
    def enterBinaryOp(self, ctx:ExpressionParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by ExpressionParser#binaryOp.
    def exitBinaryOp(self, ctx:ExpressionParser.BinaryOpContext):
        pass


    # Enter a parse tree produced by ExpressionParser#columnReference.
    def enterColumnReference(self, ctx:ExpressionParser.ColumnReferenceContext):
        pass

    # Exit a parse tree produced by ExpressionParser#columnReference.
    def exitColumnReference(self, ctx:ExpressionParser.ColumnReferenceContext):
        pass


    # Enter a parse tree produced by ExpressionParser#expressionList.
    def enterExpressionList(self, ctx:ExpressionParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by ExpressionParser#expressionList.
    def exitExpressionList(self, ctx:ExpressionParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by ExpressionParser#literal.
    def enterLiteral(self, ctx:ExpressionParser.LiteralContext):
        pass

    # Exit a parse tree produced by ExpressionParser#literal.
    def exitLiteral(self, ctx:ExpressionParser.LiteralContext):
        pass


    # Enter a parse tree produced by ExpressionParser#identifier.
    def enterIdentifier(self, ctx:ExpressionParser.IdentifierContext):
        pass

    # Exit a parse tree produced by ExpressionParser#identifier.
    def exitIdentifier(self, ctx:ExpressionParser.IdentifierContext):
        pass


    # Enter a parse tree produced by ExpressionParser#keywordAsIdentifier.
    def enterKeywordAsIdentifier(self, ctx:ExpressionParser.KeywordAsIdentifierContext):
        pass

    # Exit a parse tree produced by ExpressionParser#keywordAsIdentifier.
    def exitKeywordAsIdentifier(self, ctx:ExpressionParser.KeywordAsIdentifierContext):
        pass


    # Enter a parse tree produced by ExpressionParser#functionCall.
    def enterFunctionCall(self, ctx:ExpressionParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by ExpressionParser#functionCall.
    def exitFunctionCall(self, ctx:ExpressionParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by ExpressionParser#caseExpression.
    def enterCaseExpression(self, ctx:ExpressionParser.CaseExpressionContext):
        pass

    # Exit a parse tree produced by ExpressionParser#caseExpression.
    def exitCaseExpression(self, ctx:ExpressionParser.CaseExpressionContext):
        pass


    # Enter a parse tree produced by ExpressionParser#whenClause.
    def enterWhenClause(self, ctx:ExpressionParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by ExpressionParser#whenClause.
    def exitWhenClause(self, ctx:ExpressionParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by ExpressionParser#elseClause.
    def enterElseClause(self, ctx:ExpressionParser.ElseClauseContext):
        pass

    # Exit a parse tree produced by ExpressionParser#elseClause.
    def exitElseClause(self, ctx:ExpressionParser.ElseClauseContext):
        pass


    # Enter a parse tree produced by ExpressionParser#condition.
    def enterCondition(self, ctx:ExpressionParser.ConditionContext):
        pass

    # Exit a parse tree produced by ExpressionParser#condition.
    def exitCondition(self, ctx:ExpressionParser.ConditionContext):
        pass


    # Enter a parse tree produced by ExpressionParser#tableName.
    def enterTableName(self, ctx:ExpressionParser.TableNameContext):
        pass

    # Exit a parse tree produced by ExpressionParser#tableName.
    def exitTableName(self, ctx:ExpressionParser.TableNameContext):
        pass


    # Enter a parse tree produced by ExpressionParser#columnName.
    def enterColumnName(self, ctx:ExpressionParser.ColumnNameContext):
        pass

    # Exit a parse tree produced by ExpressionParser#columnName.
    def exitColumnName(self, ctx:ExpressionParser.ColumnNameContext):
        pass


    # Enter a parse tree produced by ExpressionParser#selectStatement.
    def enterSelectStatement(self, ctx:ExpressionParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by ExpressionParser#selectStatement.
    def exitSelectStatement(self, ctx:ExpressionParser.SelectStatementContext):
        pass



del ExpressionParser