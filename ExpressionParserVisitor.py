# Generated from grammars/ExpressionParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpressionParser import ExpressionParser
else:
    from ExpressionParser import ExpressionParser

# This class defines a complete generic visitor for a parse tree produced by ExpressionParser.

class ExpressionParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpressionParser#expression.
    def visitExpression(self, ctx:ExpressionParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#primary.
    def visitPrimary(self, ctx:ExpressionParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#binaryOp.
    def visitBinaryOp(self, ctx:ExpressionParser.BinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#columnReference.
    def visitColumnReference(self, ctx:ExpressionParser.ColumnReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#expressionList.
    def visitExpressionList(self, ctx:ExpressionParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#literal.
    def visitLiteral(self, ctx:ExpressionParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#identifier.
    def visitIdentifier(self, ctx:ExpressionParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#keywordAsIdentifier.
    def visitKeywordAsIdentifier(self, ctx:ExpressionParser.KeywordAsIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#functionCall.
    def visitFunctionCall(self, ctx:ExpressionParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#caseExpression.
    def visitCaseExpression(self, ctx:ExpressionParser.CaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#whenClause.
    def visitWhenClause(self, ctx:ExpressionParser.WhenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#elseClause.
    def visitElseClause(self, ctx:ExpressionParser.ElseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#condition.
    def visitCondition(self, ctx:ExpressionParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#tableName.
    def visitTableName(self, ctx:ExpressionParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#columnName.
    def visitColumnName(self, ctx:ExpressionParser.ColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#selectStatement.
    def visitSelectStatement(self, ctx:ExpressionParser.SelectStatementContext):
        return self.visitChildren(ctx)



del ExpressionParser