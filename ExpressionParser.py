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
        4,1,295,131,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,5,0,37,8,0,10,0,12,0,40,9,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,52,8,1,1,1,1,1,1,1,
        1,1,3,1,58,8,1,1,2,1,2,1,3,1,3,1,3,4,3,65,8,3,11,3,12,3,66,1,4,1,
        4,1,4,5,4,72,8,4,10,4,12,4,75,9,4,1,5,1,5,1,6,1,6,1,6,1,6,3,6,83,
        8,6,1,7,1,7,1,8,1,8,1,8,3,8,90,8,8,1,8,1,8,3,8,94,8,8,1,8,1,8,1,
        9,1,9,4,9,100,8,9,11,9,12,9,101,1,9,3,9,105,8,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,5,13,122,
        8,13,10,13,12,13,125,9,13,1,14,1,14,1,15,1,15,1,15,0,0,16,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,0,3,8,0,4,4,11,11,83,83,89,
        89,94,94,101,101,114,114,295,295,3,0,102,102,289,290,294,294,3,0,
        1,12,14,28,30,264,135,0,32,1,0,0,0,2,57,1,0,0,0,4,59,1,0,0,0,6,61,
        1,0,0,0,8,68,1,0,0,0,10,76,1,0,0,0,12,82,1,0,0,0,14,84,1,0,0,0,16,
        89,1,0,0,0,18,97,1,0,0,0,20,108,1,0,0,0,22,113,1,0,0,0,24,116,1,
        0,0,0,26,118,1,0,0,0,28,126,1,0,0,0,30,128,1,0,0,0,32,38,3,2,1,0,
        33,34,3,4,2,0,34,35,3,2,1,0,35,37,1,0,0,0,36,33,1,0,0,0,37,40,1,
        0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,1,1,0,0,0,40,38,1,0,0,0,41,
        58,3,10,5,0,42,58,3,16,8,0,43,58,3,18,9,0,44,58,3,6,3,0,45,58,3,
        12,6,0,46,58,5,292,0,0,47,51,5,268,0,0,48,52,3,30,15,0,49,52,3,0,
        0,0,50,52,3,8,4,0,51,48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,53,
        1,0,0,0,53,54,5,269,0,0,54,58,1,0,0,0,55,56,5,295,0,0,56,58,3,2,
        1,0,57,41,1,0,0,0,57,42,1,0,0,0,57,43,1,0,0,0,57,44,1,0,0,0,57,45,
        1,0,0,0,57,46,1,0,0,0,57,47,1,0,0,0,57,55,1,0,0,0,58,3,1,0,0,0,59,
        60,7,0,0,0,60,5,1,0,0,0,61,64,3,12,6,0,62,63,5,265,0,0,63,65,3,12,
        6,0,64,62,1,0,0,0,65,66,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,7,
        1,0,0,0,68,73,3,0,0,0,69,70,5,266,0,0,70,72,3,0,0,0,71,69,1,0,0,
        0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,9,1,0,0,0,75,73,1,
        0,0,0,76,77,7,1,0,0,77,11,1,0,0,0,78,83,5,293,0,0,79,83,5,291,0,
        0,80,83,5,290,0,0,81,83,3,14,7,0,82,78,1,0,0,0,82,79,1,0,0,0,82,
        80,1,0,0,0,82,81,1,0,0,0,83,13,1,0,0,0,84,85,7,2,0,0,85,15,1,0,0,
        0,86,90,5,202,0,0,87,90,5,204,0,0,88,90,3,12,6,0,89,86,1,0,0,0,89,
        87,1,0,0,0,89,88,1,0,0,0,90,91,1,0,0,0,91,93,5,268,0,0,92,94,3,8,
        4,0,93,92,1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,96,5,269,0,0,96,
        17,1,0,0,0,97,99,5,17,0,0,98,100,3,20,10,0,99,98,1,0,0,0,100,101,
        1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,105,3,
        22,11,0,104,103,1,0,0,0,104,105,1,0,0,0,105,106,1,0,0,0,106,107,
        5,55,0,0,107,19,1,0,0,0,108,109,5,173,0,0,109,110,3,24,12,0,110,
        111,5,154,0,0,111,112,3,0,0,0,112,21,1,0,0,0,113,114,5,54,0,0,114,
        115,3,0,0,0,115,23,1,0,0,0,116,117,3,0,0,0,117,25,1,0,0,0,118,123,
        3,12,6,0,119,120,5,265,0,0,120,122,3,12,6,0,121,119,1,0,0,0,122,
        125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,27,1,0,0,0,125,123,
        1,0,0,0,126,127,3,12,6,0,127,29,1,0,0,0,128,129,1,0,0,0,129,31,1,
        0,0,0,11,38,51,57,66,73,82,89,93,101,104,123
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

    symbolicNames = [ "<INVALID>", "ADD", "ALL", "ALTER", "AND", "ANY", 
                      "AS", "ASC", "AUTHORIZATION", "BACKUP", "BEGIN", "BETWEEN", 
                      "BREAK", "BROWSE", "BULK", "BY", "CASCADE", "CASE", 
                      "CHECK", "CHECKPOINT", "CLOSE", "CLUSTERED", "COALESCE", 
                      "COLLATE", "COLUMN", "COMMIT", "COMPUTE", "CONSTRAINT", 
                      "CONTAINS", "CONTAINSTABLE", "CONTINUE", "CONVERT", 
                      "CAST", "CREATE", "CROSS", "CURRENT", "CURRENT_DATE", 
                      "CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER", 
                      "CURSOR", "DATABASE", "DBCC", "DEALLOCATE", "DECLARE", 
                      "DEFAULT", "DELETE", "DENY", "DESC", "DISTINCT", "DISTRIBUTED", 
                      "DOUBLE", "DROP", "DUMP", "ELSE", "END", "ERRLVL", 
                      "ESCAPE", "EXCEPT", "EXEC", "EXECUTE", "EXISTS", "EXIT", 
                      "EXTERNAL", "FETCH", "FILE", "FILLFACTOR", "FOR", 
                      "FOREIGN", "FREETEXT", "FREETEXTTABLE", "FROM", "FULL", 
                      "FUNCTION", "GOTO", "GRANT", "GROUP", "HAVING", "HOLDLOCK", 
                      "IDENTITY", "IDENTITY_INSERT", "IDENTITYCOL", "IF", 
                      "IN", "INDEX", "INNER", "INSERT", "INTERSECT", "INTO", 
                      "IS", "JOIN", "KEY", "KILL", "LEFT", "LIKE", "LINENO", 
                      "LOAD", "MERGE", "NATIONAL", "NOCHECK", "NONCLUSTERED", 
                      "NOT", "NULL", "NULLIF", "OF", "OFF", "OFFSETS", "ON", 
                      "OPEN", "OPENDATASOURCE", "OPENQUERY", "OPENROWSET", 
                      "OPENXML", "OPTION", "OR", "ORDER", "OUTER", "OVER", 
                      "PERCENT", "PLAN", "PRECISION", "PRIMARY", "PRINT", 
                      "PROC", "PROCEDURE", "PUBLIC", "RAISERROR", "READ", 
                      "READTEXT", "RECONFIGURE", "REFERENCES", "REPLICATION", 
                      "RESTORE", "RESTRICT", "RETURN", "REVERT", "REVOKE", 
                      "RIGHT", "ROLLBACK", "ROWCOUNT", "ROWGUIDCOL", "RULE", 
                      "SAVE", "SAVEPOINT", "SESSION_USER", "SET", "SETUSER", 
                      "SHUTDOWN", "SOME", "STATISTICS", "SYSTEM_USER", "TABLE", 
                      "TABLESAMPLE", "TEXTSIZE", "THEN", "TO", "TOP", "TRAN", 
                      "TRANSACTION", "TRIGGER", "TRUNCATE", "TSEQUAL", "UNION", 
                      "UNIQUE", "UNPIVOT", "UPDATE", "UPDATETEXT", "USE", 
                      "USER", "VALUES", "VARYING", "VIEW", "WAITFOR", "WHEN", 
                      "WHERE", "WHILE", "WITH", "WRITETEXT", "INT", "BIGINT", 
                      "SMALLINT", "TINYINT", "BIT", "DECIMAL", "NUMERIC", 
                      "FLOAT", "REAL", "MONEY", "SMALLMONEY", "CHAR", "NCHAR", 
                      "VARCHAR", "TEXT", "NTEXT", "DATE", "DATETIME", "TIME", 
                      "TIMESTAMP", "UNIQUEIDENTIFIER", "SQL_VARIANT", "XML", 
                      "COUNT", "MAX", "MIN", "AVG", "SUM", "LEN", "UPPER", 
                      "LOWER", "GETDATE", "ISNULL", "SUBSTRING", "DATEADD", 
                      "DATEDIFF", "ROUND", "CEILING", "FLOOR", "FALSE", 
                      "ILIKE", "LIMIT", "NATURAL", "PARTITION", "OFFSET", 
                      "RETURNING", "SELECT", "UNNEST", "WINDOW", "TEMP", 
                      "TEMPORARY", "LOOP", "REPLACE", "MATERIALIZED", "FIRST", 
                      "TRY", "CATCH", "GO", "QUOTENAME", "NVARCHAR", "ERROR_MESSAGE", 
                      "ERROR_SEVERITY", "ERROR_STATE", "SCHEMA_NAME", "SCHEMA", 
                      "OBJECT", "TYPE", "INFORMATION_SCHEMA", "TABLES", 
                      "BASE", "COLUMNS", "KEYS", "PARENT", "SEQUENCES", 
                      "OUTPUT", "OPENJSON", "SP_EXECUTESQL", "FOREIGN_KEYS", 
                      "PARENT_OBJECT_ID", "EXECPT", "OBJECT_ID", "OBJECT_NAME", 
                      "OBJECT_SCHEMA_NAME", "TABLE_SCHEMA", "TABLE_NAME", 
                      "TABLE_TYPE", "VERSION", "DOT", "COMMA", "SEMI", "LPAREN", 
                      "RPAREN", "LOCAL", "GLOBAL", "FORWARD_ONLY", "SCROLL", 
                      "STATIC", "KEYSET", "DYNAMIC", "FAST_FORWARD", "READ_ONLY", 
                      "SCROLL_LOCKS", "OPTIMISTIC", "NEXT", "PRIOR", "LAST", 
                      "ABSOLUTE", "RELATIVE", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "WS", "STRING_SINGLE", "STRING_DOUBLE", "BRACKET_IDENTIFIER", 
                      "VARIABLE", "IDENTIFIER", "NUMBER", "OPERATOR" ]

    RULE_expression = 0
    RULE_primary = 1
    RULE_binaryOp = 2
    RULE_columnReference = 3
    RULE_expressionList = 4
    RULE_literal = 5
    RULE_identifier = 6
    RULE_keywordAsIdentifier = 7
    RULE_functionCall = 8
    RULE_caseExpression = 9
    RULE_whenClause = 10
    RULE_elseClause = 11
    RULE_condition = 12
    RULE_tableName = 13
    RULE_columnName = 14
    RULE_selectStatement = 15

    ruleNames =  [ "expression", "primary", "binaryOp", "columnReference", 
                   "expressionList", "literal", "identifier", "keywordAsIdentifier", 
                   "functionCall", "caseExpression", "whenClause", "elseClause", 
                   "condition", "tableName", "columnName", "selectStatement" ]

    EOF = Token.EOF
    ADD=1
    ALL=2
    ALTER=3
    AND=4
    ANY=5
    AS=6
    ASC=7
    AUTHORIZATION=8
    BACKUP=9
    BEGIN=10
    BETWEEN=11
    BREAK=12
    BROWSE=13
    BULK=14
    BY=15
    CASCADE=16
    CASE=17
    CHECK=18
    CHECKPOINT=19
    CLOSE=20
    CLUSTERED=21
    COALESCE=22
    COLLATE=23
    COLUMN=24
    COMMIT=25
    COMPUTE=26
    CONSTRAINT=27
    CONTAINS=28
    CONTAINSTABLE=29
    CONTINUE=30
    CONVERT=31
    CAST=32
    CREATE=33
    CROSS=34
    CURRENT=35
    CURRENT_DATE=36
    CURRENT_TIME=37
    CURRENT_TIMESTAMP=38
    CURRENT_USER=39
    CURSOR=40
    DATABASE=41
    DBCC=42
    DEALLOCATE=43
    DECLARE=44
    DEFAULT=45
    DELETE=46
    DENY=47
    DESC=48
    DISTINCT=49
    DISTRIBUTED=50
    DOUBLE=51
    DROP=52
    DUMP=53
    ELSE=54
    END=55
    ERRLVL=56
    ESCAPE=57
    EXCEPT=58
    EXEC=59
    EXECUTE=60
    EXISTS=61
    EXIT=62
    EXTERNAL=63
    FETCH=64
    FILE=65
    FILLFACTOR=66
    FOR=67
    FOREIGN=68
    FREETEXT=69
    FREETEXTTABLE=70
    FROM=71
    FULL=72
    FUNCTION=73
    GOTO=74
    GRANT=75
    GROUP=76
    HAVING=77
    HOLDLOCK=78
    IDENTITY=79
    IDENTITY_INSERT=80
    IDENTITYCOL=81
    IF=82
    IN=83
    INDEX=84
    INNER=85
    INSERT=86
    INTERSECT=87
    INTO=88
    IS=89
    JOIN=90
    KEY=91
    KILL=92
    LEFT=93
    LIKE=94
    LINENO=95
    LOAD=96
    MERGE=97
    NATIONAL=98
    NOCHECK=99
    NONCLUSTERED=100
    NOT=101
    NULL=102
    NULLIF=103
    OF=104
    OFF=105
    OFFSETS=106
    ON=107
    OPEN=108
    OPENDATASOURCE=109
    OPENQUERY=110
    OPENROWSET=111
    OPENXML=112
    OPTION=113
    OR=114
    ORDER=115
    OUTER=116
    OVER=117
    PERCENT=118
    PLAN=119
    PRECISION=120
    PRIMARY=121
    PRINT=122
    PROC=123
    PROCEDURE=124
    PUBLIC=125
    RAISERROR=126
    READ=127
    READTEXT=128
    RECONFIGURE=129
    REFERENCES=130
    REPLICATION=131
    RESTORE=132
    RESTRICT=133
    RETURN=134
    REVERT=135
    REVOKE=136
    RIGHT=137
    ROLLBACK=138
    ROWCOUNT=139
    ROWGUIDCOL=140
    RULE=141
    SAVE=142
    SAVEPOINT=143
    SESSION_USER=144
    SET=145
    SETUSER=146
    SHUTDOWN=147
    SOME=148
    STATISTICS=149
    SYSTEM_USER=150
    TABLE=151
    TABLESAMPLE=152
    TEXTSIZE=153
    THEN=154
    TO=155
    TOP=156
    TRAN=157
    TRANSACTION=158
    TRIGGER=159
    TRUNCATE=160
    TSEQUAL=161
    UNION=162
    UNIQUE=163
    UNPIVOT=164
    UPDATE=165
    UPDATETEXT=166
    USE=167
    USER=168
    VALUES=169
    VARYING=170
    VIEW=171
    WAITFOR=172
    WHEN=173
    WHERE=174
    WHILE=175
    WITH=176
    WRITETEXT=177
    INT=178
    BIGINT=179
    SMALLINT=180
    TINYINT=181
    BIT=182
    DECIMAL=183
    NUMERIC=184
    FLOAT=185
    REAL=186
    MONEY=187
    SMALLMONEY=188
    CHAR=189
    NCHAR=190
    VARCHAR=191
    TEXT=192
    NTEXT=193
    DATE=194
    DATETIME=195
    TIME=196
    TIMESTAMP=197
    UNIQUEIDENTIFIER=198
    SQL_VARIANT=199
    XML=200
    COUNT=201
    MAX=202
    MIN=203
    AVG=204
    SUM=205
    LEN=206
    UPPER=207
    LOWER=208
    GETDATE=209
    ISNULL=210
    SUBSTRING=211
    DATEADD=212
    DATEDIFF=213
    ROUND=214
    CEILING=215
    FLOOR=216
    FALSE=217
    ILIKE=218
    LIMIT=219
    NATURAL=220
    PARTITION=221
    OFFSET=222
    RETURNING=223
    SELECT=224
    UNNEST=225
    WINDOW=226
    TEMP=227
    TEMPORARY=228
    LOOP=229
    REPLACE=230
    MATERIALIZED=231
    FIRST=232
    TRY=233
    CATCH=234
    GO=235
    QUOTENAME=236
    NVARCHAR=237
    ERROR_MESSAGE=238
    ERROR_SEVERITY=239
    ERROR_STATE=240
    SCHEMA_NAME=241
    SCHEMA=242
    OBJECT=243
    TYPE=244
    INFORMATION_SCHEMA=245
    TABLES=246
    BASE=247
    COLUMNS=248
    KEYS=249
    PARENT=250
    SEQUENCES=251
    OUTPUT=252
    OPENJSON=253
    SP_EXECUTESQL=254
    FOREIGN_KEYS=255
    PARENT_OBJECT_ID=256
    EXECPT=257
    OBJECT_ID=258
    OBJECT_NAME=259
    OBJECT_SCHEMA_NAME=260
    TABLE_SCHEMA=261
    TABLE_NAME=262
    TABLE_TYPE=263
    VERSION=264
    DOT=265
    COMMA=266
    SEMI=267
    LPAREN=268
    RPAREN=269
    LOCAL=270
    GLOBAL=271
    FORWARD_ONLY=272
    SCROLL=273
    STATIC=274
    KEYSET=275
    DYNAMIC=276
    FAST_FORWARD=277
    READ_ONLY=278
    SCROLL_LOCKS=279
    OPTIMISTIC=280
    NEXT=281
    PRIOR=282
    LAST=283
    ABSOLUTE=284
    RELATIVE=285
    LINE_COMMENT=286
    BLOCK_COMMENT=287
    WS=288
    STRING_SINGLE=289
    STRING_DOUBLE=290
    BRACKET_IDENTIFIER=291
    VARIABLE=292
    IDENTIFIER=293
    NUMBER=294
    OPERATOR=295

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
            self.state = 32
            self.primary()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==11 or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 2147747905) != 0) or _la==295:
                self.state = 33
                self.binaryOp()
                self.state = 34
                self.primary()
                self.state = 40
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


        def columnReference(self):
            return self.getTypedRuleContext(ExpressionParser.ColumnReferenceContext,0)


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
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.caseExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.columnReference()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.identifier()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 46
                self.match(ExpressionParser.VARIABLE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 47
                self.match(ExpressionParser.LPAREN)
                self.state = 51
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 48
                    self.selectStatement()
                    pass

                elif la_ == 2:
                    self.state = 49
                    self.expression()
                    pass

                elif la_ == 3:
                    self.state = 50
                    self.expressionList()
                    pass


                self.state = 53
                self.match(ExpressionParser.RPAREN)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 55
                self.match(ExpressionParser.OPERATOR)
                self.state = 56
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
            self.state = 59
            _la = self._input.LA(1)
            if not(_la==4 or _la==11 or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 2147747905) != 0) or _la==295):
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


    class ColumnReferenceContext(ParserRuleContext):
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
            return ExpressionParser.RULE_columnReference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnReference" ):
                listener.enterColumnReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnReference" ):
                listener.exitColumnReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnReference" ):
                return visitor.visitColumnReference(self)
            else:
                return visitor.visitChildren(self)




    def columnReference(self):

        localctx = ExpressionParser.ColumnReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_columnReference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.identifier()
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.match(ExpressionParser.DOT)
                self.state = 63
                self.identifier()
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==265):
                    break

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
        self.enterRule(localctx, 8, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.expression()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 69
                self.match(ExpressionParser.COMMA)
                self.state = 70
                self.expression()
                self.state = 75
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
        self.enterRule(localctx, 10, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            _la = self._input.LA(1)
            if not(_la==102 or ((((_la - 289)) & ~0x3f) == 0 and ((1 << (_la - 289)) & 35) != 0)):
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

        def STRING_DOUBLE(self):
            return self.getToken(ExpressionParser.STRING_DOUBLE, 0)

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
        self.enterRule(localctx, 12, self.RULE_identifier)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [293]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(ExpressionParser.IDENTIFIER)
                pass
            elif token in [291]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(ExpressionParser.BRACKET_IDENTIFIER)
                pass
            elif token in [290]:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.match(ExpressionParser.STRING_DOUBLE)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264]:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
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

        def ADD(self):
            return self.getToken(ExpressionParser.ADD, 0)

        def ALL(self):
            return self.getToken(ExpressionParser.ALL, 0)

        def ALTER(self):
            return self.getToken(ExpressionParser.ALTER, 0)

        def AND(self):
            return self.getToken(ExpressionParser.AND, 0)

        def ANY(self):
            return self.getToken(ExpressionParser.ANY, 0)

        def AS(self):
            return self.getToken(ExpressionParser.AS, 0)

        def ASC(self):
            return self.getToken(ExpressionParser.ASC, 0)

        def AUTHORIZATION(self):
            return self.getToken(ExpressionParser.AUTHORIZATION, 0)

        def BACKUP(self):
            return self.getToken(ExpressionParser.BACKUP, 0)

        def BEGIN(self):
            return self.getToken(ExpressionParser.BEGIN, 0)

        def BETWEEN(self):
            return self.getToken(ExpressionParser.BETWEEN, 0)

        def BREAK(self):
            return self.getToken(ExpressionParser.BREAK, 0)

        def BULK(self):
            return self.getToken(ExpressionParser.BULK, 0)

        def BY(self):
            return self.getToken(ExpressionParser.BY, 0)

        def CASCADE(self):
            return self.getToken(ExpressionParser.CASCADE, 0)

        def CASE(self):
            return self.getToken(ExpressionParser.CASE, 0)

        def CHECK(self):
            return self.getToken(ExpressionParser.CHECK, 0)

        def CHECKPOINT(self):
            return self.getToken(ExpressionParser.CHECKPOINT, 0)

        def CLOSE(self):
            return self.getToken(ExpressionParser.CLOSE, 0)

        def CLUSTERED(self):
            return self.getToken(ExpressionParser.CLUSTERED, 0)

        def COALESCE(self):
            return self.getToken(ExpressionParser.COALESCE, 0)

        def COLLATE(self):
            return self.getToken(ExpressionParser.COLLATE, 0)

        def COLUMN(self):
            return self.getToken(ExpressionParser.COLUMN, 0)

        def COMMIT(self):
            return self.getToken(ExpressionParser.COMMIT, 0)

        def COMPUTE(self):
            return self.getToken(ExpressionParser.COMPUTE, 0)

        def CONSTRAINT(self):
            return self.getToken(ExpressionParser.CONSTRAINT, 0)

        def CONTAINS(self):
            return self.getToken(ExpressionParser.CONTAINS, 0)

        def CONTINUE(self):
            return self.getToken(ExpressionParser.CONTINUE, 0)

        def CONVERT(self):
            return self.getToken(ExpressionParser.CONVERT, 0)

        def CAST(self):
            return self.getToken(ExpressionParser.CAST, 0)

        def CREATE(self):
            return self.getToken(ExpressionParser.CREATE, 0)

        def CROSS(self):
            return self.getToken(ExpressionParser.CROSS, 0)

        def CURRENT(self):
            return self.getToken(ExpressionParser.CURRENT, 0)

        def CURRENT_DATE(self):
            return self.getToken(ExpressionParser.CURRENT_DATE, 0)

        def CURRENT_TIME(self):
            return self.getToken(ExpressionParser.CURRENT_TIME, 0)

        def CURRENT_TIMESTAMP(self):
            return self.getToken(ExpressionParser.CURRENT_TIMESTAMP, 0)

        def CURRENT_USER(self):
            return self.getToken(ExpressionParser.CURRENT_USER, 0)

        def CURSOR(self):
            return self.getToken(ExpressionParser.CURSOR, 0)

        def DATABASE(self):
            return self.getToken(ExpressionParser.DATABASE, 0)

        def DBCC(self):
            return self.getToken(ExpressionParser.DBCC, 0)

        def DEALLOCATE(self):
            return self.getToken(ExpressionParser.DEALLOCATE, 0)

        def DECLARE(self):
            return self.getToken(ExpressionParser.DECLARE, 0)

        def DEFAULT(self):
            return self.getToken(ExpressionParser.DEFAULT, 0)

        def DELETE(self):
            return self.getToken(ExpressionParser.DELETE, 0)

        def DENY(self):
            return self.getToken(ExpressionParser.DENY, 0)

        def DESC(self):
            return self.getToken(ExpressionParser.DESC, 0)

        def DISTINCT(self):
            return self.getToken(ExpressionParser.DISTINCT, 0)

        def DISTRIBUTED(self):
            return self.getToken(ExpressionParser.DISTRIBUTED, 0)

        def DOUBLE(self):
            return self.getToken(ExpressionParser.DOUBLE, 0)

        def DROP(self):
            return self.getToken(ExpressionParser.DROP, 0)

        def DUMP(self):
            return self.getToken(ExpressionParser.DUMP, 0)

        def ELSE(self):
            return self.getToken(ExpressionParser.ELSE, 0)

        def END(self):
            return self.getToken(ExpressionParser.END, 0)

        def ERRLVL(self):
            return self.getToken(ExpressionParser.ERRLVL, 0)

        def ESCAPE(self):
            return self.getToken(ExpressionParser.ESCAPE, 0)

        def EXCEPT(self):
            return self.getToken(ExpressionParser.EXCEPT, 0)

        def EXEC(self):
            return self.getToken(ExpressionParser.EXEC, 0)

        def EXECUTE(self):
            return self.getToken(ExpressionParser.EXECUTE, 0)

        def EXISTS(self):
            return self.getToken(ExpressionParser.EXISTS, 0)

        def EXIT(self):
            return self.getToken(ExpressionParser.EXIT, 0)

        def EXTERNAL(self):
            return self.getToken(ExpressionParser.EXTERNAL, 0)

        def FETCH(self):
            return self.getToken(ExpressionParser.FETCH, 0)

        def FILE(self):
            return self.getToken(ExpressionParser.FILE, 0)

        def FILLFACTOR(self):
            return self.getToken(ExpressionParser.FILLFACTOR, 0)

        def FOR(self):
            return self.getToken(ExpressionParser.FOR, 0)

        def FOREIGN(self):
            return self.getToken(ExpressionParser.FOREIGN, 0)

        def FREETEXT(self):
            return self.getToken(ExpressionParser.FREETEXT, 0)

        def FREETEXTTABLE(self):
            return self.getToken(ExpressionParser.FREETEXTTABLE, 0)

        def FROM(self):
            return self.getToken(ExpressionParser.FROM, 0)

        def FULL(self):
            return self.getToken(ExpressionParser.FULL, 0)

        def FUNCTION(self):
            return self.getToken(ExpressionParser.FUNCTION, 0)

        def GOTO(self):
            return self.getToken(ExpressionParser.GOTO, 0)

        def GRANT(self):
            return self.getToken(ExpressionParser.GRANT, 0)

        def GROUP(self):
            return self.getToken(ExpressionParser.GROUP, 0)

        def HAVING(self):
            return self.getToken(ExpressionParser.HAVING, 0)

        def HOLDLOCK(self):
            return self.getToken(ExpressionParser.HOLDLOCK, 0)

        def IDENTITY(self):
            return self.getToken(ExpressionParser.IDENTITY, 0)

        def IDENTITY_INSERT(self):
            return self.getToken(ExpressionParser.IDENTITY_INSERT, 0)

        def IDENTITYCOL(self):
            return self.getToken(ExpressionParser.IDENTITYCOL, 0)

        def IF(self):
            return self.getToken(ExpressionParser.IF, 0)

        def IN(self):
            return self.getToken(ExpressionParser.IN, 0)

        def INDEX(self):
            return self.getToken(ExpressionParser.INDEX, 0)

        def INNER(self):
            return self.getToken(ExpressionParser.INNER, 0)

        def INSERT(self):
            return self.getToken(ExpressionParser.INSERT, 0)

        def INTERSECT(self):
            return self.getToken(ExpressionParser.INTERSECT, 0)

        def INTO(self):
            return self.getToken(ExpressionParser.INTO, 0)

        def IS(self):
            return self.getToken(ExpressionParser.IS, 0)

        def JOIN(self):
            return self.getToken(ExpressionParser.JOIN, 0)

        def KEY(self):
            return self.getToken(ExpressionParser.KEY, 0)

        def KILL(self):
            return self.getToken(ExpressionParser.KILL, 0)

        def LEFT(self):
            return self.getToken(ExpressionParser.LEFT, 0)

        def LIKE(self):
            return self.getToken(ExpressionParser.LIKE, 0)

        def LINENO(self):
            return self.getToken(ExpressionParser.LINENO, 0)

        def LOAD(self):
            return self.getToken(ExpressionParser.LOAD, 0)

        def MERGE(self):
            return self.getToken(ExpressionParser.MERGE, 0)

        def NATIONAL(self):
            return self.getToken(ExpressionParser.NATIONAL, 0)

        def NOCHECK(self):
            return self.getToken(ExpressionParser.NOCHECK, 0)

        def NONCLUSTERED(self):
            return self.getToken(ExpressionParser.NONCLUSTERED, 0)

        def NOT(self):
            return self.getToken(ExpressionParser.NOT, 0)

        def NULL(self):
            return self.getToken(ExpressionParser.NULL, 0)

        def NULLIF(self):
            return self.getToken(ExpressionParser.NULLIF, 0)

        def OF(self):
            return self.getToken(ExpressionParser.OF, 0)

        def OFF(self):
            return self.getToken(ExpressionParser.OFF, 0)

        def OFFSETS(self):
            return self.getToken(ExpressionParser.OFFSETS, 0)

        def ON(self):
            return self.getToken(ExpressionParser.ON, 0)

        def OPEN(self):
            return self.getToken(ExpressionParser.OPEN, 0)

        def OPENDATASOURCE(self):
            return self.getToken(ExpressionParser.OPENDATASOURCE, 0)

        def OPENQUERY(self):
            return self.getToken(ExpressionParser.OPENQUERY, 0)

        def OPENROWSET(self):
            return self.getToken(ExpressionParser.OPENROWSET, 0)

        def OPENXML(self):
            return self.getToken(ExpressionParser.OPENXML, 0)

        def OPTION(self):
            return self.getToken(ExpressionParser.OPTION, 0)

        def OR(self):
            return self.getToken(ExpressionParser.OR, 0)

        def ORDER(self):
            return self.getToken(ExpressionParser.ORDER, 0)

        def OUTER(self):
            return self.getToken(ExpressionParser.OUTER, 0)

        def OVER(self):
            return self.getToken(ExpressionParser.OVER, 0)

        def PERCENT(self):
            return self.getToken(ExpressionParser.PERCENT, 0)

        def PLAN(self):
            return self.getToken(ExpressionParser.PLAN, 0)

        def PRECISION(self):
            return self.getToken(ExpressionParser.PRECISION, 0)

        def PRIMARY(self):
            return self.getToken(ExpressionParser.PRIMARY, 0)

        def PRINT(self):
            return self.getToken(ExpressionParser.PRINT, 0)

        def PROC(self):
            return self.getToken(ExpressionParser.PROC, 0)

        def PROCEDURE(self):
            return self.getToken(ExpressionParser.PROCEDURE, 0)

        def PUBLIC(self):
            return self.getToken(ExpressionParser.PUBLIC, 0)

        def RAISERROR(self):
            return self.getToken(ExpressionParser.RAISERROR, 0)

        def READ(self):
            return self.getToken(ExpressionParser.READ, 0)

        def READTEXT(self):
            return self.getToken(ExpressionParser.READTEXT, 0)

        def RECONFIGURE(self):
            return self.getToken(ExpressionParser.RECONFIGURE, 0)

        def REFERENCES(self):
            return self.getToken(ExpressionParser.REFERENCES, 0)

        def REPLICATION(self):
            return self.getToken(ExpressionParser.REPLICATION, 0)

        def RESTORE(self):
            return self.getToken(ExpressionParser.RESTORE, 0)

        def RESTRICT(self):
            return self.getToken(ExpressionParser.RESTRICT, 0)

        def RETURN(self):
            return self.getToken(ExpressionParser.RETURN, 0)

        def REVERT(self):
            return self.getToken(ExpressionParser.REVERT, 0)

        def REVOKE(self):
            return self.getToken(ExpressionParser.REVOKE, 0)

        def RIGHT(self):
            return self.getToken(ExpressionParser.RIGHT, 0)

        def ROLLBACK(self):
            return self.getToken(ExpressionParser.ROLLBACK, 0)

        def ROWCOUNT(self):
            return self.getToken(ExpressionParser.ROWCOUNT, 0)

        def ROWGUIDCOL(self):
            return self.getToken(ExpressionParser.ROWGUIDCOL, 0)

        def RULE(self):
            return self.getToken(ExpressionParser.RULE, 0)

        def SAVE(self):
            return self.getToken(ExpressionParser.SAVE, 0)

        def SAVEPOINT(self):
            return self.getToken(ExpressionParser.SAVEPOINT, 0)

        def SCHEMA(self):
            return self.getToken(ExpressionParser.SCHEMA, 0)

        def SCHEMA_NAME(self):
            return self.getToken(ExpressionParser.SCHEMA_NAME, 0)

        def SESSION_USER(self):
            return self.getToken(ExpressionParser.SESSION_USER, 0)

        def SET(self):
            return self.getToken(ExpressionParser.SET, 0)

        def SETUSER(self):
            return self.getToken(ExpressionParser.SETUSER, 0)

        def SHUTDOWN(self):
            return self.getToken(ExpressionParser.SHUTDOWN, 0)

        def SOME(self):
            return self.getToken(ExpressionParser.SOME, 0)

        def STATISTICS(self):
            return self.getToken(ExpressionParser.STATISTICS, 0)

        def SYSTEM_USER(self):
            return self.getToken(ExpressionParser.SYSTEM_USER, 0)

        def TABLE(self):
            return self.getToken(ExpressionParser.TABLE, 0)

        def TABLESAMPLE(self):
            return self.getToken(ExpressionParser.TABLESAMPLE, 0)

        def TEXTSIZE(self):
            return self.getToken(ExpressionParser.TEXTSIZE, 0)

        def THEN(self):
            return self.getToken(ExpressionParser.THEN, 0)

        def TO(self):
            return self.getToken(ExpressionParser.TO, 0)

        def TOP(self):
            return self.getToken(ExpressionParser.TOP, 0)

        def TRAN(self):
            return self.getToken(ExpressionParser.TRAN, 0)

        def TRANSACTION(self):
            return self.getToken(ExpressionParser.TRANSACTION, 0)

        def TRIGGER(self):
            return self.getToken(ExpressionParser.TRIGGER, 0)

        def TRUNCATE(self):
            return self.getToken(ExpressionParser.TRUNCATE, 0)

        def TSEQUAL(self):
            return self.getToken(ExpressionParser.TSEQUAL, 0)

        def UNION(self):
            return self.getToken(ExpressionParser.UNION, 0)

        def UNIQUE(self):
            return self.getToken(ExpressionParser.UNIQUE, 0)

        def UNPIVOT(self):
            return self.getToken(ExpressionParser.UNPIVOT, 0)

        def UPDATE(self):
            return self.getToken(ExpressionParser.UPDATE, 0)

        def UPDATETEXT(self):
            return self.getToken(ExpressionParser.UPDATETEXT, 0)

        def USE(self):
            return self.getToken(ExpressionParser.USE, 0)

        def USER(self):
            return self.getToken(ExpressionParser.USER, 0)

        def VALUES(self):
            return self.getToken(ExpressionParser.VALUES, 0)

        def VARYING(self):
            return self.getToken(ExpressionParser.VARYING, 0)

        def VIEW(self):
            return self.getToken(ExpressionParser.VIEW, 0)

        def WAITFOR(self):
            return self.getToken(ExpressionParser.WAITFOR, 0)

        def WHEN(self):
            return self.getToken(ExpressionParser.WHEN, 0)

        def WHERE(self):
            return self.getToken(ExpressionParser.WHERE, 0)

        def WHILE(self):
            return self.getToken(ExpressionParser.WHILE, 0)

        def WITH(self):
            return self.getToken(ExpressionParser.WITH, 0)

        def WRITETEXT(self):
            return self.getToken(ExpressionParser.WRITETEXT, 0)

        def INT(self):
            return self.getToken(ExpressionParser.INT, 0)

        def BIGINT(self):
            return self.getToken(ExpressionParser.BIGINT, 0)

        def SMALLINT(self):
            return self.getToken(ExpressionParser.SMALLINT, 0)

        def TINYINT(self):
            return self.getToken(ExpressionParser.TINYINT, 0)

        def BIT(self):
            return self.getToken(ExpressionParser.BIT, 0)

        def DECIMAL(self):
            return self.getToken(ExpressionParser.DECIMAL, 0)

        def NUMERIC(self):
            return self.getToken(ExpressionParser.NUMERIC, 0)

        def FLOAT(self):
            return self.getToken(ExpressionParser.FLOAT, 0)

        def REAL(self):
            return self.getToken(ExpressionParser.REAL, 0)

        def MONEY(self):
            return self.getToken(ExpressionParser.MONEY, 0)

        def SMALLMONEY(self):
            return self.getToken(ExpressionParser.SMALLMONEY, 0)

        def CHAR(self):
            return self.getToken(ExpressionParser.CHAR, 0)

        def NCHAR(self):
            return self.getToken(ExpressionParser.NCHAR, 0)

        def VARCHAR(self):
            return self.getToken(ExpressionParser.VARCHAR, 0)

        def NVARCHAR(self):
            return self.getToken(ExpressionParser.NVARCHAR, 0)

        def TEXT(self):
            return self.getToken(ExpressionParser.TEXT, 0)

        def NTEXT(self):
            return self.getToken(ExpressionParser.NTEXT, 0)

        def DATE(self):
            return self.getToken(ExpressionParser.DATE, 0)

        def DATETIME(self):
            return self.getToken(ExpressionParser.DATETIME, 0)

        def TIME(self):
            return self.getToken(ExpressionParser.TIME, 0)

        def TIMESTAMP(self):
            return self.getToken(ExpressionParser.TIMESTAMP, 0)

        def UNIQUEIDENTIFIER(self):
            return self.getToken(ExpressionParser.UNIQUEIDENTIFIER, 0)

        def SQL_VARIANT(self):
            return self.getToken(ExpressionParser.SQL_VARIANT, 0)

        def XML(self):
            return self.getToken(ExpressionParser.XML, 0)

        def COUNT(self):
            return self.getToken(ExpressionParser.COUNT, 0)

        def MAX(self):
            return self.getToken(ExpressionParser.MAX, 0)

        def MIN(self):
            return self.getToken(ExpressionParser.MIN, 0)

        def AVG(self):
            return self.getToken(ExpressionParser.AVG, 0)

        def SUM(self):
            return self.getToken(ExpressionParser.SUM, 0)

        def LEN(self):
            return self.getToken(ExpressionParser.LEN, 0)

        def UPPER(self):
            return self.getToken(ExpressionParser.UPPER, 0)

        def LOWER(self):
            return self.getToken(ExpressionParser.LOWER, 0)

        def GETDATE(self):
            return self.getToken(ExpressionParser.GETDATE, 0)

        def ISNULL(self):
            return self.getToken(ExpressionParser.ISNULL, 0)

        def SUBSTRING(self):
            return self.getToken(ExpressionParser.SUBSTRING, 0)

        def DATEADD(self):
            return self.getToken(ExpressionParser.DATEADD, 0)

        def DATEDIFF(self):
            return self.getToken(ExpressionParser.DATEDIFF, 0)

        def ROUND(self):
            return self.getToken(ExpressionParser.ROUND, 0)

        def CEILING(self):
            return self.getToken(ExpressionParser.CEILING, 0)

        def FLOOR(self):
            return self.getToken(ExpressionParser.FLOOR, 0)

        def FALSE(self):
            return self.getToken(ExpressionParser.FALSE, 0)

        def ILIKE(self):
            return self.getToken(ExpressionParser.ILIKE, 0)

        def LIMIT(self):
            return self.getToken(ExpressionParser.LIMIT, 0)

        def NATURAL(self):
            return self.getToken(ExpressionParser.NATURAL, 0)

        def PARTITION(self):
            return self.getToken(ExpressionParser.PARTITION, 0)

        def OFFSET(self):
            return self.getToken(ExpressionParser.OFFSET, 0)

        def RETURNING(self):
            return self.getToken(ExpressionParser.RETURNING, 0)

        def SELECT(self):
            return self.getToken(ExpressionParser.SELECT, 0)

        def UNNEST(self):
            return self.getToken(ExpressionParser.UNNEST, 0)

        def WINDOW(self):
            return self.getToken(ExpressionParser.WINDOW, 0)

        def TEMP(self):
            return self.getToken(ExpressionParser.TEMP, 0)

        def TEMPORARY(self):
            return self.getToken(ExpressionParser.TEMPORARY, 0)

        def LOOP(self):
            return self.getToken(ExpressionParser.LOOP, 0)

        def REPLACE(self):
            return self.getToken(ExpressionParser.REPLACE, 0)

        def MATERIALIZED(self):
            return self.getToken(ExpressionParser.MATERIALIZED, 0)

        def FIRST(self):
            return self.getToken(ExpressionParser.FIRST, 0)

        def TRY(self):
            return self.getToken(ExpressionParser.TRY, 0)

        def CATCH(self):
            return self.getToken(ExpressionParser.CATCH, 0)

        def GO(self):
            return self.getToken(ExpressionParser.GO, 0)

        def QUOTENAME(self):
            return self.getToken(ExpressionParser.QUOTENAME, 0)

        def ERROR_MESSAGE(self):
            return self.getToken(ExpressionParser.ERROR_MESSAGE, 0)

        def ERROR_SEVERITY(self):
            return self.getToken(ExpressionParser.ERROR_SEVERITY, 0)

        def ERROR_STATE(self):
            return self.getToken(ExpressionParser.ERROR_STATE, 0)

        def OBJECT(self):
            return self.getToken(ExpressionParser.OBJECT, 0)

        def TYPE(self):
            return self.getToken(ExpressionParser.TYPE, 0)

        def INFORMATION_SCHEMA(self):
            return self.getToken(ExpressionParser.INFORMATION_SCHEMA, 0)

        def TABLES(self):
            return self.getToken(ExpressionParser.TABLES, 0)

        def BASE(self):
            return self.getToken(ExpressionParser.BASE, 0)

        def COLUMNS(self):
            return self.getToken(ExpressionParser.COLUMNS, 0)

        def KEYS(self):
            return self.getToken(ExpressionParser.KEYS, 0)

        def PARENT(self):
            return self.getToken(ExpressionParser.PARENT, 0)

        def SEQUENCES(self):
            return self.getToken(ExpressionParser.SEQUENCES, 0)

        def OUTPUT(self):
            return self.getToken(ExpressionParser.OUTPUT, 0)

        def OPENJSON(self):
            return self.getToken(ExpressionParser.OPENJSON, 0)

        def SP_EXECUTESQL(self):
            return self.getToken(ExpressionParser.SP_EXECUTESQL, 0)

        def FOREIGN_KEYS(self):
            return self.getToken(ExpressionParser.FOREIGN_KEYS, 0)

        def PARENT_OBJECT_ID(self):
            return self.getToken(ExpressionParser.PARENT_OBJECT_ID, 0)

        def EXECPT(self):
            return self.getToken(ExpressionParser.EXECPT, 0)

        def OBJECT_ID(self):
            return self.getToken(ExpressionParser.OBJECT_ID, 0)

        def OBJECT_NAME(self):
            return self.getToken(ExpressionParser.OBJECT_NAME, 0)

        def OBJECT_SCHEMA_NAME(self):
            return self.getToken(ExpressionParser.OBJECT_SCHEMA_NAME, 0)

        def TABLE_SCHEMA(self):
            return self.getToken(ExpressionParser.TABLE_SCHEMA, 0)

        def TABLE_NAME(self):
            return self.getToken(ExpressionParser.TABLE_NAME, 0)

        def TABLE_TYPE(self):
            return self.getToken(ExpressionParser.TABLE_TYPE, 0)

        def VERSION(self):
            return self.getToken(ExpressionParser.VERSION, 0)

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
        self.enterRule(localctx, 14, self.RULE_keywordAsIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & -536879106) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & -1) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & -1) != 0) or ((((_la - 192)) & ~0x3f) == 0 and ((1 << (_la - 192)) & -1) != 0) or ((((_la - 256)) & ~0x3f) == 0 and ((1 << (_la - 256)) & 511) != 0)):
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
        self.enterRule(localctx, 16, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 86
                self.match(ExpressionParser.MAX)
                pass

            elif la_ == 2:
                self.state = 87
                self.match(ExpressionParser.AVG)
                pass

            elif la_ == 3:
                self.state = 88
                self.identifier()
                pass


            self.state = 91
            self.match(ExpressionParser.LPAREN)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -536879106) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & -1) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & -1) != 0) or ((((_la - 192)) & ~0x3f) == 0 and ((1 << (_la - 192)) & -1) != 0) or ((((_la - 256)) & ~0x3f) == 0 and ((1 << (_la - 256)) & 1090921697791) != 0):
                self.state = 92
                self.expressionList()


            self.state = 95
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
        self.enterRule(localctx, 18, self.RULE_caseExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(ExpressionParser.CASE)
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.whenClause()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==173):
                    break

            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 103
                self.elseClause()


            self.state = 106
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
        self.enterRule(localctx, 20, self.RULE_whenClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(ExpressionParser.WHEN)
            self.state = 109
            self.condition()
            self.state = 110
            self.match(ExpressionParser.THEN)
            self.state = 111
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
        self.enterRule(localctx, 22, self.RULE_elseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(ExpressionParser.ELSE)
            self.state = 114
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
        self.enterRule(localctx, 24, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
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
        self.enterRule(localctx, 26, self.RULE_tableName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.identifier()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==265:
                self.state = 119
                self.match(ExpressionParser.DOT)
                self.state = 120
                self.identifier()
                self.state = 125
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
        self.enterRule(localctx, 28, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
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
        self.enterRule(localctx, 30, self.RULE_selectStatement)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





