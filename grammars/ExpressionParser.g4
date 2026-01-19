parser grammar ExpressionParser;
options { tokenVocab=BaseLexer; }

expression: primary (binaryOp primary)*;

primary
    : literal
    | functionCall
    | caseExpression
    | identifier
    | VARIABLE
    | LPAREN (selectStatement | expression | expressionList) RPAREN
    | OPERATOR primary // For unary minus/plus
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

expressionList: expression (COMMA expression)*;

literal
    : NUMBER
    | STRING_SINGLE
    | STRING_DOUBLE
    | NULL
    ;

identifier: IDENTIFIER | BRACKET_IDENTIFIER | keywordAsIdentifier;

keywordAsIdentifier: SELECT | FROM | WHERE | INSERT | INTO | UPDATE | DELETE | CREATE | ALTER | TABLE | DROP | ADD | VALUES | SET | JOIN | INNER | LEFT | RIGHT | FULL | OUTER | ON | AND | OR | NOT | EXISTS | IF | TRY | CATCH | DECLARE | EXEC | GO | NULL | IN | IS | LIKE | BETWEEN | ORDER | BY | GROUP | HAVING | ASC | DESC | AS | INT | NVARCHAR | BIGINT | DATE | MAX | AVG | TRUNCATE | PRIMARY | KEY | CONSTRAINT | COLUMN | CLUSTERED | NONCLUSTERED;

functionCall: (MAX | AVG | identifier) LPAREN expressionList? RPAREN;

caseExpression: CASE whenClause+ elseClause? END;
whenClause: WHEN condition THEN expression;
elseClause: ELSE expression;

condition: expression;

tableName: identifier (DOT identifier)*;
columnName: identifier;

// تعريف selectStatement هنا كقاعدة فارغة سيتم استيرادها أو تجاوزها
selectStatement: ;
