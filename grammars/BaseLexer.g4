lexer grammar BaseLexer;
options { language = Python3; }

// ==========================
// Keywords - Case Insensitive
// ==========================
ADD: [aA][dD][dD] | '[' [aA][dD][dD] ']';
ALL: [aA][lL][lL] | '[' [aA][lL][lL] ']';
ALTER: [aA][lL][tT][eE][rR] | '[' [aA][lL][tT][eE][rR] ']';
AND: [aA][nN][dD] | '[' [aA][nN][dD] ']';
ANY: [aA][nN][yY] | '[' [aA][nN][yY] ']';
AS: [aA][sS] | '[' [aA][sS] ']';
ASC: [aA][sS][cC] | '[' [aA][sS][cC] ']';
AUTHORIZATION: [aA][uU][tT][hH][oO][rR][iI][zZ][aA][tT][iI][oO][nN] | '[' [aA][uU][tT][hH][oO][rR][iI][zZ][aA][tT][iI][oO][nN] ']';
BACKUP: [bB][aA][cC][kK][uU][pP] | '[' [bB][aA][cC][kK][uU][pP] ']';
BEGIN: [bB][eE][gG][iI][nN] | '[' [bB][eE][gG][iI][nN] ']';
BETWEEN: [bB][eE][tT][wW][eE][eE][nN] | '[' [bB][eE][tT][wW][eE][eE][nN] ']';
BREAK: [bB][rR][eE][aA][kK] | '[' [bB][rR][eE][aA][kK] ']';
BROWSE: [bB][rR][oO][wW][sS][eE] | '[' [bB][rR][oO][wW][sS][eE] ']';
BULK: [bB][uU][lL][kK] | '[' [bB][uU][lL][kK] ']';
BY: [bB][yY] | '[' [bB][yY] ']';
CASCADE: [cC][aA][sS][cC][aA][dD][eE] | '[' [cC][aA][sS][cC][aA][dD][eE] ']';
CASE: [cC][aA][sS][eE] | '[' [cC][aA][sS][eE] ']';
CHECK: [cC][hH][eE][cC][kK] | '[' [cC][hH][eE][cC][kK] ']';
CHECKPOINT: [cC][hH][eE][cC][kK][pP][oO][iI][nN][tT] | '[' [cC][hH][eE][cC][kK][pP][oO][iI][nN][tT] ']';
CLOSE: [cC][lL][oO][sS][eE] | '[' [cC][lL][oO][sS][eE] ']';
CLUSTERED: [cC][lL][uU][sS][tT][eE][rR][eE][dD] | '[' [cC][lL][uU][sS][tT][eE][rR][eE][dD] ']';
COALESCE: [cC][oO][aA][lL][eE][sS][cC][eE] ;
COLLATE: [cC][oO][lL][lL][aA][tT][eE] | '[' [cC][oO][lL][lL][aA][tT][eE] ']';
COLUMN: [cC][oO][lL][uU][mM][nN] | '[' [cC][oO][lL][uU][mM][nN] ']';
COMMIT: [cC][oO][mM][mM][iI][tT] | '[' [cC][oO][mM][mM][iI][tT] ']';
COMPUTE: [cC][oO][mM][pP][uU][tT][eE] | '[' [cC][oO][mM][pP][uU][tT][eE] ']';
CONSTRAINT: [cC][oO][nN][sS][tT][rR][aA][iI][nN][tT] | '[' [cC][oO][nN][sS][tT][rR][aA][iI][nN][tT] ']';
CONTAINS: [cC][oO][nN][tT][aA][iI][nN][sS] | '[' [cC][oO][nN][tT][aA][iI][nN][sS] ']';
CONTAINSTABLE: [cC][oO][nN][tT][aA][iI][nN][sS][tT][aA][bB][lL][eE] | '[' [cC][oO][nN][tT][aA][iI][nN][sS][tT][aA][bB][lL][eE] ']';
CONTINUE: [cC][oO][nN][tT][iI][nN][uU][eE] | '[' [cC][oO][nN][tT][iI][nN][uU][eE] ']';
CONVERT: [cC][oO][nN][vV][eE][rR][tT] ;
CAST: [cC][aA][sS][tT];
CREATE: [cC][rR][eE][aA][tT][eE] | '[' [cC][rR][eE][aA][tT][eE] ']';
CROSS: [cC][rR][oO][sS][sS] | '[' [cC][rR][oO][sS][sS] ']';
CURRENT: [cC][uU][rR][rR][eE][nN][tT] | '[' [cC][uU][rR][rR][eE][nN][tT] ']';
CURRENT_DATE: [cC][uU][rR][rR][eE][nN][tT] '_' [dD][aA][tT][eE] ;
CURRENT_TIME: [cC][uU][rR][rR][eE][nN][tT] '_' [tT][iI][mM][eE] ;
CURRENT_TIMESTAMP: [cC][uU][rR][rR][eE][nN][tT] '_' [tT][iI][mM][eE][sS][tT][aA][mM][pP] ;
CURRENT_USER: [cC][uU][rR][rR][eE][nN][tT] '_' [uU][sS][eE][rR] | '[' [cC][uU][rR][rR][eE][nN][tT] '_' [uU][sS][eE][rR] ']';
CURSOR: [cC][uU][rR][sS][oO][rR] | '[' [cC][uU][rR][sS][oO][rR] ']';
DATABASE: [dD][aA][tT][aA][bB][aA][sS][eE] | '[' [dD][aA][tT][aA][bB][aA][sS][eE] ']';
DBCC: [dD][bB][cC][cC] | '[' [dD][bB][cC][cC] ']';
DEALLOCATE: [dD][eE][aA][lL][lL][oO][cC][aA][tT][eE] | '[' [dD][eE][aA][lL][lL][oO][cC][aA][tT][eE] ']';
DECLARE: [dD][eE][cC][lL][aA][rR][eE] | '[' [dD][eE][cC][lL][aA][rR][eE] ']';
DEFAULT: [dD][eE][fF][aA][uU][lL][tT] | '[' [dD][eE][fF][aA][uU][lL][tT] ']';
DELETE: [dD][eE][lL][eE][tT][eE] | '[' [dD][eE][lL][eE][tT][eE] ']';
DENY: [dD][eE][nN][yY] | '[' [dD][eE][nN][yY] ']';
DESC: [dD][eE][sS][cC] | '[' [dD][eE][sS][cC] ']';
DISTINCT: [dD][iI][sS][tT][iI][nN][cC][tT] | '[' [dD][iI][sS][tT][iI][nN][cC][tT] ']';
DISTRIBUTED: [dD][iI][sS][tT][rR][iI][bB][uU][tT][eE][dD] | '[' [dD][iI][sS][tT][rR][iI][bB][uU][tT][eE][dD] ']';
DOUBLE: [dD][oO][uU][bB][lL][eE] | '[' [dD][oO][uU][bB][lL][eE] ']';
DROP: [dD][rR][oO][pP] | '[' [dD][rR][oO][pP] ']';
DUMP: [dD][uU][mM][pP] | '[' [dD][uU][mM][pP] ']';
ELSE: [eE][lL][sS][eE] | '[' [eE][lL][sS][eE] ']';
END: [eE][nN][dD] | '[' [eE][nN][dD] ']';
ERRLVL: [eE][rR][rR][lL][vV][lL] | '[' [eE][rR][rR][lL][vV][lL] ']';
ESCAPE: [eE][sS][cC][aA][pP][eE] | '[' [eE][sS][cC][aA][pP][eE] ']';
EXCEPT: [eE][xX][cC][eE][pP][tT] | '[' [eE][xX][cC][eE][pP][tT] ']';
EXEC: [eE][xX][eE][cC] | '[' [eE][xX][eE][cC] ']';
EXECUTE: [eE][xX][eE][cC][uU][tT][eE] | '[' [eE][xX][eE][cC][uU][tT][eE] ']';
EXISTS: [eE][xX][iI][sS][tT][sS] | '[' [eE][xX][iI][sS][tT][sS] ']';
EXIT: [eE][xX][iI][tT] | '[' [eE][xX][iI][tT] ']';
EXTERNAL: [eE][xX][tT][eE][rR][nN][aA][lL] | '[' [eE][xX][tT][eE][rR][nN][aA][lL] ']';
FETCH: [fF][eE][tT][cC][hH] | '[' [fF][eE][tT][cC][hH] ']';
FILE: [fF][iI][lL][eE] | '[' [fF][iI][lL][eE] ']';
FILLFACTOR: [fF][iI][lL][lL][fF][aA][cC][tT][oO][rR] | '[' [fF][iI][lL][lL][fF][aA][cC][tT][oO][rR] ']';
FOR: [fF][oO][rR] | '[' [fF][oO][rR] ']';
FOREIGN: [fF][oO][rR][eE][iI][gG][nN] | '[' [fF][oO][rR][eE][iI][gG][nN] ']';
FREETEXT: [fF][rR][eE][eE][tT][eE][xX][tT] | '[' [fF][rR][eE][eE][tT][eE][xX][tT] ']';
FREETEXTTABLE: [fF][rR][eE][eE][tT][eE][xX][tT][tT][aA][bB][lL][eE] | '[' [fF][rR][eE][eE][tT][eE][xX][tT][tT][aA][bB][lL][eE] ']';
FROM: [fF][rR][oO][mM] | '[' [fF][rR][oO][mM] ']';
FULL: [fF][uU][lL][lL] | '[' [fF][uU][lL][lL] ']';
FUNCTION: [fF][uU][nN][cC][tT][iI][oO][nN] | '[' [fF][uU][nN][cC][tT][iI][oO][nN] ']';
GOTO: [gG][oO][tT][oO] | '[' [gG][oO][tT][oO] ']';
GRANT: [gG][rR][aA][nN][tT] | '[' [gG][rR][aA][nN][tT] ']';
GROUP: [gG][rR][oO][uU][pP] | '[' [gG][rR][oO][uU][pP] ']';
HAVING: [hH][aA][vV][iI][nN][gG] | '[' [hH][aA][vV][iI][nN][gG] ']';
HOLDLOCK: [hH][oO][lL][dD][lL][oO][cC][kK] | '[' [hH][oO][lL][dD][lL][oO][cC][kK] ']';
IDENTITY: [iI][dD][eE][nN][tT][iI][tT][yY] | '[' [iI][dD][eE][nN][tT][iI][tT][yY] ']';
IDENTITY_INSERT: [iI][dD][eE][nN][tT][iI][tT][yY] '_' [iI][nN][sS][eE][rR][tT] | '[' [iI][dD][eE][nN][tT][iI][tT][yY] '_' [iI][nN][sS][eE][rR][tT] ']';
IDENTITYCOL: [iI][dD][eE][nN][tT][iI][tT][yY][cC][oO][lL] | '[' [iI][dD][eE][nN][tT][iI][tT][yY][cC][oO][lL] ']';
IF: [iI][fF] | '[' [iI][fF] ']';
IN: [iI][nN] | '[' [iI][nN] ']';
INDEX: [iI][nN][dD][eE][xX] | '[' [iI][nN][dD][eE][xX] ']';
INNER: [iI][nN][nN][eE][rR] | '[' [iI][nN][nN][eE][rR] ']';
INSERT: [iI][nN][sS][eE][rR][tT] | '[' [iI][nN][sS][eE][rR][tT] ']';
INTERSECT: [iI][nN][tT][eE][rR][sS][eE][cC][tT] | '[' [iI][nN][tT][eE][rR][sS][eE][cC][tT] ']';
INTO: [iI][nN][tT][oO] | '[' [iI][nN][tT][oO] ']';
IS: [iI][sS] | '[' [iI][sS] ']';
JOIN: [jJ][oO][iI][nN] | '[' [jJ][oO][iI][nN] ']';
KEY: [kK][eE][yY] | '[' [kK][eE][yY] ']';
KILL: [kK][iI][lL][lL] | '[' [kK][iI][lL][lL] ']';
LEFT: [lL][eE][fF][tT] | '[' [lL][eE][fF][tT] ']';
LIKE: [lL][iI][kK][eE] | '[' [lL][iI][kK][eE] ']';
LINENO: [lL][iI][nN][eE][nN][oO] | '[' [lL][iI][nN][eE][nN][oO] ']';
LOAD: [lL][oO][aA][dD] | '[' [lL][oO][aA][dD] ']';
MERGE: [mM][eE][rR][gG][eE] | '[' [mM][eE][rR][gG][eE] ']';
NATIONAL: [nN][aA][tT][iI][oO][nN][aA][lL] | '[' [nN][aA][tT][iI][oO][nN][aA][lL] ']';
NOCHECK: [nN][oO][cC][hH][eE][cC][kK] | '[' [nN][oO][cC][hH][eE][cC][kK] ']';
NONCLUSTERED: [nN][oO][nN][cC][lL][uU][sS][tT][eE][rR][eE][dD] | '[' [nN][oO][nN][cC][lL][uU][sS][tT][eE][rR][eE][dD] ']';
NOT: [nN][oO][tT] | '[' [nN][oO][tT] ']';
NULL: [nN][uU][lL][lL] | '[' [nN][uU][lL][lL] ']';
NULLIF: [nN][uU][lL][lL] '_' [iI][fF] ;
OF: [oO][fF] | '[' [oO][fF] ']';
OFF: [oO][fF][fF] | '[' [oO][fF][fF] ']';
OFFSETS: [oO][fF][fF][sS][eE][tT][sS] | '[' [oO][fF][fF][sS][eE][tT][sS] ']';
ON: [oO][nN] | '[' [oO][nN] ']';
OPEN: [oO][pP][eE][nN] | '[' [oO][pP][eE][nN] ']';
OPENDATASOURCE: [oO][pP][eE][nN][dD][aA][tT][aA][sS][oO][uU][rR][cC][eE] | '[' [oO][pP][eE][nN][dD][aA][tT][aA][sS][oO][uU][rR][cC][eE] ']';
OPENQUERY: [oO][pP][eE][nN][qQ][uU][eE][rR][yY] | '[' [oO][pP][eE][nN][qQ][uU][eE][rR][yY] ']';
OPENROWSET: [oO][pP][eE][nN][rR][oO][wW][sS][eE][tT] | '[' [oO][pP][eE][nN][rR][oO][wW][sS][eE][tT] ']';
OPENXML: [oO][pP][eE][nN][xX][mM][lL] | '[' [oO][pP][eE][nN][xX][mM][lL] ']';
OPTION: [oO][pP][tT][iI][oO][nN] | '[' [oO][pP][tT][iI][oO][nN] ']';
OR: [oO][rR] | '[' [oO][rR] ']';
ORDER: [oO][rR][dD][eE][rR] | '[' [oO][rR][dD][eE][rR] ']';
OUTER: [oO][uU][tT][eE][rR] | '[' [oO][uU][tT][eE][rR] ']';
OVER: [oO][vV][eE][rR] | '[' [oO][vV][eE][rR] ']';
PERCENT: [pP][eE][rR][cC][eE][nN][tT] | '[' [pP][eE][rR][cC][eE][nN][tT] ']';
PLAN: [pP][lL][aA][nN] | '[' [pP][lL][aA][nN] ']';
PRECISION: [pP][rR][eE][cC][iI][sS][iI][oO][nN] | '[' [pP][rR][eE][cC][iI][sS][iI][oO][nN] ']';
PRIMARY: [pP][rR][iI][mM][aA][rR][yY] | '[' [pP][rR][iI][mM][aA][rR][yY] ']';
PRINT: [pP][rR][iI][nN][tT] | '[' [pP][rR][iI][nN][tT] ']';
PROC: [pP][rR][oO][cC] | '[' [pP][rR][oO][cC] ']';
PROCEDURE: [pP][rR][oO][cC][eE][dD][uU][rR][eE] | '[' [pP][rR][oO][cC][eE][dD][uU][rR][eE] ']';
PUBLIC: [pP][uU][bB][lL][iI][cC] | '[' [pP][uU][bB][lL][iI][cC] ']';
RAISERROR: [rR][aA][iI][sS][eE][rR][rR][oO][rR] | '[' [rR][aA][iI][sS][eE][rR][rR][oO][rR] ']';
READ: [rR][eE][aA][dD] | '[' [rR][eE][aA][dD] ']';
READTEXT: [rR][eE][aA][dD][tT][eE][xX][tT] | '[' [rR][eE][aA][dD][tT][eE][xX][tT] ']';
RECONFIGURE: [rR][eE][cC][oO][nN][fF][iI][gG][uU][rR][eE] | '[' [rR][eE][cC][oO][nN][fF][iI][gG][uU][rR][eE] ']';
REFERENCES: [rR][eE][fF][eE][rR][eE][nN][cC][eE][sS] | '[' [rR][eE][fF][eE][rR][eE][nN][cC][eE][sS] ']';
REPLICATION: [rR][eE][pP][lL][iI][cC][aA][tT][iI][oO][nN] | '[' [rR][eE][pP][lL][iI][cC][aA][tT][iI][oO][nN] ']';
RESTORE: [rR][eE][sS][tT][oO][rR][eE] | '[' [rR][eE][sS][tT][oO][rR][eE] ']';
RESTRICT: [rR][eE][sS][tT][rR][iI][cC][tT] | '[' [rR][eE][sS][tT][rR][iI][cC][tT] ']';
RETURN: [rR][eE][tT][uU][rR][nN] | '[' [rR][eE][tT][uU][rR][nN] ']';
REVERT: [rR][eE][vV][eE][rR][tT] | '[' [rR][eE][vV][eE][rR][tT] ']';
REVOKE: [rR][eE][vV][oO][kK][eE] | '[' [rR][eE][vV][oO][kK][eE] ']';
RIGHT: [rR][iI][gG][hH][tT] | '[' [rR][iI][gG][hH][tT] ']';
ROLLBACK: [rR][oO][lL][lL][bB][aA][cC][kK] | '[' [rR][oO][lL][lL][bB][aA][cC][kK] ']';
ROWCOUNT: [rR][oO][wW][cC][oO][uU][nN][tT] | '[' [rR][oO][wW][cC][oO][uU][nN][tT] ']';
ROWGUIDCOL: [rR][oO][wW][gG][uU][iI][dD][cC][oO][lL] | '[' [rR][oO][wW][gG][uU][iI][dD][cC][oO][lL] ']';
RULE: [rR][uU][lL][eE] | '[' [rR][uU][lL][eE] ']';
SAVE: [sS][aA][vV][eE] | '[' [sS][aA][vV][eE] ']';
SAVEPOINT: [sS][aA][vV][eE] '_' [pP][oO][iI][nN][tT] | '[' [sS][aA][vV][eE] '_' [pP][oO][iI][nN][tT] ']';
SESSION_USER: [sS][eE][sS][sS][iI][oO][nN] '_' [uU][sS][eE][rR] | '[' [sS][eE][sS][sS][iI][oO][nN] '_' [uU][sS][eE][rR] ']';
SET: [sS][eE][tT] | '[' [sS][eE][tT] ']';
SETUSER: [sS][eE][tT][uU][sS][eE][rR] | '[' [sS][eE][tT][uU][sS][eE][rR] ']';
SHUTDOWN: [sS][hH][uU][tT][dD][oO][wW][nN] | '[' [sS][hH][uU][tT][dD][oO][wW][nN] ']';
SOME: [sS][oO][mM][eE] | '[' [sS][oO][mM][eE] ']';
STATISTICS: [sS][tT][aA][tT][iI][sS][tT][iI][cC][sS] | '[' [sS][tT][aA][tT][iI][sS][tT][iI][cC][sS] ']';
SYSTEM_USER: [sS][yY][sS][tT][eE][mM] '_' [uU][sS][eE][rR] | '[' [sS][yY][sS][tT][eE][mM] '_' [uU][sS][eE][rR] ']';
TABLE: [tT][aA][bB][lL][eE] | '[' [tT][aA][bB][lL][eE] ']';
TABLESAMPLE: [tT][aA][bB][lL][eE][sS][aA][mM][pP][lL][eE] | '[' [tT][aA][bB][lL][eE][sS][aA][mM][pP][lL][eE] ']';
TEXTSIZE: [tT][eE][xX][tT][sS][iI][zZ][eE] | '[' [tT][eE][xX][tT][sS][iI][zZ][eE] ']';
THEN: [tT][hH][eE][nN] | '[' [tT][hH][eE][nN] ']';
TO: [tT][oO] | '[' [tT][oO] ']';
TOP: [tT][oO][pP] | '[' [tT][oO][pP] ']';
TRAN: [tT][rR][aA][nN] | '[' [tT][rR][aA][nN] ']';
TRANSACTION: [tT][rR][aA][nN][sS][aA][cC][tT][iI][oO][nN] | '[' [tT][rR][aA][nN][sS][aA][cC][tT][iI][oO][nN] ']';
TRIGGER: [tT][rR][iI][gG][gG][eE][rR] | '[' [tT][rR][iI][gG][gG][eE][rR] ']';
TRUNCATE: [tT][rR][uU][nN][cC][aA][tT][eE] | '[' [tT][rR][uU][nN][cC][aA][tT][eE] ']';
TSEQUAL: [tT][sS][eE][qQ][uU][aA][lL] | '[' [tT][sS][eE][qQ][uU][aA][lL] ']';
UNION: [uU][nN][iI][oO][nN] | '[' [uU][nN][iI][oO][nN] ']';
UNIQUE: [uU][nN][iI][qQ][uU][eE] | '[' [uU][nN][iI][qQ][uU][eE] ']';
UNPIVOT: [uU][nN][pP][iI][vV][oO][tT] | '[' [uU][nN][pP][iI][vV][oO][tT] ']';
UPDATE: [uU][pP][dD][aA][tT][eE] | '[' [uU][pP][dD][aA][tT][eE] ']';
UPDATETEXT: [uU][pP][dD][aA][tT][eE][tT][eE][xX][tT] | '[' [uU][pP][dD][aA][tT][eE][tT][eE][xX][tT] ']';
USE: [uU][sS][eE] | '[' [uU][sS][eE] ']';
USER: [uU][sS][eE][rR] | '[' [uU][sS][eE][rR] ']';
VALUES: [vV][aA][lL][uU][eE][sS] | '[' [vV][aA][lL][uU][eE][sS] ']';
VARYING: [vV][aA][rR][yY][iI][nN][gG] | '[' [vV][aA][rR][yY][iI][nN][gG] ']';
VIEW: [vV][iI][eE][wW] | '[' [vV][iI][eE][wW] ']';
WAITFOR: [wW][aA][iI][tT][fF][oO][rR] | '[' [wW][aA][iI][tT][fF][oO][rR] ']';
WHEN: [wW][hH][eE][nN] | '[' [wW][hH][eE][nN] ']';
WHERE: [wW][hH][eE][rR][eE] | '[' [wW][hH][eE][rR][eE] ']';
WHILE: [wW][hH][iI][lL][eE] | '[' [wW][hH][iI][lL][eE] ']';
WITH: [wW][iI][tT][hH] | '[' [wW][iI][tT][hH] ']';
WRITETEXT: [wW][rR][iI][tT][eE][tT][eE][xX][tT] | '[' [wW][rR][iI][tT][eE][tT][eE][xX][tT] ']';
INT: [iI][nN][tT] | '[' [iI][nN][tT] ']';
BIGINT: [bB][iI][gG][iI][nN][tT] | '[' [bB][iI][gG][iI][nN][tT] ']';
SMALLINT: [sS][mM][aA][lL][lL][iI][nN][tT] | '[' [sS][mM][aA][lL][lL][iI][nN][tT] ']';
TINYINT: [tT][iI][nN][yY][iI][nN][tT] | '[' [tT][iI][nN][yY][iI][nN][tT] ']';
BIT: [bB][iI][tT] | '[' [bB][iI][tT] ']';
DECIMAL: [dD][eE][cC][iI][mM][aA][lL] | '[' [dD][eE][cC][iI][mM][aA][lL] ']';
NUMERIC: [nN][uU][mM][eE][rR][iI][cC] | '[' [nN][uU][mM][eE][rR][iI][cC] ']';
FLOAT: [fF][lL][oO][aA][tT] | '[' [fF][lL][oO][aA][tT] ']';
REAL: [rR][eE][aA][lL] | '[' [rR][eE][aA][lL] ']';
MONEY: [mM][oO][nN][eE][yY] | '[' [mM][oO][nN][eE][yY] ']';
SMALLMONEY: [sS][mM][aA][lL][lL][mM][oO][nN][eE][yY] | '[' [sS][mM][aA][lL][lL][mM][oO][nN][eE][yY] ']';
CHAR: [cC][hH][aA][rR] | '[' [cC][hH][aA][rR] ']';
NCHAR: [nN][cC][hH][aA][rR] | '[' [nN][cC][hH][aA][rR] ']';
VARCHAR: [vV][aA][rR][cC][hH][aA][rR] | '[' [vV][aA][rR][cC][hH][aA][rR] ']';
TEXT: [tT][eE][xX][tT] | '[' [tT][eE][xX][tT] ']';
NTEXT: [nN][tT][eE][xX][tT] | '[' [nN][tT][eE][xX][tT] ']';
DATE: [dD][aA][tT][eE] | '[' [dD][aA][tT][eE] ']';
DATETIME: [dD][aA][tT][eE][tT][iI][mM][eE] | '[' [dD][aA][tT][eE][tT][iI][mM][eE] ']';
TIME: [tT][iI][mM][eE] | '[' [tT][iI][mM][eE] ']';
TIMESTAMP: [tT][iI][mM][eE][sS][tT][aA][mM][pP] | '[' [tT][iI][mM][eE][sS][tT][aA][mM][pP] ']';
UNIQUEIDENTIFIER: [uU][nN][iI][qQ][uU][eE][iI][dD][eE][nN][tT][iI][fF][iI][eE][rR] | '[' [uU][nN][iI][qQ][uU][eE][iI][dD][eE][nN][tT][iI][fF][iI][eE][rR] ']';
SQL_VARIANT: [sS][qQ][lL] '_' [vV][aA][rR][iI][aA][nN][tT] | '[' [sS][qQ][lL] '_' [vV][aA][rR][iI][aA][nN][tT] ']';
XML: [xX][mM][lL] | '[' [xX][mM][lL] ']';
COUNT: [cC][oO][uU][nN][tT] ;
MAX: [mM][aA][xX] ;
MIN: [mM][iI][nN] ;
AVG: [aA][vV][gG] ;
SUM: [sS][uU][mM] ;
LEN: [lL][eE][nN] ;
UPPER: [uU][pP][pP][eE][rR] | '[' [uU][pP][pP][eE][rR] ']';
LOWER: [lL][oO][wW][eE][rR] | '[' [lL][oO][wW][eE][rR] ']';
GETDATE: [gG][eE][tT][dD][aA][tT][eE] ;
ISNULL: [iI][sS][nN][uU][lL][lL] ;
SUBSTRING: [sS][uU][bB][sS][tT][rR][iI][nN][gG] | '[' [sS][uU][bB][sS][tT][rR][iI][nN][gG] ']';
DATEADD: [dD][aA][tT][eE][aA][dD][dD] | '[' [dD][aA][tT][eE][aA][dD][dD] ']';
DATEDIFF: [dD][aA][tT][eE][dD][iI][fF][fF] | '[' [dD][aA][tT][eE][dD][iI][fF][fF] ']';
ROUND: [rR][oO][uU][nN][dD] | '[' [rR][oO][uU][nN][dD] ']';
CEILING: [cC][eE][iI][lL][iI][nN][gG] | '[' [cC][eE][iI][lL][iI][nN][gG] ']';
FLOOR: [fF][lL][oO][oO][rR] | '[' [fF][lL][oO][oO][rR] ']';
FALSE: [fF][aA][lL][sS][eE] | '[' [fF][aA][lL][sS][eE] ']';
ILIKE: [iI][lL][iI][kK][eE] | '[' [iI][lL][iI][kK][eE] ']';
LIMIT: [lL][iI][mM][iI][tT] | '[' [lL][iI][mM][iI][tT] ']';
NATURAL: [nN][aA][tT][uU][rR][aA][lL] | '[' [nN][aA][tT][uU][rR][aA][lL] ']';
PARTITION: [pP][aA][rR][tT][iI][tT][iI][oO][nN] | '[' [pP][aA][rR][tT][iI][tT][iI][oO][nN] ']';
OFFSET: [oO][fF][fF][sS][eE][tT] | '[' [oO][fF][fF][sS][eE][tT] ']';
RETURNING: [rR][eE][tT][uU][rR][nN][iI][nN][gG] | '[' [rR][eE][tT][uU][rR][nN][iI][nN][gG] ']';
SELECT: [sS][eE][lL][eE][cC][tT] | '[' [sS][eE][lL][eE][cC][tT] ']';
UNNEST: [uU][nN][nN][eE][sS][tT] | '[' [uU][nN][nN][eE][sS][tT] ']';
WINDOW: [wW][iI][nN][dD][oO][wW] | '[' [wW][iI][nN][dD][oO][wW] ']';
TEMP: [tT][eE][mM][pP] | '[' [tT][eE][mM][pP] ']';
TEMPORARY: [tT][eE][mM][pP][oO][rR][aA][rR][yY] | '[' [tT][eE][mM][pP][oO][rR][aA][rR][yY] ']';
LOOP: [lL][oO][oO][pP] | '[' [lL][oO][oO][pP] ']';
REPLACE: [rR][eE][pP][lL][aA][cC][eE] | '[' [rR][eE][pP][lL][aA][cC][eE] ']';
MATERIALIZED: [mM][aA][tT][eE][rR][iI][aA][lL][iI][zZ][eE][dD] | '[' [mM][aA][tT][eE][rR][iI][aA][lL][iI][zZ][eE][dD] ']';
FIRST: [fF][iI][rR][sS][tT] | '[' [fF][iI][rR][sS][tT] ']';
TRY: [tT][rR][yY] | '[' [tT][rR][yY] ']';
CATCH: [cC][aA][tT][cC][hH] | '[' [cC][aA][tT][cC][hH] ']';
GO: [gG][oO] | '[' [gG][oO] ']';
QUOTENAME: [qQ][uU][oO][tT][eE][nN][aA][mM][eE] | '[' [qQ][uU][oO][tT][eE][nN][aA][mM][eE] ']';
NVARCHAR: [nN][vV][aA][rR][cC][hH][aA][rR] | '[' [nN][vV][aA][rR][cC][hH][aA][rR] ']';
ERROR_MESSAGE: [eE][rR][rR][oO][rR] '_' [mM][eE][sS][sS][aA][gG][eE] | '[' [eE][rR][rR][oO][rR] '_' [mM][eE][sS][sS][aA][gG][eE] ']';
ERROR_SEVERITY: [eE][rR][rR][oO][rR] '_' [sS][eE][vV][eE][rR][iI][tT][yY] | '[' [eE][rR][rR][oO][rR] '_' [sS][eE][vV][eE][rR][iI][tT][yY] ']';
ERROR_STATE: [eE][rR][rR][oO][rR] '_' [sS][tT][aA][tT][eE] | '[' [eE][rR][rR][oO][rR] '_' [sS][tT][aA][tT][eE] ']';
SCHEMA_NAME: [sS][cC][hH][eE][mM][aA] '_' [nN][aA][mM][eE] | '[' [sS][cC][hH][eE][mM][aA] '_' [nN][aA][mM][eE] ']';
SCHEMA: [sS][cC][hH][eE][mM][aA] | '[' [sS][cC][hH][eE][mM][aA] ']';
OBJECT: [oO][bB][jJ][eE][cC][tT] | '[' [oO][bB][jJ][eE][cC][tT] ']';
TYPE: [tT][yY][pP][eE] | '[' [tT][yY][pP][eE] ']';
INFORMATION_SCHEMA: [iI][nN][fF][oO][rR][mM][aA][tT][iI][oO][nN] '_' [sS][cC][hH][eE][mM][aA] | '[' [iI][nN][fF][oO][rR][mM][aA][tT][iI][oO][nN] '_' [sS][cC][hH][eE][mM][aA] ']';
TABLES: [tT][aA][bB][lL][eE][sS] | '[' [tT][aA][bB][lL][eE][sS] ']';
BASE: [bB][aA][sS][eE] | '[' [bB][aA][sS][eE] ']';
COLUMNS: [cC][oO][lL][uU][mM][nN][sS] | '[' [cC][oO][lL][uU][mM][nN][sS] ']';
KEYS: [kK][eE][yY][sS] | '[' [kK][eE][yY][sS] ']';
PARENT: [pP][aA][rR][eE][nN][tT] | '[' [pP][aA][rR][eE][nN][tT] ']';
SEQUENCES: [sS][eE][qQ][uU][eE][nN][cC][eE][sS] | '[' [sS][eE][qQ][uU][eE][nN][cC][eE][sS] ']';
OUTPUT: [oO][uU][tT][pP][uU][tT] | '[' [oO][uU][tT][pP][uU][tT] ']';
OPENJSON: [oO][pP][eE][nN][jJ][sS][oO][nN] | '[' [oO][pP][eE][nN][jJ][sS][oO][nN] ']';
SP_EXECUTESQL: [sS][pP] '_' [eE][xX][eE][cC][uU][tT][eE][sS][qQ][lL] | '[' [sS][pP] '_' [eE][xX][eE][cC][uU][tT][eE][sS][qQ][lL] ']';
FOREIGN_KEYS: [fF][oO][rR][eE][iI][gG][nN] '_' [kK][eE][yY][sS] | '[' [fF][oO][rR][eE][iI][gG][nN] '_' [kK][eE][yY][sS] ']';
PARENT_OBJECT_ID: [pP][aA][rR][eE][nN][tT] '_' [oO][bB][jJ][eE][cC][tT] '_' [iI][dD] | '[' [pP][aA][rR][eE][nN][tT] '_' [oO][bB][jJ][eE][cC][tT] '_' [iI][dD] ']';
EXECPT: [eE][xX][eE][cC][pP][tT] | '[' [eE][xX][eE][cC][pP][tT] ']';
OBJECT_ID: [oO][bB][jJ][eE][cC][tT] '_' [iI][dD] | '[' [oO][bB][jJ][eE][cC][tT] '_' [iI][dD] ']';
OBJECT_NAME: [oO][bB][jJ][eE][cC][tT] '_' [nN][aA][mM][eE] | '[' [oO][bB][jJ][eE][cC][tT] '_' [nN][aA][mM][eE] ']';
OBJECT_SCHEMA_NAME: [oO][bB][jJ][eE][cC][tT] '_' [sS][cC][hH][eE][mM][aA] '_' [nN][aA][mM][eE] | '[' [oO][bB][jJ][eE][cC][tT] '_' [sS][cC][hH][eE][mM][aA] '_' [nN][aA][mM][eE] ']';
TABLE_SCHEMA: [tT][aA][bB][lL][eE] '_' [sS][cC][hH][eE][mM][aA] | '[' [tT][aA][bB][lL][eE] '_' [sS][cC][hH][eE][mM][aA] ']';
TABLE_NAME: [tT][aA][bB][lL][eE] '_' [nN][aA][mM][eE] | '[' [tT][aA][bB][lL][eE] '_' [nN][aA][mM][eE] ']';
TABLE_TYPE: [tT][aA][bB][lL][eE] '_' [tT][yY][pP][eE] | '[' [tT][aA][bB][lL][eE] '_' [tT][yY][pP][eE] ']';
VERSION: [vV][eE][rR][sS][iI][oO][nN] | '[' [vV][eE][rR][sS][iI][oO][nN] ']';
// Punctuation
DOT: '.';
COMMA: ',';
SEMI: ';';
LPAREN: '(';
RPAREN: ')';

// Common Rules
LINE_COMMENT: '--' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
WS: [ \t\r\n]+ -> skip;

STRING_SINGLE: [nN]? '\'' ( '\'\'' | ~['] )* '\'' | '0' [bB] [01]+ ;
STRING_DOUBLE: [nN]? '"' ( '""' | ~["] )* '"';

BRACKET_IDENTIFIER: '[' (~[\]]+)? ']';
VARIABLE: '@''@'? [a-zA-Z_] [a-zA-Z0-9_]* ;
IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;
NUMBER : [+-]? DIGITS ('.' DIGITS?)? EXP? | [+-]? '.' DIGITS EXP? |'0' [xX] [0-9a-fA-F]+ ; 
fragment DIGITS : [0-9]+ ; 
fragment EXP : [eE] [+-]? DIGITS ;

OPERATOR
    : '+'
    | '-'
    | '*'
    | '/'
    | '='
    | '<>'
    | '!='
    | '<='
    | '>='
    | '<'
    | '>'
    | '+='
    | '%'
    | '&'
    | '|'
    | '^'
    | '~'
    | '\\'
    | ':'
    | '?'
    ;
