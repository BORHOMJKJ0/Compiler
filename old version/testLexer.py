from antlr4 import *
from MyLexer import MyLexer
from semantic_analyzer import SemanticAnalyzer

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
ORANGE = "\033[38;5;214m"
GRAY = "\033[90m"
PURPLE = "\033[38;5;141m"
LIME = "\033[38;5;118m"


def colorize(ttype, text):
    if ttype == "NUMBER":
        return GREEN + text + RESET
    if ttype == "HEX_STRING":
        return LIME + text + RESET
    if ttype == "BIT_STRING":
        return PURPLE + text + RESET
    if ttype == "STRING_SINGLE" or ttype == "STRING_DOUBLE":
        return MAGENTA + text + RESET
    if ttype == "BRACKET_IDENTIFIER":
        return CYAN + text + RESET
    if ttype == "IDENTIFIER":
        return BLUE + text + RESET
    if ttype == "KEYWORD":
        return YELLOW + text + RESET
    if ttype == "OPERATOR":
        return RED + text + RESET
    if ttype == "VARIABLE":
        return ORANGE + text + RESET
    if ttype == "PUNCTUATION":
        return WHITE + text + RESET
    if ttype == "INVALID_IDENTIFIER":
        return RED + text + RESET
    if ttype == "LINE_COMMENT" or ttype == "BLOCK_COMMENT_START" or ttype == "COMMENT_CONTENT":
        return GRAY + text + RESET
    return WHITE + text + RESET


def check_syntax_errors(tokens, lexer, input_text):
    errors = []
    warnings = []

    paren_count = 0
    bracket_count = 0

    for token in tokens:
        ttype = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else "UNKNOWN"

        if token.text == '(':
            paren_count += 1
        elif token.text == ')':
            paren_count -= 1
            if paren_count < 0:
                errors.append(f"Line {token.line}, Column {token.column}: Closing parenthesis ) without opening")
                paren_count = 0

        if token.text == '[':
            bracket_count += 1
        elif token.text == ']':
            bracket_count -= 1
            if bracket_count < 0:
                errors.append(f"Line {token.line}, Column {token.column}: Closing bracket ] without opening")
                bracket_count = 0

        if ttype == "INVALID_IDENTIFIER":
            if token.text.startswith('_') and all(c == '_' for c in token.text):
                errors.append(
                    f"Line {token.line}, Column {token.column}: Invalid identifier '{token.text}' - Cannot use only underscores")
            elif token.text[0].isdigit():
                errors.append(
                    f"Line {token.line}, Column {token.column}: Invalid identifier '{token.text}' - Cannot start with digit")
            else:
                errors.append(f"Line {token.line}, Column {token.column}: Invalid identifier '{token.text}'")

        if ttype in ["IDENTIFIER", "BRACKET_IDENTIFIER"]:
            if "'" in token.text and not token.text.startswith('['):
                warnings.append(
                    f"Line {token.line}, Column {token.column}: Identifier '{token.text}' contains apostrophe - consider using bracket notation [...]")

        if token.text.startswith('[') and token.text.endswith(']'):
            if "'" in token.text:
                warnings.append(
                    f"Line {token.line}, Column {token.column}: Bracket identifier {token.text} contains apostrophe")

        if (token.text.startswith("'") and token.text.endswith("'")) or \
                (token.text.startswith('"') and token.text.endswith('"')):
            if "''" in token.text[1:-1]:
                warnings.append(f"Line {token.line}, Column {token.column}: String contains escaped single quotes")
            if '""' in token.text[1:-1]:
                warnings.append(f"Line {token.line}, Column {token.column}: String contains escaped double quotes")

        if ttype in ["STRING_SINGLE", "STRING_DOUBLE", "HEX_STRING", "BIT_STRING"]:
            if '\\' in token.text and ('\n' in token.text or '\r' in token.text):
                warnings.append(f"Line {token.line}, Column {token.column}: String/Number contains line continuation")

    if paren_count > 0:
        errors.append(f"Error: {paren_count} unclosed opening parenthesis")
    elif paren_count < 0:
        errors.append(f"Error: {abs(paren_count)} extra closing parenthesis")

    if bracket_count > 0:
        errors.append(f"Error: {bracket_count} unclosed opening bracket")
    elif bracket_count < 0:
        errors.append(f"Error: {abs(bracket_count)} extra closing bracket")

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
                    errors.append(f"Line {line_num}: Closing comment */ without opening /*")
                    comment_depth = 0
                i += 2
            else:
                i += 1

    if comment_depth > 0:
        errors.append(f"Error: {comment_depth} unclosed block comment(s)")

    return errors, warnings


def main():
    filename = "sqlInput.txt"

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            input_text = f.read()

        input_stream = InputStream(input_text)

    except FileNotFoundError:
        print(f"{RED}Error: File {filename} not found!{RESET}")
        return
    except Exception as e:
        print(f"{RED}Error reading file: {e}{RESET}")
        return

    lexer = MyLexer(input_stream)
    tokens = lexer.getAllTokens()

    if not tokens:
        print(f"{YELLOW}Warning: No tokens found!{RESET}")
        return

    lex_errors, lex_warnings = check_syntax_errors(tokens, lexer, input_text)

    token_list = []
    for token in tokens:
        ttype = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else "UNKNOWN"
        token_list.append((token.line, token.column, ttype, token.text))

    print(f"\n{CYAN}{'=' * 80}")
    print(f"{'  PERFORMING SEMANTIC ANALYSIS  ':^80}")
    print(f"{'=' * 80}{RESET}\n")

    semantic = SemanticAnalyzer()
    sem_errors, sem_warnings = semantic.analyze_tokens(token_list)

    all_errors = lex_errors + [str(e) for e in sem_errors]
    all_warnings = lex_warnings + [str(w) for w in sem_warnings]

    if all_errors:
        print(f"\n{RED}{'=' * 80}")
        print(f"{'  ERRORS  ':^80}")
        print(f"{'=' * 80}{RESET}\n")
        for error in all_errors:
            print(f"{RED}✗ {error}{RESET}")
        print()

    if all_warnings:
        print(f"\n{YELLOW}{'=' * 80}")
        print(f"{'  WARNINGS  ':^80}")
        print(f"{'=' * 80}{RESET}\n")
        for warning in all_warnings:
            print(f"{YELLOW}⚠ {warning}{RESET}")
        print()

    line_width = max(len(str(t.line)) for t in tokens) + 2
    col_width = max(len(str(t.column)) for t in tokens) + 2
    type_width = max(len(str(lexer.symbolicNames[t.type] or "UNKNOWN")) for t in tokens) + 2
    val_width = min(max(len(str(t.text)) for t in tokens) + 2, 60)

    print(f"\n{CYAN}{'=' * 80}")
    print(f"{'  TOKEN TABLE  ':^80}")
    print(f"{'=' * 80}{RESET}\n")

    print(CYAN + "┌" + "─" * (line_width) + "┬" + "─" * (col_width) +
          "┬" + "─" * (type_width) + "┬" + "─" * (val_width) + "┐" + RESET)
    print(
        f"│ {'Line'.ljust(line_width - 1)} │ {'Column'.ljust(col_width - 1)} │ {'Token Type'.ljust(type_width - 1)} │ {'Value'.ljust(val_width - 1)} │")
    print(CYAN + "├" + "─" * (line_width) + "┼" + "─" * (col_width) +
          "┼" + "─" * (type_width) + "┼" + "─" * (val_width) + "┤" + RESET)

    for token in tokens:
        ttype = lexer.symbolicNames[token.type] or "UNKNOWN"
        display_value = token.text if len(token.text) <= 50 else token.text[:47] + "..."
        colored_value = colorize(ttype, display_value)

        ansi_length = len(colored_value) - len(display_value)
        adjusted_width = val_width + ansi_length - 1

        print(
            f"│ {str(token.line).ljust(line_width - 1)} │ "
            f"{str(token.column).ljust(col_width - 1)} │ "
            f"{ttype.ljust(type_width - 1)} │ "
            f"{colored_value.ljust(adjusted_width)} │"
        )

    print(CYAN + "└" + "─" * (line_width) + "┴" + "─" * (col_width) +
          "┴" + "─" * (type_width) + "┴" + "─" * (val_width) + "┘" + RESET)

    print(f"\n{CYAN}{'=' * 80}{RESET}")
    token_types = {}
    for token in tokens:
        ttype = lexer.symbolicNames[token.type] or "UNKNOWN"
        token_types[ttype] = token_types.get(ttype, 0) + 1

    print(f"\n{GREEN}Total Tokens: {len(tokens)}{RESET}")
    print(f"{RED}Errors: {len(all_errors)}{RESET}")
    print(f"{YELLOW}Warnings: {len(all_warnings)}{RESET}\n")

    print(f"{CYAN}Token Type Distribution:{RESET}")
    for ttype, count in sorted(token_types.items(), key=lambda x: -x[1]):
        print(f"  {colorize(ttype, ttype)}: {count}")

    print(f"\n{CYAN}{'=' * 80}")
    print(semantic.generate_report())

    if not all_errors:
        print(f"\n{GREEN}✓ Analysis completed successfully without errors!{RESET}\n")
    else:
        print(f"\n{RED}✗ Analysis failed! Please fix the errors above.{RESET}\n")


if __name__ == "__main__":
    main()