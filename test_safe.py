"""
Safe Parser Test with Timeout
اختبار آمن مع حد زمني لمنع التجميد
"""

import sys
import signal
from pathlib import Path
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from datetime import datetime


class TimeoutError(Exception):
    """خطأ تجاوز الوقت"""
    pass


def timeout_handler(signum, frame):
    """معالج تجاوز الوقت"""
    raise TimeoutError("Parsing timeout!")


class SQLErrorListener(ErrorListener):
    """مستمع الأخطاء"""

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append({
            'line': line,
            'column': column,
            'message': msg[:200],  # حد أقصى 200 حرف
            'symbol': offendingSymbol.text[:50] if offendingSymbol else '<EOF>'
        })


class SafeParserTest:
    """اختبار آمن مع timeout"""

    def __init__(self, timeout_seconds=5):
        self.timeout = timeout_seconds

        try:
            from BaseLexer import BaseLexer
            from SQLParser import SQLParser
            self.BaseLexer = BaseLexer
            self.SQLParser = SQLParser
            print("✅ Successfully loaded BaseLexer and SQLParser\n")
        except ImportError as e:
            print(f"❌ Error importing: {e}")
            sys.exit(1)

    def test_file(self, filepath):
        """اختبار ملف مع timeout"""
        filepath = Path(filepath)

        print("=" * 80)
        print(f"🧪 TESTING: {filepath.name}")
        print("=" * 80)

        if not filepath.exists():
            print(f"❌ File not found")
            return None

        with open(filepath, 'r', encoding='utf-8') as f:
            sql_code = f.read()

        # عرض معلومات الملف
        lines = sql_code.strip().split('\n')
        print(f"\n📊 File: {len(lines)} lines, {len(sql_code)} chars")

        # اختبار مع timeout
        try:
            # تفعيل timeout (Windows لا يدعم signal)
            if sys.platform != 'win32':
                signal.signal(signal.SIGALRM, timeout_handler)
                signal.alarm(self.timeout)

            start_time = datetime.now()

            # Lexing
            print(f"\n⏳ Step 1/3: Lexing...")
            input_stream = InputStream(sql_code)
            lexer = self.BaseLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            token_stream.fill()

            token_count = len(token_stream.tokens)
            print(f"   ✅ Generated {token_count} tokens")

            # Parsing
            print(f"\n⏳ Step 2/3: Parsing...")
            parser = self.SQLParser(token_stream)

            error_listener = SQLErrorListener()
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)

            tree = parser.sqlScript()

            end_time = datetime.now()
            parsing_time = (end_time - start_time).total_seconds() * 1000

            # إلغاء timeout
            if sys.platform != 'win32':
                signal.alarm(0)

            print(f"   ✅ Completed in {parsing_time:.2f}ms")

            # النتائج
            print(f"\n⏳ Step 3/3: Analyzing results...")

            if len(error_listener.errors) == 0:
                print(f"\n{'=' * 80}")
                print(f"✅ SUCCESS - No syntax errors!")
                print(f"   ⏱️  Time: {parsing_time:.2f}ms")
                print(f"   🎯 Tokens: {token_count}")
                print(f"{'=' * 80}\n")
                return True
            else:
                print(f"\n{'=' * 80}")
                print(f"❌ FAILED - {len(error_listener.errors)} error(s)")
                print(f"\n📋 First 3 errors:")
                for i, err in enumerate(error_listener.errors[:3], 1):
                    print(f"\n   Error {i}:")
                    print(f"      Line {err['line']}, Col {err['column']}")
                    print(f"      {err['message'][:100]}")
                    if err['symbol']:
                        print(f"      Near: '{err['symbol'][:30]}'")

                if len(error_listener.errors) > 3:
                    print(f"\n   ... and {len(error_listener.errors) - 3} more")

                print(f"{'=' * 80}\n")
                return False

        except TimeoutError:
            print(f"\n{'=' * 80}")
            print(f"⏰ TIMEOUT - Parsing took too long (>{self.timeout}s)")
            print(f"   This indicates an infinite loop or left recursion problem")
            print(f"{'=' * 80}\n")
            return False

        except Exception as e:
            print(f"\n{'=' * 80}")
            print(f"💥 EXCEPTION - {type(e).__name__}")
            print(f"   {str(e)[:200]}")
            print(f"{'=' * 80}\n")
            return False

        finally:
            # تأكد من إلغاء timeout
            if sys.platform != 'win32':
                signal.alarm(0)

    def test_simple_queries(self):
        """اختبار استعلامات بسيطة أولاً"""
        print("\n" + "=" * 80)
        print("🎯 SIMPLE QUERY TESTS")
        print("=" * 80)

        tests = [
            ("SELECT 1;", "Literal"),
            ("SELECT * FROM T;", "Simple SELECT"),
            ("CREATE TABLE T (ID INT);", "Simple CREATE"),
            ("INSERT INTO T VALUES (1);", "Simple INSERT"),
        ]

        for sql, desc in tests:
            print(f"\n📝 Test: {desc}")
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
                    print(f"   ✅ PASS")
                else:
                    print(f"   ❌ FAIL - {len(error_listener.errors)} errors")
                    print(f"      {error_listener.errors[0]['message'][:80]}")

            except Exception as e:
                print(f"   💥 EXCEPTION - {str(e)[:80]}")


def main():
    """الدالة الرئيسية"""
    print("=" * 80)
    print("         SAFE SQL PARSER TEST (WITH TIMEOUT)")
    print("=" * 80)
    print()

    tester = SafeParserTest(timeout_seconds=10)

    # اختبار استعلامات بسيطة أولاً
    tester.test_simple_queries()

    # ثم اختبار الملفات
    print("\n" + "=" * 80)
    print("📁 TESTING FILES")
    print("=" * 80)

    files = ['sqlInput.txt', 'testing.sql', 'train.sql', 'train2.sql']

    for filename in files:
        if Path(filename).exists():
            tester.test_file(filename)
        else:
            print(f"⚠️  Skipping {filename} - not found\n")

    print("=" * 80)
    print("✅ Testing completed!")
    print("=" * 80)


if __name__ == '__main__':
    main()