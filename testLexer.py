from antlr4 import *
from MyLexer import MyLexer

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
ORANGE = "\033[38;5;214m"


def colorize(ttype, text):
    if ttype == "NUMBER":
        return GREEN + text + RESET
    if ttype == "STRING":
        return MAGENTA + text + RESET
    if ttype == "IDENTIFIER":
        return BLUE + text + RESET
    if ttype == "KEYWORD":
        return YELLOW + text + RESET
    if ttype == "OPERATOR":
        return RED + text + RESET
    if ttype == "VARIABLE":
        return ORANGE + text + RESET
    return WHITE + text + RESET


def main():
    input_stream = FileStream("sqlInput.txt", encoding="utf-8")
    lexer = MyLexer(input_stream)
    tokens = lexer.getAllTokens()

    if not tokens:
        print("No tokens found!")
        return

    line_width = max(len(str(t.line)) for t in tokens) + 2
    col_width = max(len(str(t.column)) for t in tokens) + 2
    type_width = max(
        len(str(lexer.symbolicNames[t.type] or "UNKNOWN")) for t in tokens) + 2
    val_width = max(len(str(t.text)) for t in tokens) + 2

    print(CYAN + "┌" + "─"*(line_width) + "┬" + "─"*(col_width) +
          "┬" + "─"*(type_width) + "┬" + "─"*(val_width) + "┐" + RESET)
    print(f"│ {'Line'.ljust(line_width-1)} │ {'Column'.ljust(col_width-1)} │ {'Token Type'.ljust(type_width-1)} │ {'Value'.ljust(val_width-1)} │")
    print(CYAN + "├" + "─"*(line_width) + "┼" + "─"*(col_width) +
          "┼" + "─"*(type_width) + "┼" + "─"*(val_width) + "┤" + RESET)

    for token in tokens:
        ttype = lexer.symbolicNames[token.type] or "UNKNOWN"
        colored_value = colorize(ttype, token.text)

        ansi_length = len(colored_value) - len(token.text)
        adjusted_width = val_width + ansi_length - 1

        print(
            f"│ {str(token.line).ljust(line_width-1)} │ "
            f"{str(token.column).ljust(col_width-1)} │ "
            f"{ttype.ljust(type_width-1)} │ "
            f"{colored_value.ljust(adjusted_width)} │"
        )

    print(CYAN + "└" + "─"*(line_width) + "┴" + "─"*(col_width) +
          "┴" + "─"*(type_width) + "┴" + "─"*(val_width) + "┘" + RESET)
    print(f"\nTotal Tokens: {len(tokens)}")


if __name__ == "__main__":
    main()
