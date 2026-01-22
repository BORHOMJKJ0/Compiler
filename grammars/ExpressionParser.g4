parser grammar ExpressionParser;
options { tokenVocab=BaseLexer; }

expression: primary (binaryOp primary)*;

primary
    : literal
    | functionCall
    | caseExpression
    | columnReference    
    | identifier
    | VARIABLE
    | LPAREN (selectStatement | expression | expressionList) RPAREN
    | OPERATOR primary 
    ;

binaryOp
    : OPERATOR
    | AND
    | OR
    | IN
    | IS
    | NOT
    | LIKE
    | BETWEEN
    ;
    
columnReference: identifier (DOT identifier)+;
expressionList: expression (COMMA expression)*;

literal
    : NUMBER
    | STRING_SINGLE
    | STRING_DOUBLE
    | NULL
    ;

identifier: IDENTIFIER | BRACKET_IDENTIFIER | STRING_DOUBLE | keywordAsIdentifier;

keywordAsIdentifier
    : ADD
    | ALL
    | ALTER
    | AND
    | ANY
    | AS
    | ASC
    | AUTHORIZATION
    | BACKUP
    | BEGIN
    | BETWEEN
    | BREAK
    | BULK
    | BY
    | CASCADE
    | CASE
    | CHECK
    | CHECKPOINT
    | CLOSE
    | CLUSTERED
    | COALESCE
    | COLLATE
    | COLUMN
    | COMMIT
    | COMPUTE
    | CONSTRAINT
    | CONTAINS
    | CONTINUE
    | CONVERT
    | CAST
    | CREATE
    | CROSS
    | CURRENT
    | CURRENT_DATE
    | CURRENT_TIME
    | CURRENT_TIMESTAMP
    | CURRENT_USER
    | CURSOR
    | DATABASE
    | DBCC
    | DEALLOCATE
    | DECLARE
    | DEFAULT
    | DELETE
    | DENY
    | DESC
    | DISTINCT
    | DISTRIBUTED
    | DOUBLE
    | DROP
    | DUMP
    | ELSE
    | END
    | ERRLVL
    | ESCAPE
    | EXCEPT
    | EXEC
    | EXECUTE
    | EXISTS
    | EXIT
    | EXTERNAL
    | FETCH
    | FILE
    | FILLFACTOR
    | FOR
    | FOREIGN
    | FREETEXT
    | FREETEXTTABLE
    | FROM
    | FULL
    | FUNCTION
    | GOTO
    | GRANT
    | GROUP
    | HAVING
    | HOLDLOCK
    | IDENTITY
    | IDENTITY_INSERT
    | IDENTITYCOL
    | IF
    | IN
    | INDEX
    | INNER
    | INSERT
    | INTERSECT
    | INTO
    | IS
    | JOIN
    | KEY
    | KILL
    | LEFT
    | LIKE
    | LINENO
    | LOAD
    | MERGE
    | NATIONAL
    | NOCHECK
    | NONCLUSTERED
    | NOT
    | NULL
    | NULLIF
    | OF
    | OFF
    | OFFSETS
    | ON
    | OPEN
    | OPENDATASOURCE
    | OPENQUERY
    | OPENROWSET
    | OPENXML
    | OPTION
    | OR
    | ORDER
    | OUTER
    | OVER
    | PERCENT
    | PLAN
    | PRECISION
    | PRIMARY
    | PRINT
    | PROC
    | PROCEDURE
    | PUBLIC
    | RAISERROR
    | READ
    | READTEXT
    | RECONFIGURE
    | REFERENCES
    | REPLICATION
    | RESTORE
    | RESTRICT
    | RETURN
    | REVERT
    | REVOKE
    | RIGHT
    | ROLLBACK
    | ROWCOUNT
    | ROWGUIDCOL
    | RULE
    | SAVE
    | SAVEPOINT
    | SCHEMA
    | SCHEMA_NAME
    | SESSION_USER
    | SET
    | SETUSER
    | SHUTDOWN
    | SOME
    | STATISTICS
    | SYSTEM_USER
    | TABLE
    | TABLESAMPLE
    | TEXTSIZE
    | THEN
    | TO
    | TOP
    | TRAN
    | TRANSACTION
    | TRIGGER
    | TRUNCATE
    | TSEQUAL
    | UNION
    | UNIQUE
    | UNPIVOT
    | UPDATE
    | UPDATETEXT
    | USE
    | USER
    | VALUES
    | VARYING
    | VIEW
    | WAITFOR
    | WHEN
    | WHERE
    | WHILE
    | WITH
    | WRITETEXT
    | INT
    | BIGINT
    | SMALLINT
    | TINYINT
    | BIT
    | DECIMAL
    | NUMERIC
    | FLOAT
    | REAL
    | MONEY
    | SMALLMONEY
    | CHAR
    | NCHAR
    | VARCHAR
    | NVARCHAR
    | TEXT
    | NTEXT
    | DATE
    | DATETIME
    | TIME
    | TIMESTAMP
    | UNIQUEIDENTIFIER
    | SQL_VARIANT
    | XML
    | COUNT
    | MAX
    | MIN
    | AVG
    | SUM
    | LEN
    | UPPER
    | LOWER
    | GETDATE
    | ISNULL
    | SUBSTRING
    | DATEADD
    | DATEDIFF
    | ROUND
    | CEILING
    | FLOOR
    | FALSE
    | FETCH
    | ILIKE
    | LIMIT
    | NATURAL
    | PARTITION
    | OFFSET
    | RETURNING
    | SELECT
    | UNNEST
    | WINDOW
    | TEMP
    | TEMPORARY
    | LOOP
    | REPLACE
    | MATERIALIZED
    | FIRST
    | TRY
    | CATCH
    | GO
    | QUOTENAME
    | ERROR_MESSAGE
    | ERROR_SEVERITY
    | ERROR_STATE
    | OBJECT
    | TYPE
    | INFORMATION_SCHEMA
    | TABLES
    | BASE
    | COLUMNS
    | KEYS
    | PARENT
    | SEQUENCES
    | OUTPUT
    | OPENJSON
    | SP_EXECUTESQL
    | FOREIGN_KEYS
    | PARENT_OBJECT_ID
    | EXECPT
    | OBJECT_ID
    | OBJECT_NAME
    | OBJECT_SCHEMA_NAME
    | TABLE_SCHEMA
    | TABLE_NAME
    | TABLE_TYPE
    | VERSION
    ;

functionCall: (MAX | AVG | identifier) LPAREN expressionList? RPAREN;

caseExpression: CASE whenClause+ elseClause? END;
whenClause: WHEN condition THEN expression;
elseClause: ELSE expression;

condition: expression;

tableName: identifier (DOT identifier)*;
columnName: identifier;

selectStatement: ;
