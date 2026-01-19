# SQL Compiler - Reorganized Architecture

A modular SQL compiler frontend implemented with ANTLR and Python, featuring lexical analysis, syntax parsing, AST construction, and semantic analysis.

## 📁 Project Structure
```
sql_compiler/
├── grammars/              # ANTLR grammar files
│   ├── BaseLexer.g4
│   ├── ExpressionParser.g4
│   ├── StatementParser.g4
│   └── SQLParser.g4
│
├── lexers/                # Lexical analysis
│   ├── base_lexer.py
│   └── token_classifier.py
│
│
├── ast/                   # AST node definitions
│   ├── base_nodes.py
│   ├── expression_nodes.py
│   ├── statement_nodes.py
│   └── condition_nodes.py
│
├── builders/              # AST construction
│   ├── expression_builder.py
│   ├── statement_builder.py
│   ├── condition_builder.py
│   └── ast_builder.py
│
├── semantic/              # Semantic analysis
│   ├── symbol_table.py
│   └── semantic_analyzer.py
│
├── utils/                 # Utilities
│   ├── error_handler.py
│   └── logger.py
│
├── main.py               # Main entry point
├── testLexer.py          # Lexer testing
├── token_viewer.py       # Token visualization
├── sqlInput.txt          # Sample SQL input
├── testing.sql           # Test SQL file
└── README.md
```

## ✨ Features

- **Modular Architecture**: Clean separation of concerns
- **Lexical Analysis**: Token generation and classification
- **Syntax Parsing**: ANTLR-based parser with visitor pattern
- **AST Construction**: Hierarchical AST representation
- **Semantic Analysis**: Symbol table, type checking, validation
- **Error Handling**: Comprehensive error reporting with colors
- **Visualization**: Browser-based AST and token visualization

## 🚀 Installation

### Prerequisites

- Python 3.8+
- Java 8+ (for ANTLR code generation)
- ANTLR 4.13.2

### Setup

1. Install Python dependencies:
```bash
pip install antlr4-python3-runtime
```

2. Generate parser and lexer (if needed):
```bash
# Using existing grammars
antlr4 -Dlanguage=Python3 -visitor grammars/BaseLexer.g4
antlr4 -Dlanguage=Python3 -visitor grammars/ExpressionParser.g4
antlr4 -Dlanguage=Python3 -visitor grammars/StatementParser.g4
antlr4 -Dlanguage=Python3 -visitor grammars/SQLParser.g4
```

## 📖 Usage

### Run Main Compiler
```bash
python main.py
```

This will:
1. Perform lexical analysis
2. Parse the SQL
3. Build the AST
4. Run semantic analysis
5. Open AST visualization in browser

### Run Lexer Tests
```bash
python testLexer.py
```

Features:
- Colored token output
- Syntax validation
- Semantic analysis
- Detailed reports

### Run Token Viewer (GUI)
```bash
python token_viewer.py
```

Opens a Tkinter GUI showing:
- Token table
- Error and warning dialogs
- Token statistics

## 🏗️ Architecture

### 1. Lexical Analysis (`lexers/`)

- **BaseLexer**: Wrapper for ANTLR lexer
- **TokenClassifier**: Token validation and classification

### 2. Parsing (`grammers/`)

Generated ANTLR parsers:
- Expression parser
- Statement parser
- Main SQL parser

### 3. AST Construction (`builders/`)

- **ExpressionBuilder**: Builds expression nodes
- **ConditionBuilder**: Builds condition nodes
- **StatementBuilder**: Builds statement nodes
- **AstBuilder**: Main builder coordinator

### 4. AST Nodes (`ast/`)

- **base_nodes**: Base classes
- **expression_nodes**: Expression AST nodes
- **statement_nodes**: Statement AST nodes
- **condition_nodes**: Condition AST nodes

### 5. Semantic Analysis (`semantic/`)

- **SymbolTable**: Manages tables, columns, variables
- **SemanticAnalyzer**: Validates semantics

### 6. Utilities (`utils/`)

- **ErrorHandler**: Centralized error management
- **Logger**: Logging functionality

## 🎨 Features in Detail

### Lexical Analysis
```python
from lexers.base_lexer import BaseLexer
from lexers.token_classifier import TokenClassifier

lexer = BaseLexer(sql_code)
tokens = lexer.get_token_list()

classifier = TokenClassifier()
classifier.validate_syntax(tokens, sql_code)
```

### AST Construction
```python
from builders.ast_builder import AstBuilder

builder = AstBuilder()
ast = builder.visit(parse_tree)
```

### Semantic Analysis
```python
from semantic.semantic_analyzer import SemanticAnalyzer

analyzer = SemanticAnalyzer()
errors, warnings = analyzer.analyze_tokens(tokens)
report = analyzer.generate_report()
```

### Error Handling
```python
from utils.error_handler import ErrorHandler

handler = ErrorHandler()
handler.add_error(line, col, message, "SEMANTIC")
handler.print_all()
```

## 📊 Supported SQL Features

- ✅ CREATE TABLE
- ✅ ALTER TABLE (ADD/DROP)
- ✅ SELECT (with WHERE, ORDER BY, FROM)
- ✅ INSERT (VALUES, SELECT, EXEC)
- ✅ UPDATE (with WHERE)
- ✅ DELETE (with WHERE)
- ✅ DECLARE variables
- ✅ SET variables
- ✅ IF statements
- ✅ BEGIN...END blocks
- ✅ TRY...CATCH blocks
- ✅ EXEC stored procedures
- ✅ CASE expressions
- ✅ Complex conditions (AND, OR, IN, IS NULL)

## 🧪 Testing

### Test Files

- `sqlInput.txt`: Main test SQL file
- `testing.sql`: Alternative test file

### Run Tests
```bash
# Test lexer
python testLexer.py

# Test full compiler
python main.py

# GUI token viewer
python token_viewer.py
```

## 📝 Example
```sql
CREATE TABLE [dbo].[Customers](
    [CustomerID] [int] NOT NULL,
    [FirstName] [nvarchar](50) NOT NULL,
    [LastName] [nvarchar](50) NULL
)

SELECT CustomerID, FirstName, LastName
FROM Customers
WHERE CustomerID > 100
ORDER BY LastName ASC;
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is for educational purposes.

## 🔗 Resources

- [ANTLR Documentation](https://www.antlr.org/)
- [Python dataclasses](https://docs.python.org/3/library/dataclasses.html)

SQL Server Documentation