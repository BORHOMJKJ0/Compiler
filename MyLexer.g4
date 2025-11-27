lexer grammar MyLexer;

options { language = Python3; }

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
    "WHEN","WHERE","WINDOW","WITH","VIEW","TRIGGER","FUNCTION","PROCEDURE","BEGIN","LOOP",
    "REFERENCES","GRANT","REVOKE","TEMP","TEMPORARY",
    "REPLACE","MATERIALIZED","ESCAPE","DECLARE", "KEY", "FIRST", "ONLY",
}
}

@lexer::members {
_commentLevel = 0
}

fragment A : [aA]; 
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

fragment KEY : [a-zA-Z_][a-zA-Z0-9_]*;
fragment DIGITS : [0-9]+;
fragment EXP : [eE] [+-]? DIGITS;

LINE_COMMENT : '--' ~[\r\n]* ;

BLOCK_COMMENT_START
    : '/*' { self._commentLevel = 1; } -> pushMode(COMMENT_MODE)
    ;

WS : [ \t\r\n]+ -> skip ;

STRING
    :  '\'' ( '\'\'' | '\\' . | ~['\\\r\n] )* '\''
    |  '0' X ([0-9a-fA-F] | '\\' [ \t]* [\r\n])+  
    |  '0' B ([01] | '\\' [ \t]* [\r\n])+
    ;

VARIABLE
    :  '@@' KEY
    |  '@' KEY
    ;

IDENTIFIER
    : KEY
      {
if self.text.upper() in KEYWORDS:
    self.type = MyLexer.KEYWORD
      }
    ;

KEYWORD : ; 

NUMBER
    : DIGITS ('.' DIGITS)? (EXP)?
    | '.' DIGITS (EXP)?
    ;

OPERATOR
    : '+' | '-' | '*' | '/' | '%'
    | '=' | '<>' | '!=' | '<' | '>' | '<=' | '>='
    | '+=' | '-=' | '*=' | '/='
    | '&' | '|' | '^' | '~' | '<<' | '>>'
    | '.' | ';' | ',' | '(' | ')'
    ;

mode COMMENT_MODE;

COMMENT_MODE_RULE
    : '/*' { self._commentLevel += 1; }
    | '*/' {
        self._commentLevel -= 1;
        if self._commentLevel == 0:
            self.popMode()
      }
    | .
    ;