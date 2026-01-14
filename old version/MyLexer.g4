lexer grammar MyLexer;

options { language = Python3; }

tokens { KEYWORD }

@lexer::header {
KEYWORDS = {
    "ADD","ALL","ALTER","AND","ANY","AS","ASC","BETWEEN","BY","CASE","CHECK",
    "COLUMN","CONSTRAINT","CREATE","CROSS","DATABASE","DEFAULT","DELETE",
    "DESC","DISTINCT","DROP","ELSE","END","EXCEPT","EXISTS","FALSE","FETCH",
    "FOREIGN","FROM","FULL","GROUP","HAVING","ILIKE","IN","INDEX","INNER",
    "INSERT","INTERSECT","INTO","IS","JOIN","LEFT","LIKE","LIMIT","NATURAL",
    "NOT","NULL","OFFSET","ON","OR","ORDER","OUTER","OVER","PARTITION",
    "PRIMARY","RETURNING","RIGHT","ROW","ROWS","SELECT","SET","TABLE",
    "THEN","TOP","TRUE","UNION","UNIQUE","UNNEST","UPDATE","USING","VALUES",
    "WHEN","WHERE","WINDOW","WITH","VIEW","TRIGGER","FUNCTION","PROCEDURE",
    "BEGIN","LOOP","REFERENCES","GRANT","REVOKE","TEMP","TEMPORARY",
    "REPLACE","MATERIALIZED","ESCAPE","DECLARE","KEY","FIRST","ONLY",
    "TRY","CATCH","EXEC","GO","QUOTENAME","RAISERROR","NVARCHAR","INT",
    "BIGINT","MAX","ERROR_MESSAGE","ERROR_SEVERITY","ERROR_STATE",
    "SCHEMA_NAME","SCHEMA","OBJECT","TYPE","INFORMATION_SCHEMA",
    "TABLES","BASE","COLUMNS","KEYS","PARENT","CONSTRAINTS",
    "NCHAR","VARCHAR","CHAR","DATETIME","DATE","TIME","FLOAT","REAL",
    "NUMERIC","MONEY","SMALLMONEY","BIT","TINYINT","SMALLINT",
    "CURSOR","IDENTITY","SEQUENCES","OUTPUT","OPENROWSET","OPENJSON",
    "SP_EXECUTESQL","FOREIGN_KEYS","PARENT_OBJECT_ID","EXECPT",
    "OBJECT_ID","OBJECT_NAME","OBJECT_SCHEMA_NAME","TABLE_SCHEMA","TABLE_NAME",
    "TABLE_TYPE","IF"
}
}

@lexer::members {
_commentLevel = 0
}

fragment LETTER : [a-zA-Z];
fragment DIGIT : [0-9];
fragment UNDERSCORE : '_';
fragment HEX_DIGIT : [0-9A-Fa-f];

fragment VALID_ID_START : LETTER | UNDERSCORE ;
fragment VALID_ID_CONTINUE : LETTER | DIGIT | UNDERSCORE | '\'';

fragment DIGITS : DIGIT+;
fragment EXP : [eE] [+-]? DIGITS;

LINE_COMMENT
    : '--' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT_START
    : '/*' { self._commentLevel = 1; } -> pushMode(COMMENT_MODE)
    ;

WS : [ \t\r\n]+ -> skip ;

STRING_SINGLE
    : [nN]? '\'' ( '\'\'' | '\\' '\r'? '\n' | ~['\\\r\n] | '\r' | '\n' )* '\''
    ;

STRING_DOUBLE
    : [nN]? '"' ( '""' | '\\' '\r'? '\n' | ~["\\\r\n] | '\r' | '\n' )* '"'
    ;

HEX_STRING
    : '0' [xX] HEX_DIGIT+ ( '\\' [\r\n] HEX_DIGIT* )*
    ;

BIT_STRING
    : '0' [bB] [01]+ ( '\\' [\r\n] [01]* )*
    ;

BRACKET_IDENTIFIER
    : '[' (~[\]\r\n])* ']'
      {
        self.type = MyLexer.IDENTIFIER
      }
    ;

VARIABLE
    :  '@@' VALID_ID_START VALID_ID_CONTINUE*
    |  '@' VALID_ID_START VALID_ID_CONTINUE*
    ;

IDENTIFIER
    : VALID_ID_START VALID_ID_CONTINUE*
      {
        if self.text.upper() in KEYWORDS:
            self.type = MyLexer.KEYWORD
      }
    | UNDERSCORE+ DIGIT+
      {
        if self.text.upper() in KEYWORDS:
            self.type = MyLexer.KEYWORD
      }
    ;

NUMBER
    : DIGITS ('.' DIGITS)? (EXP)?
    | '.' DIGITS (EXP)?
    ;

OPERATOR
    : '+' | '-' | '*' | '/' | '%'
    | '=' | '<>' | '!=' | '<' | '>' | '<=' | '>='
    | '+=' | '-=' | '*=' | '/='
    | '&' | '|' | '^' | '~' | '<<' | '>>'
    ;

PUNCTUATION
    : '.' | ';' | ',' | '(' | ')'
    ;

mode COMMENT_MODE;

COMMENT_OPEN
    : '/*' { self._commentLevel += 1; }
    ;

COMMENT_CLOSE
    : '*/' {
        self._commentLevel -= 1;
        if self._commentLevel == 0:
            self.popMode()
      }
    ;

COMMENT_TEXT
    : . -> skip
    ;