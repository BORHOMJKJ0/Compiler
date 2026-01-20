from dataclasses import dataclass
from typing import List, Optional
from .base_nodes import ASTNode


@dataclass
class ConditionNode(ASTNode):
    pass


@dataclass
class BinaryConditionNode(ConditionNode):
    from .expression_nodes import ExpressionNode
    left: 'ExpressionNode'
    operator: str
    right: 'ExpressionNode'


@dataclass
class InConditionNode(ConditionNode):
    from .expression_nodes import ExpressionNode
    left: 'ExpressionNode'
    keywordIn: str
    expressionList: List['ExpressionNode']
    keywordNot: Optional[str] = None


@dataclass
class IsNotConditionNode(ConditionNode):
    from .expression_nodes import ExpressionNode
    left: 'ExpressionNode'
    keywordIs: str
    keywordNot: str


@dataclass
class ParenthesizedConditionNode(ConditionNode):
    condition: ConditionNode


@dataclass
class LogicalConditionNode(ConditionNode):
    left: ConditionNode
    operator: str
    right: ConditionNode
