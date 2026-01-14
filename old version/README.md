# Simple SQL Compiler (ANTLR + Python)

**Short description**

A small compiler front-end for a SQL-like language implemented with ANTLR and Python. This repository contains the lexer and parser grammars, generated parser/lexer code, a semantic analyzer, and small utilities for testing and token inspection.

---

## ✅ Features

- Lexer and parser implemented with ANTLR 4 (Python target)
- Semantic analysis stage to validate basic SQL semantics
- Test scripts and sample SQL files for quick iteration
- Utilities to inspect tokens and debug the lexer

---

## 📁 Repository structure

- `MyLexer.g4`, `MyParser.g4` — ANTLR grammar files
- `MyLexer.py`, `MyParser.py`, `MyLexer.tokens`, ... — generated and/or runtime artifacts
- `gen/` — optional output directory for regenerated ANTLR artifacts
- `semantic_analyzer.py` — semantic analyzer implementation
- `testLexer.py` — simple lexer tests
- `token_viewer.py` — helper to print tokens from an input
- `testing.sql`, `sqlInput.txt` — example SQL inputs

---

## 🔧 Requirements

- Java 8+ (for ANTLR code generation)
- Python 3.8+ (works with 3.8–3.11)
- `antlr4-python3-runtime` (install via pip)

Recommended (Windows):

```powershell
# Install Python deps
pip install antlr4-python3-runtime
```

If you plan to regenerate sources from grammars, download the ANTLR jar from https://www.antlr.org/download.html (e.g. `antlr-4.9.3-complete.jar`).

---

## 🏗️ Generate lexer/parser (if grammar changes)

1. Place `antlr-4.*-complete.jar` somewhere accessible.
2. From project root run (adjust version and path):

```bash
# example: regenerate into 'gen' folder
java -jar path/to/antlr-4.9.3-complete.jar -Dlanguage=Python3 -visitor -o gen MyLexer.g4 MyParser.g4
```

3. The `gen/` folder will contain updated `MyLexer.py`, `MyParser.py` and supporting files. If your project imports the generated modules, update Python import paths or copy generated files to the repo root as needed.

> ⚠️ On Windows, ensure `java` is on your PATH and use the correct path separators.

---

## ▶️ Usage

- Run lexer tests:

```bash
python testLexer.py
```

- Inspect tokens produced from `sqlInput.txt`:

```bash
python token_viewer.py sqlInput.txt
```

- Run the semantic analyzer (example):

```bash
python semantic_analyzer.py sqlInput.txt
```

If scripts expect command-line arguments, pass the input file path explicitly. Check the top of each script for usage examples.

---

## 🧪 Tests

This repository contains simple scripts for testing; add `pytest` style tests if you want automated test runs. Example:

```bash
pip install pytest
pytest -q
```

---

## 🤝 Contributing

- Open an issue for bugs or feature requests
- Submit pull requests for fixes and improvements
- When changing grammars, include regenerated `gen/` artifacts or provide clear instructions for regeneration

---

## 📄 License & Contact

Add a license file (`LICENSE`) if you plan to open-source the project. For questions, open an issue or contact the repository owner.

---

If you'd like, I can:
- add a `requirements.txt` and `Makefile` (or PowerShell script) for convenience
- regenerate the ANTLR artifacts and commit them

Tell me what you'd like next.