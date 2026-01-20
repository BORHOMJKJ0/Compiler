import sys
from antlr4 import *
from BaseLexer import BaseLexer
from SQLParser import SQLParser
from antlr4.tree.Trees import Trees


def get_tree_text(tree, parser, indent=0):
    name = Trees.getNodeText(tree, parser.ruleNames)
    result = "  " * indent + name + "\n"
    if tree.getChildCount() > 0:
        for i in range(tree.getChildCount()):
            result += get_tree_text(tree.getChild(i), parser, indent + 1)
    return result


def visualize(sql_file):
    try:
        with open(sql_file, 'r', encoding='utf-8') as f:
            input_text = f.read()

        input_stream = InputStream(input_text)
        lexer = BaseLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SQLParser(token_stream)

        tree = parser.parse()

        print(f"=== HIERARCHICAL PARSE TREE FOR: {sql_file} ===")
        print(get_tree_text(tree, parser))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    file_to_parse = "sqlInput.txt"
    if len(sys.argv) > 1:
        file_to_parse = sys.argv[1]
    visualize(file_to_parse)
