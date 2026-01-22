from SQLParserVisitor import SQLParserVisitor as MyParserVisitor
from SQLParser import SQLParser as MyParser
from builders.statement_builder import StatementBuilder


class AstBuilder(MyParserVisitor):

    def __init__(self):
        self.statement_builder = StatementBuilder()
        self.errors = []
        self.warnings = []

    def visitSqlScript(self, ctx: MyParser.SqlScriptContext):
        print('Building AST...')
        statements = []
        for batch in ctx.batch():
            try:
                batch_statements = self.visit(batch)
                if batch_statements:
                    if isinstance(batch_statements, list):
                        statements.extend(batch_statements)
                    else:
                        statements.append(batch_statements)
            except Exception as e:
                self.errors.append(f"Error processing batch: {str(e)}")
                continue
        return statements

    def visitBatch(self, ctx: MyParser.BatchContext):
        statements = []
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, MyParser.StatementContext):
                try:
                    stmt = self.visit(child)
                    if stmt is not None:
                        statements.append(stmt)
                except Exception as e:
                    self.warnings.append(
                        f"Warning: Skipped malformed statement: {str(e)}")
                    from dataclasses import dataclass

                    @dataclass
                    class SkippedStatementNode:
                        type: str
                        text: str
                        error: str
                    statements.append(SkippedStatementNode(
                        type="SkippedStatement",
                        text=child.getText()[
                            :50] + "..." if len(child.getText()) > 50 else child.getText(),
                        error=str(e)
                    ))
                    continue
        return statements

    def visitStatement(self, ctx: MyParser.StatementContext):
        try:
            stmt = self.statement_builder.build_statement(ctx)
            if stmt is None:
                from dataclasses import dataclass

                @dataclass
                class UnknownStatementNode:
                    type: str
                    text: str
                return UnknownStatementNode(type="UnknownStatement", text=ctx.getText()[:50] + "...")
            return stmt
        except Exception as e:
            self.warnings.append(f"Statement parsing error: {str(e)}")
            from dataclasses import dataclass

            @dataclass
            class ErrorStatementNode:
                type: str
                text: str
                error: str
            return ErrorStatementNode(
                type="ErrorStatement",
                text=ctx.getText()[:50] + "...",
                error=str(e)
            )

    def visitGoStatement(self, ctx):
        try:
            return self.statement_builder.build_go(ctx)
        except:
            from Ast.statement_nodes import GoStatementNode
            return GoStatementNode(keywordGo="GO")

    def visitCreateTableStatement(self, ctx):
        try:
            return self.statement_builder.build_create_table(ctx)
        except Exception as e:
            self.warnings.append(f"CREATE TABLE error: {str(e)}")
            return None

    def visitAlterTableStatement(self, ctx):
        try:
            return self.statement_builder.build_alter_table(ctx)
        except Exception as e:
            self.warnings.append(f"ALTER TABLE error: {str(e)}")
            return None

    def visitUpdateStatement(self, ctx):
        try:
            return self.statement_builder.build_update(ctx)
        except Exception as e:
            self.warnings.append(f"UPDATE error: {str(e)}")
            return None

    def visitDeleteStatement(self, ctx):
        try:
            return self.statement_builder.build_delete(ctx)
        except Exception as e:
            self.warnings.append(f"DELETE error: {str(e)}")
            return None

    def visitSelectStatement(self, ctx):
        try:
            return self.statement_builder.build_select(ctx)
        except Exception as e:
            self.warnings.append(f"SELECT error: {str(e)}")
            return None

    def visitInsertStatement(self, ctx):
        try:
            return self.statement_builder.build_insert(ctx)
        except Exception as e:
            self.warnings.append(f"INSERT error: {str(e)}")
            return None

    def visitIfStatement(self, ctx):
        try:
            return self.statement_builder.build_if(ctx)
        except Exception as e:
            self.warnings.append(f"IF error: {str(e)}")
            return None

    def visitBlockStatement(self, ctx):
        try:
            return self.statement_builder.build_block(ctx)
        except Exception as e:
            self.warnings.append(f"BLOCK error: {str(e)}")
            return None

    def visitTryCatchStatement(self, ctx):
        try:
            return self.statement_builder.build_try_catch(ctx)
        except Exception as e:
            self.warnings.append(f"TRY-CATCH error: {str(e)}")
            return None

    def visitDeclareStatement(self, ctx):
        try:
            return self.statement_builder.build_declare(ctx)
        except Exception as e:
            self.warnings.append(f"DECLARE error: {str(e)}")
            return None

    def visitSetStatement(self, ctx):
        try:
            return self.statement_builder.build_set(ctx)
        except Exception as e:
            self.warnings.append(f"SET error: {str(e)}")
            return None

    def visitExecStatement(self, ctx):
        try:
            return self.statement_builder.build_exec(ctx)
        except Exception as e:
            self.warnings.append(f"EXEC error: {str(e)}")
            return None

    def get_errors(self):
        return self.errors

    def get_warnings(self):
        return self.warnings

    def has_errors(self):
        return len(self.errors) > 0
