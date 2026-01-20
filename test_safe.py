import sys
import signal
from pathlib import Path
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from datetime import datetime


class TimeoutError(Exception):
    pass


def timeout_handler(signum, frame):
    raise TimeoutError("Parsing timeout!")


class SQLErrorListener(ErrorListener):

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append({
            'line': line,
            'column': column,
            'message': msg[:200],
            'symbol': offendingSymbol.text[:50] if offendingSymbol else '<EOF>'
        })


class SafeParserTest:

    def __init__(self, timeout_seconds=5):
        self.timeout = timeout_seconds

        try:
            from BaseLexer import BaseLexer
            from SQLParser import SQLParser
            self.BaseLexer = BaseLexer
            self.SQLParser = SQLParser
            print("Successfully loaded BaseLexer and SQLParser\n")
        except ImportError as e:
            print(f"Error importing: {e}")
            sys.exit(1)

    def test_file(self, filepath):
        filepath = Path(filepath)

        print("=" * 80)
        print(f"TESTING: {filepath.name}")
        print("=" * 80)

        if not filepath.exists():
            print("File not found")
            return None

        with open(filepath, 'r', encoding='utf-8') as f:
            sql_code = f.read()

        lines = sql_code.strip().split('\n')
        print(f"File: {len(lines)} lines, {len(sql_code)} chars")

        try:
            if sys.platform != 'win32':
                signal.signal(signal.SIGALRM, timeout_handler)
                signal.alarm(self.timeout)

            start_time = datetime.now()

            print("Step 1/3: Lexing...")
            input_stream = InputStream(sql_code)
            lexer = self.BaseLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            token_stream.fill()

            token_count = len(token_stream.tokens)
            print(f"   Generated {token_count} tokens")

            print("Step 2/3: Parsing...")
            parser = self.SQLParser(token_stream)

            error_listener = SQLErrorListener()
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)

            tree = parser.sqlScript()

            end_time = datetime.now()
            parsing_time = (end_time - start_time).total_seconds() * 1000

            if sys.platform != 'win32':
                signal.alarm(0)

            print(f"   Completed in {parsing_time:.2f}ms")

            print("Step 3/3: Analyzing results...")

            if len(error_listener.errors) == 0:
                print(f"\n{'=' * 80}")
                print("SUCCESS - No syntax errors!")
                print(f"     Time: {parsing_time:.2f}ms")
                print(f"    Tokens: {token_count}")
                print(f"{'=' * 80}\n")
                return True
            else:
                print(f"\n{'=' * 80}")
                print(f" FAILED - {len(error_listener.errors)} error(s)")
                print(" First 3 errors:")
                for i, err in enumerate(error_listener.errors[:3], 1):
                    print(f"\n   Error {i}:")
                    print(f"      Line {err['line']}, Col {err['column']}")
                    print(f"      {err['message'][:100]}")
                    if err['symbol']:
                        print(f"      Near: '{err['symbol'][:30]}'")

                if len(error_listener.errors) > 3:
                    print(
                        f"\n   ... and {len(error_listener.errors) - 3} more")

                print(f"{'=' * 80}\n")
                return False

        except TimeoutError:
            print(f"\n{'=' * 80}")
            print(f"TIMEOUT - Parsing took too long (>{self.timeout}s)")
            print("   This indicates an infinite loop or left recursion problem")
            print(f"{'=' * 80}\n")
            return False

        except Exception as e:
            print(f"\n{'=' * 80}")
            print(f"EXCEPTION - {type(e).__name__}")
            print(f"   {str(e)[:200]}")
            print(f"{'=' * 80}\n")
            return False

        finally:
            if sys.platform != 'win32':
                signal.alarm(0)

    def test_simple_queries(self):
        print("\n" + "=" * 80)
        print("SIMPLE QUERY TESTS")
        print("=" * 80)

        tests = [
            ("SELECT 1;", "Literal"),
            ("SELECT * FROM T;", "Simple SELECT"),
            ("CREATE TABLE T (ID INT);", "Simple CREATE"),
            ("INSERT INTO T VALUES (1);", "Simple INSERT"),
        ]

        for sql, desc in tests:
            print(f"Test: {desc}")
            print(f"   SQL: {sql}")

            try:
                input_stream = InputStream(sql)
                lexer = self.BaseLexer(input_stream)
                token_stream = CommonTokenStream(lexer)
                parser = self.SQLParser(token_stream)

                error_listener = SQLErrorListener()
                parser.removeErrorListeners()
                parser.addErrorListener(error_listener)

                tree = parser.sqlScript()

                if len(error_listener.errors) == 0:
                    print("   PASS")
                else:
                    print(f"   FAIL - {len(error_listener.errors)} errors")
                    print(f"      {error_listener.errors[0]['message'][:80]}")

            except Exception as e:
                print(f"    EXCEPTION - {str(e)[:80]}")


def main():
    print("=" * 80)
    print("         SAFE SQL PARSER TEST (WITH TIMEOUT)")
    print("=" * 80)
    print()

    tester = SafeParserTest(timeout_seconds=10)

    tester.test_simple_queries()

    print("\n" + "=" * 80)
    print("TESTING FILES")
    print("=" * 80)

    files = ['sqlInput.txt', 'testing.sql',
             'train.sql', 'train2.sql', 'full_sql_test.sql']

    for filename in files:
        if Path(filename).exists():
            tester.test_file(filename)
        else:
            print(f"  Skipping {filename} - not found\n")

    print("=" * 80)
    print(" Testing completed!")
    print("=" * 80)


if __name__ == '__main__':
    main()
