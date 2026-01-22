import json
import os
import tempfile
import webbrowser
from antlr4 import *
from antlr4.tree.Tree import TerminalNode
from dataclasses import asdict, is_dataclass

from lexers.base_lexer import BaseLexer
from BaseLexer import BaseLexer as MyBaseLexer
from SQLParser import SQLParser as MyParser
from builders.ast_builder import AstBuilder
from lexers.token_classifier import TokenClassifier
from semantic.semantic_analyzer import SemanticAnalyzer
from utils.error_handler import ErrorHandler
from utils.logger import Logger


def to_clean_dict(obj):
    if is_dataclass(obj):
        result = {"type": obj.__class__.__name__}
        for k, v in asdict(obj).items():
            cleaned = to_clean_dict(v)
            if cleaned is not None and cleaned != "" and cleaned != []:
                result[k] = cleaned
        return result
    elif isinstance(obj, list):
        lst = [to_clean_dict(i) for i in obj]
        return [i for i in lst if i not in (None, "", [])]
    else:
        return obj


def get_tree_structure(node, rule_names, indent=0):
    if node is None:
        return []
    lines = []
    prefix = "  " * indent
    if isinstance(node, TerminalNode):
        lines.append(f"{prefix}TOKEN: {node.getText()}")
    else:
        rule_index = node.getRuleIndex()
        rule_name = rule_names[rule_index] if rule_index < len(
            rule_names) else str(rule_index)
        lines.append(f"{prefix}RULE: {rule_name}")
        for i in range(node.getChildCount()):
            lines.extend(get_tree_structure(
                node.getChild(i), rule_names, indent + 1))
    return lines


def get_tree_data_for_visualization(node, rule_names, node_id=0, parent_id=None):
    if node is None:
        return [], [], node_id
    nodes, edges = [], []
    current_id = node_id
    node_id += 1
    if isinstance(node, TerminalNode):
        nodes.append({
            "id": current_id, "label": node.getText(), "type": "token", "shape": "box",
            "color": "#ce9178", "font": {"size": 22, "color": "white"}
        })
    else:
        rule_index = node.getRuleIndex()
        rule_name = rule_names[rule_index] if rule_index < len(
            rule_names) else str(rule_index)
        nodes.append({
            "id": current_id, "label": rule_name, "type": "rule", "shape": "ellipse",
            "color": "#4ec9b0", "font": {"size": 24, "color": "white", "bold": True}
        })
        for i in range(node.getChildCount()):
            child_nodes, child_edges, node_id = get_tree_data_for_visualization(
                node.getChild(i), rule_names, node_id, current_id)
            nodes.extend(child_nodes)
            edges.extend(child_edges)
    if parent_id is not None:
        edges.append({"from": parent_id, "to": current_id})
    return nodes, edges, node_id


def convert_ast_to_tree(ast_obj, node_id=0, parent_id=None, key_name=None):
    nodes, edges = [], []
    current_id = node_id
    node_id += 1

    if isinstance(ast_obj, dict):
        node_type = ast_obj.get('type', key_name if key_name else 'Node')
        label = node_type.replace('Node', '')
        nodes.append({
            "id": current_id, "label": label, "type": "ast_node", "shape": "box",
            "color": "#c586c0", "font": {"size": 26, "bold": True, "color": "white"},
            "margin": 15
        })
        if parent_id is not None:
            edges.append({"from": parent_id, "to": current_id})
        for key, value in ast_obj.items():
            if key == 'type' or value is None or value == "" or value == []:
                continue
            if isinstance(value, (dict, list)):
                child_nodes, child_edges, node_id = convert_ast_to_tree(
                    value, node_id, current_id, key)
                nodes.extend(child_nodes)
                edges.extend(child_edges)
            else:
                nodes.append({
                    "id": node_id, "label": f"{key}: {str(value)}", "type": "ast_value", "shape": "box",
                    "color": "#dcdcaa", "font": {"size": 22, "color": "#1e1e1e"}
                })
                edges.append({"from": current_id, "to": node_id})
                node_id += 1
    elif isinstance(ast_obj, list):
        list_label = key_name if key_name else "List"
        nodes.append({
            "id": current_id, "label": list_label, "type": "ast_list", "shape": "diamond",
            "color": "#569cd6", "font": {"size": 20, "color": "white"}
        })
        if parent_id is not None:
            edges.append({"from": parent_id, "to": current_id})
        for item in ast_obj:
            if item is None or item == "" or item == []:
                continue
            child_nodes, child_edges, node_id = convert_ast_to_tree(
                item, node_id, current_id, list_label.rstrip('s'))
            nodes.extend(child_nodes)
            edges.extend(child_edges)
    else:
        nodes.append({
            "id": current_id, "label": str(ast_obj), "type": "ast_value", "shape": "box",
            "color": "#dcdcaa", "font": {"size": 22, "color": "#1e1e1e"}
        })
        if parent_id is not None:
            edges.append({"from": parent_id, "to": current_id})
    return nodes, edges, node_id


def process_file(file_path, logger):
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            sql = f.read()
    except Exception as e:
        return None, f"Error reading file: {e}"

    base_lexer = BaseLexer(sql)
    tokens = base_lexer.get_token_list()
    classifier = TokenClassifier()
    classifier.validate_syntax(tokens, sql)

    custom_lexer = BaseLexer(sql)
    processed_sql = custom_lexer.processed_text

    lexer = MyBaseLexer(InputStream(processed_sql))
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    parser = MyParser(token_stream)
    tree = parser.sqlScript()

    parse_tree_lines = get_tree_structure(tree, MyParser.ruleNames)
    nodes, edges, _ = get_tree_data_for_visualization(tree, MyParser.ruleNames)

    builder = AstBuilder()
    ast = builder.visit(tree)
    ast_json = json.dumps(to_clean_dict(ast), indent=2, ensure_ascii=False)

    semantic_analyzer = SemanticAnalyzer()
    sem_errors, sem_warnings = semantic_analyzer.analyze_tokens(tokens)

    return {
        "sql": sql,
        "tokens_count": len(tokens),
        "parse_tree": "\n".join(parse_tree_lines),
        "nodes": nodes,
        "edges": edges,
        "ast_json": ast_json,
        "errors": parser.getNumberOfSyntaxErrors() if hasattr(parser, 'getNumberOfSyntaxErrors') else 0,
        "warnings": len(classifier.warnings) + len(sem_warnings),
        "report": semantic_analyzer.generate_report()
    }, None


def create_tree_visualization(result, filename):
    parse_nodes_json = json.dumps(result['nodes'], ensure_ascii=False)
    parse_edges_json = json.dumps(result['edges'], ensure_ascii=False)
    ast_dict = json.loads(result['ast_json'])
    ast_nodes, ast_edges, _ = convert_ast_to_tree(ast_dict)
    ast_nodes_json = json.dumps(ast_nodes, ensure_ascii=False)
    ast_edges_json = json.dumps(ast_edges, ensure_ascii=False)

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SQL Visualizer - {filename}</title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/vis-network.min.js"></script>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #1e1e1e; color: #d4d4d4; overflow: hidden; }}
            .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 15px 30px; display: flex; justify-content: space-between; align-items: center; }}
            .header h1 {{ color: white; font-size: 22px; }}
            .tree-selector {{ display: flex; gap: 10px; }}
            .tree-btn {{ padding: 8px 16px; background: rgba(255,255,255,0.2); color: white; border: 2px solid white; border-radius: 6px; cursor: pointer; font-weight: 600; transition: 0.3s; }}
            .tree-btn.active {{ background: white; color: #667eea; }}
            .container {{ display: flex; height: calc(100vh - 65px); }}
            .sidebar {{ width: 280px; background: #252526; padding: 20px; border-right: 1px solid #3e3e42; overflow-y: auto; }}
            .info-box {{ background: #1e1e1e; padding: 12px; border-radius: 6px; margin-bottom: 15px; border-left: 3px solid #4ec9b0; }}
            .info-box label {{ color: #858585; font-size: 11px; display: block; }}
            .info-box .value {{ color: #d4d4d4; font-size: 16px; font-weight: 600; }}
            .main-content {{ flex: 1; position: relative; background: #1e1e1e; }}
            #network {{ width: 100%; height: 100%; }}
            .legend-item {{ display: flex; align-items: center; gap: 8px; margin-bottom: 6px; font-size: 12px; }}
            .color-box {{ width: 12px; height: 12px; border-radius: 2px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1> SQL Compiler Visualizer - {filename}</h1>
            <div class="tree-selector">
                <button id="parseTreeBtn" class="tree-btn active" onclick="showParseTree()">Parse Tree</button>
                <button id="astTreeBtn" class="tree-btn" onclick="showASTTree()">AST Tree</button>
            </div>
        </div>
        <div class="container">
            <div class="sidebar">
                <h3>Analysis Info</h3>
                <div class="info-box"><label>Tokens</label><div class="value">{result['tokens_count']}</div></div>
                <div class="info-box"><label>Syntax Errors</label><div class="value">{result['errors']}</div></div>
                <div class="info-box"><label>Warnings</label><div class="value">{result['warnings']}</div></div>
                <div style="margin-top: 20px;">
                    <h3>Legend</h3>
                    <div id="parseLegend">
                        <div class="legend-item"><div class="color-box" style="background: #4ec9b0;"></div><span>Rule Node</span></div>
                        <div class="legend-item"><div class="color-box" style="background: #ce9178;"></div><span>Token</span></div>
                    </div>
                    <div id="astLegend" style="display: none;">
                        <div class="legend-item"><div class="color-box" style="background: #c586c0;"></div><span>AST Node</span></div>
                        <div class="legend-item"><div class="color-box" style="background: #569cd6;"></div><span>List / Group</span></div>
                        <div class="legend-item"><div class="color-box" style="background: #dcdcaa;"></div><span>Value</span></div>
                    </div>
                </div>
            </div>
            <div class="main-content"><div id="network"></div></div>
        </div>
        <script>
            const parseNodes = {parse_nodes_json};
            const parseEdges = {parse_edges_json};
            const astNodes = {ast_nodes_json};
            const astEdges = {ast_edges_json};
            let network = null;
            function draw(nodes, edges, isAst) {{
                const container = document.getElementById('network');
                const data = {{ nodes: new vis.DataSet(nodes), edges: new vis.DataSet(edges) }};
                const options = {{
                    layout: {{ hierarchical: {{ direction: 'UD', sortMethod: 'directed', nodeSpacing: isAst ? 400 : 250, levelSeparation: 250 }} }},
                    physics: {{ enabled: false }},
                    interaction: {{ hover: true, navigationButtons: true, keyboard: true }}
                }};
                network = new vis.Network(container, data, options);
                network.once('afterDrawing', function() {{
                    network.moveTo({{ position: {{x: 0, y: 0}}, scale: 0.5, animation: false }});
                }});
            }}
            function showParseTree() {{
                document.getElementById('parseTreeBtn').classList.add('active');
                document.getElementById('astTreeBtn').classList.remove('active');
                document.getElementById('parseLegend').style.display = 'block';
                document.getElementById('astLegend').style.display = 'none';
                draw(parseNodes, parseEdges, false);
            }}
            function showASTTree() {{
                document.getElementById('astTreeBtn').classList.add('active');
                document.getElementById('parseTreeBtn').classList.remove('active');
                document.getElementById('astLegend').style.display = 'block';
                document.getElementById('parseLegend').style.display = 'none';
                draw(astNodes, astEdges, true);
            }}
            window.onload = showParseTree;
        </script>
    </body>
    </html>
    """
    return html


def main():
    logger = Logger("SQLCompiler")
    files = [f for f in os.listdir('.') if f.endswith(
        '.sql') or f.endswith('.txt')]
    files = [f for f in files if f in ['sqlInput.txt', 'testing.sql',
                                       'train.sql', 'train2.sql', 'full_sql_test.sql']]
    if not files:
        print("No SQL files found.")
        return
    while True:
        print("\n" + "=" * 60)
        print("SQL COMPILER - INTERACTIVE DASHBOARD")
        print("=" * 60)
        for i, f in enumerate(files, 1):
            print(f"{i}. {f}")
        print("0. Exit")
        print("=" * 60)
        choice = input("Select a file (0-{}): ".format(len(files)))
        if choice == '0':
            break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(files):
                selected_file = files[idx]
                print(f"Analyzing {selected_file}...")

                result, error = process_file(selected_file, logger)

                if error:
                    print(f"Error: {error}")
                    continue
                print(
                    f"Analysis Complete! Tokens: {result['tokens_count']}, Errors: {result['errors']}")
                while True:
                    print("\nOptions:")
                    print("1. View Trees in Browser (Visual)")
                    print("2. View Parse Tree (Console)")
                    print("3. View AST JSON (Console)")
                    print("4. Back to file list")
                    sub = input("Choice: ")
                    if sub == '1':
                        html = create_tree_visualization(result, selected_file)
                        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".html", encoding='utf-8') as f:
                            f.write(html)
                            webbrowser.open(f.name)
                            print("Visualization opened in browser.")
                    elif sub == '2':
                        print("\n=== PARSE TREE PREVIEW ===")
                        lines = result['parse_tree'].split('\n')
                        for line in lines[:100]:
                            print(line)
                        if len(lines) > 100:
                            print(f"... ({len(lines)-100} more lines)")
                    elif sub == '3':
                        print("\n=== AST JSON ===")
                        print(result['ast_json'][:2000])
                        if len(result['ast_json']) > 2000:
                            print("... (truncated)")
                    elif sub == '4':
                        break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
