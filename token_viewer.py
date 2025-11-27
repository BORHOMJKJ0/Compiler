import tkinter as tk
from tkinter import ttk
from antlr4 import *
from MyLexer import MyLexer

TOKEN_COLORS = {
    "KEYWORD": "#f4d03f",
    "IDENTIFIER": "#5dade2",
    "STRING": "#af7ac5",
    "NUMBER": "#58d68d",
    "OPERATOR": "#ec7063",
    "VARIABLE": "#e67e22",
    "WS": "#eeeeee"
}


def load_tokens(filename="sqlInput.txt"):
    input_stream = FileStream(filename, encoding="utf-8")
    lexer = MyLexer(input_stream)
    tokens = lexer.getAllTokens()
    out = []
    for t in tokens:
        ttype = lexer.symbolicNames[t.type] or "UNKNOWN"
        out.append((t.line, t.column, ttype, t.text))
    return out


def main():
    tokens = load_tokens()

    window = tk.Tk()
    window.title("SQL Token Viewer")
    window.geometry("1050x600")

    style = ttk.Style(window)
    style.theme_use("default")
    style.configure("Treeview", rowheight=24, font=("Consolas", 11))
    style.configure("Treeview.Heading", font=("Consolas", 12, "bold"))

    frame = tk.Frame(window)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    tree = ttk.Treeview(frame, columns=(
        "line", "col", "type", "value"), show="headings")
    tree.heading("line", text="Line")
    tree.heading("col", text="Column")
    tree.heading("type", text="Token Type")
    tree.heading("value", text="Value")

    tree.column("line", width=70, anchor="center")
    tree.column("col", width=70, anchor="center")
    tree.column("type", width=200, anchor="w")
    tree.column("value", width=600, anchor="w")

    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(yscroll=vsb.set, xscroll=hsb.set)

    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    for line, col, ttype, value in tokens:
        tree.insert("", "end", values=(line, col, ttype, value), tags=(ttype,))

    for ttype, color in TOKEN_COLORS.items():
        tree.tag_configure(ttype, foreground=color)

    status = tk.Label(
        window, text=f"Total Tokens: {len(tokens)}", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status.pack(side=tk.BOTTOM, fill=tk.X)

    window.mainloop()


if __name__ == "__main__":
    main()
