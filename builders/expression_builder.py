from Ast.statement_nodes import TableNameNode


class ExpressionBuilder:
    def __init__(self, statement_builder=None):
        self.statement_builder = statement_builder

    def set_statement_builder(self, statement_builder):
        self.statement_builder = statement_builder

    def build_expression(self, ctx):
        from Ast.expression_nodes import (
            ParenthesizedExpressionNode,
            BinaryExpressionNode,
            VariableExpressionNode,
            LiteralExpressionNode
        )

        if hasattr(ctx, 'primary') and ctx.primary():
            primary = ctx.primary()
            if isinstance(primary, list):
                if len(primary) > 1:
                    operators = []
                    if hasattr(ctx, 'binaryOp') and ctx.binaryOp():
                        binops = ctx.binaryOp()
                        if isinstance(binops, list):
                            operators = [op.getText() for op in binops]
                        else:
                            operators = [binops.getText()]
                    elif hasattr(ctx, 'OPERATOR') and ctx.OPERATOR():
                        ops = ctx.OPERATOR()
                        if isinstance(ops, list):
                            operators = [op.getText() for op in ops]
                        else:
                            operators = [ops.getText()]

                    if operators:
                        return self._build_binary_expression_tree(primary, operators)
                    else:
                        return self.build_primary(primary[0])
                elif len(primary) == 1:
                    return self.build_primary(primary[0])
            else:
                return self.build_primary(primary)

        if hasattr(ctx, 'literal') and ctx.literal():
            return self.build_literal(ctx.literal())
        elif hasattr(ctx, 'columnReference') and ctx.columnReference():
            return self.build_column_reference(ctx.columnReference())
        elif hasattr(ctx, 'functionCall') and ctx.functionCall():
            return self.build_function_call(ctx.functionCall())
        elif hasattr(ctx, 'caseExpression') and ctx.caseExpression():
            return self.build_case_expression(ctx.caseExpression())
        elif hasattr(ctx, 'VARIABLE') and ctx.VARIABLE():
            variableName = ctx.VARIABLE().getText()
            return VariableExpressionNode(variable_name=variableName)

        elif hasattr(ctx, 'LPAREN') and ctx.LPAREN() and hasattr(ctx, 'RPAREN') and ctx.RPAREN():
            if hasattr(ctx, 'expression'):
                expr_list = ctx.expression()
                if isinstance(expr_list, list) and len(expr_list) > 0:
                    inner_expr = self.build_expression(expr_list[0])
                elif not isinstance(expr_list, list):
                    inner_expr = self.build_expression(expr_list)
                else:
                    inner_expr = None

                if inner_expr:
                    return ParenthesizedExpressionNode(expression=inner_expr)

        elif hasattr(ctx, 'expression'):
            expr_list = ctx.expression()
            if isinstance(expr_list, list) and len(expr_list) >= 2:
                left = self.build_expression(expr_list[0])
                right = self.build_expression(expr_list[1])

                operator = None
                if hasattr(ctx, 'binaryOp') and ctx.binaryOp():
                    operator = ctx.binaryOp().getText()
                elif hasattr(ctx, 'OPERATOR') and ctx.OPERATOR():
                    operator = ctx.OPERATOR().getText()

                if operator:
                    return BinaryExpressionNode(left=left, operator=operator, right=right)
                else:
                    return left
            elif isinstance(expr_list, list) and len(expr_list) == 1:
                return self.build_expression(expr_list[0])
            elif not isinstance(expr_list, list):
                return self.build_expression(expr_list)

        elif hasattr(ctx, 'STRING_SINGLE') and ctx.STRING_SINGLE():
            value = ctx.STRING_SINGLE().getText()
            return LiteralExpressionNode(value=value, literal_type="STRING_SINGLE")
        elif hasattr(ctx, 'STRING_DOUBLE') and ctx.STRING_DOUBLE():
            value = ctx.STRING_DOUBLE().getText()
            return LiteralExpressionNode(value=value, literal_type="STRING_DOUBLE")

        from dataclasses import dataclass

        @dataclass
        class UnknownExpressionNode:
            type: str
            text: str
        return UnknownExpressionNode(type="UnknownExpression", text=ctx.getText()[:50])

    def _build_binary_expression_tree(self, primaries, operators):
        from Ast.expression_nodes import BinaryExpressionNode

        if len(primaries) == 0:
            return None
        if len(primaries) == 1:
            return self.build_primary(primaries[0])

        result = self.build_primary(primaries[0])

        for i in range(len(operators)):
            if i + 1 < len(primaries):
                right = self.build_primary(primaries[i + 1])
                result = BinaryExpressionNode(
                    left=result,
                    operator=operators[i],
                    right=right
                )

        return result

    def build_primary(self, ctx):
        from Ast.expression_nodes import (
            LiteralExpressionNode,
            VariableExpressionNode,
            ColumnReferenceExpressionNode,
            ParenthesizedExpressionNode
        )

        if hasattr(ctx, 'selectStatement') and ctx.selectStatement():
            if self.statement_builder:
                return self.statement_builder.build_select(ctx.selectStatement())

        if hasattr(ctx, 'LPAREN') and ctx.LPAREN():
            if hasattr(ctx, 'expression') and ctx.expression():
                expr = ctx.expression()
                if isinstance(expr, list) and len(expr) > 0:
                    inner = self.build_expression(expr[0])
                elif not isinstance(expr, list):
                    inner = self.build_expression(expr)
                else:
                    inner = None

                if inner:
                    return ParenthesizedExpressionNode(expression=inner)

        if hasattr(ctx, 'literal') and ctx.literal():
            lit = ctx.literal()
            if isinstance(lit, list) and len(lit) > 0:
                return self.build_literal(lit[0])
            else:
                return self.build_literal(lit)

        if hasattr(ctx, 'identifier') and ctx.identifier():
            ident_ctx = ctx.identifier()
            if isinstance(ident_ctx, list) and len(ident_ctx) > 0:
                ident_text = ident_ctx[0].getText()
            elif not isinstance(ident_ctx, list):
                ident_text = ident_ctx.getText()
            else:
                ident_text = None

            if ident_text:
                return ColumnReferenceExpressionNode(table_name=None, column_name=ident_text)

        if hasattr(ctx, 'columnReference') and ctx.columnReference():
            colref = ctx.columnReference()
            if isinstance(colref, list) and len(colref) > 0:
                return self.build_column_reference(colref[0])
            else:
                return self.build_column_reference(colref)

        if hasattr(ctx, 'functionCall') and ctx.functionCall():
            func = ctx.functionCall()
            if isinstance(func, list) and len(func) > 0:
                return self.build_function_call(func[0])
            else:
                return self.build_function_call(func)

        if hasattr(ctx, 'VARIABLE') and ctx.VARIABLE():
            return VariableExpressionNode(variable_name=ctx.VARIABLE().getText())

        if hasattr(ctx, 'expression') and ctx.expression():
            expr = ctx.expression()
            if isinstance(expr, list) and len(expr) > 0:
                return self.build_expression(expr[0])
            else:
                return self.build_expression(expr)

        if hasattr(ctx, 'OPERATOR') and ctx.OPERATOR():
            op_text = ctx.OPERATOR().getText()
            if hasattr(ctx, 'primary') and ctx.primary():
                inner = self.build_primary(ctx.primary())
                if isinstance(inner, LiteralExpressionNode):
                    inner.value = op_text + inner.value
                    return inner
                return inner

        return None

    def build_literal(self, ctx):
        from Ast.expression_nodes import LiteralExpressionNode

        if hasattr(ctx, 'NUMBER') and ctx.NUMBER():
            value = ctx.NUMBER().getText()
            return LiteralExpressionNode(value=value, literal_type="NUMBER")
        elif hasattr(ctx, 'STRING_SINGLE') and ctx.STRING_SINGLE():
            value = ctx.STRING_SINGLE().getText()
            return LiteralExpressionNode(value=value, literal_type="STRING_SINGLE")
        elif hasattr(ctx, 'STRING_DOUBLE') and ctx.STRING_DOUBLE():
            value = ctx.STRING_DOUBLE().getText()
            return LiteralExpressionNode(value=value, literal_type="STRING_DOUBLE")
        elif hasattr(ctx, 'BINARY') and ctx.BINARY():
            value = ctx.BINARY().getText()
            return LiteralExpressionNode(value=value, literal_type="BINARY")
        elif hasattr(ctx, 'HEX') and ctx.HEX():
            value = ctx.HEX().getText()
            return LiteralExpressionNode(value=value, literal_type="HEX")
        else:
            return LiteralExpressionNode(value=ctx.getText(), literal_type="KEYWORD")

    def build_column_reference(self, ctx):
        from Ast.expression_nodes import ColumnReferenceExpressionNode

        tableName = None
        columnName = None

        if hasattr(ctx, 'columnName') and ctx.columnName():
            if hasattr(ctx, 'tableName') and ctx.tableName():
                tableName = self.build_table_name(ctx.tableName())
            columnName = ctx.columnName().getText()
        else:
            columnName = ctx.getText()

        return ColumnReferenceExpressionNode(table_name=tableName, column_name=columnName)

    def build_function_call(self, ctx):
        from Ast.expression_nodes import FunctionCallExpressionNode

        functionName = ctx.getChild(0).getText()
        expressionList = None

        if hasattr(ctx, 'expressionList') and ctx.expressionList():
            expressionList = self.build_expression_list(ctx.expressionList())

        return FunctionCallExpressionNode(function_name=functionName, arguments=expressionList)

    def build_expression_list(self, ctx):
        expressions = []

        if hasattr(ctx, 'expression'):
            expr_contexts = ctx.expression()

            if isinstance(expr_contexts, list):
                for expr_ctx in expr_contexts:
                    expr = self.build_expression(expr_ctx)
                    if expr is not None:
                        expressions.append(expr)
            else:
                expr = self.build_expression(expr_contexts)
                if expr is not None:
                    expressions.append(expr)

        return expressions

    def build_case_expression(self, ctx):
        from Ast.expression_nodes import CaseExpressionNode

        whenClauseList = []
        if hasattr(ctx, 'whenClause'):
            when_clauses = ctx.whenClause()
            if isinstance(when_clauses, list):
                for whenClause in when_clauses:
                    clause = self.build_when_clause(whenClause)
                    if clause is not None:
                        whenClauseList.append(clause)
            else:
                clause = self.build_when_clause(when_clauses)
                if clause is not None:
                    whenClauseList.append(clause)

        elseClause = None
        if hasattr(ctx, 'elseClause') and ctx.elseClause():
            elseClause = self.build_else_clause(ctx.elseClause())

        return CaseExpressionNode(
            keywordCase="CASE",
            whenClauseList=whenClauseList,
            elseClause=elseClause,
            keywordEnd="END"
        )

    def build_when_clause(self, ctx):
        from Ast.expression_nodes import WhenClauseNode
        from builders.condition_builder import ConditionBuilder

        condition_builder = ConditionBuilder(self.statement_builder)

        condition = None
        if hasattr(ctx, 'condition') and ctx.condition():
            condition = condition_builder.build_condition(ctx.condition())

        expression = None
        if hasattr(ctx, 'expression') and ctx.expression():
            expression = self.build_expression(ctx.expression())

        return WhenClauseNode(
            keywordWhen="WHEN",
            condition=condition,
            keyword="THEN",
            expression=expression
        )

    def build_else_clause(self, ctx):
        from Ast.expression_nodes import ElseClauseNode

        expression = None
        if hasattr(ctx, 'expression') and ctx.expression():
            expression = self.build_expression(ctx.expression())

        return ElseClauseNode(keywordElse="ELSE", expression=expression)

    def build_table_name(self, ctx):
        text = ctx.getText()
        if '.' in text:
            parts = text.split('.')
            schema = parts[0].strip('[]').strip('"')
            name = parts[-1].strip('[]').strip('"')
        else:
            schema = None
            name = text.strip('[]').strip('"')

        return TableNameNode(schema=schema, name=name)
