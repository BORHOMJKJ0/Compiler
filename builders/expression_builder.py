from Ast.statement_nodes import TableNameNode


class ExpressionBuilder:

    def build_expression(self, ctx):
        from Ast.expression_nodes import ParenthesizedExpressionNode, BinaryExpressionNode, VariableExpressionNode, LiteralExpressionNode

        if hasattr(ctx, 'primary') and ctx.primary():
            primary = ctx.primary()
            if isinstance(primary, list):
                if len(primary) > 0:
                    primary = primary[0]
                else:
                    primary = None
            if primary:
                return self.build_primary(primary)

        if hasattr(ctx, 'literal') and ctx.literal():
            return self.build_literal(ctx.literal())
        elif hasattr(ctx, 'columnReference') and ctx.columnReference():
            return self.build_column_reference(ctx.columnReference())
        elif hasattr(ctx, 'functionCall') and ctx.functionCall():
            return self.build_function_call(ctx.functionCall())
        elif hasattr(ctx, 'caseExpression') and ctx.caseExpression():
            return self.build_case_expression(ctx.caseExpression())
        elif hasattr(ctx, 'LPAREN') and ctx.LPAREN() and hasattr(ctx, 'RPAREN') and ctx.RPAREN():
            expression = self.build_expression(ctx.expression(0))
            return ParenthesizedExpressionNode(expression=expression)
        elif hasattr(ctx, 'binaryOp') and ctx.binaryOp():
            expr_list = ctx.expression()
            if expr_list and len(expr_list) == 2:
                left = self.build_expression(expr_list[0])
                operator = ctx.binaryOp().getText()
                right = self.build_expression(expr_list[1])
                return BinaryExpressionNode(left=left, operator=operator, right=right)
        elif hasattr(ctx, 'OPERATOR') and ctx.OPERATOR():
            expr_list = ctx.expression()
            if expr_list and len(expr_list) == 2:
                left = self.build_expression(expr_list[0])
                operator = ctx.OPERATOR().getText()
                right = self.build_expression(expr_list[1])
                return BinaryExpressionNode(left=left, operator=operator, right=right)
        elif hasattr(ctx, 'VARIABLE') and ctx.VARIABLE():
            variableName = ctx.VARIABLE().getText()
            return VariableExpressionNode(variable_name=variableName)
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

    def build_primary(self, ctx):
        from Ast.expression_nodes import LiteralExpressionNode, VariableExpressionNode, ColumnReferenceExpressionNode

        if hasattr(ctx, 'selectStatement') and ctx.selectStatement():
            from builders.statement_builder import StatementBuilder
            stmt_builder = StatementBuilder()
            return stmt_builder.build_select(ctx.selectStatement())

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

        if hasattr(ctx, 'OPERATOR') and ctx.OPERATOR() and ctx.primary():
            op = ctx.OPERATOR().getText()
            inner = self.build_primary(ctx.primary())
            if isinstance(inner, LiteralExpressionNode):
                inner.value = op + inner.value
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
        expressionList = self.build_expression_list(ctx.expressionList()) if hasattr(
            ctx, 'expressionList') and ctx.expressionList() else None
        return FunctionCallExpressionNode(function_name=functionName, arguments=expressionList)

    def build_expression_list(self, ctx):
        expressions = []
        for expression in ctx.expression():
            expr = self.build_expression(expression)
            if expr is not None:
                expressions.append(expr)
        return expressions

    def build_case_expression(self, ctx):
        from Ast.expression_nodes import CaseExpressionNode
        whenClauseList = []
        if hasattr(ctx, 'whenClause'):
            for whenClause in ctx.whenClause():
                clause = self.build_when_clause(whenClause)
                if clause is not None:
                    whenClauseList.append(clause)
        elseClause = self.build_else_clause(ctx.elseClause()) if hasattr(
            ctx, 'elseClause') and ctx.elseClause() else None
        return CaseExpressionNode(
            keywordCase="CASE",
            whenClauseList=whenClauseList,
            elseClause=elseClause,
            keywordEnd="END"
        )

    def build_when_clause(self, ctx):
        from Ast.expression_nodes import WhenClauseNode
        from .condition_builder import ConditionBuilder
        condition_builder = ConditionBuilder()

        condition = condition_builder.build_condition(ctx.condition())
        expression = self.build_expression(ctx.expression())
        return WhenClauseNode(
            keywordWhen="WHEN",
            condition=condition,
            keyword="THEN",
            expression=expression
        )

    def build_else_clause(self, ctx):
        from Ast.expression_nodes import ElseClauseNode
        expression = self.build_expression(ctx.expression())
        return ElseClauseNode(keywordElse="ELSE", expression=expression)

    def build_table_name(self, ctx):
        text = ctx.getText()
        if '.' in text:
            parts = text.split('.')
            schema = parts[0].strip('[]')
            name = parts[-1].strip('[]')
        else:
            schema = None
            name = text.strip('[]')

        return TableNameNode(schema=schema, name=name)
