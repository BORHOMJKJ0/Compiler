from dataclasses import dataclass
from typing import Optional


@dataclass
class ASTNode:
    """Base class for all AST nodes"""
    pass


@dataclass
class StatementNode(ASTNode):
    """Base class for all statement nodes"""
    pass