parser grammar StatementParser;
options { tokenVocab=BaseLexer; }
import ExpressionParser;

// القاعدة الأساسية للبرنامج
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
    | SEMI
    ;

// DDL
ddlStatement: createTableStatement | alterTableStatement;

createTableStatement
    : CREATE TABLE tableName LPAREN columnDefinitionList RPAREN
    ;

columnDefinitionList: columnDefinition (COMMA columnDefinition)*;

columnDefinition: columnName dataType constraint*;

dataType: (INT | NVARCHAR | BIGINT | DATE | identifier) typeSize?;

typeSize: LPAREN (NUMBER | identifier) (COMMA NUMBER)* RPAREN;

constraint: (NOT NULL | NULL | PRIMARY KEY (CLUSTERED | NONCLUSTERED)? (LPAREN columnList RPAREN)? | identifier)+;

alterTableStatement
    : ALTER TABLE tableName (addColumnClause | dropConstraintClause)
    ;

addColumnClause: ADD columnDefinition;

dropConstraintClause: DROP (CONSTRAINT | COLUMN) identifier;

truncateStatement: TRUNCATE TABLE tableName;

// DML
dmlStatement: selectStatement | insertStatement | updateStatement | deleteStatement;

// تجاوز قاعدة selectStatement الفارغة من ExpressionParser
selectStatement
    : SELECT selectList (FROM tableList)? (WHERE condition)? (GROUP BY expressionList)? (HAVING condition)? (ORDER BY orderByList)?
    ;

orderByList: orderByItem (COMMA orderByItem)*;

orderByItem: expression (ASC | DESC)?;

selectList: selectItem (COMMA selectItem)*;

selectItem: (OPERATOR | expression) (AS? (columnName | literal))?;

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

// Control Flow
controlFlowStatement: ifStatement | tryCatchStatement | blockStatement;

ifStatement: IF (NOT EXISTS LPAREN selectStatement RPAREN | condition)? thenBlock (ELSE elseBlock)?;

thenBlock: blockStatement | statement;

elseBlock: blockStatement | statement;

blockStatement: BEGIN (statement | GO)* END;

tryCatchStatement
    : BEGIN TRY statement* END TRY
      BEGIN CATCH statement* END CATCH
    ;

// Variables
variableStatement: declareStatement | setStatement;

declareStatement: DECLARE VARIABLE dataType (OPERATOR expression)?;

setStatement: SET (VARIABLE | columnName) OPERATOR expression;

// EXEC
execStatement: EXEC (identifier | SP_EXECUTESQL) expressionList?;
