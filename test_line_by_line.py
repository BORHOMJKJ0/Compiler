"""
Statement-Based SQL Parser Test
اختبار Parser بناءً على SQL Statements الكاملة
"""

import sys
from pathlib import Path
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from datetime import datetime
import re


class SQLErrorListener(ErrorListener):
    """مستمع الأخطاء"""

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


class StatementBasedTester:
    """اختبار بناءً على Statements"""

    def __init__(self):
        try:
            from BaseLexer import BaseLexer
            from SQLParser import SQLParser
            self.BaseLexer = BaseLexer
            self.SQLParser = SQLParser
            print("✅ Successfully loaded BaseLexer and SQLParser\n")
        except ImportError as e:
            print(f"❌ Error importing: {e}")
            sys.exit(1)

    def split_into_statements(self, sql_code):
        """تقسيم SQL إلى statements بناءً على GO و semicolon"""
        # استبدل GO بـ separator
        sql_code = re.sub(r'\bGO\b', '\n---STATEMENT_SEPARATOR---\n', sql_code, flags=re.IGNORECASE)

        # قسّم على separator
        statements = []
        current = []

        for line in sql_code.split('\n'):
            if line.strip() == '---STATEMENT_SEPARATOR---':
                if current:
                    stmt = '\n'.join(current).strip()
                    if stmt:
                        statements.append(stmt)
                    current = []
            else:
                current.append(line)

        # آخر statement
        if current:
            stmt = '\n'.join(current).strip()
            if stmt:
                statements.append(stmt)

        return statements

    def test_statement(self, stmt_num, statement):
        """اختبار statement واحد"""
        try:
            start_time = datetime.now()

            # Lexing
            input_stream = InputStream(statement)
            lexer = self.BaseLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            token_stream.fill()

            token_count = len(token_stream.tokens)

            # Parsing
            parser = self.SQLParser(token_stream)
            error_listener = SQLErrorListener()
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)

            tree = parser.sqlScript()

            end_time = datetime.now()
            parsing_time = (end_time - start_time).total_seconds() * 1000

            # النتائج
            if len(error_listener.errors) == 0:
                return {
                    'status': 'SUCCESS',
                    'time': parsing_time,
                    'tokens': token_count,
                    'errors': []
                }
            else:
                return {
                    'status': 'FAILED',
                    'time': parsing_time,
                    'tokens': token_count,
                    'errors': error_listener.errors
                }

        except Exception as e:
            return {
                'status': 'EXCEPTION',
                'time': 0,
                'tokens': 0,
                'errors': [{'message': str(e)[:200]}]
            }

    def test_file(self, filepath):
        """اختبار ملف كامل"""
        filepath = Path(filepath)

        print("=" * 100)
        print(f"📁 TESTING FILE: {filepath.name}")
        print("=" * 100)

        if not filepath.exists():
            print(f"❌ File not found")
            return

        with open(filepath, 'r', encoding='utf-8') as f:
            sql_code = f.read()

        # تقسيم إلى statements
        statements = self.split_into_statements(sql_code)

        print(f"\n📊 File Statistics:")
        print(f"   Total Characters: {len(sql_code)}")
        print(f"   Total Lines: {len(sql_code.split(chr(10)))}")
        print(f"   Total Statements: {len(statements)}")
        print()

        # اختبار كل statement
        print("🔍 Testing each statement:")
        print("─" * 100)
        print(f"{'#':>3} | {'Status':^10} | {'Time':>8} | {'Tokens':>6} | {'Preview':<60}")
        print("─" * 100)

        results = []

        for i, stmt in enumerate(statements, 1):
            # Preview من أول سطر
            preview = stmt.split('\n')[0].strip()[:60]
            if len(stmt.split('\n')[0]) > 60:
                preview += "..."

            # اختبار
            result = self.test_statement(i, stmt)
            results.append(result)

            # عرض النتيجة
            if result['status'] == 'SUCCESS':
                icon = '✅'
                status = 'SUCCESS'
            elif result['status'] == 'FAILED':
                icon = '❌'
                status = 'FAILED'
            else:
                icon = '💥'
                status = 'EXCEPT'

            print(f"{i:3d} | {icon} {status:^8} | {result['time']:>7.1f}ms | {result['tokens']:>6d} | {preview}")

        print("─" * 100)

        # عرض تفاصيل الأخطاء
        failed = [r for r in results if r['status'] != 'SUCCESS']

        if failed:
            print(f"\n❌ FAILED STATEMENTS DETAILS:")
            print("=" * 100)

            for i, stmt in enumerate(statements, 1):
                result = results[i-1]
                if result['status'] != 'SUCCESS':
                    print(f"\n📋 Statement {i}:")
                    # عرض أول 5 أسطر من statement
                    lines = stmt.split('\n')[:5]
                    for line in lines:
                        print(f"   {line}")
                    num_lines = len(stmt.split('\n'))
                    if num_lines > 5:
                        print(f"   ... ({num_lines - 5} more lines)")

                    print(f"\n   Errors:")
                    for err in result['errors'][:3]:
                        print(f"      └─ Line {err.get('line', '?')}: {err['message'][:80]}")

        # الملخص
        success_count = sum(1 for r in results if r['status'] == 'SUCCESS')
        failed_count = len(results) - success_count

        print(f"\n{'=' * 100}")
        print("📊 SUMMARY")
        print("=" * 100)
        print(f"\n   Total Statements:  {len(results):3d}")
        print(f"   ✅ Success:        {success_count:3d} ({success_count/len(results)*100:.1f}%)")
        print(f"   ❌ Failed:         {failed_count:3d} ({failed_count/len(results)*100:.1f}%)")

        if results:
            times = [r['time'] for r in results if r['time'] > 0]
            if times:
                print(f"\n   Performance:")
                print(f"      Average: {sum(times)/len(times):.1f}ms")
                print(f"      Max:     {max(times):.1f}ms")
                print(f"      Min:     {min(times):.1f}ms")

        print("=" * 100)

        return success_count == len(results)


def main():
    """الدالة الرئيسية"""
    print("=" * 100)
    print("         STATEMENT-BASED SQL PARSER TEST")
    print("=" * 100)
    print()

    tester = StatementBasedTester()

    # اختبار الملفات
    files = [
        ('sqlInput.txt', 'Main test file'),
        ('testing.sql', 'Testing file'),
        ('train.sql', 'Training queries'),
        ('train2.sql', 'Advanced training'),
    ]

    results = {}

    for filename, description in files:
        if Path(filename).exists():
            print(f"\n📝 {description}")
            success = tester.test_file(filename)
            results[filename] = success
        else:
            print(f"\n⚠️  Skipping {filename} - not found")

    # ملخص نهائي
    print("\n" + "=" * 100)
    print("🏁 FINAL RESULTS")
    print("=" * 100)

    for filename, success in results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"   {status} - {filename}")

    total_pass = sum(1 for s in results.values() if s)
    print(f"\n   Overall: {total_pass}/{len(results)} files passed")
    print("=" * 100)


if __name__ == '__main__':
    main()