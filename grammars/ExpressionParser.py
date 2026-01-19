# Generated from grammars/ExpressionParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,78,120,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,49,8,1,1,1,1,1,1,1,1,1,3,1,55,8,1,
        1,2,1,2,1,3,1,3,1,3,5,3,62,8,3,10,3,12,3,65,9,3,1,4,1,4,1,5,1,5,
        1,5,3,5,72,8,5,1,6,1,6,1,7,1,7,1,7,3,7,79,8,7,1,7,1,7,3,7,83,8,7,
        1,7,1,7,1,8,1,8,4,8,89,8,8,11,8,12,8,90,1,8,3,8,94,8,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,5,12,111,
        8,12,10,12,12,12,114,9,12,1,13,1,13,1,14,1,14,1,14,0,0,15,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,0,3,3,0,22,24,39,42,78,78,3,0,
        38,38,72,73,77,77,4,0,1,26,29,33,38,60,67,68,122,0,30,1,0,0,0,2,
        54,1,0,0,0,4,56,1,0,0,0,6,58,1,0,0,0,8,66,1,0,0,0,10,71,1,0,0,0,
        12,73,1,0,0,0,14,78,1,0,0,0,16,86,1,0,0,0,18,97,1,0,0,0,20,102,1,
        0,0,0,22,105,1,0,0,0,24,107,1,0,0,0,26,115,1,0,0,0,28,117,1,0,0,
        0,30,36,3,2,1,0,31,32,3,4,2,0,32,33,3,2,1,0,33,35,1,0,0,0,34,31,
        1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,1,1,0,0,0,38,
        36,1,0,0,0,39,55,3,8,4,0,40,55,3,14,7,0,41,55,3,16,8,0,42,55,3,10,
        5,0,43,55,5,75,0,0,44,48,5,64,0,0,45,49,3,28,14,0,46,49,3,0,0,0,
        47,49,3,6,3,0,48,45,1,0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,50,1,
        0,0,0,50,51,5,65,0,0,51,55,1,0,0,0,52,53,5,78,0,0,53,55,3,2,1,0,
        54,39,1,0,0,0,54,40,1,0,0,0,54,41,1,0,0,0,54,42,1,0,0,0,54,43,1,
        0,0,0,54,44,1,0,0,0,54,52,1,0,0,0,55,3,1,0,0,0,56,57,7,0,0,0,57,
        5,1,0,0,0,58,63,3,0,0,0,59,60,5,62,0,0,60,62,3,0,0,0,61,59,1,0,0,
        0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,7,1,0,0,0,65,63,1,
        0,0,0,66,67,7,1,0,0,67,9,1,0,0,0,68,72,5,76,0,0,69,72,5,74,0,0,70,
        72,3,12,6,0,71,68,1,0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,72,11,1,0,
        0,0,73,74,7,2,0,0,74,13,1,0,0,0,75,79,5,50,0,0,76,79,5,51,0,0,77,
        79,3,10,5,0,78,75,1,0,0,0,78,76,1,0,0,0,78,77,1,0,0,0,79,80,1,0,
        0,0,80,82,5,64,0,0,81,83,3,6,3,0,82,81,1,0,0,0,82,83,1,0,0,0,83,
        84,1,0,0,0,84,85,5,65,0,0,85,15,1,0,0,0,86,88,5,34,0,0,87,89,3,18,
        9,0,88,87,1,0,0,0,89,90,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,93,
        1,0,0,0,92,94,3,20,10,0,93,92,1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,
        0,95,96,5,28,0,0,96,17,1,0,0,0,97,98,5,35,0,0,98,99,3,22,11,0,99,
        100,5,36,0,0,100,101,3,0,0,0,101,19,1,0,0,0,102,103,5,37,0,0,103,
        104,3,0,0,0,104,21,1,0,0,0,105,106,3,0,0,0,106,23,1,0,0,0,107,112,
        3,10,5,0,108,109,5,61,0,0,109,111,3,10,5,0,110,108,1,0,0,0,111,114,
        1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,25,1,0,0,0,114,112,1,
        0,0,0,115,116,3,10,5,0,116,27,1,0,0,0,117,118,1,0,0,0,118,29,1,0,
        0,0,10,36,48,54,63,71,78,82,90,93,112
    ]

class ExpressionParser ( Parser ):

    grammarFileName = "ExpressionParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'", "','", "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "WHERE", "INSERT", 
                      "INTO", "UPDATE", "DELETE", "CREATE", "ALTER", "TABLE", 
                      "DROP", "ADD", "VALUES", "SET", "JOIN", "INNER", "LEFT", 
                      "RIGHT", "FULL", "OUTER", "ON", "AND", "OR", "NOT", 
                      "EXISTS", "IF", "BEGIN", "END", "TRY", "CATCH", "DECLARE", 
                      "EXEC", "GO", "CASE", "WHEN", "THEN", "ELSE", "NULL", 
                      "IN", "IS", "LIKE", "BETWEEN", "ORDER", "BY", "GROUP", 
                      "HAVING", "ASC", "DESC", "AS", "MAX", "AVG", "TRUNCATE", 
                      "PRIMARY", "KEY", "CONSTRAINT", "COLUMN", "INT", "NVARCHAR", 
                      "BIGINT", "DATE", "DOT", "COMMA", "SEMI", "LPAREN", 
                      "RPAREN", "SP_EXECUTESQL", "CLUSTERED", "NONCLUSTERED", 
                      "LINE_COMMENT", "BLOCK_COMMENT", "WS", "STRING_SINGLE", 
                      "STRING_DOUBLE", "BRACKET_IDENTIFIER", "VARIABLE", 
                      "IDENTIFIER", "NUMBER", "OPERATOR" ]

    RULE_expression = 0
    RULE_primary = 1
    RULE_binaryOp = 2
    RULE_expressionList = 3
    RULE_literal = 4
    RULE_identifier = 5
    RULE_keywordAsIdentifier = 6
    RULE_functionCall = 7
    RULE_caseExpression = 8
    RULE_whenClause = 9
    RULE_elseClause = 10
    RULE_condition = 11
    RULE_tableName = 12
    RULE_columnName = 13
    RULE_selectStatement = 14

    ruleNames =  [ "expression", "primary", "binaryOp", "expressionList", 
                   "literal", "identifier", "keywordAsIdentifier", "functionCall", 
                   "caseExpression", "whenClause", "elseClause", "condition", 
                   "tableName", "columnName", "selectStatement" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    WHERE=3
    INSERT=4
    INTO=5
    UPDATE=6
    DELETE=7
    CREATE=8
    ALTER=9
    TABLE=10
    DROP=11
    ADD=12
    VALUES=13
    SET=14
    JOIN=15
    INNER=16
    LEFT=17
    RIGHT=18
    FULL=19
    OUTER=20
    ON=21
    AND=22
    OR=23
    NOT=24
    EXISTS=25
    IF=26
    BEGIN=27
    END=28
    TRY=29
    CATCH=30
    DECLARE=31
    EXEC=32
    GO=33
    CASE=34
    WHEN=35
    THEN=36
    ELSE=37
    NULL=38
    IN=39
    IS=40
    LIKE=41
    BETWEEN=42
    ORDER=43
    BY=44
    GROUP=45
    HAVING=46
    ASC=47
    DESC=48
    AS=49
    MAX=50
    AVG=51
    TRUNCATE=52
    PRIMARY=53
    KEY=54
    CONSTRAINT=55
    COLUMN=56
    INT=57
    NVARCHAR=58
    BIGINT=59
    DATE=60
    DOT=61
    COMMA=62
    SEMI=63
    LPAREN=64
    RPAREN=65
    SP_EXECUTESQL=66
    CLUSTERED=67
    NONCLUSTERED=68
    LINE_COMMENT=69
    BLOCK_COMMENT=70
    WS=71
    STRING_SINGLE=72
    STRING_DOUBLE=73
    BRACKET_IDENTIFIER=74
    VARIABLE=75
    IDENTIFIER=76
    NUMBER=77
    OPERATOR=78

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.PrimaryContext,i)


        def binaryOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.BinaryOpContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.BinaryOpContext,i)


        def getRuleIndex(self):
            return ExpressionParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ExpressionParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.primary()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 22)) & ~0x3f) == 0 and ((1 << (_la - 22)) & 72057594039894023) != 0):
                self.state = 31
                self.binaryOp()
                self.state = 32
                self.primary()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ExpressionParser.LiteralContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(ExpressionParser.FunctionCallContext,0)


        def caseExpression(self):
            return self.getTypedRuleContext(ExpressionParser.CaseExpressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(ExpressionParser.IdentifierContext,0)


        def VARIABLE(self):
            return self.getToken(ExpressionParser.VARIABLE, 0)

        def LPAREN(self):
            return self.getToken(ExpressionParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExpressionParser.RPAREN, 0)

        def selectStatement(self):
            return self.getTypedRuleContext(ExpressionParser.SelectStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(ExpressionParser.ExpressionContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(ExpressionParser.ExpressionListContext,0)


        def OPERATOR(self):
            return self.getToken(ExpressionParser.OPERATOR, 0)

        def primary(self):
            return self.getTypedRuleContext(ExpressionParser.PrimaryContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = ExpressionParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_primary)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.caseExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.identifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.match(ExpressionParser.VARIABLE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 44
                self.match(ExpressionParser.LPAREN)
                self.state = 48
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 45
                    self.selectStatement()
                    pass

                elif la_ == 2:
                    self.state = 46
                    self.expression()
                    pass

                elif la_ == 3:
                    self.state = 47
                    self.expressionList()
                    pass


                self.state = 50
                self.match(ExpressionParser.RPAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.match(ExpressionParser.OPERATOR)
                self.state = 53
                self.primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(ExpressionParser.OPERATOR, 0)

        def AND(self):
            return self.getToken(ExpressionParser.AND, 0)

        def OR(self):
            return self.getToken(ExpressionParser.OR, 0)

        def IN(self):
            return self.getToken(ExpressionParser.IN, 0)

        def IS(self):
            return self.getToken(ExpressionParser.IS, 0)

        def NOT(self):
            return self.getToken(ExpressionParser.NOT, 0)

        def LIKE(self):
            return self.getToken(ExpressionParser.LIKE, 0)

        def BETWEEN(self):
            return self.getToken(ExpressionParser.BETWEEN, 0)

        def getRuleIndex(self):
            return ExpressionParser.RULE_binaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOp" ):
                listener.enterBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOp" ):
                listener.exitBinaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOp" ):
                return visitor.visitBinaryOp(self)
            else:
                return visitor.visitChildren(self)




    def binaryOp(self):

        localctx = ExpressionParser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            _la = self._input.LA(1)
            if not(((((_la - 22)) & ~0x3f) == 0 and ((1 << (_la - 22)) & 72057594039894023) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExpressionParser.COMMA)
            else:
                return self.getToken(ExpressionParser.COMMA, i)

        def getRuleIndex(self):
            return ExpressionParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = ExpressionParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.expression()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 59
                self.match(ExpressionParser.COMMA)
                self.state = 60
                self.expression()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ExpressionParser.NUMBER, 0)

        def STRING_SINGLE(self):
            return self.getToken(ExpressionParser.STRING_SINGLE, 0)

        def STRING_DOUBLE(self):
            return self.getToken(ExpressionParser.STRING_DOUBLE, 0)

        def NULL(self):
            return self.getToken(ExpressionParser.NULL, 0)

        def getRuleIndex(self):
            return ExpressionParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ExpressionParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            _la = self._input.LA(1)
            if not(((((_la - 38)) & ~0x3f) == 0 and ((1 << (_la - 38)) & 601295421441) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExpressionParser.IDENTIFIER, 0)

        def BRACKET_IDENTIFIER(self):
            return self.getToken(ExpressionParser.BRACKET_IDENTIFIER, 0)

        def keywordAsIdentifier(self):
            return self.getTypedRuleContext(ExpressionParser.KeywordAsIdentifierContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = ExpressionParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_identifier)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [76]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(ExpressionParser.IDENTIFIER)
                pass
            elif token in [74]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(ExpressionParser.BRACKET_IDENTIFIER)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 67, 68]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.keywordAsIdentifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordAsIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(ExpressionParser.SELECT, 0)

        def FROM(self):
            return self.getToken(ExpressionParser.FROM, 0)

        def WHERE(self):
            return self.getToken(ExpressionParser.WHERE, 0)

        def INSERT(self):
            return self.getToken(ExpressionParser.INSERT, 0)

        def INTO(self):
            return self.getToken(ExpressionParser.INTO, 0)

        def UPDATE(self):
            return self.getToken(ExpressionParser.UPDATE, 0)

        def DELETE(self):
            return self.getToken(ExpressionParser.DELETE, 0)

        def CREATE(self):
            return self.getToken(ExpressionParser.CREATE, 0)

        def ALTER(self):
            return self.getToken(ExpressionParser.ALTER, 0)

        def TABLE(self):
            return self.getToken(ExpressionParser.TABLE, 0)

        def DROP(self):
            return self.getToken(ExpressionParser.DROP, 0)

        def ADD(self):
            return self.getToken(ExpressionParser.ADD, 0)

        def VALUES(self):
            return self.getToken(ExpressionParser.VALUES, 0)

        def SET(self):
            return self.getToken(ExpressionParser.SET, 0)

        def JOIN(self):
            return self.getToken(ExpressionParser.JOIN, 0)

        def INNER(self):
            return self.getToken(ExpressionParser.INNER, 0)

        def LEFT(self):
            return self.getToken(ExpressionParser.LEFT, 0)

        def RIGHT(self):
            return self.getToken(ExpressionParser.RIGHT, 0)

        def FULL(self):
            return self.getToken(ExpressionParser.FULL, 0)

        def OUTER(self):
            return self.getToken(ExpressionParser.OUTER, 0)

        def ON(self):
            return self.getToken(ExpressionParser.ON, 0)

        def AND(self):
            return self.getToken(ExpressionParser.AND, 0)

        def OR(self):
            return self.getToken(ExpressionParser.OR, 0)

        def NOT(self):
            return self.getToken(ExpressionParser.NOT, 0)

        def EXISTS(self):
            return self.getToken(ExpressionParser.EXISTS, 0)

        def IF(self):
            return self.getToken(ExpressionParser.IF, 0)

        def TRY(self):
            return self.getToken(ExpressionParser.TRY, 0)

        def CATCH(self):
            return self.getToken(ExpressionParser.CATCH, 0)

        def DECLARE(self):
            return self.getToken(ExpressionParser.DECLARE, 0)

        def EXEC(self):
            return self.getToken(ExpressionParser.EXEC, 0)

        def GO(self):
            return self.getToken(ExpressionParser.GO, 0)

        def NULL(self):
            return self.getToken(ExpressionParser.NULL, 0)

        def IN(self):
            return self.getToken(ExpressionParser.IN, 0)

        def IS(self):
            return self.getToken(ExpressionParser.IS, 0)

        def LIKE(self):
            return self.getToken(ExpressionParser.LIKE, 0)

        def BETWEEN(self):
            return self.getToken(ExpressionParser.BETWEEN, 0)

        def ORDER(self):
            return self.getToken(ExpressionParser.ORDER, 0)

        def BY(self):
            return self.getToken(ExpressionParser.BY, 0)

        def GROUP(self):
            return self.getToken(ExpressionParser.GROUP, 0)

        def HAVING(self):
            return self.getToken(ExpressionParser.HAVING, 0)

        def ASC(self):
            return self.getToken(ExpressionParser.ASC, 0)

        def DESC(self):
            return self.getToken(ExpressionParser.DESC, 0)

        def AS(self):
            return self.getToken(ExpressionParser.AS, 0)

        def INT(self):
            return self.getToken(ExpressionParser.INT, 0)

        def NVARCHAR(self):
            return self.getToken(ExpressionParser.NVARCHAR, 0)

        def BIGINT(self):
            return self.getToken(ExpressionParser.BIGINT, 0)

        def DATE(self):
            return self.getToken(ExpressionParser.DATE, 0)

        def MAX(self):
            return self.getToken(ExpressionParser.MAX, 0)

        def AVG(self):
            return self.getToken(ExpressionParser.AVG, 0)

        def TRUNCATE(self):
            return self.getToken(ExpressionParser.TRUNCATE, 0)

        def PRIMARY(self):
            return self.getToken(ExpressionParser.PRIMARY, 0)

        def KEY(self):
            return self.getToken(ExpressionParser.KEY, 0)

        def CONSTRAINT(self):
            return self.getToken(ExpressionParser.CONSTRAINT, 0)

        def COLUMN(self):
            return self.getToken(ExpressionParser.COLUMN, 0)

        def CLUSTERED(self):
            return self.getToken(ExpressionParser.CLUSTERED, 0)

        def NONCLUSTERED(self):
            return self.getToken(ExpressionParser.NONCLUSTERED, 0)

        def getRuleIndex(self):
            return ExpressionParser.RULE_keywordAsIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeywordAsIdentifier" ):
                listener.enterKeywordAsIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeywordAsIdentifier" ):
                listener.exitKeywordAsIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeywordAsIdentifier" ):
                return visitor.visitKeywordAsIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def keywordAsIdentifier(self):

        localctx = ExpressionParser.KeywordAsIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_keywordAsIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2305842751113003006) != 0) or _la==67 or _la==68):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ExpressionParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExpressionParser.RPAREN, 0)

        def MAX(self):
            return self.getToken(ExpressionParser.MAX, 0)

        def AVG(self):
            return self.getToken(ExpressionParser.AVG, 0)

        def identifier(self):
            return self.getTypedRuleContext(ExpressionParser.IdentifierContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(ExpressionParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = ExpressionParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 75
                self.match(ExpressionParser.MAX)
                pass

            elif la_ == 2:
                self.state = 76
                self.match(ExpressionParser.AVG)
                pass

            elif la_ == 3:
                self.state = 77
                self.identifier()
                pass


            self.state = 80
            self.match(ExpressionParser.LPAREN)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2305842768292872190) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 32537) != 0):
                self.state = 81
                self.expressionList()


            self.state = 84
            self.match(ExpressionParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(ExpressionParser.CASE, 0)

        def END(self):
            return self.getToken(ExpressionParser.END, 0)

        def whenClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.WhenClauseContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.WhenClauseContext,i)


        def elseClause(self):
            return self.getTypedRuleContext(ExpressionParser.ElseClauseContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_caseExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseExpression" ):
                listener.enterCaseExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseExpression" ):
                listener.exitCaseExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseExpression" ):
                return visitor.visitCaseExpression(self)
            else:
                return visitor.visitChildren(self)




    def caseExpression(self):

        localctx = ExpressionParser.CaseExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_caseExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(ExpressionParser.CASE)
            self.state = 88 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 87
                self.whenClause()
                self.state = 90 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==35):
                    break

            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 92
                self.elseClause()


            self.state = 95
            self.match(ExpressionParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhenClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHEN(self):
            return self.getToken(ExpressionParser.WHEN, 0)

        def condition(self):
            return self.getTypedRuleContext(ExpressionParser.ConditionContext,0)


        def THEN(self):
            return self.getToken(ExpressionParser.THEN, 0)

        def expression(self):
            return self.getTypedRuleContext(ExpressionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_whenClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhenClause" ):
                listener.enterWhenClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhenClause" ):
                listener.exitWhenClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhenClause" ):
                return visitor.visitWhenClause(self)
            else:
                return visitor.visitChildren(self)




    def whenClause(self):

        localctx = ExpressionParser.WhenClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whenClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(ExpressionParser.WHEN)
            self.state = 98
            self.condition()
            self.state = 99
            self.match(ExpressionParser.THEN)
            self.state = 100
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ExpressionParser.ELSE, 0)

        def expression(self):
            return self.getTypedRuleContext(ExpressionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_elseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseClause" ):
                listener.enterElseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseClause" ):
                listener.exitElseClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseClause" ):
                return visitor.visitElseClause(self)
            else:
                return visitor.visitChildren(self)




    def elseClause(self):

        localctx = ExpressionParser.ElseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(ExpressionParser.ELSE)
            self.state = 103
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ExpressionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = ExpressionParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.IdentifierContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ExpressionParser.DOT)
            else:
                return self.getToken(ExpressionParser.DOT, i)

        def getRuleIndex(self):
            return ExpressionParser.RULE_tableName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableName" ):
                listener.enterTableName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableName" ):
                listener.exitTableName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableName" ):
                return visitor.visitTableName(self)
            else:
                return visitor.visitChildren(self)




    def tableName(self):

        localctx = ExpressionParser.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tableName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.identifier()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 108
                self.match(ExpressionParser.DOT)
                self.state = 109
                self.identifier()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ExpressionParser.IdentifierContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_columnName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnName" ):
                listener.enterColumnName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnName" ):
                listener.exitColumnName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnName" ):
                return visitor.visitColumnName(self)
            else:
                return visitor.visitChildren(self)




    def columnName(self):

        localctx = ExpressionParser.ColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExpressionParser.RULE_selectStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStatement" ):
                listener.enterSelectStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStatement" ):
                listener.exitSelectStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectStatement" ):
                return visitor.visitSelectStatement(self)
            else:
                return visitor.visitChildren(self)




    def selectStatement(self):

        localctx = ExpressionParser.SelectStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_selectStatement)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





