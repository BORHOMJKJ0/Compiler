from typing import Dict, List
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


class SymbolTable:
    """Manages symbols (tables, variables) in the SQL script"""

    def __init__(self):
        self.tables: Dict[str, Table] = {}
        self.variables: Dict[str, Variable] = {}
        self.current_scope = "GLOBAL"
        self._init_system_tables()

    def _init_system_tables(self):
        """Initialize system tables"""
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

    def add_table(self, table: Table):
        """Add a table to the symbol table"""
        full_name = f"{table.schema.upper()}.{table.name.upper()}"
        self.tables[full_name] = table

    def get_table(self, name: str, schema: str = "dbo") -> Table:
        full_name = f"{schema.upper()}.{name.upper()}"
        return self.tables.get(full_name)

    def has_table(self, name: str, schema: str = "dbo") -> bool:
        """Check if a table exists"""
        full_name = f"{schema.upper()}.{name.upper()}"
        return full_name in self.tables

    def add_variable(self, variable: Variable):
        """Add a variable to the symbol table"""
        self.variables[variable.name.upper()] = variable

    def get_variable(self, name: str) -> Variable:
        """Get a variable from the symbol table"""
        return self.variables.get(name.upper())

    def has_variable(self, name: str) -> bool:
        """Check if a variable exists"""
        return name.upper() in self.variables
