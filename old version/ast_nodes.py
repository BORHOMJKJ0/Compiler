
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ASTNode:
    pass


@dataclass
class StatementNode(ASTNode):
    pass


@dataclass
class GoStatementNode(StatementNode):
    keywordGo: str


@dataclass
class TableNameNode(ASTNode):
    name: str
    schema: Optional[str] = None


@dataclass
class ColumnDefinitionNode(ASTNode):
    column_name: str
    data_type: str
    constraints: Optional[List['columnConstraintsNode']] = None

@dataclass
class DeleteStatementNode(StatementNode):
    keywordDelete: str
    tableName: Optional['TableNameNode']=None
    fromClause: Optional['FromClauseNode']=None
    whereClause:Optional['WhenClauseNode']=None

@dataclass
class columnConstraintsNode(ASTNode):
    keyword1: str
    keyword2: Optional[str]


@dataclass
class CreateTableStatementNode(StatementNode):
    table_name: 'TableNameNode'  # Use the node, not just str
    columns: List['ColumnDefinitionNode']
    keywordCreate: str
    keywordTable: str


@dataclass
class AlterTableStatementNode(StatementNode):
    keywordAlter: str
    keywordTable: str
    table_name: 'TableNameNode'
    addColumnClause: Optional['AddColumnClauseNode'] = None
    dropConstraintClause: Optional['DropConstraintClauseNode'] = None


@dataclass
class AddColumnClauseNode(ASTNode):
    keywordAdd: str
    columnDefinition: 'ColumnDefinitionNode'


@dataclass
class DropConstraintClauseNode(ASTNode):
    keywordDrop: str
    keywordConstrain: str
    constraintName: str


@dataclass
class UpdateStatementNode(StatementNode):
    keywordUpdate: str
    tableName: 'TableNameNode'
    assignmentList: List['AssignmentNode']
    whereClause: Optional['WhereClauseNode'] = None


@dataclass
class AssignmentNode(ASTNode):
    columnName: str
    expression: 'ExpressionNode'


@dataclass
class WhereClauseNode(ASTNode):
    keywordWhere: str
    condition: 'ConditionNode'


@dataclass
class SelectStatementNode(StatementNode):
    keywordSelect: str
    selectList: List['SelectItemNode']
    orderByClause:Optional['OrderByClauseNode']=None
    whereClause: Optional['WhereClauseNode'] = None
    fromClause: Optional['FromClauseNode'] = None

@dataclass
class OrderByClauseNode(ASTNode):
    keywordOrder: Optional[str] = None
    keywordBy: Optional[str] = None
    orderByitem: List['OrderByItemNode']=None
    keywordAscDesc: Optional[str] = None
    
@dataclass
class OrderByItemNode(ASTNode):
    expression:Optional['ExpressionNode']=None
    identifier:Optional['str']=None
    
@dataclass
class SelectItemNode(ASTNode):
    expression: Optional['ExpressionNode']
    keywordAs: Optional['str'] = None
    identifier: Optional['str'] = None


@dataclass
class FromClauseNode(ASTNode):
    keywordFrom: str
    tableSource: List['TableSourceNode']


@dataclass
class TableSourceNode(ASTNode):
    tableName: 'TableNameNode'
    keyword: Optional['str'] = None
    identifier: Optional['str'] = None


@dataclass
class IfStatementNode(StatementNode):
    keywordIf: str
    selectStatement: 'SelectStatementNode'
    blockStatement: 'BlockStatementNode'
    keywordNot: Optional[str]=None
    keywordEXISTS: Optional[str]=None
    


@dataclass
class BlockStatementNode(StatementNode):
    keywordBegin: str
    statementList: List['StatementNode']
    keywordEnd: str


@dataclass
class tryCatchStatementNode(StatementNode):
    keywordBeginForTry: str
    keywordBeginTry: str
    tryStatementList: List['StatementNode']
    keywordEndForTry: str
    keywordEndTry: str
    keywordBeginForCatch: str
    keywordBeginCatch: str
    catchStatementList: List['StatementNode']
    keywordEndForCatch: str
    keywordEndCatch: str


@dataclass
class declareStatementNode(StatementNode):
    keywordDeclare: str
    variableName: str
    dataType: str
    operator: Optional[str] = None
    expression: Optional['ExpressionNode'] = None


@dataclass
class setStatementNode(StatementNode):
    keywordSet: str
    variableName: str
    operator: str
    expression: 'ExpressionNode'


@dataclass
class execStatementNode(StatementNode):
    keywordExec: str
    identifier: str
    expressionList: Optional[List['ExpressionNode']] = None


@dataclass
class ExpressionNode(ASTNode):
    pass


@dataclass
class CaseExpressionNode(ExpressionNode):
    keywordCase: str
    whenClauseList: List['WhenClauseNode']
    elseClause: Optional['ElseClauseNode']
    keywordEnd: str


@dataclass
class WhenClauseNode(ASTNode):
    keywordWhen: str
    condition: 'ConditionNode'
    keyword: str
    expression: 'ExpressionNode'


@dataclass
class ElseClauseNode(ASTNode):
    keywordElse: str
    expression: 'ExpressionNode'


@dataclass
class ConditionNode(ASTNode):
    pass


@dataclass
class BinaryConditionNode(ConditionNode):
    left: 'ExpressionNode'
    operator: str
    right: 'ExpressionNode'


@dataclass
class InConditionNode(ConditionNode):
    left: 'ExpressionNode'
    keywordIn: str
    expressionList: List['ExpressionNode']
    keywordNot: Optional[str] = None


@dataclass
class IsNotConditionNode(ConditionNode):
    left: 'ExpressionNode'
    keywordIs: str
    keywordNot: str  # might need one more key word


@dataclass
class ParenthesizedConditionNode(ConditionNode):
    condition: 'ConditionNode'


@dataclass
class LogicalConditionNode(ConditionNode):
    left: 'ConditionNode'
    operator: str
    right: 'ConditionNode'


@dataclass
class LiteralExpressionNode(ExpressionNode):
    value: str
    literal_type: str  # "NUMBER", "STRING_SINGLE", "STRING_DOUBLE", "KEYWORD"


@dataclass
class ColumnReferenceExpressionNode(ExpressionNode):
    column_name: str
    table_name: Optional['TableNameNode'] = None


@dataclass
class FunctionCallExpressionNode(ExpressionNode):
    function_name: str
    arguments: Optional[List['ExpressionNode']] = None


@dataclass
class VariableExpressionNode(ExpressionNode):
    variable_name: str


@dataclass
class BinaryExpressionNode(ExpressionNode):
    left: 'ExpressionNode'
    operator: str
    right: 'ExpressionNode'


@dataclass
class ParenthesizedExpressionNode(ExpressionNode):
    expression: 'ExpressionNode'
