from dataclasses import dataclass
from typing import List, Optional
from .base_nodes import ASTNode, StatementNode


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
class columnConstraintsNode(ASTNode):
    keyword1: str
    keyword2: Optional[str] = None


@dataclass
class GoStatementNode(StatementNode):
    keywordGo: str


@dataclass
class CreateTableStatementNode(StatementNode):
    table_name: TableNameNode
    columns: List[ColumnDefinitionNode]
    keywordCreate: str
    keywordTable: str


@dataclass
class AlterTableStatementNode(StatementNode):
    keywordAlter: str
    keywordTable: str
    table_name: TableNameNode
    addColumnClause: Optional['AddColumnClauseNode'] = None
    dropConstraintClause: Optional['DropConstraintClauseNode'] = None


@dataclass
class AddColumnClauseNode(ASTNode):
    keywordAdd: str
    columnDefinition: ColumnDefinitionNode


@dataclass
class DropConstraintClauseNode(ASTNode):
    keywordDrop: str
    keywordConstrain: str
    constraintName: str


@dataclass
class UpdateStatementNode(StatementNode):
    keywordUpdate: str
    tableName: TableNameNode
    assignmentList: List['AssignmentNode']
    whereClause: Optional['WhereClauseNode'] = None


@dataclass
class AssignmentNode(ASTNode):
    from .expression_nodes import ExpressionNode
    columnName: str
    expression: 'ExpressionNode'


@dataclass
class WhereClauseNode(ASTNode):
    from .condition_nodes import ConditionNode
    keywordWhere: str
    condition: 'ConditionNode'


@dataclass
class DeleteStatementNode(StatementNode):
    keywordDelete: str
    tableName: Optional[TableNameNode] = None
    fromClause: Optional['FromClauseNode'] = None
    whereClause: Optional[WhereClauseNode] = None


@dataclass
class InsertStatement(StatementNode):
    keywordInsert: str
    tableName: TableNameNode
    keywordInto: Optional[str] = None
    insertColumns: Optional['InsertColumnsNode'] = None
    insertValues: Optional['InsertValuesNode'] = None
    selectStatement: Optional['SelectStatementNode'] = None
    execStatement: Optional['execStatementNode'] = None


@dataclass
class InsertColumnsNode(ASTNode):
    identifier: List[str]


@dataclass
class SelectItemNode(ASTNode):
    from .expression_nodes import ExpressionNode
    expression: Optional['ExpressionNode']
    keywordAs: Optional[str] = None
    identifier: Optional[str] = None


@dataclass
class OrderByClauseNode(ASTNode):
    keywordOrder: Optional[str] = None
    keywordBy: Optional[str] = None
    orderByitem: List['OrderByItemNode'] = None
    keywordAscDesc: Optional[str] = None


@dataclass
class FromClauseNode(ASTNode):
    keywordFrom: str
    tableSource: List['TableSourceNode']


@dataclass
class BlockStatementNode(StatementNode):
    keywordBegin: str
    statementList: List[StatementNode]
    keywordEnd: str


@dataclass
class tryCatchStatementNode(StatementNode):
    keywordBeginForTry: str
    keywordBeginTry: str
    tryStatementList: List[StatementNode]
    keywordEndForTry: str
    keywordEndTry: str
    keywordBeginForCatch: str
    keywordBeginCatch: str
    catchStatementList: List[StatementNode]
    keywordEndForCatch: str
    keywordEndCatch: str


@dataclass
class declareStatementNode(StatementNode):
    from .expression_nodes import ExpressionNode
    keywordDeclare: str
    variableName: str
    dataType: str
    operator: Optional[str] = None
    expression: Optional['ExpressionNode'] = None


@dataclass
class setStatementNode(StatementNode):
    from .expression_nodes import ExpressionNode
    keywordSet: str
    variableName: str
    operator: str
    expression: 'ExpressionNode'


@dataclass
class execStatementNode(StatementNode):
    from .expression_nodes import ExpressionNode
    keywordExec: str
    identifier: str
    expressionList: Optional[List['ExpressionNode']] = None


@dataclass
class TruncateStatementNode(StatementNode):
    keywordTruncate: str
    keywordTable: str
    tableName: 'TableNameNode'


@dataclass
class GroupByClauseNode(ASTNode):
    from .expression_nodes import ExpressionNode
    keywordGroup: str
    keywordBy: str
    expressions: List['ExpressionNode']


@dataclass
class HavingClauseNode(ASTNode):
    from .condition_nodes import ConditionNode
    keywordHaving: str
    condition: 'ConditionNode'


@dataclass
class SelectStatementNode(StatementNode):
    keywordSelect: str
    selectList: List['SelectItemNode']
    orderByClause: Optional['OrderByClauseNode'] = None
    whereClause: Optional['WhereClauseNode'] = None
    fromClause: Optional['FromClauseNode'] = None
    groupByClause: Optional['GroupByClauseNode'] = None
    havingClause: Optional['HavingClauseNode'] = None


@dataclass
class OrderByItemNode(ASTNode):
    from .expression_nodes import ExpressionNode
    expression: Optional['ExpressionNode'] = None
    identifier: Optional[str] = None
    ascDesc: Optional[str] = None


@dataclass
class TableSourceNode(ASTNode):
    from .condition_nodes import ConditionNode
    tableName: 'TableNameNode'
    keyword: Optional[str] = None
    identifier: Optional[str] = None
    joinCondition: Optional['ConditionNode'] = None


@dataclass
class InsertValuesNode(ASTNode):
    from .expression_nodes import ExpressionNode
    keywordValues: str
    valueSets: List[List['ExpressionNode']]


@dataclass
class IfStatementNode(StatementNode):
    from .condition_nodes import ConditionNode
    keywordIf: str
    selectStatement: Optional['SelectStatementNode'] = None
    condition: Optional['ConditionNode'] = None
    blockStatement: Optional['BlockStatementNode'] = None
    elseStatement: Optional['BlockStatementNode'] = None
    keywordNot: Optional[str] = None
    keywordEXISTS: Optional[str] = None


@dataclass
class CTEDefinitionNode(ASTNode):
    name: str
    columns: Optional[List[str]] = None
    selectStatement: 'SelectStatementNode' = None


@dataclass
class CTEStatementNode(StatementNode):
    keywordWith: str
    cteList: List[CTEDefinitionNode]
    statement: StatementNode


@dataclass
class DropTableStatementNode(StatementNode):
    keywordDrop: str
    keywordTable: str
    keywordIf: Optional[str] = None
    keywordExists: Optional[str] = None
    tableName: 'TableNameNode' = None


@dataclass
class DropConstraintStatementNode(StatementNode):
    keywordDrop: str
    keywordConstraint: str
    constraintName: str
    keywordIf: Optional[str] = None
    keywordExists: Optional[str] = None


@dataclass
class DropIndexStatementNode(StatementNode):
    keywordDrop: str
    keywordIndex: str
    indexName: str
    keywordIf: Optional[str] = None
    keywordExists: Optional[str] = None
    tableName: Optional['TableNameNode'] = None


@dataclass
class DropViewStatementNode(StatementNode):
    keywordDrop: str
    keywordView: str
    viewName: str
    keywordIf: Optional[str] = None
    keywordExists: Optional[str] = None


@dataclass
class DropProcedureStatementNode(StatementNode):
    keywordDrop: str
    keywordProcedure: str
    procedureName: str
    keywordIf: Optional[str] = None
    keywordExists: Optional[str] = None


@dataclass
class UseStatementNode(StatementNode):
    keywordUse: str
    databaseName: str


@dataclass
class DeclareCursorStatementNode(StatementNode):
    keywordDeclare: str
    cursorName: str
    keywordCursor: str
    keywordFor: str
    options: Optional[List[str]] = None
    selectStatement: 'SelectStatementNode' = None


@dataclass
class OpenCursorStatementNode(StatementNode):
    keywordOpen: str
    cursorName: str


@dataclass
class FetchCursorStatementNode(StatementNode):
    from .expression_nodes import ExpressionNode
    keywordFetch: str
    keywordFrom: str
    cursorName: str
    fetchType: Optional[str] = None
    expression: Optional['ExpressionNode'] = None
    keywordInto: Optional[str] = None
    variables: Optional[List[str]] = None


@dataclass
class CloseCursorStatementNode(StatementNode):
    keywordClose: str
    cursorName: str


@dataclass
class DeallocateCursorStatementNode(StatementNode):
    keywordDeallocate: str
    cursorName: str
