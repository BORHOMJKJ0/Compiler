import json
import tempfile
import webbrowser
from antlr4 import *
from dataclasses import asdict, is_dataclass

from MyLexer import MyLexer
from MyParser import MyParser
from ast_builder import AstBuilder


def to_clean_dict(obj):
    """
    Recursively convert dataclass or list objects into dictionaries suitable for JSON.
    Adds a 'type' field for dataclass nodes.
    Skips any fields that are None, empty string, or empty list.
    """
    if is_dataclass(obj):
        result = {"type": obj.__class__.__name__}
        for k, v in asdict(obj).items():
            cleaned = to_clean_dict(v)
            # Skip None, empty string, empty list
            if cleaned is not None and cleaned != "" and cleaned != []:
                result[k] = cleaned
        return result
    elif isinstance(obj, list):
        lst = [to_clean_dict(i) for i in obj]
        # Remove any None or empty elements
        return [i for i in lst if i not in (None, "", [])]
    else:
        return obj


def main():
    sql = """
DELETE FROM Orders
    """

    # 1️⃣ Parse
    input_stream = InputStream(sql)
    lexer = MyLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    tokens.fill()
    parser = MyParser(tokens)
    tree = parser.sqlScript()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("❌ Syntax errors")
        return

    # 2️⃣ Build AST
    builder = AstBuilder()
    ast = builder.visit(tree)  # List[StatementNode]

    # 3️⃣ Print statement types
    print("=== STATEMENT TYPES ===")
    for i, stmt in enumerate(ast, start=1):
        print(f"{i}. {stmt.__class__.__name__}")

    # 4️⃣ Convert AST → JSON
    ast_json = json.dumps(to_clean_dict(ast), indent=2)

    # 5️⃣ Show JSON in browser
    html = f"""
<html>
<head>
    <title>AST Viewer</title>
    <style>
        body {{ font-family: monospace; background: #111; color: #eee; }}
        pre {{ white-space: pre-wrap; word-wrap: break-word; }}
    </style>
</head>
<body>
    <h2>Abstract Syntax Tree</h2>
    <pre>{ast_json}</pre>
</body>
</html>
"""

    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".html") as f:
        f.write(html)
        webbrowser.open(f.name)


if __name__ == "__main__":
    main()
