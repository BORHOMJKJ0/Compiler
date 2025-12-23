from typing import Dict, List, Set, Tuple
from dataclasses import dataclass, field


@dataclass
class Column:
    name: str
    data_type: str
    nullable: bool = True
    is_primary_key: bool = False
    is_foreign_key: bool = False

    def __hash__(self):
        return hash(self.name.upper())

    def __eq__(self, other):
        if isinstance(other, Column):
            return self.name.upper() == other.name.upper()
        return False


@dataclass
class Table:
    name: str
    schema: str = "dbo"
    columns: Dict[str, Column] = field(default_factory=dict)
    constraints: List[str] = field(default_factory=list)

    def add_column(self, column: Column):
        self.columns[column.name.upper()] = column

    def has_column(self, column_name: str) -> bool:
        return column_name.upper() in self.columns

    def get_column(self, column_name: str) -> Column:
        return self.columns.get(column_name.upper())


@dataclass
class Variable:
    name: str
    data_type: str
    initialized: bool = False


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
        self.tables: Dict[str, Table] = {}
        self.variables: Dict[str, Variable] = {}
        self.errors: List[SemanticError] = []
        self.warnings: List[SemanticError] = []
        self.current_scope = "GLOBAL"

        self.stats = {
            'hex_strings': 0,
            'bit_strings': 0,
            'regular_strings': 0,
            'numbers': 0,
            'total_literals': 0
        }

        self._init_system_tables()

    def _init_system_tables(self):
        sys_columns = Table("columns", "sys")
        sys_columns.add_column(Column("Name", "nvarchar"))
        sys_columns.add_column(Column("Object_ID", "int"))
        sys_columns.add_column(Column("column_id", "int"))
        self.tables["SYS.COLUMNS"] = sys_columns

        sys_fk = Table("foreign_keys", "sys")
        sys_fk.add_column(Column("name", "nvarchar"))
        sys_fk.add_column(Column("object_id", "int"))
        sys_fk.add_column(Column("parent_object_id", "int"))
        self.tables["SYS.FOREIGN_KEYS"] = sys_fk

        info_tables = Table("TABLES", "INFORMATION_SCHEMA")
        info_tables.add_column(Column("TABLE_SCHEMA", "nvarchar"))
        info_tables.add_column(Column("TABLE_NAME", "nvarchar"))
        info_tables.add_column(Column("TABLE_TYPE", "nvarchar"))
        self.tables["INFORMATION_SCHEMA.TABLES"] = info_tables

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

            elif ttype == "INVALID_IDENTIFIER":
                self.add_error(line, col,
                               f"Invalid identifier '{text}'", "ERROR")

            i += 1

        return self.errors, self.warnings

    def _validate_hex_string(self, line: int, col: int, text: str):
        hex_part = text[2:].replace('\\', '').replace('\n', '').replace('\r', '')

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
        bit_part = text[2:].replace('\\', '').replace('\n', '').replace('\r', '')

        invalid_chars = [c for c in bit_part if c not in '01']

        if invalid_chars:
            self.add_error(line, col,
                           f"Invalid characters in bit string: {set(invalid_chars)}",
                           "ERROR")

    def _analyze_create_table(self, tokens: List[Tuple], start: int) -> int:
        i = start + 1

        while i < len(tokens) and tokens[i][2] != "IDENTIFIER" and tokens[i][2] != "BRACKET_IDENTIFIER":
            i += 1

        if i >= len(tokens):
            return i

        line, col, ttype, table_name = tokens[i]

        if table_name.startswith('[') and table_name.endswith(']'):
            parts = table_name.strip('[]').split('].[')
            if len(parts) == 2:
                schema, table_name = parts
            else:
                schema = "dbo"
                table_name = parts[0]
        else:
            schema = "dbo"

        full_table_name = f"{schema.upper()}.{table_name.upper()}"

        if full_table_name in self.tables:
            self.add_error(line, col,
                           f"Table '{table_name}' already exists", "WARNING")
        else:
            table = Table(table_name, schema)
            self.tables[full_table_name] = table

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

                    if ttype2 == "KEYWORD" and dtype.upper() in ["NOT", "NULL", "PRIMARY", "FOREIGN", "UNIQUE",
                                                                 "CHECK"]:
                        i -= 1
                        i += 1
                        continue

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
        table_name_clean = table_name.strip('[]').upper()

        full_name = f"DBO.{table_name_clean}"
        if full_name not in self.tables and table_name_clean not in self.tables:
            self.add_error(line, col,
                           f"Table '{table_name}' does not exist", "ERROR")
            return i

        i += 1
        while i < len(tokens):
            if tokens[i][2] == "KEYWORD" and tokens[i][3].upper() == "ADD":
                i += 1
                if i < len(tokens) and tokens[i][2] in ["IDENTIFIER", "BRACKET_IDENTIFIER"]:
                    col_line, col_col, col_type, col_name = tokens[i]
                    col_name_clean = col_name.strip('[]').upper()

                    table = self.tables.get(full_name) or self.tables.get(table_name_clean)
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
            if tokens[i - 1][3] == ';' or tokens[i - 1][3].upper() == "GO":
                break

        return i

    def _analyze_update(self, tokens: List[Tuple], start: int) -> int:
        i = start + 1

        if i < len(tokens):
            line, col, ttype, table_name = tokens[i]
            table_name_clean = table_name.strip('[]').upper()

            full_name = f"DBO.{table_name_clean}"
            if full_name not in self.tables and table_name_clean not in self.tables:
                self.add_error(line, col,
                               f"Table '{table_name}' does not exist", "ERROR")

        while i < len(tokens):
            if tokens[i][2] == "KEYWORD" and tokens[i][3].upper() == "SET":
                i += 1
                if i < len(tokens) and tokens[i][2] in ["IDENTIFIER", "BRACKET_IDENTIFIER"]:
                    col_line, col_col, col_type, col_name = tokens[i]
                    col_name_clean = col_name.strip('[]').upper()

                    table = self.tables.get(full_name) or self.tables.get(table_name_clean)
                    if table and not table.has_column(col_name_clean):
                        self.add_error(col_line, col_col,
                                       f"Column '{col_name}' does not exist in table '{table_name}'",
                                       "ERROR")

            i += 1
            if i > 0 and tokens[i - 1][3] in [';', 'GO']:
                break

        return i

    def _analyze_select(self, tokens: List[Tuple], start: int) -> int:
        i = start + 1

        while i < len(tokens):
            if tokens[i][2] == "KEYWORD" and tokens[i][3].upper() == "FROM":
                i += 1
                if i < len(tokens):
                    line, col, ttype, table_name = tokens[i]

                    schema = "dbo"
                    if '.' in table_name:
                        parts = table_name.split('.')
                        schema = parts[0].strip('[]').upper()
                        table_name = parts[-1]

                    table_name_clean = table_name.strip('[]').upper()

                    if schema in ["SYS", "INFORMATION_SCHEMA"]:
                        i += 1
                        continue

                    if table_name_clean in ["COLUMNS", "FOREIGN_KEYS", "TABLES", "OBJECTS"]:
                        i += 1
                        continue

                    full_name = f"{schema}.{table_name_clean}"

                    if (full_name not in self.tables and
                            table_name_clean not in self.tables and
                            f"DBO.{table_name_clean}" not in self.tables):
                        self.add_error(line, col,
                                       f"Table '{table_name}' does not exist", "WARNING")

            i += 1
            if i > 0 and tokens[i - 1][3] in [';', ')']:
                break

        return i

    def _analyze_declare(self, tokens: List[Tuple], start: int) -> int:
        i = start + 1

        if i < len(tokens) and tokens[i][2] == "VARIABLE":
            line, col, ttype, var_name = tokens[i]

            if var_name.upper() in self.variables:
                self.add_error(line, col,
                               f"Variable '{var_name}' already declared", "WARNING")
            else:
                i += 1
                if i < len(tokens):
                    dtype = tokens[i][3]
                    self.variables[var_name.upper()] = Variable(var_name, dtype)

        return i + 1

    def _analyze_set(self, tokens: List[Tuple], start: int) -> int:
        i = start + 1

        if i < len(tokens) and tokens[i][2] == "VARIABLE":
            line, col, ttype, var_name = tokens[i]

            if var_name.upper() not in self.variables:
                self.add_error(line, col,
                               f"Variable '{var_name}' not declared", "ERROR")
            else:
                self.variables[var_name.upper()].initialized = True

        return i + 1

    def generate_report(self) -> str:
        report = []
        report.append("=" * 80)
        report.append("SEMANTIC ANALYSIS REPORT".center(80))
        report.append("=" * 80)
        report.append("")

        if self.stats['total_literals'] > 0:
            report.append("Literal Statistics:")
            report.append(f"  • Total Literals: {self.stats['total_literals']}")
            report.append(f"  • Regular Strings: {self.stats['regular_strings']}")
            report.append(f"  • Hex Strings: {self.stats['hex_strings']}")
            report.append(f"  • Bit Strings: {self.stats['bit_strings']}")
            report.append(f"  • Numbers: {self.stats['numbers']}")
            report.append("")

        report.append(f"Tables Defined: {len(self.tables)}")
        for table_name, table in self.tables.items():
            if not table_name.startswith("SYS.") and not table_name.startswith("INFORMATION_SCHEMA."):
                report.append(f"  • {table.schema}.{table.name} ({len(table.columns)} columns)")
                for col_name, col in table.columns.items():
                    null_str = "NULL" if col.nullable else "NOT NULL"
                    report.append(f"      - {col.name}: {col.data_type} {null_str}")
        report.append("")

        report.append(f"Variables Declared: {len(self.variables)}")
        for var in self.variables.values():
            init_str = "initialized" if var.initialized else "not initialized"
            report.append(f"  • {var.name}: {var.data_type} ({init_str})")
        report.append("")

        if self.errors:
            report.append(f"ERRORS: {len(self.errors)}")
            for error in self.errors:
                report.append(f"  ✗ {error}")
            report.append("")

        if self.warnings:
            report.append(f"WARNINGS: {len(self.warnings)}")
            for warning in self.warnings:
                report.append(f"  ⚠ {warning}")
            report.append("")

        if not self.errors:
            report.append("✓ No semantic errors found!")

        report.append("=" * 80)

        return "\n".join(report)