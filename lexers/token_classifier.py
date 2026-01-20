from typing import List, Tuple, Dict


class TokenClassifier:
    """Classifies and validates tokens"""

    KEYWORDS = {
        "CAST","FALSE", "FETCH", "ILIKE", "LIMIT", "NATURAL", "PARTITION", "OFFSET", "RETURNING", "SELECT", "UNNEST", "WINDOW", "TEMP", "TEMPORARY", "LOOP", "REPLACE", "MATERIALIZED", "FIRST", "TRY", "CATCH", "GO", "QUOTENAME", "NVARCHAR", "ERROR_MESSAGE", "ERROR_SEVERITY", "ERROR_STATE", "SCHEMA_NAME", "SCHEMA", "OBJECT", "TYPE", "INFORMATION_SCHEMA", "TABLES", "BASE", "COLUMNS", "KEYS", "PARENT", "TINYINT", "SEQUENCES", "OUTPUT", "OPENJSON", "SP_EXECUTESQL", "FOREIGN_KEYS", "PARENT_OBJECT_ID", "EXECPT", "OBJECT_ID", "OBJECT_NAME", "OBJECT_SCHEMA_NAME", "TABLE_SCHEMA", "TABLE_NAME", "TABLE_TYPE"
        "ADD", "ALL", "ALTER", "AND", "ANY", "AS", "ASC", "AUTHORIZATION", "BACKUP", "BEGIN", "BETWEEN",
        "BREAK", "BROWSE", "BULK", "BY", "CASCADE", "CASE", "CHECK", "CHECKPOINT", "CLOSE", "CLUSTERED",
        "COALESCE", "COLLATE", "COLUMN", "COMMIT", "COMPUTE", "CONSTRAINT", "CONTAINS", "CONTAINSTABLE",
        "CONTINUE", "CONVERT", "CREATE", "CROSS", "CURRENT", "CURRENT_DATE", "CURRENT_TIME",
        "CURRENT_TIMESTAMP", "CURRENT_USER", "CURSOR", "DATABASE", "DBCC", "DEALLOCATE", "DECLARE",
        "DEFAULT", "DELETE", "DENY", "DESC", "DISK", "DISTINCT", "DISTRIBUTED", "DOUBLE", "DROP", "DUMP",
        "ELSE", "END", "ERRLVL", "ESCAPE", "EXCEPT", "EXEC", "EXECUTE", "EXISTS", "EXIT", "EXTERNAL", "FETCH",
        "FILE", "FILLFACTOR", "FOR", "FOREIGN", "FREETEXT", "FREETEXTTABLE", "FROM", "FULL", "FUNCTION",
        "GOTO", "GRANT", "GROUP", "HAVING", "HOLDLOCK", "IDENTITY", "IDENTITY_INSERT", "IDENTITYCOL",
        "IF", "IN", "INDEX", "INNER", "INSERT", "INTERSECT", "INTO", "IS", "JOIN", "KEY", "KILL", "LEFT",
        "LIKE", "LINENO", "LOAD", "MERGE", "NATIONAL", "NOCHECK", "NONCLUSTERED", "NOT", "NULL", "NULLIF",
        "OF", "OFF", "OFFSETS", "ON", "OPEN", "OPENDATASOURCE", "OPENQUERY", "OPENROWSET", "OPENXML",
        "OPTION", "OR", "ORDER", "OUTER", "OVER", "PERCENT", "PLAN", "PRECISION", "PRIMARY", "PRINT",
        "PROC", "PROCEDURE", "PUBLIC", "RAISERROR", "READ", "READTEXT", "RECONFIGURE", "REFERENCES",
        "REPLICATION", "RESTORE", "RESTRICT", "RETURN", "REVERT", "REVOKE", "RIGHT", "ROLLBACK", "ROWCOUNT",
        "ROWGUIDCOL", "RULE", "SAVE", "SAVEPOINT", "SCHEMA", "SESSION_USER", "SET", "SETUSER", "SHUTDOWN",
        "SOME", "STATISTICS", "SYSTEM_USER", "TABLE", "TABLESAMPLE", "TEXTSIZE", "THEN", "TO", "TOP",
        "TRAN", "TRANSACTION", "TRIGGER", "TRUNCATE", "TSEQUAL", "UNION", "UNIQUE", "UNPIVOT", "UPDATE",
        "UPDATETEXT", "USE", "USER", "VALUES", "VARYING", "VIEW", "WAITFOR", "WHEN", "WHERE", "WHILE",
        "WITH", "WRITETEXT", "ABS", "ABSENT", "ACTION", "ADMIN", "AFTER", "AGGREGATE", "ALIAS", "ASSERTION", "AT", "BEFORE",
        "BINARY", "BIT", "BOOLEAN", "BOTH", "CALL", "CAST", "CHAR", "CHARACTER", "CLASS", "CLOB", "COLUMN_NAME",
        "CONNECTION", "CONSTRAINTS", "CUBE", "CURRENT_PATH", "DATA", "DAY", "DECIMAL", "DOMAIN",
        "ELEMENT", "END_EXEC", "EXTRACT", "FREE", "GLOBAL", "HOST", "HOUR", "IDENTIFIER", "INTERVAL",
        "ISOLATION", "LANGUAGE", "LAST", "LATERAL", "LEADING", "LEVEL", "LOCAL", "LOCK", "MATCH",
        "MINUTE", "MONTH", "NAMES", "NEW", "NEXT", "ONLY", "PARAMETER", "POWER", "PRECISION", "POSITION",
        "PROCEDURE_CATALOG", "QUARTER", "REPEATABLE", "RESTRICT", "RLIKE", "ROLLUP", "ROW", "ROWS",
        "SAVEPOINT", "SECOND", "SESSION", "SCOPE", "SEARCH", "SECTION", "SIMILAR", "SQL", "SQLSTATE",
        "SQLWARNING", "START", "STATE", "STATEMENT", "SUBSTRING", "SYSTEM", "SYSTEM_USER", "TERMINATE",
        "TIMEZONE_HOUR", "TIMEZONE_MINUTE", "TRUE", "TYPE", "UNBOUNDED", "UNKNOWN", "USAGE", "USING",
        "VARIABLE", "WHENEVER", "WITHOUT", "YEAR", "ZONE", "ABS", "ACOS", "ASIN", "ATAN", "ATAN2", "CEILING", "CHARINDEX", "CONCAT", "COUNT", "COUNT_BIG",
        "DATEADD", "DATEDIFF", "DATENAME", "DATEPART", "GETDATE", "ISNULL", "LEFT", "LEN", "LOWER",
        "MAX", "MIN", "POWER", "RANK", "ROW_NUMBER", "RTRIM", "SUBSTRING", "SUM", "UPPER",
        "BIGINT", "BINARY", "BIT", "CHAR", "DATE", "DATETIME", "DECIMAL", "FLOAT", "IMAGE", "INT",
        "MONEY", "NCHAR", "NTEXT", "NUMERIC", "REAL", "SMALLINT", "SMALLMONEY", "SQL_VARIANT",
        "TEXT", "TIME", "TIMESTAMP", "UNIQUEIDENTIFIER", "VARBINARY", "VARCHAR", "XML","VERSION"
    }

    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def classify_tokens(self, tokens: List[Tuple]) -> Dict[str, int]:
        """Classify tokens and return statistics"""
        stats = {}
        for line, col, ttype, text in tokens:
            stats[ttype] = stats.get(ttype, 0) + 1
        return stats

    def validate_syntax(self, tokens: List[Tuple], input_text: str):
        """Validate basic syntax rules"""
        self.errors.clear()
        self.warnings.clear()

        self._check_parentheses(tokens)
        self._check_brackets(tokens)
        self._check_identifiers(tokens)
        self._check_strings(tokens)
        self._check_comments(input_text)

    def _check_parentheses(self, tokens: List[Tuple]):
        """Check for balanced parentheses"""
        paren_count = 0
        for line, col, ttype, text in tokens:
            if text == '(':
                paren_count += 1
            elif text == ')':
                paren_count -= 1
                if paren_count < 0:
                    self.errors.append(
                        f"Line {line}, Column {col}: Closing parenthesis ) without opening"
                    )
                    paren_count = 0

        if paren_count > 0:
            self.errors.append(
                f"Error: {paren_count} unclosed opening parenthesis")

    def _check_brackets(self, tokens: List[Tuple]):
        """Check for balanced brackets"""
        bracket_count = 0
        for line, col, ttype, text in tokens:
            if text == '[':
                bracket_count += 1
            elif text == ']':
                bracket_count -= 1
                if bracket_count < 0:
                    self.errors.append(
                        f"Line {line}, Column {col}: Closing bracket ] without opening"
                    )
                    bracket_count = 0

        if bracket_count > 0:
            self.errors.append(
                f"Error: {bracket_count} unclosed opening bracket")

    def _check_identifiers(self, tokens: List[Tuple]):
        """Validate identifiers"""
        for line, col, ttype, text in tokens:
            if ttype in ["IDENTIFIER", "BRACKET_IDENTIFIER"]:
                if "'" in text and not text.startswith('['):
                    self.warnings.append(
                        f"Line {line}, Column {col}: Identifier '{text}' contains apostrophe - "
                        "consider using bracket notation [...]"
                    )

            if text.startswith('[') and text.endswith(']'):
                if "'" in text:
                    self.warnings.append(
                        f"Line {line}, Column {col}: Bracket identifier {text} contains apostrophe"
                    )

    def _check_strings(self, tokens: List[Tuple]):
        """Validate string literals"""
        for line, col, ttype, text in tokens:
            if ttype in ["STRING_SINGLE", "STRING_DOUBLE"]:
                if "''" in text[1:-1]:
                    self.warnings.append(
                        f"Line {line}, Column {col}: String contains escaped single quotes"
                    )
                if '""' in text[1:-1]:
                    self.warnings.append(
                        f"Line {line}, Column {col}: String contains escaped double quotes"
                    )

                if '\\' in text and ('\n' in text or '\r' in text):
                    self.warnings.append(
                        f"Line {line}, Column {col}: String contains line continuation"
                    )

    def _check_comments(self, input_text: str):
        """Check for balanced block comments"""
        comment_depth = 0
        lines = input_text.split('\n')
        for line_num, line in enumerate(lines, 1):
            i = 0
            while i < len(line) - 1:
                if line[i:i + 2] == '/*':
                    comment_depth += 1
                    i += 2
                elif line[i:i + 2] == '*/':
                    comment_depth -= 1
                    if comment_depth < 0:
                        self.errors.append(
                            f"Line {line_num}: Closing comment */ without opening /*"
                        )
                        comment_depth = 0
                    i += 2
                else:
                    i += 1

        if comment_depth > 0:
            self.errors.append(
                f"Error: {comment_depth} unclosed block comment(s)")
