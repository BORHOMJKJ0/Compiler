from antlr4 import *
from lexers.base_lexer import BaseLexer
from lexers.token_classifier import TokenClassifier
from semantic.semantic_analyzer import SemanticAnalyzer
from utils.logger import Logger

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
    if ttype == "LINE_COMMENT" or ttype == "BLOCK_COMMENT_START":
        return GRAY + text + RESET
    return WHITE + text + RESET


def main():
    filename = "sqlInput.txt"
    logger = Logger("TestLexer")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            input_text = f.read()
    except FileNotFoundError:
        print(f"{RED}Error: File {filename} not found!{RESET}")
        return
    except Exception as e:
        print(f"{RED}Error reading file: {e}{RESET}")
        return

    logger.info(f"Reading file: {filename}")

    base_lexer = BaseLexer(input_text)
    tokens = base_lexer.get_token_list()

    if not tokens:
        print(f"{YELLOW}Warning: No tokens found!{RESET}")
        return

    logger.info(f"Tokens generated: {len(tokens)}")

    classifier = TokenClassifier()
    classifier.validate_syntax(tokens, input_text)

    print(f"\n{CYAN}{'=' * 80}")
    print(f"{'PERFORMING SEMANTIC ANALYSIS':^80}")
    print(f"{'=' * 80}{RESET}\n")

    semantic = SemanticAnalyzer()
    sem_errors, sem_warnings = semantic.analyze_tokens(tokens)

    all_errors = classifier.errors + [str(e) for e in sem_errors]
    all_warnings = classifier.warnings + [str(w) for w in sem_warnings]

    if all_errors:
        print(f"\n{RED}{'=' * 80}")
        print(f"{'ERRORS':^80}")
        print(f"{'=' * 80}{RESET}\n")
        for error in all_errors:
            print(f"{RED} {error}{RESET}")
        print()

    if all_warnings:
        print(f"\n{YELLOW}{'=' * 80}")
        print(f"{'WARNINGS':^80}")
        print(f"{'=' * 80}{RESET}\n")
        for warning in all_warnings:
            print(f"{YELLOW} {warning}{RESET}")
        print()

    with open("sqlInput.txt", "r") as f:
        input_text = f.read()
    lexer = BaseLexer(input_text)
    raw_tokens = lexer.tokenize()

    line_width = max(len(str(t.line)) for t in raw_tokens) + 2
    col_width = max(len(str(t.column)) for t in raw_tokens) + 2
    type_width = max(len(str(lexer.get_token_type_name(
        t.type) or "UNKNOWN")) for t in raw_tokens) + 2
    val_width = min(max(len(str(t.text)) for t in raw_tokens) + 2, 60)

    print(f"\n{CYAN}{'=' * 80}")
    print(f"{'TOKEN TABLE':^80}")
    print(f"{'=' * 80}{RESET}\n")

    print(CYAN + "┌" + "─" * line_width + "┬" + "─" * col_width +
          "┬" + "─" * type_width + "┬" + "─" * val_width + "┐" + RESET)
    print(f"│ {'Line'.ljust(line_width - 1)} │ {'Column'.ljust(col_width - 1)} │ "
          f"{'Token Type'.ljust(type_width - 1)} │ {'Value'.ljust(val_width - 1)} │")
    print(CYAN + "├" + "─" * line_width + "┼" + "─" * col_width +
          "┼" + "─" * type_width + "┼" + "─" * val_width + "┤" + RESET)

    for token in raw_tokens:
        ttype = lexer.get_token_type_name(token.type) or "UNKNOWN"
        display_value = token.text if len(
            token.text) <= 50 else token.text[:47] + "..."
        colored_value = colorize(ttype, display_value)

        ansi_length = len(colored_value) - len(display_value)
        adjusted_width = val_width + ansi_length - 1

        print(f"│ {str(token.line).ljust(line_width - 1)} │ "
              f"{str(token.column).ljust(col_width - 1)} │ "
              f"{ttype.ljust(type_width - 1)} │ "
              f"{colored_value.ljust(adjusted_width)} │")

    print(CYAN + "└" + "─" * line_width + "┴" + "─" * col_width +
          "┴" + "─" * type_width + "┴" + "─" * val_width + "┘" + RESET)

    print(f"\n{CYAN}{'=' * 80}{RESET}")
    token_types = {}
    for token in raw_tokens:
        ttype = lexer.get_token_type_name(token.type) or "UNKNOWN"
        token_types[ttype] = token_types.get(ttype, 0) + 1

    print(f"\n{GREEN}Total Tokens: {len(raw_tokens)}{RESET}")
    print(f"{RED}Errors: {len(all_errors)}{RESET}")
    print(f"{YELLOW}Warnings: {len(all_warnings)}{RESET}\n")

    print(f"{CYAN}Token Type Distribution:{RESET}")
    for ttype, count in sorted(token_types.items(), key=lambda x: -x[1]):
        print(f"  {colorize(ttype, ttype)}: {count}")

    print(f"\n{CYAN}{'=' * 80}")
    print(semantic.generate_report())

    if not all_errors:
        print(f"\n{GREEN}Analysis completed successfully without errors!{RESET}\n")
    else:
        print(f"\n{RED}Analysis failed! Please fix the errors above.{RESET}\n")


if __name__ == "__main__":
    main()
