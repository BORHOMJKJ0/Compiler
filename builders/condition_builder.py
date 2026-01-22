class ConditionBuilder:
    def __init__(self, statement_builder=None):
        self.statement_builder = statement_builder

    def set_statement_builder(self, statement_builder):
        self.statement_builder = statement_builder

    def build_condition(self, ctx):
        try:
            from builders.expression_builder import ExpressionBuilder
        except ImportError:
            try:
                from .expression_builder import ExpressionBuilder  
            except ImportError:
                from expression_builder import ExpressionBuilder  
        from Ast.condition_nodes import (
            BinaryConditionNode,
            LogicalConditionNode,
            ParenthesizedConditionNode,
            InConditionNode,
            IsNotConditionNode
        )
        expr_builder = ExpressionBuilder(self.statement_builder)

        if self._is_not_exists(ctx):
            return self._build_not_exists_condition(ctx, expr_builder)

        if self._is_exists(ctx):
            return self._build_exists_condition(ctx, expr_builder)

        if self._is_between_condition(ctx):
            return self._build_between_condition(ctx, expr_builder)

        if hasattr(ctx, 'LPAREN') and ctx.LPAREN() and hasattr(ctx, 'RPAREN') and ctx.RPAREN():
            if hasattr(ctx, 'condition') and ctx.condition():
                condition_ctx = ctx.condition()
                if isinstance(condition_ctx, list) and len(condition_ctx) > 0:
                    inner_condition = self.build_condition(condition_ctx[0])
                elif not isinstance(condition_ctx, list):
                    inner_condition = self.build_condition(condition_ctx)
                else:
                    inner_condition = None

                if inner_condition:
                    return ParenthesizedConditionNode(condition=inner_condition)

        if self._is_in_condition(ctx):
            return self._build_in_condition(ctx, expr_builder)

        if self._is_is_not_condition(ctx):
            return self._build_is_not_condition(ctx, expr_builder)

        if self._has_logical_operator(ctx):
            return self._build_logical_condition(ctx, expr_builder)

        if self._is_binary_condition(ctx):
            return self._build_binary_condition(ctx, expr_builder)

        if hasattr(ctx, 'expression') and ctx.expression():
            expr_ctx = ctx.expression()

            if isinstance(expr_ctx, list):
                expr_ctx = expr_ctx[0] if len(expr_ctx) > 0 else None

            if expr_ctx:
                return self._build_expression_as_condition(expr_ctx, expr_builder)

        return expr_builder.build_expression(ctx)

    def _is_not_exists(self, ctx):
        text = ctx.getText().upper() if hasattr(ctx, 'getText') else ""
        return 'NOTEXISTS' in text.replace(' ', '') or (
            hasattr(ctx, 'NOT') and ctx.NOT() and
            hasattr(ctx, 'EXISTS') and ctx.EXISTS()
        )

    def _is_exists(self, ctx):
        text = ctx.getText().upper() if hasattr(ctx, 'getText') else ""
        return 'EXISTS' in text and 'NOTEXISTS' not in text.replace(' ', '') or (
            hasattr(ctx, 'EXISTS') and ctx.EXISTS() and
            not (hasattr(ctx, 'NOT') and ctx.NOT())
        )

    def _build_not_exists_condition(self, ctx, expr_builder):
        from Ast.condition_nodes import BinaryConditionNode
        from Ast.expression_nodes import LiteralExpressionNode

        subquery = None
        if hasattr(ctx, 'selectStatement') and ctx.selectStatement():
            if self.statement_builder:
                subquery = self.statement_builder.build_select(
                    ctx.selectStatement())
        elif hasattr(ctx, 'primary') and ctx.primary():
            primary = ctx.primary()
            if isinstance(primary, list):
                primary = primary[0] if len(primary) > 0 else None
            if primary and hasattr(primary, 'selectStatement') and primary.selectStatement():
                if self.statement_builder:
                    subquery = self.statement_builder.build_select(
                        primary.selectStatement())

        left_expr = LiteralExpressionNode(
            value="NOT EXISTS", literal_type="KEYWORD")

        return BinaryConditionNode(
            left=left_expr,
            operator="NOT EXISTS",
            right=subquery if subquery else expr_builder.build_expression(ctx)
        )

    def _build_exists_condition(self, ctx, expr_builder):
        from Ast.condition_nodes import BinaryConditionNode
        from Ast.expression_nodes import LiteralExpressionNode

        subquery = None
        if hasattr(ctx, 'selectStatement') and ctx.selectStatement():
            if self.statement_builder:
                subquery = self.statement_builder.build_select(
                    ctx.selectStatement())
        elif hasattr(ctx, 'primary') and ctx.primary():
            primary = ctx.primary()
            if isinstance(primary, list):
                primary = primary[0] if len(primary) > 0 else None
            if primary and hasattr(primary, 'selectStatement') and primary.selectStatement():
                if self.statement_builder:
                    subquery = self.statement_builder.build_select(
                        primary.selectStatement())

        left_expr = LiteralExpressionNode(
            value="EXISTS", literal_type="KEYWORD")

        return BinaryConditionNode(
            left=left_expr,
            operator="EXISTS",
            right=subquery if subquery else expr_builder.build_expression(ctx)
        )

    def _is_between_condition(self, ctx):
        text = ctx.getText().upper() if hasattr(ctx, 'getText') else ""
        return 'BETWEEN' in text or (hasattr(ctx, 'BETWEEN') and ctx.BETWEEN())

    def _build_between_condition(self, ctx, expr_builder):
        from Ast.condition_nodes import BinaryConditionNode, LogicalConditionNode

        is_not_between = False
        text = ctx.getText().upper() if hasattr(ctx, 'getText') else ""
        if 'NOTBETWEEN' in text.replace(' ', '') or (
            hasattr(ctx, 'NOT') and ctx.NOT() and hasattr(
                ctx, 'BETWEEN') and ctx.BETWEEN()
        ):
            is_not_between = True

        value_expr = None
        low_expr = None
        high_expr = None

        if hasattr(ctx, 'expression') and ctx.expression():
            expr_list = ctx.expression()
            if isinstance(expr_list, list):
                if len(expr_list) >= 3:
                    value_expr = expr_builder.build_expression(expr_list[0])
                    low_expr = expr_builder.build_expression(expr_list[1])
                    high_expr = expr_builder.build_expression(expr_list[2])
                elif len(expr_list) >= 1:
                    value_expr = expr_builder.build_expression(expr_list[0])
        elif hasattr(ctx, 'primary') and ctx.primary():
            primaries = ctx.primary()
            if isinstance(primaries, list) and len(primaries) >= 3:
                value_expr = expr_builder.build_primary(primaries[0])
                low_expr = expr_builder.build_primary(primaries[1])
                high_expr = expr_builder.build_primary(primaries[2])

        if value_expr and low_expr and high_expr:
            if is_not_between:
                left_condition = BinaryConditionNode(
                    left=value_expr,
                    operator="<",
                    right=low_expr
                )
                right_condition = BinaryConditionNode(
                    left=value_expr,
                    operator=">",
                    right=high_expr
                )
                return LogicalConditionNode(
                    left=left_condition,
                    operator="OR",
                    right=right_condition
                )
            else:
                left_condition = BinaryConditionNode(
                    left=value_expr,
                    operator=">=",
                    right=low_expr
                )
                right_condition = BinaryConditionNode(
                    left=value_expr,
                    operator="<=",
                    right=high_expr
                )
                return LogicalConditionNode(
                    left=left_condition,
                    operator="AND",
                    right=right_condition
                )

        return expr_builder.build_expression(ctx)

    def _is_in_condition(self, ctx):
        text = ctx.getText().upper() if hasattr(ctx, 'getText') else ""
        return 'IN(' in text.replace(' ', '') or (
            hasattr(ctx, 'IN') and ctx.IN()
        )

    def _build_in_condition(self, ctx, expr_builder):
        from Ast.condition_nodes import InConditionNode

        left_expr = None
        if hasattr(ctx, 'expression') and ctx.expression():
            expr_list = ctx.expression()
            if isinstance(expr_list, list) and len(expr_list) > 0:
                left_expr = expr_builder.build_expression(expr_list[0])
            elif not isinstance(expr_list, list):
                left_expr = expr_builder.build_expression(expr_list)
        elif hasattr(ctx, 'primary') and ctx.primary():
            primary = ctx.primary()
            if isinstance(primary, list) and len(primary) > 0:
                left_expr = expr_builder.build_primary(primary[0])
            else:
                left_expr = expr_builder.build_primary(primary)

        expression_list = []

        if hasattr(ctx, 'selectStatement') and ctx.selectStatement():
            if self.statement_builder:
                subquery = self.statement_builder.build_select(
                    ctx.selectStatement())
                expression_list = [subquery]

        elif hasattr(ctx, 'expressionList') and ctx.expressionList():
            expression_list = expr_builder.build_expression_list(
                ctx.expressionList())

        elif hasattr(ctx, 'expression') and ctx.expression():
            expr_list = ctx.expression()
            if isinstance(expr_list, list) and len(expr_list) > 1:
                for expr_ctx in expr_list[1:]:
                    expression_list.append(
                        expr_builder.build_expression(expr_ctx))

        elif hasattr(ctx, 'primary') and ctx.primary():
            primaries = ctx.primary()
            if isinstance(primaries, list) and len(primaries) > 1:
                for p in primaries[1:]:
                    if hasattr(p, 'selectStatement') and p.selectStatement():
                        if self.statement_builder:
                            subquery = self.statement_builder.build_select(
                                p.selectStatement())
                            expression_list = [subquery]
                            break
                    else:
                        expression_list.append(expr_builder.build_primary(p))

        keyword_not = None
        if hasattr(ctx, 'NOT') and ctx.NOT():
            keyword_not = "NOT"
        elif 'NOTIN' in ctx.getText().upper().replace(' ', ''):
            keyword_not = "NOT"

        return InConditionNode(
            left=left_expr,
            keywordIn="IN",
            expressionList=expression_list,
            keywordNot=keyword_not
        )

    def _is_is_not_condition(self, ctx):
        text = ctx.getText().upper() if hasattr(ctx, 'getText') else ""
        return 'ISNOT' in text.replace(' ', '') or (
            hasattr(ctx, 'IS') and ctx.IS() and
            hasattr(ctx, 'NOT') and ctx.NOT()
        )

    def _build_is_not_condition(self, ctx, expr_builder):
        from Ast.condition_nodes import IsNotConditionNode

        left_expr = None
        if hasattr(ctx, 'expression') and ctx.expression():
            expr_list = ctx.expression()
            if isinstance(expr_list, list) and len(expr_list) > 0:
                left_expr = expr_builder.build_expression(expr_list[0])
            elif not isinstance(expr_list, list):
                left_expr = expr_builder.build_expression(expr_list)

        return IsNotConditionNode(
            left=left_expr,
            keywordIs="IS",
            keywordNot="NOT"
        )

    def _has_logical_operator(self, ctx):
        text = ctx.getText().upper() if hasattr(ctx, 'getText') else ""
        if 'BETWEEN' in text:
            return False
        if hasattr(ctx, 'AND') and ctx.AND():
            return True
        if hasattr(ctx, 'OR') and ctx.OR():
            return True
        return ' AND ' in ' ' + text + ' ' or ' OR ' in ' ' + text + ' '

    def _build_logical_condition(self, ctx, expr_builder):
        from Ast.condition_nodes import LogicalConditionNode

        if hasattr(ctx, 'condition') and ctx.condition():
            conditions = ctx.condition()
            if isinstance(conditions, list) and len(conditions) >= 2:
                left_cond = self.build_condition(conditions[0])
                right_cond = self.build_condition(conditions[1])

                operator = "AND"
                if hasattr(ctx, 'OR') and ctx.OR():
                    operator = "OR"
                elif hasattr(ctx, 'AND') and ctx.AND():
                    operator = "AND"

                return LogicalConditionNode(
                    left=left_cond,
                    operator=operator,
                    right=right_cond
                )

        return self._build_expression_as_condition(ctx, expr_builder)

    def _is_binary_condition(self, ctx):
        if hasattr(ctx, 'binaryOp') and ctx.binaryOp():
            return True
        if hasattr(ctx, 'OPERATOR') and ctx.OPERATOR():
            op = ctx.OPERATOR().getText()
            return op in ('=', '<>', '!=', '<', '>', '<=', '>=')
        text = ctx.getText() if hasattr(ctx, 'getText') else ""
        return any(op in text for op in ['=', '<>', '!=', '<', '>', '<=', '>=', 'LIKE'])

    def _build_binary_condition(self, ctx, expr_builder):
        from Ast.condition_nodes import BinaryConditionNode

        left_expr = None
        right_expr = None
        operator = None

        if hasattr(ctx, 'expression') and ctx.expression():
            expr_list = ctx.expression()
            if isinstance(expr_list, list) and len(expr_list) >= 2:
                left_expr = expr_builder.build_expression(expr_list[0])
                right_expr = expr_builder.build_expression(expr_list[1])
        elif hasattr(ctx, 'primary') and ctx.primary():
            primaries = ctx.primary()
            if isinstance(primaries, list) and len(primaries) >= 2:
                left_expr = expr_builder.build_primary(primaries[0])
                right_expr = expr_builder.build_primary(primaries[1])

        if hasattr(ctx, 'binaryOp') and ctx.binaryOp():
            operator = ctx.binaryOp().getText()
        elif hasattr(ctx, 'OPERATOR') and ctx.OPERATOR():
            operator = ctx.OPERATOR().getText()
        elif hasattr(ctx, 'LIKE') and ctx.LIKE():
            operator = "LIKE"

        if left_expr and right_expr and operator:
            return BinaryConditionNode(
                left=left_expr,
                operator=operator,
                right=right_expr
            )

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
