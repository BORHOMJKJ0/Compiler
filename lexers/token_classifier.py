from typing import List, Tuple, Dict


class TokenClassifier:
    """Classifies and validates tokens"""

    KEYWORDS = {
        "ADD", "ALL", "ALTER", "AND", "ANY", "AS", "ASC", "BETWEEN", "BY", "CASE", "CHECK",
        "COLUMN", "CONSTRAINT", "CREATE", "CROSS", "DATABASE", "DEFAULT", "DELETE",
        "DESC", "DISTINCT", "DROP", "ELSE", "END", "EXCEPT", "EXISTS", "FALSE", "FETCH",
        "FOREIGN", "FROM", "FULL", "GROUP", "HAVING", "ILIKE", "IN", "INDEX", "INNER",
        "INSERT", "INTERSECT", "INTO", "IS", "JOIN", "LEFT", "LIKE", "LIMIT", "NATURAL",
        "NOT", "NULL", "OFFSET", "ON", "OR", "ORDER", "OUTER", "OVER", "PARTITION",
        "PRIMARY", "RETURNING", "RIGHT", "ROW", "ROWS", "SELECT", "SET", "TABLE",
        "THEN", "TOP", "TRUE", "UNION", "UNIQUE", "UNNEST", "UPDATE", "USING", "VALUES",
        "WHEN", "WHERE", "WINDOW", "WITH", "VIEW", "TRIGGER", "FUNCTION", "PROCEDURE",
        "BEGIN", "LOOP", "REFERENCES", "GRANT", "REVOKE", "TEMP", "TEMPORARY",
        "REPLACE", "MATERIALIZED", "ESCAPE", "DECLARE", "KEY", "FIRST", "ONLY",
        "TRY", "CATCH", "EXEC", "GO", "QUOTENAME", "RAISERROR", "NVARCHAR", "INT",
        "BIGINT", "MAX", "ERROR_MESSAGE", "ERROR_SEVERITY", "ERROR_STATE",
        "SCHEMA_NAME", "SCHEMA", "OBJECT", "TYPE", "INFORMATION_SCHEMA",
        "TABLES", "BASE", "COLUMNS", "KEYS", "PARENT", "CONSTRAINTS",
        "NCHAR", "VARCHAR", "CHAR", "DATETIME", "DATE", "TIME", "FLOAT", "REAL",
        "NUMERIC", "MONEY", "SMALLMONEY", "BIT", "TINYINT", "SMALLINT",
        "CURSOR", "IDENTITY", "SEQUENCES", "OUTPUT", "OPENROWSET", "OPENJSON",
        "SP_EXECUTESQL", "FOREIGN_KEYS", "PARENT_OBJECT_ID", "EXECPT",
        "OBJECT_ID", "OBJECT_NAME", "OBJECT_SCHEMA_NAME", "TABLE_SCHEMA", "TABLE_NAME",
        "TABLE_TYPE", "IF", "BULK"
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
            self.errors.append(f"Error: {paren_count} unclosed opening parenthesis")

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
            self.errors.append(f"Error: {bracket_count} unclosed opening bracket")

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
            self.errors.append(f"Error: {comment_depth} unclosed block comment(s)")