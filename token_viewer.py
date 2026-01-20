import tkinter as tk
from tkinter import ttk, messagebox
from antlr4 import *
from lexers.base_lexer import BaseLexer

TOKEN_COLORS = {
    "KEYWORD": "#f39c12",
    "IDENTIFIER": "#3498db",
    "BRACKET_IDENTIFIER": "#1abc9c",
    "STRING_SINGLE": "#9b59b6",
    "STRING_DOUBLE": "#8e44ad",
    "HEX_STRING": "#16a085",
    "BIT_STRING": "#8e44ad",
    "NUMBER": "#27ae60",
    "OPERATOR": "#e74c3c",
    "VARIABLE": "#e67e22",
    "PUNCTUATION": "#34495e",
    "INVALID_IDENTIFIER": "#c0392b",
    "LINE_COMMENT": "#95a5a6",
    "BLOCK_COMMENT_START": "#95a5a6",
    "COMMENT_CONTENT": "#95a5a6",
    "WS": "#ecf0f1"
}


def check_syntax_errors(tokens, lexer, input_text):
    errors = []
    warnings = []

    paren_count = 0

    for token in tokens:
        ttype = lexer.get_token_type_name(token.type)
        if token.text == '(':
            paren_count += 1
        elif token.text == ')':
            paren_count -= 1
            if paren_count < 0:
                errors.append(
                    f"Line {token.line}, Column {token.column}: Closing parenthesis ) without opening")
                paren_count = 0

        if ttype == "INVALID_IDENTIFIER":
            if token.text.startswith('_') and all(c == '_' for c in token.text):
                errors.append(
                    f"Line {token.line}, Column {token.column}: Invalid identifier '{token.text}' - Cannot use only underscores")
            elif token.text[0].isdigit():
                errors.append(
                    f"Line {token.line}, Column {token.column}: Invalid identifier '{token.text}' - Cannot start with digit")
            else:
                errors.append(
                    f"Line {token.line}, Column {token.column}: Invalid identifier '{token.text}'")

        if token.text.startswith('[') and token.text.endswith(']'):
            if "'" in token.text:
                warnings.append(
                    f"Line {token.line}, Column {token.column}: Identifier {token.text} contains single quote")

        if (token.text.startswith("'") and token.text.endswith("'")) or \
                (token.text.startswith('"') and token.text.endswith('"')):
            if "''" in token.text[1:-1] or '""' in token.text[1:-1]:
                warnings.append(
                    f"Line {token.line}, Column {token.column}: String contains escaped quotes")

        # Check for line continuation
        if ttype in ["STRING_SINGLE", "STRING_DOUBLE", "HEX_STRING", "BIT_STRING"]:
            if '\\' in token.text:
                warnings.append(
                    f"Line {token.line}, Column {token.column}: Contains line continuation character")

    if paren_count > 0:
        errors.append(f"Error: {paren_count} unclosed opening parenthesis")

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
                    errors.append(
                        f"Line {line_num}: Closing comment */ without opening /*")
                    comment_depth = 0
                i += 2
            else:
                i += 1

    if comment_depth > 0:
        errors.append(f"Error: {comment_depth} unclosed block comment")

    return errors, warnings


def load_tokens(filename="testing.sql"):
    try:
        input_text = open(filename, "r", encoding="utf-8").read()
        input_stream = InputStream(input_text)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found!")
    except Exception as e:
        raise Exception(f"Error reading file: {e}")

    with open("sqlInput.txt", "r") as f:
        input_text = f.read()
    lexer = BaseLexer(input_text)
    tokens = lexer.tokenize()

    errors, warnings = check_syntax_errors(tokens, lexer, input_text)

    out = []
    for t in tokens:
        ttype = lexer.get_token_type_name(t.type) or "UNKNOWN"
        out.append((t.line, t.column, ttype, t.text))

    return out, errors, warnings


def main():
    try:
        tokens, errors, warnings = load_tokens()
    except FileNotFoundError as e:
        messagebox.showerror("Error", str(e))
        return
    except Exception as e:
        messagebox.showerror("Error", f"Analysis error:\n{str(e)}")
        return

    window = tk.Tk()
    window.title("SQL Token Viewer")
    window.geometry("1200x700")
    window.configure(bg="#2c3e50")

    style = ttk.Style(window)
    style.theme_use("default")

    style.configure("Treeview",
                    background="#ecf0f1",
                    foreground="#2c3e50",
                    rowheight=28,
                    fieldbackground="#ecf0f1",
                    font=("Consolas", 10))
    style.configure("Treeview.Heading",
                    background="#34495e",
                    foreground="white",
                    font=("Arial", 11, "bold"))
    style.map('Treeview', background=[('selected', '#3498db')])

    header_frame = tk.Frame(window, bg="#34495e", height=80)
    header_frame.pack(fill=tk.X, padx=0, pady=0)

    title_label = tk.Label(header_frame,
                           text="Advanced SQL Lexical Analyzer",
                           font=("Arial", 20, "bold"),
                           bg="#34495e",
                           fg="white")
    title_label.pack(pady=15)

    if errors or warnings:
        error_frame = tk.Frame(window, bg="#2c3e50")
        error_frame.pack(fill=tk.X, padx=10, pady=5)

        if errors:
            error_label = tk.Label(error_frame,
                                   text=f"⚠ Errors: {len(errors)}",
                                   font=("Arial", 12, "bold"),
                                   bg="#e74c3c",
                                   fg="white",
                                   padx=10,
                                   pady=5)
            error_label.pack(side=tk.LEFT, padx=5)

            def show_errors():
                error_window = tk.Toplevel(window)
                error_window.title("Syntax Errors")
                error_window.geometry("900x400")
                error_window.configure(bg="#2c3e50")

                error_text = tk.Text(error_window,
                                     font=("Consolas", 10),
                                     bg="#ecf0f1",
                                     fg="#c0392b",
                                     wrap=tk.WORD)
                error_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                for error in errors:
                    error_text.insert(tk.END, f"✗ {error}\n\n")

                error_text.config(state=tk.DISABLED)

            error_btn = tk.Button(error_frame,
                                  text="Show Errors",
                                  command=show_errors,
                                  bg="#c0392b",
                                  fg="white",
                                  font=("Arial", 10, "bold"),
                                  cursor="hand2")
            error_btn.pack(side=tk.LEFT, padx=5)

        if warnings:
            warning_label = tk.Label(error_frame,
                                     text=f"⚠ Warnings: {len(warnings)}",
                                     font=("Arial", 12, "bold"),
                                     bg="#f39c12",
                                     fg="white",
                                     padx=10,
                                     pady=5)
            warning_label.pack(side=tk.LEFT, padx=5)

            def show_warnings():
                warning_window = tk.Toplevel(window)
                warning_window.title("Warnings")
                warning_window.geometry("900x400")
                warning_window.configure(bg="#2c3e50")

                warning_text = tk.Text(warning_window,
                                       font=("Consolas", 10),
                                       bg="#ecf0f1",
                                       fg="#d68910",
                                       wrap=tk.WORD)
                warning_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

                for warning in warnings:
                    warning_text.insert(tk.END, f"⚠ {warning}\n\n")

                warning_text.config(state=tk.DISABLED)

            warning_btn = tk.Button(error_frame,
                                    text="Show Warnings",
                                    command=show_warnings,
                                    bg="#d68910",
                                    fg="white",
                                    font=("Arial", 10, "bold"),
                                    cursor="hand2")
            warning_btn.pack(side=tk.LEFT, padx=5)

    frame = tk.Frame(window, bg="#2c3e50")
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    tree = ttk.Treeview(frame,
                        columns=("line", "col", "type", "value"),
                        show="headings",
                        selectmode="browse")

    tree.heading("line", text="Line")
    tree.heading("col", text="Column")
    tree.heading("type", text="Token Type")
    tree.heading("value", text="Value")

    tree.column("line", width=80, anchor="center")
    tree.column("col", width=80, anchor="center")
    tree.column("type", width=200, anchor="w")
    tree.column("value", width=700, anchor="w")

    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(yscroll=vsb.set, xscroll=hsb.set)

    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    for line, col, ttype, value in tokens:
        display_value = value if len(value) <= 100 else value[:97] + "..."
        tree.insert("", "end", values=(
            line, col, ttype, display_value), tags=(ttype,))

    for ttype, color in TOKEN_COLORS.items():
        tree.tag_configure(ttype, foreground=color)

    status_frame = tk.Frame(window, bg="#34495e")
    status_frame.pack(side=tk.BOTTOM, fill=tk.X)

    token_stats = {}
    for _, _, ttype, _ in tokens:
        token_stats[ttype] = token_stats.get(ttype, 0) + 1

    stats_text = f"Total Tokens: {len(tokens)}"
    if errors:
        stats_text += f"  |  Errors: {len(errors)}"
    if warnings:
        stats_text += f"  |  Warnings: {len(warnings)}"

    status_left = tk.Label(status_frame,
                           text=stats_text,
                           bd=1,
                           relief=tk.FLAT,
                           anchor=tk.W,
                           bg="#34495e",
                           fg="white",
                           font=("Arial", 10),
                           padx=10)
    status_left.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def show_stats():
        stats_window = tk.Toplevel(window)
        stats_window.title("Token Statistics")
        stats_window.geometry("500x600")
        stats_window.configure(bg="#2c3e50")

        title = tk.Label(stats_window,
                         text="Token Type Distribution",
                         font=("Arial", 16, "bold"),
                         bg="#34495e",
                         fg="white",
                         pady=10)
        title.pack(fill=tk.X)

        stats_frame = tk.Frame(stats_window, bg="#ecf0f1")
        stats_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        for i, (ttype, count) in enumerate(sorted(token_stats.items(), key=lambda x: -x[1])):
            color = TOKEN_COLORS.get(ttype, "#2c3e50")

            row_frame = tk.Frame(stats_frame, bg="#ecf0f1", pady=5)
            row_frame.pack(fill=tk.X)

            type_label = tk.Label(row_frame,
                                  text=ttype,
                                  font=("Consolas", 11),
                                  bg="#ecf0f1",
                                  fg=color,
                                  width=25,
                                  anchor="w")
            type_label.pack(side=tk.LEFT)

            count_label = tk.Label(row_frame,
                                   text=str(count),
                                   font=("Arial", 11, "bold"),
                                   bg="#ecf0f1",
                                   fg="#2c3e50")
            count_label.pack(side=tk.RIGHT)

    stats_btn = tk.Button(status_frame,
                          text="Show Statistics",
                          command=show_stats,
                          bg="#3498db",
                          fg="white",
                          font=("Arial", 9, "bold"),
                          cursor="hand2",
                          padx=15,
                          pady=3)
    stats_btn.pack(side=tk.RIGHT, padx=10, pady=5)

    if not errors:
        success_label = tk.Label(status_frame,
                                 text="✓ Analysis Successful",
                                 bg="#27ae60",
                                 fg="white",
                                 font=("Arial", 10, "bold"),
                                 padx=15,
                                 pady=3)
        success_label.pack(side=tk.RIGHT, padx=5, pady=5)

    window.mainloop()


if __name__ == "__main__":
    main()
