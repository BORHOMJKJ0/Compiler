parser grammar StatementParser;
options { tokenVocab=BaseLexer; }
import ExpressionParser;

sqlScript: batch*;
batch: (statement | GO)+;

statement
    : ddlStatement
    | dmlStatement
    | controlFlowStatement
    | variableStatement
    | execStatement
    | truncateStatement
    | blockStatement
    | cursorStatement
    | useStatement
    | SEMI
    ;

ddlStatement: createTableStatement | alterTableStatement | dropStatement;

createTableStatement
    : CREATE TABLE tableName LPAREN columnDefinitionList RPAREN
    ;

columnDefinitionList: columnDefinition (COMMA columnDefinition)*;

columnDefinition: columnName dataType constraint*;

dataType: (INT | NVARCHAR | BIGINT | DATE | DATETIME | VARCHAR | NCHAR | CHAR | BIT | DECIMAL | FLOAT | REAL | MONEY | SMALLMONEY | TEXT | NTEXT | TIME | TIMESTAMP | UNIQUEIDENTIFIER | SQL_VARIANT | XML | SMALLINT | TINYINT | NUMERIC | identifier) typeSize?;

typeSize: LPAREN (NUMBER | identifier) (COMMA NUMBER)* RPAREN ;

constraint: (NOT NULL | NULL | PRIMARY KEY (CLUSTERED | NONCLUSTERED)? (LPAREN columnList RPAREN)?  | DEFAULT expression| UNIQUE | FOREIGN KEY | CHECK | identifier)+;

alterTableStatement
    : ALTER TABLE tableName (addColumnClause | dropConstraintClause)
    ;

addColumnClause: ADD columnDefinition;

dropConstraintClause: DROP (CONSTRAINT | COLUMN) identifier;

dropStatement
    : DROP TABLE (IF EXISTS)? tableName
    | DROP CONSTRAINT (IF EXISTS)? identifier
    | DROP INDEX (IF EXISTS)? identifier (ON tableName)?
    | DROP VIEW (IF EXISTS)? identifier
    | DROP PROCEDURE (IF EXISTS)? identifier
    ;

truncateStatement: TRUNCATE TABLE tableName;

useStatement: USE identifier;

dmlStatement: cteStatement | selectStatement | insertStatement | updateStatement | deleteStatement;

cteStatement
    : WITH cteList selectStatement
    | WITH cteList insertStatement
    | WITH cteList updateStatement
    | WITH cteList deleteStatement
    ;

cteList: cteDefinition (COMMA cteDefinition)*;

cteDefinition: identifier (LPAREN columnList RPAREN)? AS LPAREN selectStatement RPAREN;

selectStatement
    : SELECT selectList (FROM tableList)? (WHERE condition)? (GROUP BY expressionList)? (HAVING condition)? (ORDER BY orderByList)?
    ;

orderByList: orderByItem (COMMA orderByItem)*;

orderByItem: expression (ASC | DESC)?;

selectList: selectItem (COMMA selectItem)*;

selectItem: (OPERATOR | expression) (AS? (columnName | literal | identifier))?;

tableList: tableRef (joinClause)*;

joinClause: joinType? JOIN tableRef ON condition;

joinType: INNER | LEFT OUTER? | RIGHT OUTER? | FULL OUTER?;

tableRef
    : tableName (AS? identifier)?
    | LPAREN selectStatement RPAREN (AS? identifier)
    ;

insertStatement
    : INSERT INTO? tableName ( LPAREN columnList RPAREN )? (insertValues | selectStatement)
    ;

columnList: columnName (COMMA columnName)*;

insertValues: VALUES (LPAREN expressionList RPAREN) (COMMA LPAREN expressionList RPAREN)*;

updateStatement
    : UPDATE tableName SET assignments (WHERE condition)?
    ;

assignments: assignment (COMMA assignment)*;

assignment: columnName OPERATOR expression;

deleteStatement: DELETE FROM? tableName (WHERE condition)?;

controlFlowStatement: ifStatement | tryCatchStatement | blockStatement;

ifStatement: IF (NOT EXISTS LPAREN selectStatement RPAREN | condition)? thenBlock (ELSE elseBlock)?;

thenBlock: blockStatement | statement;

elseBlock: blockStatement | statement;

blockStatement: BEGIN (statement | GO)* END;

tryCatchStatement
    : BEGIN TRY statement* END TRY
      BEGIN CATCH statement* END CATCH
    ;

variableStatement: declareStatement | setStatement;

declareStatement: DECLARE VARIABLE dataType (OPERATOR expression)?;

setStatement: SET (VARIABLE | columnName) OPERATOR expression;

execStatement: EXEC (identifier | SP_EXECUTESQL) expressionList?;

cursorStatement
    : declareCursorStatement
    | openCursorStatement
    | fetchCursorStatement
    | closeCursorStatement
    | deallocateCursorStatement
    ;

declareCursorStatement
    : DECLARE identifier CURSOR (cursorOptions)* FOR selectStatement
    ;

cursorOptions
    : LOCAL
    | GLOBAL
    | FORWARD_ONLY
    | SCROLL
    | STATIC
    | KEYSET
    | DYNAMIC
    | FAST_FORWARD
    | READ_ONLY
    | SCROLL_LOCKS
    | OPTIMISTIC
    ;

openCursorStatement: OPEN identifier;

fetchCursorStatement
    : FETCH (NEXT | PRIOR | FIRST | LAST | ABSOLUTE expression | RELATIVE expression)? 
      FROM identifier (INTO variableList)?
    ;

variableList: VARIABLE (COMMA VARIABLE)*;

closeCursorStatement: CLOSE identifier;

deallocateCursorStatement: DEALLOCATE identifier;