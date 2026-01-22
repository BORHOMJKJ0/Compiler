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
            return SemicolonNode()

        if hasattr(ctx, 'cteStatement') and ctx.cteStatement():
            return self.build_cte(ctx.cteStatement())

        if hasattr(ctx, 'ddlStatement') and ctx.ddlStatement():
            ddl_ctx = ctx.ddlStatement()

            if hasattr(ddl_ctx, 'createTableStatement') and ddl_ctx.createTableStatement():
                return self.build_create_table(ddl_ctx.createTableStatement())

            if hasattr(ddl_ctx, 'alterTableStatement') and ddl_ctx.alterTableStatement():
                return self.build_alter_table(ddl_ctx.alterTableStatement())

            if hasattr(ddl_ctx, 'dropStatement') and ddl_ctx.dropStatement():
                return self.build_drop(ddl_ctx.dropStatement())

            if hasattr(ddl_ctx, 'truncateStatement') and ddl_ctx.truncateStatement():
                return self.build_truncate(ddl_ctx.truncateStatement())

        if hasattr(ctx, 'dmlStatement') and ctx.dmlStatement():
            dml_ctx = ctx.dmlStatement()

            if hasattr(dml_ctx, 'selectStatement') and dml_ctx.selectStatement():
                return self.build_select(dml_ctx.selectStatement())

            if hasattr(dml_ctx, 'insertStatement') and dml_ctx.insertStatement():
                return self.build_insert(dml_ctx.insertStatement())

            if hasattr(dml_ctx, 'updateStatement') and dml_ctx.updateStatement():
                return self.build_update(dml_ctx.updateStatement())

            if hasattr(dml_ctx, 'deleteStatement') and dml_ctx.deleteStatement():
                return self.build_delete(dml_ctx.deleteStatement())

        if hasattr(ctx, 'selectStatement') and ctx.selectStatement():
            return self.build_select(ctx.selectStatement())

        if hasattr(ctx, 'insertStatement') and ctx.insertStatement():
            return self.build_insert(ctx.insertStatement())

        if hasattr(ctx, 'updateStatement') and ctx.updateStatement():
            return self.build_update(ctx.updateStatement())

        if hasattr(ctx, 'deleteStatement') and ctx.deleteStatement():
            return self.build_delete(ctx.deleteStatement())

        if hasattr(ctx, 'createTableStatement') and ctx.createTableStatement():
            return self.build_create_table(ctx.createTableStatement())

        if hasattr(ctx, 'alterTableStatement') and ctx.alterTableStatement():
            return self.build_alter_table(ctx.alterTableStatement())

        if hasattr(ctx, 'dropStatement') and ctx.dropStatement():
            return self.build_drop(ctx.dropStatement())

        if hasattr(ctx, 'truncateStatement') and ctx.truncateStatement():
            return self.build_truncate(ctx.truncateStatement())

        if hasattr(ctx, 'declareStatement') and ctx.declareStatement():
            return self.build_declare(ctx.declareStatement())

        if hasattr(ctx, 'setStatement') and ctx.setStatement():
            return self.build_set(ctx.setStatement())

        if hasattr(ctx, 'execStatement') and ctx.execStatement():
            return self.build_exec(ctx.execStatement())

        if hasattr(ctx, 'ifStatement') and ctx.ifStatement():
            return self.build_if(ctx.ifStatement())

        if hasattr(ctx, 'blockStatement') and ctx.blockStatement():
            return self.build_block(ctx.blockStatement())

        if hasattr(ctx, 'tryCatchStatement') and ctx.tryCatchStatement():
            return self.build_try_catch(ctx.tryCatchStatement())

        if hasattr(ctx, 'useStatement') and ctx.useStatement():
            return self.build_use(ctx.useStatement())

        if hasattr(ctx, 'cursorStatement') and ctx.cursorStatement():
            return self.build_cursor_statement(ctx.cursorStatement())

        if hasattr(ctx, 'GO') and ctx.GO():
            return self.build_go(ctx)

        if hasattr(ctx, 'tableName') and ctx.tableName():
            from Ast.statement_nodes import TableSourceNode

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

        return None

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
        try:
            select_item_contexts = ctx.selectItem()
            if isinstance(select_item_contexts, list):
                for selectItem in select_item_contexts:
                    try:
                        item = self.build_select_item(selectItem)
                        if item is not None:
                            selectItems.append(item)
                    except:
                        continue
            else:
                try:
                    item = self.build_select_item(select_item_contexts)
                    if item is not None:
                        selectItems.append(item)
                except:
                    pass
        except:
            pass

        return selectItems

    def build_select_item(self, ctx):
        from Ast.statement_nodes import SelectItemNode
        from Ast.expression_nodes import LiteralExpressionNode

        try:
            expression = None
            keywordAs = None
            identifier = None

            if hasattr(ctx, 'expression') and ctx.expression():
                try:
                    expression = self.expr_builder.build_expression(
                        ctx.expression())
                except:
                    expression = LiteralExpressionNode(
                        value="NULL", literal_type="KEYWORD")
            elif hasattr(ctx, 'OPERATOR') and ctx.OPERATOR():
                op_text = ctx.OPERATOR().getText()
                if op_text == '*':
                    expression = LiteralExpressionNode(
                        value='*', literal_type='OPERATOR')
                else:
                    try:
                        expression = self.expr_builder.build_expression(ctx)
                    except:
                        expression = LiteralExpressionNode(
                            value="NULL", literal_type="KEYWORD")

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
        except:
            return SelectItemNode(
                expression=LiteralExpressionNode(
                    value="NULL", literal_type="KEYWORD"),
                keywordAs=None,
                identifier=None
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
        keywordIf = None
        keywordExists = None
        tableName = None

        if hasattr(ctx, 'IF') and ctx.IF():
            keywordIf = "IF"

        if hasattr(ctx, 'EXISTS') and ctx.EXISTS():
            keywordExists = "EXISTS"

        if hasattr(ctx, 'tableName') and ctx.tableName():
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
        keywordIf = None
        keywordExists = None
        constraintName = None

        if hasattr(ctx, 'IF') and ctx.IF():
            keywordIf = "IF"

        if hasattr(ctx, 'EXISTS') and ctx.EXISTS():
            keywordExists = "EXISTS"

        if hasattr(ctx, 'identifier') and ctx.identifier():
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
        keywordIf = None
        keywordExists = None
        indexName = None
        tableName = None

        if hasattr(ctx, 'IF') and ctx.IF():
            keywordIf = "IF"

        if hasattr(ctx, 'EXISTS') and ctx.EXISTS():
            keywordExists = "EXISTS"

        if hasattr(ctx, 'identifier') and ctx.identifier():
            identifiers = ctx.identifier()
            if isinstance(identifiers, list):
                indexName = identifiers[0].getText()
            else:
                indexName = identifiers.getText()

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
        keywordIf = None
        keywordExists = None
        viewName = None

        if hasattr(ctx, 'IF') and ctx.IF():
            keywordIf = "IF"

        if hasattr(ctx, 'EXISTS') and ctx.EXISTS():
            keywordExists = "EXISTS"

        if hasattr(ctx, 'identifier') and ctx.identifier():
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
        keywordIf = None
        keywordExists = None
        procedureName = None

        if hasattr(ctx, 'IF') and ctx.IF():
            keywordIf = "IF"

        if hasattr(ctx, 'EXISTS') and ctx.EXISTS():
            keywordExists = "EXISTS"

        if hasattr(ctx, 'identifier') and ctx.identifier():
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
        databaseName = None

        if hasattr(ctx, 'identifier') and ctx.identifier():
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
        tableName = None

        if hasattr(ctx, 'tableName') and ctx.tableName():
            tableName = self.expr_builder.build_table_name(ctx.tableName())

        return TruncateStatementNode(
            keywordTruncate="TRUNCATE",
            keywordTable="TABLE",
            tableName=tableName
        )

    def build_create_table(self, ctx):
        from Ast.statement_nodes import CreateTableStatementNode
        tableName = self.expr_builder.build_table_name(ctx.tableName())
        columns = []

        if hasattr(ctx, 'columnDefinitionList') and ctx.columnDefinitionList():
            columns = self.build_column_definition_list(
                ctx.columnDefinitionList())

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
        tableName = None
        addColumnClause = None
        dropConstraintClause = None

        if hasattr(ctx, 'tableName') and ctx.tableName():
            tableName = self.expr_builder.build_table_name(ctx.tableName())

        if hasattr(ctx, 'addColumnClause') and ctx.addColumnClause():
            addColumnClause = self.build_add_column_clause(
                ctx.addColumnClause())

        if hasattr(ctx, 'dropConstraintClause') and ctx.dropConstraintClause():
            dropConstraintClause = self.build_drop_constraint_clause(
                ctx.dropConstraintClause())

        return AlterTableStatementNode(
            keywordAlter="ALTER",
            keywordTable="TABLE",
            table_name=tableName,
            addColumnClause=addColumnClause,
            dropConstraintClause=dropConstraintClause
        )

    def build_add_column_clause(self, ctx):
        from Ast.statement_nodes import AddColumnClauseNode
        columnDefinition = None

        if hasattr(ctx, 'columnDefinition') and ctx.columnDefinition():
            columnDefinition = self.build_column_definition(
                ctx.columnDefinition())

        return AddColumnClauseNode(keywordAdd="ADD", columnDefinition=columnDefinition)

    def build_drop_constraint_clause(self, ctx):
        from Ast.statement_nodes import DropConstraintClauseNode
        constraintName = None

        if hasattr(ctx, 'identifier') and ctx.identifier():
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
        tableName = None
        whereClause = None

        if hasattr(ctx, 'tableName') and ctx.tableName():
            tableName = self.expr_builder.build_table_name(ctx.tableName())

        if hasattr(ctx, 'whereClause') and ctx.whereClause():
            whereClause = self.build_where_clause(ctx.whereClause())
        elif hasattr(ctx, 'condition') and ctx.condition():
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
        tableName = None
        assignmentList = []
        whereClause = None

        if hasattr(ctx, 'tableName') and ctx.tableName():
            tableName = self.expr_builder.build_table_name(ctx.tableName())

        if hasattr(ctx, 'assignments') and ctx.assignments():
            assignmentList = self.build_assignment_list(ctx.assignments())
        elif hasattr(ctx, 'assignment') and ctx.assignment():
            assignments = ctx.assignment()
            if isinstance(assignments, list):
                for assignment in assignments:
                    assnment = self.build_assignment(assignment)
                    if assnment is not None:
                        assignmentList.append(assnment)
            else:
                assnment = self.build_assignment(assignments)
                if assnment is not None:
                    assignmentList.append(assnment)

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
        columnName = None
        expression = None

        if hasattr(ctx, 'columnName') and ctx.columnName():
            columnName = ctx.columnName().getText()

        if hasattr(ctx, 'expression') and ctx.expression():
            expression = self.expr_builder.build_expression(ctx.expression())

        return AssignmentNode(columnName=columnName, expression=expression)

    def build_where_clause(self, ctx):
        from Ast.statement_nodes import WhereClauseNode
        condition = None

        if hasattr(ctx, 'condition') and ctx.condition():
            condition = self.cond_builder.build_condition(ctx.condition())

        return WhereClauseNode(keywordWhere="WHERE", condition=condition)

    def build_select(self, ctx):
        from Ast.statement_nodes import (
            SelectStatementNode,
            FromClauseNode,
            OrderByClauseNode,
            GroupByClauseNode,
            HavingClauseNode,
            SelectItemNode
        )
        from Ast.expression_nodes import LiteralExpressionNode

        try:
            if not hasattr(ctx, 'selectList') or not ctx.selectList():
                default_item = SelectItemNode(
                    expression=LiteralExpressionNode(
                        value="1", literal_type="NUMBER"),
                    keywordAs=None,
                    identifier=None
                )
                return SelectStatementNode(
                    keywordSelect="SELECT",
                    selectList=[default_item],
                    orderByClause=None,
                    whereClause=None,
                    fromClause=None,
                    groupByClause=None,
                    havingClause=None
                )

            selectList = self.build_select_list(ctx.selectList())

            if not selectList:
                default_item = SelectItemNode(
                    expression=LiteralExpressionNode(
                        value="1", literal_type="NUMBER"),
                    keywordAs=None,
                    identifier=None
                )
                selectList = [default_item]

            fromClause = None
            if hasattr(ctx, 'tableList') and ctx.tableList():
                try:
                    fromClause = self.build_from_clause(ctx.tableList())
                except:
                    pass

            whereClause = None
            if hasattr(ctx, 'condition') and ctx.condition():
                conditions = ctx.condition()
                condition_list = conditions if isinstance(
                    conditions, list) else [conditions]
                if len(condition_list) > 0:
                    from Ast.statement_nodes import WhereClauseNode
                    try:
                        condition = self.cond_builder.build_condition(
                            condition_list[0])
                        whereClause = WhereClauseNode(
                            keywordWhere="WHERE", condition=condition)
                    except:
                        pass

            groupByClause = None
            if hasattr(ctx, 'expressionList') and ctx.expressionList():
                expr_lists = ctx.expressionList()
                if isinstance(expr_lists, list) and len(expr_lists) > 0:
                    try:
                        groupByClause = self.build_group_by_clause(
                            expr_lists[0])
                    except:
                        pass
                elif not isinstance(expr_lists, list):
                    try:
                        groupByClause = self.build_group_by_clause(expr_lists)
                    except:
                        pass

            havingClause = None
            if hasattr(ctx, 'condition') and ctx.condition():
                conditions = ctx.condition()
                condition_list = conditions if isinstance(
                    conditions, list) else [conditions]
                if len(condition_list) > 1 and groupByClause:
                    try:
                        havingClause = self.build_having_clause(
                            condition_list[1])
                    except:
                        pass

            orderByClause = None
            if hasattr(ctx, 'orderByList') and ctx.orderByList():
                try:
                    orderByClause = self.build_order_by_clause(
                        ctx.orderByList())
                except:
                    pass

            return SelectStatementNode(
                keywordSelect="SELECT",
                selectList=selectList,
                orderByClause=orderByClause,
                whereClause=whereClause,
                fromClause=fromClause,
                groupByClause=groupByClause,
                havingClause=havingClause
            )
        except Exception as e:
            from Ast.expression_nodes import LiteralExpressionNode
            default_item = SelectItemNode(
                expression=LiteralExpressionNode(
                    value="1", literal_type="NUMBER"),
                keywordAs=None,
                identifier=None
            )
            return SelectStatementNode(
                keywordSelect="SELECT",
                selectList=[default_item],
                orderByClause=None,
                whereClause=None,
                fromClause=None,
                groupByClause=None,
                havingClause=None
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

        try:
            if hasattr(ctx, 'tableRef') and ctx.tableRef():
                table_refs = ctx.tableRef()

                if isinstance(table_refs, list):
                    if len(table_refs) > 0:
                        try:
                            table_source = self.build_table_source(
                                table_refs[0])
                            if table_source:
                                tableSources.append(table_source)
                        except:
                            pass
                else:
                    try:
                        table_source = self.build_table_source(table_refs)
                        if table_source:
                            tableSources.append(table_source)
                    except:
                        pass

            if hasattr(ctx, 'joinClause') and ctx.joinClause():
                join_clauses = ctx.joinClause()

                if isinstance(join_clauses, list):
                    for joinClause in join_clauses:
                        try:
                            joined_table = self.build_join_clause(joinClause)
                            if joined_table:
                                tableSources.append(joined_table)
                        except:
                            continue
                else:
                    try:
                        joined_table = self.build_join_clause(join_clauses)
                        if joined_table:
                            tableSources.append(joined_table)
                    except:
                        pass
        except:
            pass

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
