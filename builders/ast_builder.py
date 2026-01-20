from SQLParserVisitor import SQLParserVisitor as MyParserVisitor
from SQLParser import SQLParser as MyParser
from builders.statement_builder import StatementBuilder


class AstBuilder(MyParserVisitor):

    def __init__(self):
        self.statement_builder = StatementBuilder()

    def visitSqlScript(self, ctx: MyParser.SqlScriptContext):
        print('Building AST...')
        statements = []
        for batch in ctx.batch():
            batch_statements = self.visit(batch)
            if batch_statements:
                if isinstance(batch_statements, list):
                    statements.extend(batch_statements)
                else:
                    statements.append(batch_statements)
        return statements

    def visitBatch(self, ctx: MyParser.BatchContext):
        statements = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, MyParser.StatementContext):
                stmt = self.visit(child)
                if stmt is not None:
                    statements.append(stmt)
        return statements

    def visitStatement(self, ctx: MyParser.StatementContext):
        stmt = self.statement_builder.build_statement(ctx)
        if stmt is None:
            from dataclasses import dataclass

            @dataclass
            class UnknownStatementNode:
                type: str
                text: str
            return UnknownStatementNode(type="UnknownStatement", text=ctx.getText()[:50] + "...")
        return stmt

    def visitGoStatement(self, ctx):
        return self.statement_builder.build_go(ctx)

    def visitCreateTableStatement(self, ctx):
        return self.statement_builder.build_create_table(ctx)

    def visitAlterTableStatement(self, ctx):
        return self.statement_builder.build_alter_table(ctx)

    def visitUpdateStatement(self, ctx):
        return self.statement_builder.build_update(ctx)

    def visitDeleteStatement(self, ctx):
        return self.statement_builder.build_delete(ctx)

    def visitSelectStatement(self, ctx):
        return self.statement_builder.build_select(ctx)

    def visitInsertStatement(self, ctx):
        return self.statement_builder.build_insert(ctx)

    def visitIfStatement(self, ctx):
        return self.statement_builder.build_if(ctx)

    def visitBlockStatement(self, ctx):
        return self.statement_builder.build_block(ctx)

    def visitTryCatchStatement(self, ctx):
        return self.statement_builder.build_try_catch(ctx)

    def visitDeclareStatement(self, ctx):
        return self.statement_builder.build_declare(ctx)

    def visitSetStatement(self, ctx):
        return self.statement_builder.build_set(ctx)

    def visitExecStatement(self, ctx):
        return self.statement_builder.build_exec(ctx)
