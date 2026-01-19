from dataclasses import dataclass
from typing import List, Optional
from .base_nodes import ASTNode


@dataclass
class ExpressionNode(ASTNode):
    """Base class for expression nodes"""
    pass


@dataclass
class LiteralExpressionNode(ExpressionNode):
    value: str
    literal_type: str  # "NUMBER", "STRING_SINGLE", "STRING_DOUBLE", "KEYWORD", "OPERATOR"


@dataclass
class ColumnReferenceExpressionNode(ExpressionNode):
    from .statement_nodes import TableNameNode
    column_name: str
    table_name: Optional['TableNameNode'] = None


@dataclass
class FunctionCallExpressionNode(ExpressionNode):
    function_name: str
    arguments: Optional[List[ExpressionNode]] = None


@dataclass
class VariableExpressionNode(ExpressionNode):
    variable_name: str


@dataclass
class BinaryExpressionNode(ExpressionNode):
    left: ExpressionNode
    operator: str
    right: ExpressionNode


@dataclass
class ParenthesizedExpressionNode(ExpressionNode):
    expression: ExpressionNode


@dataclass
class CaseExpressionNode(ExpressionNode):
    keywordCase: str
    whenClauseList: List['WhenClauseNode']
    elseClause: Optional['ElseClauseNode']
    keywordEnd: str


@dataclass
class WhenClauseNode(ASTNode):
    from .condition_nodes import ConditionNode
    keywordWhen: str
    condition: 'ConditionNode'
    keyword: str
    expression: ExpressionNode


@dataclass
class ElseClauseNode(ASTNode):
    keywordElse: str
    expression: ExpressionNode