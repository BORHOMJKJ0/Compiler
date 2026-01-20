from typing import List, Tuple
from dataclasses import dataclass
from .symbol_table import SymbolTable, Table, Column, Variable


@dataclass
class SemanticError:
    line: int
    column: int
    message: str
    severity: str = "ERROR"

    def __str__(self):
        return f"[{self.severity}] Line {self.line}, Col {self.column}: {self.message}"


class SemanticAnalyzer:

    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors: List[SemanticError] = []
        self.warnings: List[SemanticError] = []

        self.stats = {
            'hex_strings': 0,
            'bit_strings': 0,
            'regular_strings': 0,
            'numbers': 0,
            'total_literals': 0
        }

    def add_error(self, line: int, column: int, message: str, severity: str = "ERROR"):
        error = SemanticError(line, column, message, severity)
        if severity == "ERROR":
            self.errors.append(error)
        elif severity == "WARNING":
            self.warnings.append(error)

    def analyze_tokens(self, tokens: List[Tuple]):
        i = 0
        while i < len(tokens):
            line, col, ttype, text = tokens[i]

            if ttype == "HEX_STRING":
                self.stats['hex_strings'] += 1
                self.stats['total_literals'] += 1
                self._validate_hex_string(line, col, text)

            elif ttype == "BIT_STRING":
                self.stats['bit_strings'] += 1
                self.stats['total_literals'] += 1
                self._validate_bit_string(line, col, text)

            elif ttype in ["STRING_SINGLE", "STRING_DOUBLE"]:
                self.stats['regular_strings'] += 1
                self.stats['total_literals'] += 1

            elif ttype == "NUMBER":
                self.stats['numbers'] += 1
                self.stats['total_literals'] += 1

            if ttype == "KEYWORD" and text.upper() == "CREATE":
                i = self._analyze_create_table(tokens, i)

            elif ttype == "KEYWORD" and text.upper() == "ALTER":
                i = self._analyze_alter_table(tokens, i)

            elif ttype == "KEYWORD" and text.upper() == "UPDATE":
                i = self._analyze_update(tokens, i)

            elif ttype == "KEYWORD" and text.upper() == "SELECT":
                i = self._analyze_select(tokens, i)

            elif ttype == "KEYWORD" and text.upper() == "DECLARE":
                i = self._analyze_declare(tokens, i)

            elif ttype == "KEYWORD" and text.upper() == "SET":
                i = self._analyze_set(tokens, i)

            i += 1

        return self.errors, self.warnings

    def _validate_hex_string(self, line: int, col: int, text: str):
        hex_part = text[2:].replace('\\', '').replace(
            '\n', '').replace('\r', '')

        valid_hex = set('0123456789abcdefABCDEF')
        invalid_chars = [c for c in hex_part if c not in valid_hex]

        if invalid_chars:
            self.add_error(line, col,
                           f"Invalid characters in hex string: {set(invalid_chars)}",
                           "ERROR")

        if len(hex_part) % 2 != 0:
            self.add_error(line, col,
                           f"Hex string length must be even (got {len(hex_part)} digits)",
                           "WARNING")

    def _validate_bit_string(self, line: int, col: int, text: str):
        bit_part = text[2:].replace('\\', '').replace(
            '\n', '').replace('\r', '')

        invalid_chars = [c for c in bit_part if c not in '01']

        if invalid_chars:
            self.add_error(line, col,
                           f"Invalid characters in bit string: {set(invalid_chars)}",
                           "ERROR")

    def _analyze_create_table(self, tokens: List[Tuple], start: int) -> int:
        i = start + 1

        while i < len(tokens) and tokens[i][2] not in ["IDENTIFIER", "BRACKET_IDENTIFIER"]:
            i += 1

        if i >= len(tokens):
            return i

        line, col, ttype, first = tokens[i]

        schema = "dbo"
        table_name = first.strip('[]')

        if i + 2 < len(tokens):
            if tokens[i + 1][3] == '.' and tokens[i + 2][2] in ["IDENTIFIER", "BRACKET_IDENTIFIER"]:
                schema = table_name.upper()
                table_name = tokens[i + 2][3].strip('[]')
                i += 2

        schema = schema.upper()
        table_name = table_name.upper()

        full_table_name = f"{schema.upper()}.{table_name.upper()}"

        if self.symbol_table.has_table(table_name, schema):
            self.add_error(line, col,
                           f"Table '{table_name}' already exists", "WARNING")
        else:
            table = Table(table_name, schema)
            self.symbol_table.add_table(table)

            i = self._parse_columns(tokens, i + 1, table)

        return i

    def _parse_columns(self, tokens: List[Tuple], start: int, table: Table) -> int:
        i = start

        while i < len(tokens):
            line, col, ttype, text = tokens[i]

            if text == ')':
                break

            if ttype in ["IDENTIFIER", "BRACKET_IDENTIFIER"]:
                col_name = text.strip('[]')

                if "'" in col_name:
                    self.add_error(line, col,
                                   f"Column name '{col_name}' contains apostrophe - consider using bracket notation",
                                   "WARNING")

                i += 1
                if i < len(tokens):
                    line2, col2, ttype2, dtype = tokens[i]

                    valid_types = ["INT", "BIGINT", "NVARCHAR", "VARCHAR", "CHAR",
                                   "DATETIME", "DATE", "BIT", "FLOAT", "DECIMAL",
                                   "VARBINARY", "BINARY", "TINYINT", "SMALLINT",
                                   "MONEY", "SMALLMONEY", "REAL", "NUMERIC"]

                    dtype_clean = dtype.strip('[]').upper()

                    if ttype2 in ["KEYWORD", "IDENTIFIER", "BRACKET_IDENTIFIER"]:
                        if dtype_clean not in valid_types and dtype.upper() not in valid_types:
                            self.add_error(line2, col2,
                                           f"Unknown data type '{dtype}'", "WARNING")

                    nullable = True
                    i += 1
                    while i < len(tokens) and tokens[i][2] == "KEYWORD":
                        if tokens[i][3].upper() == "NOT":
                            nullable = False
                        i += 1

                    column = Column(col_name, dtype_clean, nullable)
                    table.add_column(column)

            i += 1

        return i

    def _analyze_alter_table(self, tokens: List[Tuple], start: int) -> int:
        i = start + 1

        while i < len(tokens) and tokens[i][2] not in ["IDENTIFIER", "BRACKET_IDENTIFIER"]:
            i += 1

        if i >= len(tokens):
            return i

        line, col, ttype, table_name = tokens[i]
        raw_name = table_name.strip('[]')

        schema = "dbo"
        if '.' in raw_name:
            parts = raw_name.split('.')
            schema = parts[0].upper()
            table_name_clean = parts[1].upper()
        else:
            table_name_clean = raw_name.upper()

        if not self.symbol_table.has_table(table_name_clean, schema):
            table = Table(table_name_clean, schema)
            self.symbol_table.add_table(table)

            self.add_error(
                line, col,
                f"Table '{table_name_clean}' assumed to exist (ALTER without CREATE)",
                "WARNING"
            )

        i += 1
        while i < len(tokens):
            if tokens[i][2] == "KEYWORD" and tokens[i][3].upper() == "ADD":
                i += 1
                if i < len(tokens) and tokens[i][2] in ["IDENTIFIER", "BRACKET_IDENTIFIER"]:
                    col_line, col_col, col_type, col_name = tokens[i]
                    col_name_clean = col_name.strip('[]').upper()

                    table = self.symbol_table.get_table(
                        table_name_clean) or self.symbol_table.get_table(table_name_clean, "DBO")
                    if table and table.has_column(col_name_clean):
                        self.add_error(col_line, col_col,
                                       f"Column '{col_name}' already exists in table '{table_name}'",
                                       "WARNING")
                    elif table:
                        i += 1
                        if i < len(tokens):
                            dtype = tokens[i][3]
                            column = Column(col_name_clean, dtype)
                            table.add_column(column)
            i += 1
            if i - 1 < len(tokens):
                token_text = tokens[i - 1][3]
                if token_text == ';' or token_text.upper() == "GO":
                    break

        return i

    def _analyze_update(self, tokens: List[Tuple], start: int) -> int:
        i = start + 1

        if i < len(tokens):
            line, col, ttype, table_name = tokens[i]
            raw_name = table_name.strip('[]')

            schema = "dbo"
            if '.' in raw_name:
                parts = raw_name.split('.')
                schema = parts[0].upper()
                table_name_clean = parts[1].upper()
            else:
                table_name_clean = raw_name.upper()

        if not self.symbol_table.has_table(table_name_clean, schema):
            table = Table(table_name_clean, schema)
            self.symbol_table.add_table(table)

            self.add_error(
                line, col,
                f"Table '{table_name_clean}' assumed to exist (UPDATE without CREATE)",
                "WARNING"
            )
        while i < len(tokens):
            if tokens[i][2] == "KEYWORD" and tokens[i][3].upper() == "SET":
                i += 1
                while i < len(tokens):
                    if tokens[i][2] in ["IDENTIFIER", "BRACKET_IDENTIFIER"]:
                        col_line, col_col, _, col_name = tokens[i]
                        col_name_clean = col_name.strip('[]').upper()

                        table = (
                            self.symbol_table.get_table(table_name_clean) or
                            self.symbol_table.get_table(
                                table_name_clean, "DBO")
                        )

                        if table and not table.has_column(col_name_clean):
                            self.add_error(
                                col_line, col_col,
                                f"Column '{col_name}' does not exist in table '{table_name}'",
                                "ERROR"
                            )

                    if i < len(tokens):
                        token_text = tokens[i][3] if len(tokens[i]) > 3 else ''
                        if token_text in [';'] or token_text.upper() in ['WHERE', 'GO']:
                            break

                    i += 1
                break

            i += 1
            if i > 0 and i - 1 < len(tokens) and tokens[i - 1][3] in [';', 'GO']:
                break

        return i

    def _analyze_select(self, tokens: List[Tuple], start: int) -> int:
        i = start + 1

        while i < len(tokens):
            if tokens[i][2] == "KEYWORD" and tokens[i][3].upper() == "FROM":
                i += 1
                if i < len(tokens):
                    line, col, ttype, table_name = tokens[i]

                    schema = "DBO"
                    table_name_clean = ""

                    if i + 2 < len(tokens) and tokens[i + 1][3] == '.':
                        schema = tokens[i][3].strip('[]').upper()
                        table_name_clean = tokens[i + 2][3].strip('[]').upper()
                        i += 2
                    else:
                        table_name_clean = tokens[i][3].strip('[]').upper()

                    if schema.upper() in ["SYS", "INFORMATION_SCHEMA"]:
                        i += 1
                        continue

                    if table_name_clean in ["COLUMNS", "FOREIGN_KEYS", "TABLES", "OBJECTS"]:
                        i += 1
                        continue

                    if (not self.symbol_table.has_table(table_name_clean, schema) and
                            not self.symbol_table.has_table(table_name_clean, "DBO")):
                        self.add_error(line, col,
                                       f"Table '{schema}.{table_name_clean}' does not exist", "WARNING")

            i += 1
            if i > 0 and tokens[i - 1][3] in [';', ')']:
                break

        return i

    def _analyze_declare(self, tokens: List[Tuple], start: int) -> int:
        i = start + 1

        if i < len(tokens) and tokens[i][2] == "VARIABLE":
            line, col, ttype, var_name = tokens[i]

            if self.symbol_table.has_variable(var_name):
                self.add_error(line, col,
                               f"Variable '{var_name}' already declared", "WARNING")
            else:
                i += 1
                if i < len(tokens):
                    dtype = tokens[i][3]
                    self.symbol_table.add_variable(Variable(var_name, dtype))

        return i + 1

    def _analyze_set(self, tokens: List[Tuple], start: int) -> int:
        i = start + 1

        if i < len(tokens) and tokens[i][2] == "VARIABLE":
            line, col, ttype, var_name = tokens[i]

            if not self.symbol_table.has_variable(var_name):
                self.add_error(line, col,
                               f"Variable '{var_name}' not declared", "ERROR")
            else:
                variable = self.symbol_table.get_variable(var_name)
                variable.initialized = True

        return i + 1

    def generate_report(self) -> str:
        report = []
        report.append("=" * 80)
        report.append("SEMANTIC ANALYSIS REPORT".center(80))
        report.append("=" * 80)
        report.append("")

        if self.stats['total_literals'] > 0:
            report.append("Literal Statistics:")
            report.append(
                f"  • Total Literals: {self.stats['total_literals']}")
            report.append(
                f"  • Regular Strings: {self.stats['regular_strings']}")
            report.append(f"  • Hex Strings: {self.stats['hex_strings']}")
            report.append(f"  • Bit Strings: {self.stats['bit_strings']}")
            report.append(f"  • Numbers: {self.stats['numbers']}")
            report.append("")

        report.append(f"Tables Defined: {len(self.symbol_table.tables)}")
        for table_name, table in self.symbol_table.tables.items():
            if not table_name.startswith("SYS.") and not table_name.startswith("INFORMATION_SCHEMA."):
                report.append(
                    f"  • {table.schema}.{table.name} ({len(table.columns)} columns)")
                for col_name, col in table.columns.items():
                    null_str = "NULL" if col.nullable else "NOT NULL"
                    report.append(
                        f"      - {col.name}: {col.data_type} {null_str}")
        report.append("")

        report.append(
            f"Variables Declared: {len(self.symbol_table.variables)}")
        for var in self.symbol_table.variables.values():
            init_str = "initialized" if var.initialized else "not initialized"
            report.append(f"  • {var.name}: {var.data_type} ({init_str})")
        report.append("")

        if self.errors:
            report.append(f"ERRORS: {len(self.errors)}")
            for error in self.errors:
                report.append(f"   {error}")
            report.append("")

        if self.warnings:
            report.append(f"WARNINGS: {len(self.warnings)}")
            for warning in self.warnings:
                report.append(f"   {warning}")
            report.append("")

        if not self.errors:
            report.append("✓ No semantic errors found!")

        report.append("=" * 80)

        return "\n".join(report)
