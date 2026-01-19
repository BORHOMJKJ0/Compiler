class ConditionBuilder:
    """Builder for condition AST nodes"""

    def build_condition(self, ctx):
        """Build a condition node from context"""
        from builders.expression_builder import ExpressionBuilder
        from Ast.condition_nodes import BinaryConditionNode, InConditionNode, IsNotConditionNode, ParenthesizedConditionNode, LogicalConditionNode
        expr_builder = ExpressionBuilder()

        if hasattr(ctx, 'expression') and len(ctx.expression()) == 2:
            left = expr_builder.build_expression(ctx.expression(0))
            right = expr_builder.build_expression(ctx.expression(1))
            operator = None
            if hasattr(ctx, 'OPERATOR') and ctx.OPERATOR():
                operator = ctx.OPERATOR().getText()
            elif hasattr(ctx, 'binaryOp') and ctx.binaryOp():
                operator = ctx.binaryOp().getText()
            elif hasattr(ctx, 'KEYWORD') and ctx.KEYWORD():
                keywords = ctx.KEYWORD()
                if len(keywords) == 1:
                    operator = keywords[0].getText()
            return BinaryConditionNode(left=left, operator=operator, right=right)

        elif hasattr(ctx, 'expressionList') and ctx.expressionList():
            left = expr_builder.build_expression(ctx.expression(0))
            expressionList = expr_builder.build_expression_list(ctx.expressionList())
            keywordIn = "IN"
            keywordNot = "NOT" if "NOT" in ctx.getText().upper() else None
            return InConditionNode(
                left=left,
                keywordIn=keywordIn,
                expressionList=expressionList,
                keywordNot=keywordNot
            )

        elif "IS" in ctx.getText().upper() and hasattr(ctx, 'expression') and len(ctx.expression()) == 1:
            left = expr_builder.build_expression(ctx.expression(0))
            keywordIs = "IS"
            keywordNot = "NOT" if "NOT" in ctx.getText().upper() else None
            return IsNotConditionNode(
                left=left,
                keywordIs=keywordIs,
                keywordNot=keywordNot
            )

        elif hasattr(ctx, 'condition') and len(ctx.condition()) == 1:
            condition = self.build_condition(ctx.condition(0))
            return ParenthesizedConditionNode(condition=condition)

        elif hasattr(ctx, 'condition') and len(ctx.condition()) == 2:
            left = self.build_condition(ctx.condition(0))
            right = self.build_condition(ctx.condition(1))
            operator = "AND" if "AND" in ctx.getText().upper() else "OR"
            return LogicalConditionNode(left=left, operator=operator, right=right)

        # Fallback for EXISTS or other conditions
        from dataclasses import dataclass
        @dataclass
        class GenericConditionNode:
            type: str
            text: str
        return GenericConditionNode(type="Condition", text=ctx.getText()[:50])
