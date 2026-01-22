from builders.expression_builder import ExpressionBuilder
from builders.condition_builder import ConditionBuilder


class StatementBuilder:
    def __init__(self):
        self.expr_builder = ExpressionBuilder(self)
        self.cond_builder = ConditionBuilder(self)

    def build_statement(self, ctx):
        if ctx.getText() == ';':
            from dataclasses import dataclass

            @dataclass
            class SemicolonNode:
                type: str = "Semicolon"
            return TableSourceNode(
                tableName=subquery_node,
                keyword=None,
                identifier=alias,
                joinCondition=None
            )

        tableName = self.expr_builder.build_table_name(ctx.tableName())
        alias = None

        if hasattr(ctx, 'identifier') and ctx.identifier():
            identifiers = ctx.identifier()
            if isinstance(identifiers, list) and len(identifiers) > 0:
                alias = identifiers[-1].getText()
            elif not isinstance(identifiers, list):
                alias = identifiers.getText()

        return TableSourceNode(
            tableName=tableName,
            keyword=None,
            identifier=alias,
            joinCondition=None
        )

    def build_order_by_clause(self, ctx):
        from Ast.statement_nodes import OrderByClauseNode
        orderByItems = []
        order_by_items = ctx.orderByItem()
        if isinstance(order_by_items, list):
            for orderByItem in order_by_items:
                item = self.build_order_by_item(orderByItem)
                if item:
                    orderByItems.append(item)
        else:
            item = self.build_order_by_item(order_by_items)
            if item:
                orderByItems.append(item)
        return OrderByClauseNode(
            keywordOrder="ORDER",
            keywordBy="BY",
            orderByitem=orderByItems
        )

    def build_order_by_item(self, ctx):
        from Ast.statement_nodes import OrderByItemNode

        expression = None
        if hasattr(ctx, 'expression') and ctx.expression():
            expression = self.expr_builder.build_expression(ctx.expression())

        ascDesc = None
        if hasattr(ctx, 'ASC') and ctx.ASC():
            ascDesc = "ASC"
        elif hasattr(ctx, 'DESC') and ctx.DESC():
            ascDesc = "DESC"

        return OrderByItemNode(expression=expression, ascDesc=ascDesc)

    def build_select_list(self, ctx):
        selectItems = []
        select_item_contexts = ctx.selectItem()
        if isinstance(select_item_contexts, list):
            for selectItem in select_item_contexts:
                item = self.build_select_item(selectItem)
                if item is not None:
                    selectItems.append(item)
        else:
            item = self.build_select_item(select_item_contexts)
            if item is not None:
                selectItems.append(item)
        return selectItems

    def build_select_item(self, ctx):
        from Ast.statement_nodes import SelectItemNode
        expression = None
        keywordAs = None
        identifier = None

        if hasattr(ctx, 'expression') and ctx.expression():
            expression = self.expr_builder.build_expression(ctx.expression())
        elif hasattr(ctx, 'OPERATOR') and ctx.OPERATOR():
            op_text = ctx.OPERATOR().getText()
            if op_text == '*':
                from Ast.expression_nodes import LiteralExpressionNode
                expression = LiteralExpressionNode(
                    value='*', literal_type='OPERATOR')
            else:
                expression = self.expr_builder.build_expression(ctx)

        if hasattr(ctx, 'AS') and ctx.AS():
            keywordAs = "AS"

        if hasattr(ctx, 'columnName') and ctx.columnName():
            identifier = ctx.columnName().getText()
        elif hasattr(ctx, 'literal') and ctx.literal():
            identifier = ctx.literal().getText()

        return SelectItemNode(
            expression=expression,
            keywordAs=keywordAs,
            identifier=identifier
        )

    def build_insert(self, ctx):
        from Ast.statement_nodes import InsertStatement, InsertColumnsNode, InsertValuesNode

        tableName = self.expr_builder.build_table_name(ctx.tableName())

        insertColumns = None
        if hasattr(ctx, 'columnList') and ctx.columnList():
            column_list = ctx.columnList()
            if hasattr(column_list, 'columnName'):
                column_names = column_list.columnName()
                if isinstance(column_names, list):
                    identifiers = [col.getText() for col in column_names]
                else:
                    identifiers = [column_names.getText()]
                insertColumns = InsertColumnsNode(identifier=identifiers)

        insertValues = None
        selectStatement = None

        if hasattr(ctx, 'insertValues') and ctx.insertValues():
            insertValues = self.build_insert_values(ctx.insertValues())

        elif hasattr(ctx, 'selectStatement') and ctx.selectStatement():
            selectStatement = self.build_select(ctx.selectStatement())

        return InsertStatement(
            keywordInsert="INSERT",
            tableName=tableName,
            keywordInto="INTO",
            insertColumns=insertColumns,
            insertValues=insertValues,
            selectStatement=selectStatement,
            execStatement=None
        )

    def build_insert_values(self, ctx):
        from Ast.statement_nodes import InsertValuesNode

        all_value_sets = []

        if hasattr(ctx, 'expressionList'):
            expr_lists = ctx.expressionList()

            if isinstance(expr_lists, list):
                for expr_list in expr_lists:
                    value_set = self.expr_builder.build_expression_list(
                        expr_list)
                    all_value_sets.append(value_set)
            else:
                value_set = self.expr_builder.build_expression_list(expr_lists)
                all_value_sets.append(value_set)

        return InsertValuesNode(
            keywordValues="VALUES",
            valueSets=all_value_sets
        )

    def build_if(self, ctx):
        from Ast.statement_nodes import IfStatementNode

        keywordNot = None
        keywordEXISTS = None
        selectStatement = None
        condition = None

        if "NOT" in ctx.getText().upper():
            keywordNot = "NOT"
        if "EXISTS" in ctx.getText().upper():
            keywordEXISTS = "EXISTS"

        if hasattr(ctx, 'selectStatement') and ctx.selectStatement():
            selectStatement = self.build_select(ctx.selectStatement())
        elif hasattr(ctx, 'condition') and ctx.condition():
            condition = self.cond_builder.build_condition(ctx.condition())

        blockStatement = None
        if hasattr(ctx, 'thenBlock') and ctx.thenBlock():
            then_block = ctx.thenBlock()
            if hasattr(then_block, 'blockStatement') and then_block.blockStatement():
                blockStatement = self.build_block(then_block.blockStatement())
            elif hasattr(then_block, 'statement') and then_block.statement():
                blockStatement = self.build_statement(then_block.statement())

        elseStatement = None
        if hasattr(ctx, 'elseBlock') and ctx.elseBlock():
            else_block = ctx.elseBlock()
            if hasattr(else_block, 'blockStatement') and else_block.blockStatement():
                elseStatement = self.build_block(else_block.blockStatement())
            elif hasattr(else_block, 'statement') and else_block.statement():
                elseStatement = self.build_statement(else_block.statement())

        return IfStatementNode(
            keywordIf="IF",
            selectStatement=selectStatement,
            condition=condition,
            blockStatement=blockStatement,
            elseStatement=elseStatement,
            keywordNot=keywordNot,
            keywordEXISTS=keywordEXISTS
        )

    def build_block(self, ctx):
        from Ast.statement_nodes import BlockStatementNode
        statements = []

        if hasattr(ctx, 'statement'):
            stmt_contexts = ctx.statement()
            if isinstance(stmt_contexts, list):
                for stmt_ctx in stmt_contexts:
                    stmt = self.build_statement(stmt_ctx)
                    if stmt:
                        statements.append(stmt)
            else:
                stmt = self.build_statement(stmt_contexts)
                if stmt:
                    statements.append(stmt)

        if hasattr(ctx, 'GO') and ctx.GO():
            go_tokens = ctx.GO()
            if isinstance(go_tokens, list):
                for _ in go_tokens:
                    statements.append(self.build_go(None))
            else:
                statements.append(self.build_go(None))

        return BlockStatementNode(
            keywordBegin="BEGIN",
            statementList=statements,
            keywordEnd="END"
        )

    def build_try_catch(self, ctx):
        from Ast.statement_nodes import tryCatchStatementNode

        try_statements = []
        catch_statements = []

        if hasattr(ctx, 'statement'):
            all_statements = ctx.statement()
            if isinstance(all_statements, list):
                mid_point = len(all_statements) // 2
                for i, stmt_ctx in enumerate(all_statements):
                    stmt = self.build_statement(stmt_ctx)
                    if stmt:
                        if i < mid_point:
                            try_statements.append(stmt)
                        else:
                            catch_statements.append(stmt)

        return tryCatchStatementNode(
            keywordBeginForTry="BEGIN",
            keywordBeginTry="TRY",
            tryStatementList=try_statements,
            keywordEndForTry="END",
            keywordEndTry="TRY",
            keywordBeginForCatch="BEGIN",
            keywordBeginCatch="CATCH",
            catchStatementList=catch_statements,
            keywordEndForCatch="END",
            keywordEndCatch="CATCH"
        )

    def build_declare(self, ctx):
        from Ast.statement_nodes import declareStatementNode

        variableName = ctx.VARIABLE().getText() if hasattr(
            ctx, 'VARIABLE') and ctx.VARIABLE() else None
        dataType = ctx.dataType().getText() if hasattr(
            ctx, 'dataType') and ctx.dataType() else None

        operator = None
        expression = None

        if hasattr(ctx, 'OPERATOR') and ctx.OPERATOR():
            operator = ctx.OPERATOR().getText()

        if hasattr(ctx, 'expression') and ctx.expression():
            expression = self.expr_builder.build_expression(ctx.expression())

        return declareStatementNode(
            keywordDeclare="DECLARE",
            variableName=variableName,
            dataType=dataType,
            operator=operator,
            expression=expression
        )

    def build_set(self, ctx):
        from Ast.statement_nodes import setStatementNode

        variableName = None
        if hasattr(ctx, 'VARIABLE') and ctx.VARIABLE():
            variableName = ctx.VARIABLE().getText()
        elif hasattr(ctx, 'columnName') and ctx.columnName():
            variableName = ctx.columnName().getText()

        operator = "="
        if hasattr(ctx, 'OPERATOR') and ctx.OPERATOR():
            operator = ctx.OPERATOR().getText()

        expression = None
        if hasattr(ctx, 'expression') and ctx.expression():
            expression = self.expr_builder.build_expression(ctx.expression())

        return setStatementNode(
            keywordSet="SET",
            variableName=variableName,
            operator=operator,
            expression=expression
        )

    def build_exec(self, ctx):
        from Ast.statement_nodes import execStatementNode

        identifier = None
        if ctx.identifier():
            identifier = ctx.identifier().getText()
        elif ctx.SP_EXECUTESQL():
            identifier = "sp_executesql"

        expressionList = None
        if ctx.expressionList():
            expressionList = self.expr_builder.build_expression_list(
                ctx.expressionList()
            )

        return execStatementNode(
            keywordExec="EXEC",
            identifier=identifier,
            expressionList=expressionList
        )

    def build_cte(self, ctx):
        from Ast.statement_nodes import CTEStatementNode, CTEDefinitionNode

        cte_list = []
        if hasattr(ctx, 'cteList') and ctx.cteList():
            cte_list_ctx = ctx.cteList()
            if hasattr(cte_list_ctx, 'cteDefinition'):
                cte_defs = cte_list_ctx.cteDefinition()
                if isinstance(cte_defs, list):
                    for cte_def in cte_defs:
                        cte_list.append(self.build_cte_definition(cte_def))
                else:
                    cte_list.append(self.build_cte_definition(cte_defs))

        statement = None
        if hasattr(ctx, 'selectStatement') and ctx.selectStatement():
            statement = self.build_select(ctx.selectStatement())
        elif hasattr(ctx, 'insertStatement') and ctx.insertStatement():
            statement = self.build_insert(ctx.insertStatement())
        elif hasattr(ctx, 'updateStatement') and ctx.updateStatement():
            statement = self.build_update(ctx.updateStatement())
        elif hasattr(ctx, 'deleteStatement') and ctx.deleteStatement():
            statement = self.build_delete(ctx.deleteStatement())

        return CTEStatementNode(
            keywordWith="WITH",
            cteList=cte_list,
            statement=statement
        )

    def build_cte_definition(self, ctx):
        from Ast.statement_nodes import CTEDefinitionNode

        name = None
        if hasattr(ctx, 'identifier') and ctx.identifier():
            identifiers = ctx.identifier()
            if isinstance(identifiers, list) and len(identifiers) > 0:
                name = identifiers[0].getText()
            else:
                name = identifiers.getText()

        columns = None
        if hasattr(ctx, 'columnList') and ctx.columnList():
            column_list = ctx.columnList()
            if hasattr(column_list, 'columnName'):
                column_names = column_list.columnName()
                if isinstance(column_names, list):
                    columns = [col.getText() for col in column_names]
                else:
                    columns = [column_names.getText()]

        select_statement = None
        if hasattr(ctx, 'selectStatement') and ctx.selectStatement():
            select_statement = self.build_select(ctx.selectStatement())

        return CTEDefinitionNode(
            name=name,
            columns=columns,
            selectStatement=select_statement
        )

    def build_drop(self, ctx):
        if hasattr(ctx, 'TABLE') and ctx.TABLE():
            return self.build_drop_table(ctx)
        elif hasattr(ctx, 'CONSTRAINT') and ctx.CONSTRAINT():
            return self.build_drop_constraint(ctx)
        elif hasattr(ctx, 'INDEX') and ctx.INDEX():
            return self.build_drop_index(ctx)
        elif hasattr(ctx, 'VIEW') and ctx.VIEW():
            return self.build_drop_view(ctx)
        elif hasattr(ctx, 'PROCEDURE') and ctx.PROCEDURE():
            return self.build_drop_procedure(ctx)

    def build_drop_table(self, ctx):
        from Ast.statement_nodes import DropTableStatementNode

        keywordIf = "IF" if hasattr(ctx, 'IF') and ctx.IF() else None
        keywordExists = "EXISTS" if hasattr(
            ctx, 'EXISTS') and ctx.EXISTS() else None
        tableName = self.expr_builder.build_table_name(ctx.tableName())

        return DropTableStatementNode(
            keywordDrop="DROP",
            keywordTable="TABLE",
            keywordIf=keywordIf,
            keywordExists=keywordExists,
            tableName=tableName
        )

    def build_drop_constraint(self, ctx):
        from Ast.statement_nodes import DropConstraintStatementNode

        keywordIf = "IF" if hasattr(ctx, 'IF') and ctx.IF() else None
        keywordExists = "EXISTS" if hasattr(
            ctx, 'EXISTS') and ctx.EXISTS() else None

        identifiers = ctx.identifier()
        if isinstance(identifiers, list) and len(identifiers) > 0:
            constraintName = identifiers[0].getText()
        else:
            constraintName = identifiers.getText()

        return DropConstraintStatementNode(
            keywordDrop="DROP",
            keywordConstraint="CONSTRAINT",
            keywordIf=keywordIf,
            keywordExists=keywordExists,
            constraintName=constraintName
        )

    def build_drop_index(self, ctx):
        from Ast.statement_nodes import DropIndexStatementNode

        keywordIf = "IF" if hasattr(ctx, 'IF') and ctx.IF() else None
        keywordExists = "EXISTS" if hasattr(
            ctx, 'EXISTS') and ctx.EXISTS() else None

        identifiers = ctx.identifier()
        if isinstance(identifiers, list):
            indexName = identifiers[0].getText()
        else:
            indexName = identifiers.getText()

        tableName = None
        if hasattr(ctx, 'tableName') and ctx.tableName():
            tableName = self.expr_builder.build_table_name(ctx.tableName())

        return DropIndexStatementNode(
            keywordDrop="DROP",
            keywordIndex="INDEX",
            keywordIf=keywordIf,
            keywordExists=keywordExists,
            indexName=indexName,
            tableName=tableName
        )

    def build_drop_view(self, ctx):
        from Ast.statement_nodes import DropViewStatementNode

        keywordIf = "IF" if hasattr(ctx, 'IF') and ctx.IF() else None
        keywordExists = "EXISTS" if hasattr(
            ctx, 'EXISTS') and ctx.EXISTS() else None

        identifiers = ctx.identifier()
        if isinstance(identifiers, list) and len(identifiers) > 0:
            viewName = identifiers[0].getText()
        else:
            viewName = identifiers.getText()

        return DropViewStatementNode(
            keywordDrop="DROP",
            keywordView="VIEW",
            keywordIf=keywordIf,
            keywordExists=keywordExists,
            viewName=viewName
        )

    def build_drop_procedure(self, ctx):
        from Ast.statement_nodes import DropProcedureStatementNode

        keywordIf = "IF" if hasattr(ctx, 'IF') and ctx.IF() else None
        keywordExists = "EXISTS" if hasattr(
            ctx, 'EXISTS') and ctx.EXISTS() else None

        identifiers = ctx.identifier()
        if isinstance(identifiers, list) and len(identifiers) > 0:
            procedureName = identifiers[0].getText()
        else:
            procedureName = identifiers.getText()

        return DropProcedureStatementNode(
            keywordDrop="DROP",
            keywordProcedure="PROCEDURE",
            keywordIf=keywordIf,
            keywordExists=keywordExists,
            procedureName=procedureName
        )

    def build_use(self, ctx):
        from Ast.statement_nodes import UseStatementNode

        identifiers = ctx.identifier()
        if isinstance(identifiers, list) and len(identifiers) > 0:
            databaseName = identifiers[0].getText()
        else:
            databaseName = identifiers.getText()

        return UseStatementNode(
            keywordUse="USE",
            databaseName=databaseName
        )

    def build_cursor_statement(self, ctx):
        if hasattr(ctx, 'declareCursorStatement') and ctx.declareCursorStatement():
            return self.build_declare_cursor(ctx.declareCursorStatement())
        elif hasattr(ctx, 'openCursorStatement') and ctx.openCursorStatement():
            return self.build_open_cursor(ctx.openCursorStatement())
        elif hasattr(ctx, 'fetchCursorStatement') and ctx.fetchCursorStatement():
            return self.build_fetch_cursor(ctx.fetchCursorStatement())
        elif hasattr(ctx, 'closeCursorStatement') and ctx.closeCursorStatement():
            return self.build_close_cursor(ctx.closeCursorStatement())
        elif hasattr(ctx, 'deallocateCursorStatement') and ctx.deallocateCursorStatement():
            return self.build_deallocate_cursor(ctx.deallocateCursorStatement())

    def build_declare_cursor(self, ctx):
        from Ast.statement_nodes import DeclareCursorStatementNode

        identifiers = ctx.identifier()
        if isinstance(identifiers, list):
            cursorName = identifiers[0].getText()
        else:
            cursorName = identifiers.getText()

        options = []
        if hasattr(ctx, 'cursorOptions') and ctx.cursorOptions():
            option_contexts = ctx.cursorOptions()
            if isinstance(option_contexts, list):
                for opt in option_contexts:
                    options.append(opt.getText())
            else:
                options.append(option_contexts.getText())

        selectStatement = None
        if hasattr(ctx, 'selectStatement') and ctx.selectStatement():
            selectStatement = self.build_select(ctx.selectStatement())

        return DeclareCursorStatementNode(
            keywordDeclare="DECLARE",
            cursorName=cursorName,
            keywordCursor="CURSOR",
            options=options if options else None,
            keywordFor="FOR",
            selectStatement=selectStatement
        )

    def build_open_cursor(self, ctx):
        from Ast.statement_nodes import OpenCursorStatementNode

        identifiers = ctx.identifier()
        if isinstance(identifiers, list) and len(identifiers) > 0:
            cursorName = identifiers[0].getText()
        else:
            cursorName = identifiers.getText()

        return OpenCursorStatementNode(
            keywordOpen="OPEN",
            cursorName=cursorName
        )

    def build_fetch_cursor(self, ctx):
        from Ast.statement_nodes import FetchCursorStatementNode

        fetchType = None
        if hasattr(ctx, 'NEXT') and ctx.NEXT():
            fetchType = "NEXT"
        elif hasattr(ctx, 'PRIOR') and ctx.PRIOR():
            fetchType = "PRIOR"
        elif hasattr(ctx, 'FIRST') and ctx.FIRST():
            fetchType = "FIRST"
        elif hasattr(ctx, 'LAST') and ctx.LAST():
            fetchType = "LAST"
        elif hasattr(ctx, 'ABSOLUTE') and ctx.ABSOLUTE():
            fetchType = "ABSOLUTE"
        elif hasattr(ctx, 'RELATIVE') and ctx.RELATIVE():
            fetchType = "RELATIVE"

        expression = None
        if hasattr(ctx, 'expression') and ctx.expression():
            expression = self.expr_builder.build_expression(ctx.expression())

        identifiers = ctx.identifier()
        if isinstance(identifiers, list) and len(identifiers) > 0:
            cursorName = identifiers[0].getText()
        else:
            cursorName = identifiers.getText()

        keywordInto = "INTO" if hasattr(ctx, 'INTO') and ctx.INTO() else None
        variables = None
        if hasattr(ctx, 'variableList') and ctx.variableList():
            var_list = ctx.variableList()
            if hasattr(var_list, 'VARIABLE'):
                vars = var_list.VARIABLE()
                if isinstance(vars, list):
                    variables = [v.getText() for v in vars]
                else:
                    variables = [vars.getText()]

        return FetchCursorStatementNode(
            keywordFetch="FETCH",
            fetchType=fetchType,
            expression=expression,
            keywordFrom="FROM",
            cursorName=cursorName,
            keywordInto=keywordInto,
            variables=variables
        )

    def build_close_cursor(self, ctx):
        from Ast.statement_nodes import CloseCursorStatementNode

        identifiers = ctx.identifier()
        if isinstance(identifiers, list) and len(identifiers) > 0:
            cursorName = identifiers[0].getText()
        else:
            cursorName = identifiers.getText()

        return CloseCursorStatementNode(
            keywordClose="CLOSE",
            cursorName=cursorName
        )

    def build_deallocate_cursor(self, ctx):
        from Ast.statement_nodes import DeallocateCursorStatementNode

        identifiers = ctx.identifier()
        if isinstance(identifiers, list) and len(identifiers) > 0:
            cursorName = identifiers[0].getText()
        else:
            cursorName = identifiers.getText()

        return DeallocateCursorStatementNode(
            keywordDeallocate="DEALLOCATE",
            cursorName=cursorName
        )

    def build_go(self, ctx):
        from Ast.statement_nodes import GoStatementNode
        return GoStatementNode(keywordGo="GO")

    def build_truncate(self, ctx):
        from Ast.statement_nodes import TruncateStatementNode
        tableName = self.expr_builder.build_table_name(ctx.tableName())
        return TruncateStatementNode(
            keywordTruncate="TRUNCATE",
            keywordTable="TABLE",
            tableName=tableName
        )

    def build_create_table(self, ctx):
        from Ast.statement_nodes import CreateTableStatementNode
        tableName = self.expr_builder.build_table_name(ctx.tableName())
        columns = self.build_column_definition_list(ctx.columnDefinitionList())

        return CreateTableStatementNode(
            table_name=tableName,
            columns=columns,
            keywordCreate="CREATE",
            keywordTable="TABLE"
        )

    def build_column_definition_list(self, ctx):
        columns = []
        column_defs = ctx.columnDefinition()
        if isinstance(column_defs, list):
            for column in column_defs:
                clmn = self.build_column_definition(column)
                if clmn is not None:
                    columns.append(clmn)
        else:
            clmn = self.build_column_definition(column_defs)
            if clmn is not None:
                columns.append(clmn)
        return columns

    def build_column_definition(self, ctx):
        from Ast.statement_nodes import ColumnDefinitionNode
        columnName = ctx.columnName().getText()
        dataType = ctx.dataType().getText()
        columnConstraints = []
        if hasattr(ctx, 'constraint') and ctx.constraint():
            constraints = ctx.constraint()
            if isinstance(constraints, list):
                for constraint in constraints:
                    clmn = self.build_column_constraint(constraint)
                    if clmn is not None:
                        columnConstraints.append(clmn)
            else:
                clmn = self.build_column_constraint(constraints)
                if clmn is not None:
                    columnConstraints.append(clmn)

        return ColumnDefinitionNode(
            column_name=columnName,
            data_type=dataType,
            constraints=columnConstraints if columnConstraints else None
        )

    def build_column_constraint(self, ctx):
        from Ast.statement_nodes import columnConstraintsNode
        text = ctx.getText()
        return columnConstraintsNode(keyword1=text, keyword2=None)

    def build_alter_table(self, ctx):
        from Ast.statement_nodes import AlterTableStatementNode
        tableName = self.expr_builder.build_table_name(ctx.tableName())
        addColumnClause = self.build_add_column_clause(ctx.addColumnClause()) if hasattr(
            ctx, 'addColumnClause') and ctx.addColumnClause() else None
        dropConstraintClause = self.build_drop_constraint_clause(
            ctx.dropConstraintClause()) if hasattr(ctx, 'dropConstraintClause') and ctx.dropConstraintClause() else None

        return AlterTableStatementNode(
            keywordAlter="ALTER",
            keywordTable="TABLE",
            table_name=tableName,
            addColumnClause=addColumnClause,
            dropConstraintClause=dropConstraintClause
        )

    def build_add_column_clause(self, ctx):
        from Ast.statement_nodes import AddColumnClauseNode
        columnDefinition = self.build_column_definition(ctx.columnDefinition())
        return AddColumnClauseNode(keywordAdd="ADD", columnDefinition=columnDefinition)

    def build_drop_constraint_clause(self, ctx):
        from Ast.statement_nodes import DropConstraintClauseNode
        identifiers = ctx.identifier()
        if isinstance(identifiers, list) and len(identifiers) > 0:
            constraintName = identifiers[0].getText()
        else:
            constraintName = identifiers.getText()
        return DropConstraintClauseNode(
            keywordDrop="DROP",
            keywordConstrain="CONSTRAINT",
            constraintName=constraintName
        )

    def build_delete(self, ctx):
        from Ast.statement_nodes import DeleteStatementNode
        tableName = self.expr_builder.build_table_name(
            ctx.tableName()) if ctx.tableName() else None
        whereClause = self.build_where_clause(ctx.whereClause()) if hasattr(
            ctx, 'whereClause') and ctx.whereClause() else None

        if not whereClause and hasattr(ctx, 'condition') and ctx.condition():
            from Ast.statement_nodes import WhereClauseNode
            condition = self.cond_builder.build_condition(ctx.condition())
            whereClause = WhereClauseNode(
                keywordWhere="WHERE", condition=condition)

        return DeleteStatementNode(
            keywordDelete="DELETE",
            tableName=tableName,
            fromClause=None,
            whereClause=whereClause
        )

    def build_update(self, ctx):
        from Ast.statement_nodes import UpdateStatementNode
        tableName = self.expr_builder.build_table_name(
            ctx.tableName()) if ctx.tableName() else None

        assignmentList = []
        if hasattr(ctx, 'assignments') and ctx.assignments():
            assignmentList = self.build_assignment_list(ctx.assignments())
        elif hasattr(ctx, 'assignment'):
            assignments = ctx.assignment()
            if isinstance(assignments, list):
                for assignment in assignments:
                    assnment = self.build_assignment(assignment)
                    if assnment is not None:
                        assignmentList.append(assnment)
            elif assignments:
                assnment = self.build_assignment(assignments)
                if assnment is not None:
                    assignmentList.append(assnment)

        whereClause = None
        if hasattr(ctx, 'condition') and ctx.condition():
            from Ast.statement_nodes import WhereClauseNode
            condition = self.cond_builder.build_condition(ctx.condition())
            whereClause = WhereClauseNode(
                keywordWhere="WHERE", condition=condition)

        return UpdateStatementNode(
            keywordUpdate="UPDATE",
            tableName=tableName,
            assignmentList=assignmentList,
            whereClause=whereClause
        )

    def build_assignment_list(self, ctx):
        assignments = []
        assignment_contexts = ctx.assignment()
        if isinstance(assignment_contexts, list):
            for assignment in assignment_contexts:
                assnment = self.build_assignment(assignment)
                if assnment is not None:
                    assignments.append(assnment)
        else:
            assnment = self.build_assignment(assignment_contexts)
            if assnment is not None:
                assignments.append(assnment)
        return assignments

    def build_assignment(self, ctx):
        from Ast.statement_nodes import AssignmentNode
        columnName = ctx.columnName().getText() if hasattr(
            ctx, 'columnName') and ctx.columnName() else None

        expression = None
        if hasattr(ctx, 'expression') and ctx.expression():
            expression = self.expr_builder.build_expression(ctx.expression())

        return AssignmentNode(columnName=columnName, expression=expression)

    def build_where_clause(self, ctx):
        from Ast.statement_nodes import WhereClauseNode
        condition = self.cond_builder.build_condition(
            ctx.condition()) if ctx.condition() else None
        return WhereClauseNode(keywordWhere="WHERE", condition=condition)

    def build_select(self, ctx):
        from Ast.statement_nodes import (
            SelectStatementNode,
            FromClauseNode,
            OrderByClauseNode,
            GroupByClauseNode,
            HavingClauseNode
        )

        selectList = self.build_select_list(ctx.selectList())

        fromClause = None
        if hasattr(ctx, 'tableList') and ctx.tableList():
            fromClause = self.build_from_clause(ctx.tableList())

        whereClause = None
        if hasattr(ctx, 'condition') and ctx.condition():
            conditions = ctx.condition()
            condition_list = conditions if isinstance(
                conditions, list) else [conditions]
            if len(condition_list) > 0:
                from Ast.statement_nodes import WhereClauseNode
                condition = self.cond_builder.build_condition(
                    condition_list[0])
                whereClause = WhereClauseNode(
                    keywordWhere="WHERE", condition=condition)

        groupByClause = None
        if hasattr(ctx, 'expressionList') and ctx.expressionList():
            expr_lists = ctx.expressionList()
            if isinstance(expr_lists, list) and len(expr_lists) > 0:
                groupByClause = self.build_group_by_clause(expr_lists[0])
            elif not isinstance(expr_lists, list):
                groupByClause = self.build_group_by_clause(expr_lists)

        havingClause = None
        if hasattr(ctx, 'condition') and ctx.condition():
            conditions = ctx.condition()
            condition_list = conditions if isinstance(
                conditions, list) else [conditions]
            if len(condition_list) > 1 and groupByClause:
                havingClause = self.build_having_clause(condition_list[1])

        orderByClause = None
        if hasattr(ctx, 'orderByList') and ctx.orderByList():
            orderByClause = self.build_order_by_clause(ctx.orderByList())

        return SelectStatementNode(
            keywordSelect="SELECT",
            selectList=selectList,
            orderByClause=orderByClause,
            whereClause=whereClause,
            fromClause=fromClause,
            groupByClause=groupByClause,
            havingClause=havingClause
        )

    def build_group_by_clause(self, ctx):
        from Ast.statement_nodes import GroupByClauseNode
        expressions = self.expr_builder.build_expression_list(ctx)
        return GroupByClauseNode(
            keywordGroup="GROUP",
            keywordBy="BY",
            expressions=expressions
        )

    def build_having_clause(self, ctx):
        from Ast.statement_nodes import HavingClauseNode
        condition = self.cond_builder.build_condition(ctx)
        return HavingClauseNode(
            keywordHaving="HAVING",
            condition=condition
        )

    def build_from_clause(self, ctx):
        from Ast.statement_nodes import FromClauseNode
        tableSources = []

        if hasattr(ctx, 'tableRef') and ctx.tableRef():
            table_refs = ctx.tableRef()

            if isinstance(table_refs, list):
                if len(table_refs) > 0:
                    table_source = self.build_table_source(table_refs[0])
                    if table_source:
                        tableSources.append(table_source)
            else:
                table_source = self.build_table_source(table_refs)
                if table_source:
                    tableSources.append(table_source)

        if hasattr(ctx, 'joinClause') and ctx.joinClause():
            join_clauses = ctx.joinClause()

            if isinstance(join_clauses, list):
                for joinClause in join_clauses:
                    joined_table = self.build_join_clause(joinClause)
                    if joined_table:
                        tableSources.append(joined_table)
            else:
                joined_table = self.build_join_clause(join_clauses)
                if joined_table:
                    tableSources.append(joined_table)

        return FromClauseNode(keywordFrom="FROM", tableSource=tableSources)

    def build_join_clause(self, ctx):
        from Ast.statement_nodes import TableSourceNode

        join_type = "JOIN"
        if hasattr(ctx, 'joinType') and ctx.joinType():
            join_type_ctx = ctx.joinType()
            join_type = join_type_ctx.getText().upper()

        table_name = None
        alias = None
        if hasattr(ctx, 'tableRef') and ctx.tableRef():
            table_ref = ctx.tableRef()

            if hasattr(table_ref, 'tableName') and table_ref.tableName():
                table_name = self.expr_builder.build_table_name(
                    table_ref.tableName())

            if hasattr(table_ref, 'identifier') and table_ref.identifier():
                identifiers = table_ref.identifier()
                if isinstance(identifiers, list) and len(identifiers) > 0:
                    alias = identifiers[-1].getText()
                elif not isinstance(identifiers, list):
                    alias = identifiers.getText()

        join_condition = None
        if hasattr(ctx, 'condition') and ctx.condition():
            join_condition = self.cond_builder.build_condition(ctx.condition())

        return TableSourceNode(
            tableName=table_name,
            keyword=join_type,
            identifier=alias,
            joinCondition=join_condition
        )

    def build_table_source(self, ctx):
        from Ast.statement_nodes import TableSourceNode

        if hasattr(ctx, 'selectStatement') and ctx.selectStatement():
            select_stmt = self.build_select(ctx.selectStatement())
            alias = None
            if hasattr(ctx, 'identifier') and ctx.identifier():
                identifiers = ctx.identifier()
                if isinstance(identifiers, list) and len(identifiers) > 0:
                    alias = identifiers[-1].getText()
                elif not isinstance(identifiers, list):
                    alias = identifiers.getText()

            from dataclasses import dataclass

            @dataclass
            class SubqueryTableNode:
                type: str
                selectStatement: object

            subquery_node = SubqueryTableNode(
                type="Subquery",
                selectStatement=select_stmt
            )

            return
