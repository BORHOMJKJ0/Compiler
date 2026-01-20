from builders.expression_builder import ExpressionBuilder
from builders.condition_builder import ConditionBuilder


class StatementBuilder:
    def __init__(self):
        self.expr_builder = ExpressionBuilder()
        self.cond_builder = ConditionBuilder()

    def build_statement(self, ctx):
        if ctx.getText() == ';':
            from dataclasses import dataclass

            @dataclass
            class SemicolonNode:
                type: str = "Semicolon"
            return SemicolonNode()

        if hasattr(ctx, 'ddlStatement') and ctx.ddlStatement():
            ddl = ctx.ddlStatement()
            if hasattr(ddl, 'createTableStatement') and ddl.createTableStatement():
                return self.build_create_table(ddl.createTableStatement())
            elif hasattr(ddl, 'alterTableStatement') and ddl.alterTableStatement():
                return self.build_alter_table(ddl.alterTableStatement())

        elif hasattr(ctx, 'dmlStatement') and ctx.dmlStatement():
            dml = ctx.dmlStatement()
            if hasattr(dml, 'selectStatement') and ddl.selectStatement() if 'ddl' in locals() else dml.selectStatement():
                return self.build_select(dml.selectStatement())
            elif hasattr(dml, 'insertStatement') and dml.insertStatement():
                return self.build_insert(dml.insertStatement())
            elif hasattr(dml, 'updateStatement') and dml.updateStatement():
                return self.build_update(dml.updateStatement())
            elif hasattr(dml, 'deleteStatement') and dml.deleteStatement():
                return self.build_delete(dml.deleteStatement())

        elif hasattr(ctx, 'controlFlowStatement') and ctx.controlFlowStatement():
            cf = ctx.controlFlowStatement()
            if hasattr(cf, 'ifStatement') and cf.ifStatement():
                return self.build_if(cf.ifStatement())
            elif hasattr(cf, 'tryCatchStatement') and cf.tryCatchStatement():
                return self.build_try_catch(cf.tryCatchStatement())
            elif hasattr(cf, 'blockStatement') and cf.blockStatement():
                return self.build_block(cf.blockStatement())

        elif hasattr(ctx, 'variableStatement') and ctx.variableStatement():
            var = ctx.variableStatement()
            if hasattr(var, 'declareStatement') and var.declareStatement():
                return self.build_declare(var.declareStatement())
            elif hasattr(var, 'setStatement') and var.setStatement():
                return self.build_set(var.setStatement())

        elif hasattr(ctx, 'execStatement') and ctx.execStatement():
            return self.build_exec(ctx.execStatement())

        elif hasattr(ctx, 'blockStatement') and ctx.blockStatement():
            return self.build_block(ctx.blockStatement())

        elif hasattr(ctx, 'goStatement') and ctx.goStatement():
            return self.build_go(ctx.goStatement())

        return None

    def build_go(self, ctx):
        from Ast.statement_nodes import GoStatementNode
        return GoStatementNode(keywordGo="GO")

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
        for column in ctx.columnDefinition():
            clmn = self.build_column_definition(column)
            if clmn is not None:
                columns.append(clmn)
        return columns

    def build_column_definition(self, ctx):
        from Ast.statement_nodes import ColumnDefinitionNode
        columnName = ctx.columnName().getText()
        dataType = ctx.dataType().getText()
        columnConstraints = []
        if hasattr(ctx, 'constraint'):
            for constraint in ctx.constraint():
                clmn = self.build_column_constraint(constraint)
                if clmn is not None:
                    columnConstraints.append(clmn)

        return ColumnDefinitionNode(
            column_name=columnName,
            data_type=dataType,
            constraints=columnConstraints
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
        constraintName = ctx.identifier().getText()
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
        assignmentList = self.build_assignment_list(ctx.assignments()) if hasattr(
            ctx, 'assignments') and ctx.assignments() else []
        whereClause = self.build_where_clause(ctx.whereClause()) if hasattr(
            ctx, 'whereClause') and ctx.whereClause() else None
        return UpdateStatementNode(
            keywordUpdate="UPDATE",
            tableName=tableName,
            assignmentList=assignmentList,
            whereClause=whereClause
        )

    def build_assignment_list(self, ctx):
        assignments = []
        for assignment in ctx.assignment():
            assnment = self.build_assignment(assignment)
            if assnment is not None:
                assignments.append(assnment)
        return assignments

    def build_assignment(self, ctx):
        from Ast.statement_nodes import AssignmentNode
        columnName = ctx.columnName().getText()
        expression = self.expr_builder.build_expression(
            ctx.expression()) if ctx.expression() else None
        return AssignmentNode(columnName=columnName, expression=expression)

    def build_where_clause(self, ctx):
        from Ast.statement_nodes import WhereClauseNode
        condition = self.cond_builder.build_condition(
            ctx.condition()) if ctx.condition() else None
        return WhereClauseNode(keywordWhere="WHERE", condition=condition)

    def build_select(self, ctx):
        from Ast.statement_nodes import SelectStatementNode
        selectList = self.build_select_list(ctx.selectList())
        return SelectStatementNode(
            keywordSelect="SELECT",
            selectList=selectList,
            orderByClause=None,
            whereClause=None,
            fromClause=None
        )

    def build_select_list(self, ctx):
        selectItems = []
        for selectItem in ctx.selectItem():
            item = self.build_select_item(selectItem)
            if item is not None:
                selectItems.append(item)
        return selectItems

    def build_select_item(self, ctx):
        from Ast.statement_nodes import SelectItemNode
        expression = None
        if ctx.expression():
            expression = self.expr_builder.build_expression(ctx.expression())
        return SelectItemNode(
            expression=expression,
            keywordAs=None,
            identifier=None
        )

    def build_insert(self, ctx):
        from Ast.statement_nodes import InsertStatement
        tableName = self.expr_builder.build_table_name(ctx.tableName())
        return InsertStatement(
            keywordInsert="INSERT",
            tableName=tableName,
            keywordInto="INTO",
            insertColumns=None,
            insertValues=None,
            selectStatement=None,
            execStatement=None
        )

    def build_if(self, ctx):
        from Ast.statement_nodes import IfStatementNode
        keywordNot = "NOT" if "NOT" in ctx.getText().upper() else None
        keywordEXISTS = "EXISTS" if "EXISTS" in ctx.getText().upper() else None

        selectStatement = None
        if hasattr(ctx, 'selectStatement') and ctx.selectStatement():
            selectStatement = self.build_select(ctx.selectStatement())

        blockStatement = None
        if hasattr(ctx, 'blockStatement') and ctx.blockStatement():
            blockStatement = self.build_block(ctx.blockStatement())
        elif hasattr(ctx, 'statement') and ctx.statement():
            blockStatement = self.build_statement(ctx.statement())

        return IfStatementNode(
            keywordIf="IF",
            selectStatement=selectStatement,
            blockStatement=blockStatement,
            keywordNot=keywordNot,
            keywordEXISTS=keywordEXISTS
        )

    def build_block(self, ctx):
        from Ast.statement_nodes import BlockStatementNode
        statements = []
        if hasattr(ctx, 'statement'):
            for stmt_ctx in ctx.statement():
                stmt = self.build_statement(stmt_ctx)
                if stmt:
                    statements.append(stmt)

        return BlockStatementNode(
            keywordBegin="BEGIN",
            statementList=statements,
            keywordEnd="END"
        )

    def build_try_catch(self, ctx):
        from Ast.statement_nodes import tryCatchStatementNode

        try_statements = []
        if hasattr(ctx, 'statement'):
            for stmt_ctx in ctx.statement():
                stmt = self.build_statement(stmt_ctx)
                if stmt:
                    try_statements.append(stmt)

        return tryCatchStatementNode(
            keywordBeginForTry="BEGIN",
            keywordBeginTry="TRY",
            tryStatementList=try_statements,
            keywordEndForTry="END",
            keywordEndTry="TRY",
            keywordBeginForCatch="BEGIN",
            keywordBeginCatch="CATCH",
            catchStatementList=[],
            keywordEndForCatch="END",
            keywordEndCatch="CATCH"
        )

    def build_declare(self, ctx):
        from Ast.statement_nodes import declareStatementNode
        return declareStatementNode(
            keywordDeclare="DECLARE",
            variableName=ctx.VARIABLE().getText(),
            dataType=ctx.dataType().getText(),
            operator=None,
            expression=None
        )

    def build_set(self, ctx):
        from Ast.statement_nodes import setStatementNode
        variableName = ctx.VARIABLE().getText(
        ) if ctx.VARIABLE() else ctx.columnName().getText()
        expression = self.expr_builder.build_expression(ctx.expression()) if hasattr(
            ctx, 'expression') and ctx.expression() else None

        return setStatementNode(
            keywordSet="SET",
            variableName=variableName,
            operator="=",
            expression=expression
        )

    def build_exec(self, ctx):
        from Ast.statement_nodes import execStatementNode
        identifier = ctx.getChild(1).getText()
        return execStatementNode(
            keywordExec="EXEC",
            identifier=identifier,
            expressionList=None
        )
