class ConditionBuilder:
    def __init__(self, statement_builder=None):
        self.statement_builder = statement_builder

    def set_statement_builder(self, statement_builder):
        self.statement_builder = statement_builder

    def build_condition(self, ctx):
        from builders.expression_builder import ExpressionBuilder
        from Ast.condition_nodes import (
            BinaryConditionNode,
            LogicalConditionNode,
            ParenthesizedConditionNode,
            InConditionNode,
            IsNotConditionNode
        )
        expr_builder = ExpressionBuilder(self.statement_builder)

        if hasattr(ctx, 'expression') and ctx.expression():
            expr_ctx = ctx.expression()

            if isinstance(expr_ctx, list):
                expr_ctx = expr_ctx[0] if len(expr_ctx) > 0 else None

            if expr_ctx:
                return self._build_expression_as_condition(expr_ctx, expr_builder)

        return expr_builder.build_expression(ctx)

    def _build_expression_as_condition(self, expr_ctx, expr_builder):
        from Ast.condition_nodes import BinaryConditionNode, LogicalConditionNode

        primaries = []
        operators = []

        if hasattr(expr_ctx, 'getChildCount'):
            for i in range(expr_ctx.getChildCount()):
                child = expr_ctx.getChild(i)
                child_text = child.getText() if hasattr(child, 'getText') else str(child)

                if hasattr(child, 'getRuleIndex'):
                    rule_name = type(child).__name__
                    if 'Primary' in rule_name or 'primary' in rule_name:
                        primaries.append(child)

                if hasattr(child, 'getRuleIndex'):
                    rule_name = type(child).__name__
                    if 'BinaryOp' in rule_name or 'binaryOp' in rule_name:
                        operators.append(child.getText())

        if len(primaries) > 0 and len(operators) > 0:
            return self._build_condition_tree(primaries, operators, expr_builder)

        try:
            primary_result = expr_ctx.primary() if hasattr(expr_ctx, 'primary') else None
            if primary_result:
                if isinstance(primary_result, list) and len(primary_result) > 0:
                    primaries = primary_result
                elif not isinstance(primary_result, list):
                    primaries = [primary_result]

            binop_result = expr_ctx.binaryOp() if hasattr(expr_ctx, 'binaryOp') else None
            if binop_result:
                if isinstance(binop_result, list):
                    operators = [op.getText() for op in binop_result]
                else:
                    operators = [binop_result.getText()]

            if len(primaries) > 0 and len(operators) > 0:
                return self._build_condition_tree(primaries, operators, expr_builder)
        except:
            pass

        return expr_builder.build_expression(expr_ctx)

    def _build_condition_tree(self, primaries, operators, expr_builder):
        from Ast.condition_nodes import BinaryConditionNode, LogicalConditionNode

        if len(primaries) == 0:
            return None

        if len(primaries) == 1:
            return expr_builder.build_primary(primaries[0])

        conditions = []
        i = 0

        while i < len(primaries):
            if i < len(operators):
                op = operators[i].upper()

                if op in ('=', '<>', '!=', '<', '>', '<=', '>=', 'LIKE', 'IN', 'IS'):
                    if i + 1 < len(primaries):
                        left_expr = expr_builder.build_primary(primaries[i])
                        right_expr = expr_builder.build_primary(
                            primaries[i + 1])
                        condition = BinaryConditionNode(
                            left=left_expr, operator=op, right=right_expr)
                        conditions.append(condition)
                        i += 2
                        continue

                elif op in ('AND', 'OR'):
                    conditions.append(expr_builder.build_primary(primaries[i]))
                    i += 1
                    continue

            conditions.append(expr_builder.build_primary(primaries[i]))
            i += 1

        logical_operators = []
        for op in operators:
            if op.upper() in ('AND', 'OR'):
                logical_operators.append(op.upper())

        if len(conditions) == 1:
            return conditions[0]

        result = conditions[0]
        op_idx = 0

        for i in range(1, len(conditions)):
            if op_idx < len(logical_operators):
                result = LogicalConditionNode(
                    left=result,
                    operator=logical_operators[op_idx],
                    right=conditions[i]
                )
                op_idx += 1
            else:
                break

        return result
