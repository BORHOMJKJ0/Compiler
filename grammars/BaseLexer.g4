lexer grammar BaseLexer;

options { language = Python3; }

// Keywords - Case Insensitive
SELECT: [sS][eE][lL][eE][cC][tT];
FROM: [fF][rR][oO][mM];
WHERE: [wW][hH][eE][rR][eE];
INSERT: [iI][nN][sS][eE][rR][tT];
INTO: [iI][nN][tT][oO];
UPDATE: [uU][pP][dD][aA][tT][eE];
DELETE: [dD][eE][lL][eE][tT][eE];
CREATE: [cC][rR][eE][aA][tT][eE];
ALTER: [aA][lL][tT][eE][rR];
TABLE: [tT][aA][bB][lL][eE];
DROP: [dD][rR][oO][pP];
ADD: [aA][dD][dD];
VALUES: [vV][aA][lL][uU][eE][sS];
SET: [sS][eE][tT];
JOIN: [jJ][oO][iI][nN];
INNER: [iI][nN][nN][eE][rR];
LEFT: [lL][eE][fF][tT];
RIGHT: [rR][iI][gG][hH][tT];
FULL: [fF][uU][lL][lL];
OUTER: [oO][uU][tT][eE][rR];
ON: [oO][nN];
AND: [aA][nN][dD];
OR: [oO][rR];
NOT: [nN][oO][tT];
EXISTS: [eE][xX][iI][sS][tT][sS];
IF: [iI][fF];
BEGIN: [bB][eE][gG][iI][nN];
END: [eE][nN][dD];
TRY: [tT][rR][yY];
CATCH: [cC][aA][tT][cC][hH];
DECLARE: [dD][eE][cC][lL][aA][rR][eE];
EXEC: [eE][xX][eE][cC];
GO: [gG][oO];
CASE: [cC][aA][sS][eE];
WHEN: [wW][hH][eE][nN];
THEN: [tT][hH][eE][nN];
ELSE: [eE][lL][sS][eE];
NULL: [nN][uU][lL][lL];
IN: [iI][nN];
IS: [iI][sS];
LIKE: [lL][iI][kK][eE];
BETWEEN: [bB][eE][tT][wW][eE][eE][nN];
ORDER: [oO][rR][dD][eE][rR];
BY: [bB][yY];
GROUP: [gG][rR][oO][uU][pP];
HAVING: [hH][aA][vV][iI][nN][gG];
ASC: [aA][sS][cC];
DESC: [dD][eE][sS][cC];
AS: [aA][sS];
MAX: [mM][aA][xX];
AVG: [aA][vV][gG];
TRUNCATE: [tT][rR][uU][nN][cC][aA][tT][eE];
PRIMARY: [pP][rR][iI][mM][aA][rR][yY];
KEY: [kK][eE][yY];
CONSTRAINT: [cC][oO][nN][sS][tT][rR][aA][iI][nN][tT];
COLUMN: [cC][oO][lL][uU][mM][nN];

// Data Types
INT: [iI][nN][tT];
NVARCHAR: [nN][vV][aA][rR][cC][hH][aA][rR];
BIGINT: [bB][iI][gG][iI][nN][tT];
DATE: [dD][aA][tT][eE];

// Punctuation
DOT: '.';
COMMA: ',';
SEMI: ';';
LPAREN: '(';
RPAREN: ')';

// Other SQL specific
SP_EXECUTESQL: [sS][pP] '_' [eE][xX][eE][cC][uU][tT][eE][sS][qQ][lL];

// T-SQL Specific Keywords
CLUSTERED: [cC][lL][uU][sS][tT][eE][rR][eE][dD];
NONCLUSTERED: [nN][oO][nN][cC][lL][uU][sS][tT][eE][rR][eE][dD];

// Common Rules
LINE_COMMENT: '--' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
WS: [ \t\r\n]+ -> skip;

STRING_SINGLE: [nN]? '\'' ( '\'\'' | ~['] )* '\'';
STRING_DOUBLE: [nN]? '"' ( '""' | ~["] )* '"';

BRACKET_IDENTIFIER: '[' (~[\]])* ']';
VARIABLE: '@' [a-zA-Z_] [a-zA-Z0-9_]*;
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;

OPERATOR: '+' | '-' | '*' | '/' | '=' | '<>' | '!=' | '<' | '>' | '<=' | '>=' | '+=' ;
