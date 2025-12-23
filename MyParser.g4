parser grammar MyParser;

options {
    tokenVocab=MyLexer;
    language=Python3;
}

sqlScript
    : statementList EOF
    ;

statementList
    : (statement PUNCTUATION?)*
    ;

statement
    : createTableStatement
    | alterTableStatement
    | updateStatement
    | selectStatement
    | declareStatement
    | setStatement
    | execStatement
    | ifStatement
    | tryCatchStatement
    | goStatement
    | blockStatement
    | PUNCTUATION
    ;

goStatement
    : KEYWORD
    ;

createTableStatement
    : KEYWORD KEYWORD tableName PUNCTUATION columnDefinitionList PUNCTUATION
    ;

tableName
    : (IDENTIFIER PUNCTUATION)? IDENTIFIER
    | BRACKET_IDENTIFIER
    | IDENTIFIER
    ;

columnDefinitionList
    : columnDefinition (PUNCTUATION columnDefinition)*
    ;

columnDefinition
    : columnName dataType columnConstraint*
    ;

columnName
    : IDENTIFIER
    | BRACKET_IDENTIFIER
    ;

dataType
    : KEYWORD (PUNCTUATION NUMBER PUNCTUATION)?
    | IDENTIFIER (PUNCTUATION NUMBER PUNCTUATION)?
    ;

columnConstraint
    : KEYWORD KEYWORD?
    ;

alterTableStatement
    : KEYWORD KEYWORD tableName
      (addColumnClause | dropConstraintClause)
    ;

addColumnClause
    : KEYWORD columnDefinition
    ;

dropConstraintClause
    : KEYWORD KEYWORD constraintName
    ;

constraintName
    : IDENTIFIER
    | BRACKET_IDENTIFIER
    ;

updateStatement
    : KEYWORD tableName
      KEYWORD assignmentList
      (whereClause)?
    ;

assignmentList
    : assignment (PUNCTUATION assignment)*
    ;

assignment
    : columnName OPERATOR expression
    ;

whereClause
    : KEYWORD condition
    ;

selectStatement
    : KEYWORD selectList
      fromClause?
      whereClause?
      (KEYWORD KEYWORD)?
    ;

selectList
    : selectItem (PUNCTUATION selectItem)*
    ;

selectItem
    : expression (KEYWORD? IDENTIFIER)?
    | OPERATOR
    ;

fromClause
    : KEYWORD tableSource (PUNCTUATION tableSource)*
    ;

tableSource
    : tableName (KEYWORD? IDENTIFIER)?
    ;

ifStatement
    : KEYWORD KEYWORD KEYWORD PUNCTUATION
      selectStatement
      PUNCTUATION
      blockStatement
    ;

blockStatement
    : KEYWORD
      statementList
      KEYWORD
    ;

tryCatchStatement
    : KEYWORD KEYWORD
      statementList
      KEYWORD KEYWORD
      KEYWORD KEYWORD
      statementList
      KEYWORD KEYWORD
    ;

declareStatement
    : KEYWORD VARIABLE dataType (OPERATOR expression)?
    ;

setStatement
    : KEYWORD VARIABLE OPERATOR expression
    ;

execStatement
    : KEYWORD (IDENTIFIER | KEYWORD) expressionList?
    ;

expression
    : literal
    | columnReference
    | functionCall
    | caseExpression
    | PUNCTUATION expression PUNCTUATION
    | expression OPERATOR expression
    | expression KEYWORD expression
    | VARIABLE
    | STRING_SINGLE
    | STRING_DOUBLE
    ;

expressionList
    : expression (PUNCTUATION expression)*
    ;

caseExpression
    : KEYWORD whenClause+ elseClause? KEYWORD
    ;

whenClause
    : KEYWORD condition KEYWORD expression
    ;

elseClause
    : KEYWORD expression
    ;

condition
    : expression (OPERATOR | KEYWORD) expression
    | expression KEYWORD PUNCTUATION expressionList PUNCTUATION
    | expression KEYWORD KEYWORD
    | PUNCTUATION condition PUNCTUATION
    | condition KEYWORD condition
    ;

columnReference
    : (tableName PUNCTUATION)? columnName
    | IDENTIFIER
    | BRACKET_IDENTIFIER
    ;

functionCall
    : IDENTIFIER PUNCTUATION expressionList? PUNCTUATION
    | KEYWORD PUNCTUATION expressionList? PUNCTUATION
    ;

literal
    : NUMBER
    | STRING_SINGLE
    | STRING_DOUBLE
    | KEYWORD
    ;