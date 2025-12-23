# Generated from MyParser.g4 by ANTLR 4.13.2
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
        4,1,17,390,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,1,0,1,
        0,1,1,1,1,3,1,84,8,1,5,1,86,8,1,10,1,12,1,89,9,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,103,8,2,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,5,1,5,3,5,116,8,5,1,5,1,5,1,5,3,5,121,8,5,1,6,
        1,6,1,6,5,6,126,8,6,10,6,12,6,129,9,6,1,7,1,7,1,7,5,7,134,8,7,10,
        7,12,7,137,9,7,1,8,1,8,1,9,1,9,1,9,1,9,3,9,145,8,9,1,9,1,9,1,9,1,
        9,3,9,151,8,9,3,9,153,8,9,1,10,1,10,3,10,157,8,10,1,11,1,11,1,11,
        1,11,1,11,3,11,164,8,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,
        1,14,1,15,1,15,1,15,1,15,1,15,3,15,180,8,15,1,16,1,16,1,16,5,16,
        185,8,16,10,16,12,16,188,9,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,
        1,19,1,19,1,19,3,19,200,8,19,1,19,3,19,203,8,19,1,19,1,19,3,19,207,
        8,19,1,20,1,20,1,20,5,20,212,8,20,10,20,12,20,215,9,20,1,21,1,21,
        3,21,219,8,21,1,21,3,21,222,8,21,1,21,3,21,225,8,21,1,22,1,22,1,
        22,1,22,5,22,231,8,22,10,22,12,22,234,9,22,1,23,1,23,3,23,238,8,
        23,1,23,3,23,241,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,
        25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,27,1,27,1,27,1,27,1,27,3,27,271,8,27,1,28,1,28,1,28,1,
        28,1,28,1,29,1,29,1,29,3,29,281,8,29,1,30,1,30,1,30,1,30,1,30,1,
        30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,295,8,30,1,30,1,30,1,30,1,
        30,1,30,1,30,5,30,303,8,30,10,30,12,30,306,9,30,1,31,1,31,1,31,5,
        31,311,8,31,10,31,12,31,314,9,31,1,32,1,32,4,32,318,8,32,11,32,12,
        32,319,1,32,3,32,323,8,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,34,
        1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
        1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,354,8,35,1,35,1,35,
        1,35,5,35,359,8,35,10,35,12,35,362,9,35,1,36,1,36,1,36,3,36,367,
        8,36,1,36,1,36,1,36,3,36,372,8,36,1,37,1,37,1,37,3,37,377,8,37,1,
        37,1,37,1,37,1,37,3,37,383,8,37,1,37,3,37,386,8,37,1,38,1,38,1,38,
        0,2,60,70,39,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,0,4,
        2,0,9,9,11,11,2,0,1,1,11,11,2,0,1,1,13,13,3,0,1,1,5,6,12,12,409,
        0,78,1,0,0,0,2,87,1,0,0,0,4,102,1,0,0,0,6,104,1,0,0,0,8,106,1,0,
        0,0,10,120,1,0,0,0,12,122,1,0,0,0,14,130,1,0,0,0,16,138,1,0,0,0,
        18,152,1,0,0,0,20,154,1,0,0,0,22,158,1,0,0,0,24,165,1,0,0,0,26,168,
        1,0,0,0,28,172,1,0,0,0,30,174,1,0,0,0,32,181,1,0,0,0,34,189,1,0,
        0,0,36,193,1,0,0,0,38,196,1,0,0,0,40,208,1,0,0,0,42,224,1,0,0,0,
        44,226,1,0,0,0,46,235,1,0,0,0,48,242,1,0,0,0,50,250,1,0,0,0,52,254,
        1,0,0,0,54,265,1,0,0,0,56,272,1,0,0,0,58,277,1,0,0,0,60,294,1,0,
        0,0,62,307,1,0,0,0,64,315,1,0,0,0,66,326,1,0,0,0,68,331,1,0,0,0,
        70,353,1,0,0,0,72,371,1,0,0,0,74,385,1,0,0,0,76,387,1,0,0,0,78,79,
        3,2,1,0,79,80,5,0,0,1,80,1,1,0,0,0,81,83,3,4,2,0,82,84,5,14,0,0,
        83,82,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,81,1,0,0,0,86,89,1,
        0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,3,1,0,0,0,89,87,1,0,0,0,90,
        103,3,8,4,0,91,103,3,22,11,0,92,103,3,30,15,0,93,103,3,38,19,0,94,
        103,3,54,27,0,95,103,3,56,28,0,96,103,3,58,29,0,97,103,3,48,24,0,
        98,103,3,52,26,0,99,103,3,6,3,0,100,103,3,50,25,0,101,103,5,14,0,
        0,102,90,1,0,0,0,102,91,1,0,0,0,102,92,1,0,0,0,102,93,1,0,0,0,102,
        94,1,0,0,0,102,95,1,0,0,0,102,96,1,0,0,0,102,97,1,0,0,0,102,98,1,
        0,0,0,102,99,1,0,0,0,102,100,1,0,0,0,102,101,1,0,0,0,103,5,1,0,0,
        0,104,105,5,1,0,0,105,7,1,0,0,0,106,107,5,1,0,0,107,108,5,1,0,0,
        108,109,3,10,5,0,109,110,5,14,0,0,110,111,3,12,6,0,111,112,5,14,
        0,0,112,9,1,0,0,0,113,114,5,11,0,0,114,116,5,14,0,0,115,113,1,0,
        0,0,115,116,1,0,0,0,116,117,1,0,0,0,117,121,5,11,0,0,118,121,5,9,
        0,0,119,121,5,11,0,0,120,115,1,0,0,0,120,118,1,0,0,0,120,119,1,0,
        0,0,121,11,1,0,0,0,122,127,3,14,7,0,123,124,5,14,0,0,124,126,3,14,
        7,0,125,123,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,
        0,0,128,13,1,0,0,0,129,127,1,0,0,0,130,131,3,16,8,0,131,135,3,18,
        9,0,132,134,3,20,10,0,133,132,1,0,0,0,134,137,1,0,0,0,135,133,1,
        0,0,0,135,136,1,0,0,0,136,15,1,0,0,0,137,135,1,0,0,0,138,139,7,0,
        0,0,139,17,1,0,0,0,140,144,5,1,0,0,141,142,5,14,0,0,142,143,5,12,
        0,0,143,145,5,14,0,0,144,141,1,0,0,0,144,145,1,0,0,0,145,153,1,0,
        0,0,146,150,5,11,0,0,147,148,5,14,0,0,148,149,5,12,0,0,149,151,5,
        14,0,0,150,147,1,0,0,0,150,151,1,0,0,0,151,153,1,0,0,0,152,140,1,
        0,0,0,152,146,1,0,0,0,153,19,1,0,0,0,154,156,5,1,0,0,155,157,5,1,
        0,0,156,155,1,0,0,0,156,157,1,0,0,0,157,21,1,0,0,0,158,159,5,1,0,
        0,159,160,5,1,0,0,160,163,3,10,5,0,161,164,3,24,12,0,162,164,3,26,
        13,0,163,161,1,0,0,0,163,162,1,0,0,0,164,23,1,0,0,0,165,166,5,1,
        0,0,166,167,3,14,7,0,167,25,1,0,0,0,168,169,5,1,0,0,169,170,5,1,
        0,0,170,171,3,28,14,0,171,27,1,0,0,0,172,173,7,0,0,0,173,29,1,0,
        0,0,174,175,5,1,0,0,175,176,3,10,5,0,176,177,5,1,0,0,177,179,3,32,
        16,0,178,180,3,36,18,0,179,178,1,0,0,0,179,180,1,0,0,0,180,31,1,
        0,0,0,181,186,3,34,17,0,182,183,5,14,0,0,183,185,3,34,17,0,184,182,
        1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,33,1,
        0,0,0,188,186,1,0,0,0,189,190,3,16,8,0,190,191,5,13,0,0,191,192,
        3,60,30,0,192,35,1,0,0,0,193,194,5,1,0,0,194,195,3,70,35,0,195,37,
        1,0,0,0,196,197,5,1,0,0,197,199,3,40,20,0,198,200,3,44,22,0,199,
        198,1,0,0,0,199,200,1,0,0,0,200,202,1,0,0,0,201,203,3,36,18,0,202,
        201,1,0,0,0,202,203,1,0,0,0,203,206,1,0,0,0,204,205,5,1,0,0,205,
        207,5,1,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,39,1,0,0,0,208,213,
        3,42,21,0,209,210,5,14,0,0,210,212,3,42,21,0,211,209,1,0,0,0,212,
        215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,41,1,0,0,0,215,213,
        1,0,0,0,216,221,3,60,30,0,217,219,5,1,0,0,218,217,1,0,0,0,218,219,
        1,0,0,0,219,220,1,0,0,0,220,222,5,11,0,0,221,218,1,0,0,0,221,222,
        1,0,0,0,222,225,1,0,0,0,223,225,5,13,0,0,224,216,1,0,0,0,224,223,
        1,0,0,0,225,43,1,0,0,0,226,227,5,1,0,0,227,232,3,46,23,0,228,229,
        5,14,0,0,229,231,3,46,23,0,230,228,1,0,0,0,231,234,1,0,0,0,232,230,
        1,0,0,0,232,233,1,0,0,0,233,45,1,0,0,0,234,232,1,0,0,0,235,240,3,
        10,5,0,236,238,5,1,0,0,237,236,1,0,0,0,237,238,1,0,0,0,238,239,1,
        0,0,0,239,241,5,11,0,0,240,237,1,0,0,0,240,241,1,0,0,0,241,47,1,
        0,0,0,242,243,5,1,0,0,243,244,5,1,0,0,244,245,5,1,0,0,245,246,5,
        14,0,0,246,247,3,38,19,0,247,248,5,14,0,0,248,249,3,50,25,0,249,
        49,1,0,0,0,250,251,5,1,0,0,251,252,3,2,1,0,252,253,5,1,0,0,253,51,
        1,0,0,0,254,255,5,1,0,0,255,256,5,1,0,0,256,257,3,2,1,0,257,258,
        5,1,0,0,258,259,5,1,0,0,259,260,5,1,0,0,260,261,5,1,0,0,261,262,
        3,2,1,0,262,263,5,1,0,0,263,264,5,1,0,0,264,53,1,0,0,0,265,266,5,
        1,0,0,266,267,5,10,0,0,267,270,3,18,9,0,268,269,5,13,0,0,269,271,
        3,60,30,0,270,268,1,0,0,0,270,271,1,0,0,0,271,55,1,0,0,0,272,273,
        5,1,0,0,273,274,5,10,0,0,274,275,5,13,0,0,275,276,3,60,30,0,276,
        57,1,0,0,0,277,278,5,1,0,0,278,280,7,1,0,0,279,281,3,62,31,0,280,
        279,1,0,0,0,280,281,1,0,0,0,281,59,1,0,0,0,282,283,6,30,-1,0,283,
        295,3,76,38,0,284,295,3,72,36,0,285,295,3,74,37,0,286,295,3,64,32,
        0,287,288,5,14,0,0,288,289,3,60,30,0,289,290,5,14,0,0,290,295,1,
        0,0,0,291,295,5,10,0,0,292,295,5,5,0,0,293,295,5,6,0,0,294,282,1,
        0,0,0,294,284,1,0,0,0,294,285,1,0,0,0,294,286,1,0,0,0,294,287,1,
        0,0,0,294,291,1,0,0,0,294,292,1,0,0,0,294,293,1,0,0,0,295,304,1,
        0,0,0,296,297,10,5,0,0,297,298,5,13,0,0,298,303,3,60,30,6,299,300,
        10,4,0,0,300,301,5,1,0,0,301,303,3,60,30,5,302,296,1,0,0,0,302,299,
        1,0,0,0,303,306,1,0,0,0,304,302,1,0,0,0,304,305,1,0,0,0,305,61,1,
        0,0,0,306,304,1,0,0,0,307,312,3,60,30,0,308,309,5,14,0,0,309,311,
        3,60,30,0,310,308,1,0,0,0,311,314,1,0,0,0,312,310,1,0,0,0,312,313,
        1,0,0,0,313,63,1,0,0,0,314,312,1,0,0,0,315,317,5,1,0,0,316,318,3,
        66,33,0,317,316,1,0,0,0,318,319,1,0,0,0,319,317,1,0,0,0,319,320,
        1,0,0,0,320,322,1,0,0,0,321,323,3,68,34,0,322,321,1,0,0,0,322,323,
        1,0,0,0,323,324,1,0,0,0,324,325,5,1,0,0,325,65,1,0,0,0,326,327,5,
        1,0,0,327,328,3,70,35,0,328,329,5,1,0,0,329,330,3,60,30,0,330,67,
        1,0,0,0,331,332,5,1,0,0,332,333,3,60,30,0,333,69,1,0,0,0,334,335,
        6,35,-1,0,335,336,3,60,30,0,336,337,7,2,0,0,337,338,3,60,30,0,338,
        354,1,0,0,0,339,340,3,60,30,0,340,341,5,1,0,0,341,342,5,14,0,0,342,
        343,3,62,31,0,343,344,5,14,0,0,344,354,1,0,0,0,345,346,3,60,30,0,
        346,347,5,1,0,0,347,348,5,1,0,0,348,354,1,0,0,0,349,350,5,14,0,0,
        350,351,3,70,35,0,351,352,5,14,0,0,352,354,1,0,0,0,353,334,1,0,0,
        0,353,339,1,0,0,0,353,345,1,0,0,0,353,349,1,0,0,0,354,360,1,0,0,
        0,355,356,10,1,0,0,356,357,5,1,0,0,357,359,3,70,35,2,358,355,1,0,
        0,0,359,362,1,0,0,0,360,358,1,0,0,0,360,361,1,0,0,0,361,71,1,0,0,
        0,362,360,1,0,0,0,363,364,3,10,5,0,364,365,5,14,0,0,365,367,1,0,
        0,0,366,363,1,0,0,0,366,367,1,0,0,0,367,368,1,0,0,0,368,372,3,16,
        8,0,369,372,5,11,0,0,370,372,5,9,0,0,371,366,1,0,0,0,371,369,1,0,
        0,0,371,370,1,0,0,0,372,73,1,0,0,0,373,374,5,11,0,0,374,376,5,14,
        0,0,375,377,3,62,31,0,376,375,1,0,0,0,376,377,1,0,0,0,377,378,1,
        0,0,0,378,386,5,14,0,0,379,380,5,1,0,0,380,382,5,14,0,0,381,383,
        3,62,31,0,382,381,1,0,0,0,382,383,1,0,0,0,383,384,1,0,0,0,384,386,
        5,14,0,0,385,373,1,0,0,0,385,379,1,0,0,0,386,75,1,0,0,0,387,388,
        7,3,0,0,388,77,1,0,0,0,39,83,87,102,115,120,127,135,144,150,152,
        156,163,179,186,199,202,206,213,218,221,224,232,237,240,270,280,
        294,302,304,312,319,322,353,360,366,371,376,382,385
    ]

class MyParser ( Parser ):

    grammarFileName = "MyParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'/*'", "'*/'" ]

    symbolicNames = [ "<INVALID>", "KEYWORD", "LINE_COMMENT", "BLOCK_COMMENT_START", 
                      "WS", "STRING_SINGLE", "STRING_DOUBLE", "HEX_STRING", 
                      "BIT_STRING", "BRACKET_IDENTIFIER", "VARIABLE", "IDENTIFIER", 
                      "NUMBER", "OPERATOR", "PUNCTUATION", "COMMENT_OPEN", 
                      "COMMENT_CLOSE", "COMMENT_TEXT" ]

    RULE_sqlScript = 0
    RULE_statementList = 1
    RULE_statement = 2
    RULE_goStatement = 3
    RULE_createTableStatement = 4
    RULE_tableName = 5
    RULE_columnDefinitionList = 6
    RULE_columnDefinition = 7
    RULE_columnName = 8
    RULE_dataType = 9
    RULE_columnConstraint = 10
    RULE_alterTableStatement = 11
    RULE_addColumnClause = 12
    RULE_dropConstraintClause = 13
    RULE_constraintName = 14
    RULE_updateStatement = 15
    RULE_assignmentList = 16
    RULE_assignment = 17
    RULE_whereClause = 18
    RULE_selectStatement = 19
    RULE_selectList = 20
    RULE_selectItem = 21
    RULE_fromClause = 22
    RULE_tableSource = 23
    RULE_ifStatement = 24
    RULE_blockStatement = 25
    RULE_tryCatchStatement = 26
    RULE_declareStatement = 27
    RULE_setStatement = 28
    RULE_execStatement = 29
    RULE_expression = 30
    RULE_expressionList = 31
    RULE_caseExpression = 32
    RULE_whenClause = 33
    RULE_elseClause = 34
    RULE_condition = 35
    RULE_columnReference = 36
    RULE_functionCall = 37
    RULE_literal = 38

    ruleNames =  [ "sqlScript", "statementList", "statement", "goStatement", 
                   "createTableStatement", "tableName", "columnDefinitionList", 
                   "columnDefinition", "columnName", "dataType", "columnConstraint", 
                   "alterTableStatement", "addColumnClause", "dropConstraintClause", 
                   "constraintName", "updateStatement", "assignmentList", 
                   "assignment", "whereClause", "selectStatement", "selectList", 
                   "selectItem", "fromClause", "tableSource", "ifStatement", 
                   "blockStatement", "tryCatchStatement", "declareStatement", 
                   "setStatement", "execStatement", "expression", "expressionList", 
                   "caseExpression", "whenClause", "elseClause", "condition", 
                   "columnReference", "functionCall", "literal" ]

    EOF = Token.EOF
    KEYWORD=1
    LINE_COMMENT=2
    BLOCK_COMMENT_START=3
    WS=4
    STRING_SINGLE=5
    STRING_DOUBLE=6
    HEX_STRING=7
    BIT_STRING=8
    BRACKET_IDENTIFIER=9
    VARIABLE=10
    IDENTIFIER=11
    NUMBER=12
    OPERATOR=13
    PUNCTUATION=14
    COMMENT_OPEN=15
    COMMENT_CLOSE=16
    COMMENT_TEXT=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SqlScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(MyParser.StatementListContext,0)


        def EOF(self):
            return self.getToken(MyParser.EOF, 0)

        def getRuleIndex(self):
            return MyParser.RULE_sqlScript

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqlScript" ):
                listener.enterSqlScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqlScript" ):
                listener.exitSqlScript(self)




    def sqlScript(self):

        localctx = MyParser.SqlScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sqlScript)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.statementList()
            self.state = 79
            self.match(MyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyParser.StatementContext,i)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def getRuleIndex(self):
            return MyParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = MyParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statementList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 81
                    self.statement()
                    self.state = 83
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 82
                        self.match(MyParser.PUNCTUATION)

             
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def createTableStatement(self):
            return self.getTypedRuleContext(MyParser.CreateTableStatementContext,0)


        def alterTableStatement(self):
            return self.getTypedRuleContext(MyParser.AlterTableStatementContext,0)


        def updateStatement(self):
            return self.getTypedRuleContext(MyParser.UpdateStatementContext,0)


        def selectStatement(self):
            return self.getTypedRuleContext(MyParser.SelectStatementContext,0)


        def declareStatement(self):
            return self.getTypedRuleContext(MyParser.DeclareStatementContext,0)


        def setStatement(self):
            return self.getTypedRuleContext(MyParser.SetStatementContext,0)


        def execStatement(self):
            return self.getTypedRuleContext(MyParser.ExecStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MyParser.IfStatementContext,0)


        def tryCatchStatement(self):
            return self.getTypedRuleContext(MyParser.TryCatchStatementContext,0)


        def goStatement(self):
            return self.getTypedRuleContext(MyParser.GoStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(MyParser.BlockStatementContext,0)


        def PUNCTUATION(self):
            return self.getToken(MyParser.PUNCTUATION, 0)

        def getRuleIndex(self):
            return MyParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MyParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.createTableStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.alterTableStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.updateStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 93
                self.selectStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 94
                self.declareStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 95
                self.setStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 96
                self.execStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 97
                self.ifStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 98
                self.tryCatchStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 99
                self.goStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 100
                self.blockStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 101
                self.match(MyParser.PUNCTUATION)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GoStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def getRuleIndex(self):
            return MyParser.RULE_goStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoStatement" ):
                listener.enterGoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoStatement" ):
                listener.exitGoStatement(self)




    def goStatement(self):

        localctx = MyParser.GoStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_goStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(MyParser.KEYWORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateTableStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def tableName(self):
            return self.getTypedRuleContext(MyParser.TableNameContext,0)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def columnDefinitionList(self):
            return self.getTypedRuleContext(MyParser.ColumnDefinitionListContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_createTableStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateTableStatement" ):
                listener.enterCreateTableStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateTableStatement" ):
                listener.exitCreateTableStatement(self)




    def createTableStatement(self):

        localctx = MyParser.CreateTableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_createTableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(MyParser.KEYWORD)
            self.state = 107
            self.match(MyParser.KEYWORD)
            self.state = 108
            self.tableName()
            self.state = 109
            self.match(MyParser.PUNCTUATION)
            self.state = 110
            self.columnDefinitionList()
            self.state = 111
            self.match(MyParser.PUNCTUATION)
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.IDENTIFIER)
            else:
                return self.getToken(MyParser.IDENTIFIER, i)

        def PUNCTUATION(self):
            return self.getToken(MyParser.PUNCTUATION, 0)

        def BRACKET_IDENTIFIER(self):
            return self.getToken(MyParser.BRACKET_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MyParser.RULE_tableName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableName" ):
                listener.enterTableName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableName" ):
                listener.exitTableName(self)




    def tableName(self):

        localctx = MyParser.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tableName)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 113
                    self.match(MyParser.IDENTIFIER)
                    self.state = 114
                    self.match(MyParser.PUNCTUATION)


                self.state = 117
                self.match(MyParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(MyParser.BRACKET_IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.match(MyParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnDefinitionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ColumnDefinitionContext)
            else:
                return self.getTypedRuleContext(MyParser.ColumnDefinitionContext,i)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def getRuleIndex(self):
            return MyParser.RULE_columnDefinitionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnDefinitionList" ):
                listener.enterColumnDefinitionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnDefinitionList" ):
                listener.exitColumnDefinitionList(self)




    def columnDefinitionList(self):

        localctx = MyParser.ColumnDefinitionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_columnDefinitionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.columnDefinition()
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 123
                    self.match(MyParser.PUNCTUATION)
                    self.state = 124
                    self.columnDefinition() 
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(MyParser.ColumnNameContext,0)


        def dataType(self):
            return self.getTypedRuleContext(MyParser.DataTypeContext,0)


        def columnConstraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ColumnConstraintContext)
            else:
                return self.getTypedRuleContext(MyParser.ColumnConstraintContext,i)


        def getRuleIndex(self):
            return MyParser.RULE_columnDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnDefinition" ):
                listener.enterColumnDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnDefinition" ):
                listener.exitColumnDefinition(self)




    def columnDefinition(self):

        localctx = MyParser.ColumnDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_columnDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.columnName()
            self.state = 131
            self.dataType()
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 132
                    self.columnConstraint() 
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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

        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def BRACKET_IDENTIFIER(self):
            return self.getToken(MyParser.BRACKET_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MyParser.RULE_columnName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnName" ):
                listener.enterColumnName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnName" ):
                listener.exitColumnName(self)




    def columnName(self):

        localctx = MyParser.ColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_columnName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            _la = self._input.LA(1)
            if not(_la==9 or _la==11):
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


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def NUMBER(self):
            return self.getToken(MyParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MyParser.RULE_dataType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataType" ):
                listener.enterDataType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataType" ):
                listener.exitDataType(self)




    def dataType(self):

        localctx = MyParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dataType)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(MyParser.KEYWORD)
                self.state = 144
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 141
                    self.match(MyParser.PUNCTUATION)
                    self.state = 142
                    self.match(MyParser.NUMBER)
                    self.state = 143
                    self.match(MyParser.PUNCTUATION)


                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(MyParser.IDENTIFIER)
                self.state = 150
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 147
                    self.match(MyParser.PUNCTUATION)
                    self.state = 148
                    self.match(MyParser.NUMBER)
                    self.state = 149
                    self.match(MyParser.PUNCTUATION)


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


    class ColumnConstraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def getRuleIndex(self):
            return MyParser.RULE_columnConstraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnConstraint" ):
                listener.enterColumnConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnConstraint" ):
                listener.exitColumnConstraint(self)




    def columnConstraint(self):

        localctx = MyParser.ColumnConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_columnConstraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(MyParser.KEYWORD)
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 155
                self.match(MyParser.KEYWORD)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlterTableStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def tableName(self):
            return self.getTypedRuleContext(MyParser.TableNameContext,0)


        def addColumnClause(self):
            return self.getTypedRuleContext(MyParser.AddColumnClauseContext,0)


        def dropConstraintClause(self):
            return self.getTypedRuleContext(MyParser.DropConstraintClauseContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_alterTableStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlterTableStatement" ):
                listener.enterAlterTableStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlterTableStatement" ):
                listener.exitAlterTableStatement(self)




    def alterTableStatement(self):

        localctx = MyParser.AlterTableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_alterTableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(MyParser.KEYWORD)
            self.state = 159
            self.match(MyParser.KEYWORD)
            self.state = 160
            self.tableName()
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 161
                self.addColumnClause()
                pass

            elif la_ == 2:
                self.state = 162
                self.dropConstraintClause()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddColumnClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def columnDefinition(self):
            return self.getTypedRuleContext(MyParser.ColumnDefinitionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_addColumnClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddColumnClause" ):
                listener.enterAddColumnClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddColumnClause" ):
                listener.exitAddColumnClause(self)




    def addColumnClause(self):

        localctx = MyParser.AddColumnClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_addColumnClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(MyParser.KEYWORD)
            self.state = 166
            self.columnDefinition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DropConstraintClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def constraintName(self):
            return self.getTypedRuleContext(MyParser.ConstraintNameContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_dropConstraintClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDropConstraintClause" ):
                listener.enterDropConstraintClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDropConstraintClause" ):
                listener.exitDropConstraintClause(self)




    def dropConstraintClause(self):

        localctx = MyParser.DropConstraintClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dropConstraintClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(MyParser.KEYWORD)
            self.state = 169
            self.match(MyParser.KEYWORD)
            self.state = 170
            self.constraintName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def BRACKET_IDENTIFIER(self):
            return self.getToken(MyParser.BRACKET_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MyParser.RULE_constraintName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraintName" ):
                listener.enterConstraintName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraintName" ):
                listener.exitConstraintName(self)




    def constraintName(self):

        localctx = MyParser.ConstraintNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_constraintName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            _la = self._input.LA(1)
            if not(_la==9 or _la==11):
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


    class UpdateStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def tableName(self):
            return self.getTypedRuleContext(MyParser.TableNameContext,0)


        def assignmentList(self):
            return self.getTypedRuleContext(MyParser.AssignmentListContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(MyParser.WhereClauseContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_updateStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdateStatement" ):
                listener.enterUpdateStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdateStatement" ):
                listener.exitUpdateStatement(self)




    def updateStatement(self):

        localctx = MyParser.UpdateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_updateStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(MyParser.KEYWORD)
            self.state = 175
            self.tableName()
            self.state = 176
            self.match(MyParser.KEYWORD)
            self.state = 177
            self.assignmentList()
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 178
                self.whereClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(MyParser.AssignmentContext,i)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def getRuleIndex(self):
            return MyParser.RULE_assignmentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentList" ):
                listener.enterAssignmentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentList" ):
                listener.exitAssignmentList(self)




    def assignmentList(self):

        localctx = MyParser.AssignmentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assignmentList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.assignment()
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 182
                    self.match(MyParser.PUNCTUATION)
                    self.state = 183
                    self.assignment() 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(MyParser.ColumnNameContext,0)


        def OPERATOR(self):
            return self.getToken(MyParser.OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = MyParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.columnName()
            self.state = 190
            self.match(MyParser.OPERATOR)
            self.state = 191
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def condition(self):
            return self.getTypedRuleContext(MyParser.ConditionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_whereClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereClause" ):
                listener.enterWhereClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereClause" ):
                listener.exitWhereClause(self)




    def whereClause(self):

        localctx = MyParser.WhereClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_whereClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MyParser.KEYWORD)
            self.state = 194
            self.condition(0)
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

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def selectList(self):
            return self.getTypedRuleContext(MyParser.SelectListContext,0)


        def fromClause(self):
            return self.getTypedRuleContext(MyParser.FromClauseContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(MyParser.WhereClauseContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_selectStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStatement" ):
                listener.enterSelectStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStatement" ):
                listener.exitSelectStatement(self)




    def selectStatement(self):

        localctx = MyParser.SelectStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_selectStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(MyParser.KEYWORD)
            self.state = 197
            self.selectList()
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 198
                self.fromClause()


            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 201
                self.whereClause()


            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 204
                self.match(MyParser.KEYWORD)
                self.state = 205
                self.match(MyParser.KEYWORD)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.SelectItemContext)
            else:
                return self.getTypedRuleContext(MyParser.SelectItemContext,i)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def getRuleIndex(self):
            return MyParser.RULE_selectList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectList" ):
                listener.enterSelectList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectList" ):
                listener.exitSelectList(self)




    def selectList(self):

        localctx = MyParser.SelectListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_selectList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.selectItem()
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 209
                    self.match(MyParser.PUNCTUATION)
                    self.state = 210
                    self.selectItem() 
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def OPERATOR(self):
            return self.getToken(MyParser.OPERATOR, 0)

        def getRuleIndex(self):
            return MyParser.RULE_selectItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectItem" ):
                listener.enterSelectItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectItem" ):
                listener.exitSelectItem(self)




    def selectItem(self):

        localctx = MyParser.SelectItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_selectItem)
        self._la = 0 # Token type
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 5, 6, 9, 10, 11, 12, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.expression(0)
                self.state = 221
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 218
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==1:
                        self.state = 217
                        self.match(MyParser.KEYWORD)


                    self.state = 220
                    self.match(MyParser.IDENTIFIER)


                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.match(MyParser.OPERATOR)
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


    class FromClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def tableSource(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.TableSourceContext)
            else:
                return self.getTypedRuleContext(MyParser.TableSourceContext,i)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def getRuleIndex(self):
            return MyParser.RULE_fromClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFromClause" ):
                listener.enterFromClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFromClause" ):
                listener.exitFromClause(self)




    def fromClause(self):

        localctx = MyParser.FromClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_fromClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(MyParser.KEYWORD)
            self.state = 227
            self.tableSource()
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 228
                    self.match(MyParser.PUNCTUATION)
                    self.state = 229
                    self.tableSource() 
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableSourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(MyParser.TableNameContext,0)


        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def getRuleIndex(self):
            return MyParser.RULE_tableSource

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableSource" ):
                listener.enterTableSource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableSource" ):
                listener.exitTableSource(self)




    def tableSource(self):

        localctx = MyParser.TableSourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_tableSource)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.tableName()
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 236
                    self.match(MyParser.KEYWORD)


                self.state = 239
                self.match(MyParser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def selectStatement(self):
            return self.getTypedRuleContext(MyParser.SelectStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(MyParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = MyParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MyParser.KEYWORD)
            self.state = 243
            self.match(MyParser.KEYWORD)
            self.state = 244
            self.match(MyParser.KEYWORD)
            self.state = 245
            self.match(MyParser.PUNCTUATION)
            self.state = 246
            self.selectStatement()
            self.state = 247
            self.match(MyParser.PUNCTUATION)
            self.state = 248
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def statementList(self):
            return self.getTypedRuleContext(MyParser.StatementListContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)




    def blockStatement(self):

        localctx = MyParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_blockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(MyParser.KEYWORD)
            self.state = 251
            self.statementList()
            self.state = 252
            self.match(MyParser.KEYWORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryCatchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def statementList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.StatementListContext)
            else:
                return self.getTypedRuleContext(MyParser.StatementListContext,i)


        def getRuleIndex(self):
            return MyParser.RULE_tryCatchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryCatchStatement" ):
                listener.enterTryCatchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryCatchStatement" ):
                listener.exitTryCatchStatement(self)




    def tryCatchStatement(self):

        localctx = MyParser.TryCatchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_tryCatchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(MyParser.KEYWORD)
            self.state = 255
            self.match(MyParser.KEYWORD)
            self.state = 256
            self.statementList()
            self.state = 257
            self.match(MyParser.KEYWORD)
            self.state = 258
            self.match(MyParser.KEYWORD)
            self.state = 259
            self.match(MyParser.KEYWORD)
            self.state = 260
            self.match(MyParser.KEYWORD)
            self.state = 261
            self.statementList()
            self.state = 262
            self.match(MyParser.KEYWORD)
            self.state = 263
            self.match(MyParser.KEYWORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def VARIABLE(self):
            return self.getToken(MyParser.VARIABLE, 0)

        def dataType(self):
            return self.getTypedRuleContext(MyParser.DataTypeContext,0)


        def OPERATOR(self):
            return self.getToken(MyParser.OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_declareStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclareStatement" ):
                listener.enterDeclareStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclareStatement" ):
                listener.exitDeclareStatement(self)




    def declareStatement(self):

        localctx = MyParser.DeclareStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_declareStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(MyParser.KEYWORD)
            self.state = 266
            self.match(MyParser.VARIABLE)
            self.state = 267
            self.dataType()
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 268
                self.match(MyParser.OPERATOR)
                self.state = 269
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def VARIABLE(self):
            return self.getToken(MyParser.VARIABLE, 0)

        def OPERATOR(self):
            return self.getToken(MyParser.OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_setStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetStatement" ):
                listener.enterSetStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetStatement" ):
                listener.exitSetStatement(self)




    def setStatement(self):

        localctx = MyParser.SetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_setStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(MyParser.KEYWORD)
            self.state = 273
            self.match(MyParser.VARIABLE)
            self.state = 274
            self.match(MyParser.OPERATOR)
            self.state = 275
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExecStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MyParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_execStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecStatement" ):
                listener.enterExecStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecStatement" ):
                listener.exitExecStatement(self)




    def execStatement(self):

        localctx = MyParser.ExecStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_execStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(MyParser.KEYWORD)
            self.state = 278
            _la = self._input.LA(1)
            if not(_la==1 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 279
                self.expressionList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MyParser.LiteralContext,0)


        def columnReference(self):
            return self.getTypedRuleContext(MyParser.ColumnReferenceContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(MyParser.FunctionCallContext,0)


        def caseExpression(self):
            return self.getTypedRuleContext(MyParser.CaseExpressionContext,0)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyParser.ExpressionContext,i)


        def VARIABLE(self):
            return self.getToken(MyParser.VARIABLE, 0)

        def STRING_SINGLE(self):
            return self.getToken(MyParser.STRING_SINGLE, 0)

        def STRING_DOUBLE(self):
            return self.getToken(MyParser.STRING_DOUBLE, 0)

        def OPERATOR(self):
            return self.getToken(MyParser.OPERATOR, 0)

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def getRuleIndex(self):
            return MyParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 283
                self.literal()
                pass

            elif la_ == 2:
                self.state = 284
                self.columnReference()
                pass

            elif la_ == 3:
                self.state = 285
                self.functionCall()
                pass

            elif la_ == 4:
                self.state = 286
                self.caseExpression()
                pass

            elif la_ == 5:
                self.state = 287
                self.match(MyParser.PUNCTUATION)
                self.state = 288
                self.expression(0)
                self.state = 289
                self.match(MyParser.PUNCTUATION)
                pass

            elif la_ == 6:
                self.state = 291
                self.match(MyParser.VARIABLE)
                pass

            elif la_ == 7:
                self.state = 292
                self.match(MyParser.STRING_SINGLE)
                pass

            elif la_ == 8:
                self.state = 293
                self.match(MyParser.STRING_DOUBLE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 302
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = MyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 296
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 297
                        self.match(MyParser.OPERATOR)
                        self.state = 298
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = MyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 299
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 300
                        self.match(MyParser.KEYWORD)
                        self.state = 301
                        self.expression(5)
                        pass

             
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyParser.ExpressionContext,i)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def getRuleIndex(self):
            return MyParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = MyParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expressionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.expression(0)
            self.state = 312
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 308
                    self.match(MyParser.PUNCTUATION)
                    self.state = 309
                    self.expression(0) 
                self.state = 314
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def whenClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.WhenClauseContext)
            else:
                return self.getTypedRuleContext(MyParser.WhenClauseContext,i)


        def elseClause(self):
            return self.getTypedRuleContext(MyParser.ElseClauseContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_caseExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseExpression" ):
                listener.enterCaseExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseExpression" ):
                listener.exitCaseExpression(self)




    def caseExpression(self):

        localctx = MyParser.CaseExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_caseExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(MyParser.KEYWORD)
            self.state = 317 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 316
                    self.whenClause()

                else:
                    raise NoViableAltException(self)
                self.state = 319 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 321
                self.elseClause()


            self.state = 324
            self.match(MyParser.KEYWORD)
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

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def condition(self):
            return self.getTypedRuleContext(MyParser.ConditionContext,0)


        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_whenClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhenClause" ):
                listener.enterWhenClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhenClause" ):
                listener.exitWhenClause(self)




    def whenClause(self):

        localctx = MyParser.WhenClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_whenClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(MyParser.KEYWORD)
            self.state = 327
            self.condition(0)
            self.state = 328
            self.match(MyParser.KEYWORD)
            self.state = 329
            self.expression(0)
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

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_elseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseClause" ):
                listener.enterElseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseClause" ):
                listener.exitElseClause(self)




    def elseClause(self):

        localctx = MyParser.ElseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(MyParser.KEYWORD)
            self.state = 332
            self.expression(0)
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyParser.ExpressionContext,i)


        def OPERATOR(self):
            return self.getToken(MyParser.OPERATOR, 0)

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def expressionList(self):
            return self.getTypedRuleContext(MyParser.ExpressionListContext,0)


        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ConditionContext)
            else:
                return self.getTypedRuleContext(MyParser.ConditionContext,i)


        def getRuleIndex(self):
            return MyParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_condition, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 335
                self.expression(0)
                self.state = 336
                _la = self._input.LA(1)
                if not(_la==1 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 337
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 339
                self.expression(0)
                self.state = 340
                self.match(MyParser.KEYWORD)
                self.state = 341
                self.match(MyParser.PUNCTUATION)
                self.state = 342
                self.expressionList()
                self.state = 343
                self.match(MyParser.PUNCTUATION)
                pass

            elif la_ == 3:
                self.state = 345
                self.expression(0)
                self.state = 346
                self.match(MyParser.KEYWORD)
                self.state = 347
                self.match(MyParser.KEYWORD)
                pass

            elif la_ == 4:
                self.state = 349
                self.match(MyParser.PUNCTUATION)
                self.state = 350
                self.condition(0)
                self.state = 351
                self.match(MyParser.PUNCTUATION)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 360
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 355
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 356
                    self.match(MyParser.KEYWORD)
                    self.state = 357
                    self.condition(2) 
                self.state = 362
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ColumnReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(MyParser.ColumnNameContext,0)


        def tableName(self):
            return self.getTypedRuleContext(MyParser.TableNameContext,0)


        def PUNCTUATION(self):
            return self.getToken(MyParser.PUNCTUATION, 0)

        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def BRACKET_IDENTIFIER(self):
            return self.getToken(MyParser.BRACKET_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MyParser.RULE_columnReference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnReference" ):
                listener.enterColumnReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnReference" ):
                listener.exitColumnReference(self)




    def columnReference(self):

        localctx = MyParser.ColumnReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_columnReference)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 363
                    self.tableName()
                    self.state = 364
                    self.match(MyParser.PUNCTUATION)


                self.state = 368
                self.columnName()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.match(MyParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 370
                self.match(MyParser.BRACKET_IDENTIFIER)
                pass


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

        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def expressionList(self):
            return self.getTypedRuleContext(MyParser.ExpressionListContext,0)


        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def getRuleIndex(self):
            return MyParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)




    def functionCall(self):

        localctx = MyParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_functionCall)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(MyParser.IDENTIFIER)
                self.state = 374
                self.match(MyParser.PUNCTUATION)
                self.state = 376
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 375
                    self.expressionList()


                self.state = 378
                self.match(MyParser.PUNCTUATION)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.match(MyParser.KEYWORD)
                self.state = 380
                self.match(MyParser.PUNCTUATION)
                self.state = 382
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 381
                    self.expressionList()


                self.state = 384
                self.match(MyParser.PUNCTUATION)
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MyParser.NUMBER, 0)

        def STRING_SINGLE(self):
            return self.getToken(MyParser.STRING_SINGLE, 0)

        def STRING_DOUBLE(self):
            return self.getToken(MyParser.STRING_DOUBLE, 0)

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def getRuleIndex(self):
            return MyParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = MyParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4194) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[30] = self.expression_sempred
        self._predicates[35] = self.condition_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




