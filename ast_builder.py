from MyParserVisitor import MyParserVisitor
from MyParser import MyParser
from ast_nodes import *


class AstBuilder(MyParserVisitor):

    def visitSqlScript(self, ctx: MyParser.SqlScriptContext):
        print('rech')
        statementList = self.visit(ctx.statementList())
        return statementList

    def visitStatementList(self, ctx: MyParser.StatementListContext):
        statments = []
        for statement in ctx.statement():
            stmt = self.visit(statement)
            if (stmt is not None):
                statments.append(stmt)

        return statments
    
    def visitStatement(self, ctx: MyParser.StatementContext):

        if ctx.createTableStatement():
            return self.visit(ctx.createTableStatement())
        elif ctx.alterTableStatement():
            return self.visit(ctx.alterTableStatement())
        elif ctx.updateStatement():
            return self.visit(ctx.updateStatement())
        elif ctx.declareStatement():
            return self.visit(ctx.declareStatement())
        elif ctx.setStatement():
            return self.visit(ctx.setStatement())
        elif ctx.execStatement():
            return self.visit(ctx.execStatement())
        elif ctx.deleteStatement():
            return self.visit(ctx.deleteStatement())
        elif ctx.insertStatement():
            return self.visit(ctx.insertStatement())
        elif ctx.ifStatement():
            return self.visit(ctx.ifStatement())
        elif ctx.tryCatchStatement():
            return self.visit(ctx.tryCatchStatement())
        elif ctx.goStatement():
            return self.visit(ctx.goStatement())
        elif ctx.blockStatement():
            return self.visit(ctx.blockStatement())
        elif ctx.selectStatement():
            return self.visit(ctx.selectStatement())
        else:
            return None

    def visitGoStatement(self, ctx: MyParser.GoStatementContext):
        keywordGo = ctx.KEYWORD().getText()
        return GoStatementNode(keywordGo=keywordGo)

    def visitCreateTableStatement(self, ctx: MyParser.CreateTableStatementContext):
        keywords = ctx.KEYWORD()
        keywordCreate = keywords[0].getText()
        keywordTable = keywords[1].getText()
        tableName = self.visit(ctx.tableName())
        columns = self.visit(ctx.columnDefinitionList())

        return CreateTableStatementNode(table_name=tableName, columns=columns, keywordCreate=keywordCreate, keywordTable=keywordTable)

    def visitTableName(self, ctx: MyParser.TableNameContext):
        schema = None
        name = None
        if ctx.IDENTIFIER():
            identifier = ctx.IDENTIFIER()
            if len(identifier) != 1:
                schema = identifier[0].getText()
                name = identifier[-1].getText()
            else:
                name = identifier[0].getText()
        else:
            identifier = ctx.BRACKET_IDENTIFIER()[0]
            name = identifier.getText().strip('[]')

        return TableNameNode(schema=schema, name=name)

    def visitColumnDefinitionList(self, ctx: MyParser.ColumnDefinitionListContext):
        columns = []
        for column in ctx.columnDefinition():
            clmn = self.visit(column)
            if (clmn is not None):
                columns.append(clmn)
        return columns

    def visitColumnDefinition(self, ctx: MyParser.ColumnDefinitionContext):
        columnName = ctx.columnName().getText()
        dataType = ctx.dataType().getText()
        columnConstraints = []
        for columnConstraint in ctx.columnConstraint():
            clmn = self.visit(columnConstraint)
            if (clmn is not None):
                columnConstraints.append(clmn)

        return ColumnDefinitionNode(column_name=columnName, data_type=dataType, constraints=columnConstraints)

    def visitColumnConstraint(self, ctx: MyParser.ColumnConstraintContext):
        keyword = ctx.KEYWORD()
        keyword1 = None
        keyword2 = None
        if len(ctx.KEYWORD()) != 1:
            keyword1 = keyword[0].getText()
            keyword2 = keyword[1].getText()
        else:
            keyword1 = keyword[0].getText()

        return columnConstraintsNode(keyword1=keyword1, keyword2=keyword2)

    def visitAlterTableStatement(self, ctx: MyParser.AlterTableStatementContext):
        keywords = ctx.KEYWORD()
        keywordAlter = keywords[0].getText()
        keywordTable = keywords[1].getText()
        tableName = self.visit(ctx.tableName())
        addColumnClause = self.visit(
            ctx.addColumnClause())if ctx.addColumnClause() else None
        dropConstraintClause = self.visit(
            ctx.dropConstraintClause())if ctx.dropConstraintClause() else None

        return AlterTableStatementNode(keywordAlter=keywordAlter,
                                       keywordTable=keywordTable,
                                       table_name=tableName,
                                       addColumnClause=addColumnClause,
                                       dropConstraintClause=dropConstraintClause)

    def visitAddColumnClause(self, ctx: MyParser.AddColumnClauseContext):
        keywords = ctx.KEYWORD()
        keywordAdd = keywords.getText()
        columnDefinition = self.visit(ctx.columnDefinition())
        return AddColumnClauseNode(keywordAdd=keywordAdd, columnDefinition=columnDefinition)

    def visitDropConstraintClause(self, ctx: MyParser.DropConstraintClauseContext):
        keywords = ctx.KEYWORD()
        keywordDrop = keywords[0].getText()
        keywordConstrain = keywords[1].getText()
        constraintName = ctx.constraintName().getText()
        return DropConstraintClauseNode(keywordDrop=keywordDrop,
                                        keywordConstrain=keywordConstrain,
                                        constraintName=constraintName)

    def visitDeleteStatement(self, ctx):
        keywordDelete=ctx.KEYWORD().getText()
        tableName=self.visit(ctx.tableName())if ctx.tableName() else None
        fromClause=self.visit(ctx.fromClause())if ctx.fromClause() else None
        whereClause=self.visit(ctx.whereClause())if ctx.whereClause() else None
        return DeleteStatementNode(keywordDelete=keywordDelete,
                                   tableName=tableName,
                                   fromClause=fromClause,
                                   whereClause=whereClause)
    
    def visitUpdateStatement(self, ctx: MyParser.UpdateStatementContext):
        keywords = ctx.KEYWORD()
        keywordUpdate = keywords[0].getText()
        tableName = self.visit(ctx.tableName())if ctx.tableName() else None
        assignmentList = self.visit(
            ctx.assignmentList())if ctx.assignmentList() else None
        whereClause = self.visit(
            ctx.whereClause())if ctx.whereClause() else None
        return UpdateStatementNode(keywordUpdate=keywordUpdate,
                                   tableName=tableName,
                                   assignmentList=assignmentList,
                                   whereClause=whereClause)

    def visitAssignmentList(self, ctx: MyParser.AssignmentListContext):
        assignments = []
        for assignment in ctx.assignment():
            assnment = self.visit(assignment)
            if (assnment is not None):
                assignments.append(assnment)
        return assignments

    def visitAssignment(self, ctx):
        columnName = ctx.columnName().getText()
        expression = self.visit(ctx.expression())if ctx.expression() else None
        return AssignmentNode(columnName=columnName, expression=expression)

    def visitWhereClause(self, ctx):
        keywordWhere = ctx.KEYWORD().getText()
        condition = self.visit(ctx.condition())if ctx.condition() else None
        return WhereClauseNode(keywordWhere=keywordWhere, condition=condition)

    def visitSelectStatement(self, ctx):
        keywords = ctx.KEYWORD()
        keywordSelect = keywords.getText() 
        selectList = self.visit(ctx.selectList())
        orderByClause = self.visit(
            ctx.orderByClause())if ctx.orderByClause()else None
        whereClause = self.visit(
            ctx.whereClause())if ctx.whereClause()else None
        fromClause = self.visit(ctx.fromClause())if ctx.fromClause()else None
        return SelectStatementNode(keywordSelect=keywordSelect,
                                   orderByClause=orderByClause,
                                   selectList=selectList,
                                   whereClause=whereClause,
                                   fromClause=fromClause,)

    def visitSelectList(self, ctx):
        selectItems = []
        for selectItem in ctx.selectItem():
            item = self.visit(selectItem)
            if item is not None:
                selectItems.append(item)
        return selectItems

    def visitSelectItem(self, ctx):
        expression = None
        if ctx.expression():
            expression = self.visit(ctx.expression())
        elif ctx.OPERATOR():
            operator = ctx.OPERATOR().getText()
            expression = LiteralExpressionNode(value=operator, literal_type="OPERATOR")
        keywordAs = ctx.KEYWORD().getText() if ctx.KEYWORD() else None
        identifier = ctx.IDENTIFIER().getText() if ctx.IDENTIFIER() else None
        return SelectItemNode(expression=expression,
                              keywordAs=keywordAs,
                              identifier=identifier)

    def visitOrderByClause(self, ctx):
        keywords = ctx.KEYWORD()
        keywordOrder = keywords[0].getText()
        keywordBy = keywords[1].getText()
        orderItems = []
        for orderItem in ctx.orderByItem():
            item = self.visit(orderItem)
            if item is not None:
                orderItems.append(item)
        keywordAscDesc=keywords[2].getText() if( len(keywords)>2) else None
        return OrderByClauseNode(keywordOrder=keywordOrder,
                                 keywordBy=keywordBy,
                                 orderByitem=orderItems,
                                 keywordAscDesc=keywordAscDesc)

    def visitOrderByItem(self, ctx):
        identifier = ctx.IDENTIFIER().getText() if ctx.IDENTIFIER() else None
        expression = self.visit(ctx.expression())if ctx.expression() else None
        return OrderByItemNode(identifier=identifier, expression=expression)

    def visitFromClause(self, ctx):
        keywordFrom = ctx.KEYWORD().getText()
        tableSources = []
        for tableSource in ctx.tableSource():
            source = self.visit(tableSource)
            if source is not None:
                tableSources.append(source)
        return FromClauseNode(keywordFrom=keywordFrom, tableSource=tableSources)

    def visitTableSource(self, ctx):
        tableName = self.visit(ctx.tableName())
        keyword = ctx.KEYWORD().getText() if ctx.KEYWORD() else None
        identifier = ctx.IDENTIFIER().getText() if ctx.IDENTIFIER() else None
        return TableSourceNode(tableName=tableName, keyword=keyword, identifier=identifier)

    def visitIfStatement(self, ctx):
        keywords = ctx.KEYWORD()
        keywordIf = keywords[0].getText()
        selectStatement = self.visit(ctx.selectStatement())
        blockStatement = self.visit(ctx.blockStatement())
        keywordNot = None
        keywordEXISTS = None
        if (len(keywords) == 2):
            keywordEXISTS = keywords[1].getText()
        elif (len(keywords) == 3):
            keywordNot = keywords[1].getText()
            keywordEXISTS = keywords[2].getText()

        return IfStatementNode(keywordIf=keywordIf,
                               keywordNot=keywordNot,
                               keywordEXISTS=keywordEXISTS,
                               selectStatement=selectStatement,
                               blockStatement=blockStatement)

    def visitBlockStatement(self, ctx):
        keywords = ctx.KEYWORD()
        keywordBegin = keywords[0].getText()
        statementList = self.visit(ctx.statementList())
        keywordEnd = keywords[1].getText()
        return BlockStatementNode(keywordBegin=keywordBegin,
                                  keywordEnd=keywordEnd,
                                  statementList=statementList)

    def visitTryCatchStatement(self, ctx):
        keywords = ctx.KEYWORD()
        keywordBeginForTry = keywords[0].getText()
        keywordBeginTry = keywords[1].getText()
        tryStatementList = self.visit(ctx.statementList(0))
        keywordEndForTry = keywords[2].getText()
        keywordEndTry = keywords[3].getText()
        keywordBeginForCatch = keywords[4].getText()
        keywordBeginCatch = keywords[5].getText()
        catchStatementList = self.visit(ctx.statementList(1))
        keywordEndCatch = keywords[6].getText()
        keywordEndForCatch = keywords[7].getText()
        return tryCatchStatementNode(keywordBeginForTry=keywordBeginForTry,
                                     keywordBeginTry=keywordBeginTry,
                                     tryStatementList=tryStatementList,
                                     keywordEndTry=keywordEndTry,
                                     keywordEndForTry=keywordEndForTry,
                                     keywordBeginForCatch=keywordBeginForCatch,
                                     keywordBeginCatch=keywordBeginCatch,
                                     catchStatementList=catchStatementList,
                                     keywordEndCatch=keywordEndCatch,
                                     keywordEndForCatch=keywordEndForCatch)
    def visitDeclareStatement(self, ctx):
        keywordDeclare=ctx.KEYWORD().getText()
        variableName=ctx.VARIABLE().getText()
        dataType=ctx.dataType().getText()
        operator=ctx.OPERATOR().getText() if ctx.OPERATOR() else None
        expression =self.visit(ctx.expression()) if ctx.expression() else None
        return declareStatementNode(keywordDeclare=keywordDeclare,
                                    variableName=variableName,
                                    dataType=dataType,
                                    operator=operator,
                                    expression=expression)

    def visitSetStatement(self, ctx):
        keywordSet = ctx.KEYWORD().getText()
        variableName = ctx.VARIABLE().getText()
        operator = ctx.OPERATOR().getText()
        expression = self.visit(ctx.expression())
        return setStatementNode(keywordSet=keywordSet,
                                variableName=variableName,
                                operator=operator,
                                expression=expression)

    def visitExecStatement(self, ctx):
        keywordExec = ctx.KEYWORD().getText()
        identifier = ctx.IDENTIFIER().getText()
        expressionList = self.visit(ctx.expressionList())if ctx.expressionList() else None
        return execStatementNode(keywordExec=keywordExec,
                                 identifier=identifier,
                                 expressionList=expressionList)

    def visitExpressionList(self, ctx):
        expressions = []
        for expression in ctx.expression():
            expr = self.visit(expression)
            if expr is not None:
                expressions.append(expr)
        return expressions

    def visitInsertStatement(self, ctx):
        keywords=ctx.KEYWORD()
        keywordInsert=keywords[0].getText() if isinstance(keywords,list) else keywords.getText()
        if isinstance(keywords,list) and len(keywords)>1:
            keywordInto=keywords[1].getText() if  keywords[1] else None
        else:
            keywordInto=None
        
        tableName=self.visit(ctx.tableName())
        insertColumns=self.visit(ctx.insertColumns()) if ctx.insertColumns() else None 
        insertValues=self.visit(ctx.insertValues()) if ctx.insertValues() else None 
        selectStatement=self.visit(ctx.selectStatement()) if ctx.selectStatement() else None 
        execStatement=self.visit(ctx.execStatement()) if ctx.execStatement() else None 
        return InsertStatement(keywordInsert=keywordInsert,
                               keywordInto=keywordInto,
                               tableName=tableName,
                               insertColumns=insertColumns,
                               insertValues=insertValues,
                               selectStatement=selectStatement,
                               execStatement=execStatement)
    
    def visitInsertColumns(self, ctx):
        identifiers=[]
        for identifier in ctx.IDENTIFIER():
            if identifier is not None:
                identifiers.append(identifier.getText())
        
        return InsertColumnsNode(identifier=identifiers)
    
    def visitInsertValues(self, ctx):
        keywordValues=ctx.KEYWORD().getText()
        expressions=[]
        for expression in ctx.expression():
            if expression is not None:
                expressions.append(expression)
        return InsertValuesNode(keywordValues=keywordValues,
                                expression=expression)
    
    def visitExpression(self, ctx):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.columnReference():
            return self.visit(ctx.columnReference())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.caseExpression():
            return self.visit(ctx.caseExpression())
        elif ctx.PUNCTUATION() and len(ctx.PUNCTUATION()) == 2:
            expression = self.visit(ctx.expression(0))
            return ParenthesizedExpressionNode(expression=expression)
        elif ctx.OPERATOR() and len(ctx.expression()) == 2:
            left = self.visit(ctx.expression(0))
            operator = ctx.OPERATOR().getText()
            right = self.visit(ctx.expression(1))
            return BinaryExpressionNode(left=left, operator=operator, right=right)
        elif ctx.KEYWORD() and len(ctx.expression()) == 2:
            left = self.visit(ctx.expression(0))
            operator = ctx.KEYWORD().getText()
            right = self.visit(ctx.expression(1))
            return BinaryExpressionNode(left=left, operator=operator, right=right)
        elif ctx.VARIABLE():
            variableName = ctx.VARIABLE().getText()
            return VariableExpressionNode(variable_name=variableName)
        elif ctx.STRING_SINGLE():
            value = ctx.STRING_SINGLE().getText()
            return LiteralExpressionNode(value=value, literal_type="STRING_SINGLE")
        elif ctx.STRING_DOUBLE():
            value = ctx.STRING_DOUBLE().getText()
            return LiteralExpressionNode(value=value, literal_type="STRING_DOUBLE")
        else:
            return None

    def visitLiteral(self, ctx):
        if ctx.NUMBER():
            value = ctx.NUMBER().getText()
            return LiteralExpressionNode(value=value, literal_type="NUMBER")
        elif ctx.STRING_SINGLE():
            value = ctx.STRING_SINGLE().getText()
            return LiteralExpressionNode(value=value, literal_type="STRING_SINGLE")
        elif ctx.STRING_DOUBLE():
            value = ctx.STRING_DOUBLE().getText()
            return LiteralExpressionNode(value=value, literal_type="STRING_DOUBLE")
        elif ctx.KEYWORD():
            value = ctx.KEYWORD().getText()
            return LiteralExpressionNode(value=value, literal_type="KEYWORD")
        else:
            return None

    def visitColumnReference(self, ctx):
        tableName = None
        columnName = None
        if ctx.columnName():
            if ctx.tableName():
                tableName = self.visit(ctx.tableName())
            columnName = ctx.columnName().getText()
        elif ctx.IDENTIFIER():
            columnName = ctx.IDENTIFIER().getText()
        elif ctx.BRACKET_IDENTIFIER():
            columnName = ctx.BRACKET_IDENTIFIER()[0].getText().strip('[]')
        return ColumnReferenceExpressionNode(table_name=tableName, column_name=columnName)

    def visitFunctionCall(self, ctx):
        functionName = None
        if ctx.IDENTIFIER():
            functionName = ctx.IDENTIFIER().getText()
        elif ctx.KEYWORD():
            functionName = ctx.KEYWORD().getText()
        expressionList = self.visit(ctx.expressionList())if ctx.expressionList() else None
        return FunctionCallExpressionNode(function_name=functionName, arguments=expressionList)

    def visitCaseExpression(self, ctx):
        keywords = ctx.KEYWORD()
        keywordCase = keywords[0].getText()
        keywordEnd = keywords[-1].getText()
        whenClauseList = []
        for whenClause in ctx.whenClause():
            clause = self.visit(whenClause)
            if clause is not None:
                whenClauseList.append(clause)
        elseClause = self.visit(ctx.elseClause())if ctx.elseClause() else None
        return CaseExpressionNode(keywordCase=keywordCase,
                                  whenClauseList=whenClauseList,
                                  elseClause=elseClause,
                                  keywordEnd=keywordEnd)

    def visitWhenClause(self, ctx):
        keywords = ctx.KEYWORD()
        keywordWhen = keywords[0].getText()
        keyword = keywords[1].getText()
        condition = self.visit(ctx.condition())
        expression = self.visit(ctx.expression())
        return WhenClauseNode(keywordWhen=keywordWhen,
                              condition=condition,
                              keyword=keyword,
                              expression=expression)

    def visitElseClause(self, ctx):
        keywordElse = ctx.KEYWORD().getText()
        expression = self.visit(ctx.expression())
        return ElseClauseNode(keywordElse=keywordElse, expression=expression)

    def visitCondition(self, ctx):
        if len(ctx.expression()) == 2 and (ctx.OPERATOR() or ctx.KEYWORD()):
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            operator = None
            if ctx.OPERATOR():
                operator = ctx.OPERATOR().getText()
            elif ctx.KEYWORD():
                keywords = ctx.KEYWORD()
                if len(keywords) == 1:
                    operator = keywords[0].getText()
            return BinaryConditionNode(left=left, operator=operator, right=right)
        elif ctx.expressionList() and ctx.PUNCTUATION():
            left = self.visit(ctx.expression(0))
            expressionList = self.visit(ctx.expressionList())
            keywords = ctx.KEYWORD()
            keywordIn = keywords[-1].getText()
            keywordNot = keywords[0].getText()if len(keywords) == 2 else None
            return InConditionNode(left=left,
                                   keywordIn=keywordIn,
                                   expressionList=expressionList,
                                   keywordNot=keywordNot)
        elif len(ctx.KEYWORD()) == 2 and len(ctx.expression()) == 1:
            left = self.visit(ctx.expression(0))
            keywords = ctx.KEYWORD()
            keywordIs = keywords[0].getText()
            keywordNot = keywords[1].getText()
            return IsNotConditionNode(left=left,
                                      keywordIs=keywordIs,
                                      keywordNot=keywordNot)
        elif ctx.PUNCTUATION() and len(ctx.PUNCTUATION()) == 2 and ctx.condition():
            condition = self.visit(ctx.condition(0))
            return ParenthesizedConditionNode(condition=condition)
        elif len(ctx.condition()) == 2:
            left = self.visit(ctx.condition(0))
            right = self.visit(ctx.condition(1))
            keywords = ctx.KEYWORD()
            operator = keywords[0].getText()if keywords else None
            return LogicalConditionNode(left=left, operator=operator, right=right)
        else:
            return None
