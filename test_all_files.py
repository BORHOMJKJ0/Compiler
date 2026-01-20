"""
Comprehensive SQL Parser Test Suite
نظام اختبار شامل لجميع ملفات SQL مع عرض شجرة التحليل
"""

import sys
from pathlib import Path
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from datetime import datetime
import json


class SQLErrorListener(ErrorListener):
    """مستمع الأخطاء"""

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append({
            'line': line,
            'column': column,
            'message': msg,
            'symbol': offendingSymbol.text if offendingSymbol else '<EOF>'
        })


class ComprehensiveTestSuite:
    """مجموعة اختبارات شاملة"""

    def __init__(self):
        # استيراد Lexer و Parser
        try:
            from BaseLexer import BaseLexer
            from SQLParser import SQLParser
            self.BaseLexer = BaseLexer
            self.SQLParser = SQLParser
            print("✅ Successfully loaded BaseLexer and SQLParser\n")
        except ImportError as e:
            print(f"❌ Error importing modules: {e}")
            print("   Make sure you have generated the parser files:")
            print("   antlr4 -Dlanguage=Python3 BaseLexer.g4")
            print("   antlr4 -Dlanguage=Python3 SQLParser.g4")
            sys.exit(1)

        self.results = {
            'timestamp': datetime.now().isoformat(),
            'test_files': [],
            'summary': {
                'total_files': 0,
                'passed_files': 0,
                'failed_files': 0,
                'total_errors': 0
            }
        }

    def test_file(self, filepath, description=""):
        """اختبار ملف SQL واحد"""
        filepath = Path(filepath)

        print("=" * 80)
        print(f"🧪 TESTING: {filepath.name}")
        if description:
            print(f"📝 Description: {description}")
        print("=" * 80)

        if not filepath.exists():
            print(f"❌ File not found: {filepath}")
            return None

        # قراءة الملف
        with open(filepath, 'r', encoding='utf-8') as f:
            sql_code = f.read()

        # عرض إحصائيات الملف
        lines = sql_code.strip().split('\n')
        print(f"\n📊 File Statistics:")
        print(f"   Lines: {len(lines)}")
        print(f"   Characters: {len(sql_code)}")
        print(f"   Size: {len(sql_code.encode('utf-8'))} bytes")

        # Parsing
        result = self._parse(sql_code, filepath.name)

        # عرض النتائج
        print(f"\n{'=' * 80}")
        if result['success']:
            print(f"✅ SUCCESS - File parsed successfully!")
            print(f"   ⏱️  Parsing Time: {result['parsing_time']:.2f}ms")
            print(f"   📏 Tree Depth: {result['tree_depth']}")
            print(f"   🌳 Node Count: {result['node_count']}")
            print(f"   🎯 Token Count: {result['token_count']}")
            
            # عرض شجرة التحليل بشكل مبسط
            print(f"\n🌳 PARSE TREE PREVIEW:")
            print("-" * 40)
            self._print_tree_preview(result['tree'], self.SQLParser.ruleNames)
            print("-" * 40)
            
        else:
            print(f"❌ FAILED - {len(result['errors'])} error(s) found")
            print(f"\n📋 Errors:")
            for i, err in enumerate(result['errors'][:5], 1):  # عرض أول 5 أخطاء
                print(f"\n   Error {i}:")
                print(f"      📍 Location: Line {err['line']}, Column {err['column']}")
                print(f"      💬 Message: {err['message'][:100]}...")
                print(f"      🔤 Near: '{err['symbol'][:30]}'")

            if len(result['errors']) > 5:
                print(f"\n   ... and {len(result['errors']) - 5} more errors")

        print(f"{'=' * 80}\n")

        # حفظ النتيجة (بدون كائن الشجرة لأنه غير قابل للتحويل لـ JSON بسهولة)
        save_result = result.copy()
        del save_result['tree']
        self.results['test_files'].append(save_result)
        self.results['summary']['total_files'] += 1

        if result['success']:
            self.results['summary']['passed_files'] += 1
        else:
            self.results['summary']['failed_files'] += 1
            self.results['summary']['total_errors'] += len(result['errors'])

        return result

    def _parse(self, sql_code, filename):
        """دالة داخلية للـ parsing"""
        start_time = datetime.now()

        try:
            # 1. Lexer
            input_stream = InputStream(sql_code)
            lexer = self.BaseLexer(input_stream)
            token_stream = CommonTokenStream(lexer)

            # عد التوكنز
            token_stream.fill()
            token_count = len(token_stream.tokens)

            # 2. Parser
            parser = self.SQLParser(token_stream)

            # Error listener
            error_listener = SQLErrorListener()
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)

            # 3. Parse
            tree = parser.sqlScript()

            end_time = datetime.now()
            parsing_time = (end_time - start_time).total_seconds() * 1000

            # النتائج
            return {
                'filename': filename,
                'success': len(error_listener.errors) == 0,
                'errors': error_listener.errors,
                'parsing_time': parsing_time,
                'tree_depth': self._get_tree_depth(tree),
                'node_count': self._count_nodes(tree),
                'token_count': token_count,
                'tree': tree
            }

        except Exception as e:
            end_time = datetime.now()
            parsing_time = (end_time - start_time).total_seconds() * 1000

            return {
                'filename': filename,
                'success': False,
                'errors': [{'line': 0, 'column': 0, 'message': str(e), 'symbol': ''}],
                'parsing_time': parsing_time,
                'tree_depth': 0,
                'node_count': 0,
                'token_count': 0,
                'tree': None
            }

    def _get_tree_depth(self, node, depth=0):
        """حساب عمق Parse Tree"""
        if node is None or node.getChildCount() == 0:
            return depth
        max_depth = depth
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            child_depth = self._get_tree_depth(child, depth + 1)
            max_depth = max(max_depth, child_depth)
        return max_depth

    def _count_nodes(self, node):
        """عد العقد في Parse Tree"""
        if node is None: return 0
        count = 1
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            count += self._count_nodes(child)
        return count

    def _print_tree_preview(self, node, rule_names, indent=0, max_lines=20):
        """طباعة معاينة للشجرة بشكل نصي"""
        if node is None or max_lines <= 0:
            return 0
        
        line_count = 1
        prefix = "  " * indent
        
        if isinstance(node, TerminalNode):
            print(f"{prefix}TOKEN: {node.getText()}")
        else:
            rule_index = node.getRuleIndex()
            rule_name = rule_names[rule_index] if rule_index < len(rule_names) else str(rule_index)
            print(f"{prefix}RULE: {rule_name}")
            
            for i in range(node.getChildCount()):
                if line_count >= max_lines:
                    if i == 0: print(f"{prefix}  ...")
                    break
                added_lines = self._print_tree_preview(node.getChild(i), rule_names, indent + 1, max_lines - line_count)
                line_count += added_lines
                
        return line_count

    def print_summary(self):
        """طباعة ملخص النتائج"""
        print("\n" + "=" * 80)
        print("📊 FINAL TEST SUMMARY")
        print("=" * 80)

        summary = self.results['summary']

        print(f"\n📁 Files Tested: {summary['total_files']}")
        print(f"✅ Passed: {summary['passed_files']}")
        print(f"❌ Failed: {summary['failed_files']}")

        if summary['total_files'] > 0:
            success_rate = (summary['passed_files'] / summary['total_files']) * 100
            print(f"📈 Success Rate: {success_rate:.1f}%")

        if summary['failed_files'] > 0:
            print(f"⚠️  Total Errors: {summary['total_errors']}")

        # تفاصيل كل ملف
        print(f"\n{'=' * 80}")
        print("📋 Detailed Results:")
        print(f"{'=' * 80}")

        for result in self.results['test_files']:
            status = "✅ PASS" if result['success'] else "❌ FAIL"
            errors = f" ({len(result['errors'])} errors)" if not result['success'] else ""
            print(f"{status:10} | {result['filename']:30} | {result['parsing_time']:8.2f}ms{errors}")

        # أفضل وأسوأ أداء
        if self.results['test_files']:
            print(f"\n{'=' * 80}")
            print("⏱️  Performance:")
            print(f"{'=' * 80}")

            times = [r['parsing_time'] for r in self.results['test_files']]
            avg_time = sum(times) / len(times)
            max_time = max(times)
            min_time = min(times)

            print(f"Average Parsing Time: {avg_time:.2f}ms")
            print(f"Fastest: {min_time:.2f}ms")
            print(f"Slowest: {max_time:.2f}ms")

        print(f"\n{'=' * 80}\n")

    def save_report(self, filename='test_report.json'):
        """حفظ تقرير JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        print(f"💾 Report saved to: {filename}")

    def test_specific_queries(self):
        """اختبار استعلامات محددة"""
        print("\n" + "=" * 80)
        print("🎯 SPECIFIC QUERY TESTS")
        print("=" * 80)

        test_cases = [
            # Test 1: Simple SELECT
            ("SELECT * FROM Users;", "Simple SELECT"),

            # Test 2: JOIN
            ("SELECT u.Name, o.Total FROM Users u INNER JOIN Orders o ON u.ID = o.UserID;",
             "INNER JOIN"),

            # Test 3: Subquery
            ("SELECT * FROM (SELECT ID FROM Users) AS T;",
             "Subquery"),

            # Test 4: CASE
            ("SELECT CASE WHEN x = 1 THEN 'A' ELSE 'B' END FROM T;",
             "CASE expression"),

            # Test 5: Multiple statements
            ("""
             CREATE TABLE T
             (
                 ID INT
             );
             INSERT INTO T
             VALUES (1);
             SELECT *
             FROM T;
             """, "Multiple statements"),

            # Test 6: DECLARE and SET
            ("""
                DECLARE @x INT;
                SET @x = 10;
                SELECT @x;
            """, "Variables"),

            # Test 7: IF statement
            ("""
                IF NOT EXISTS (SELECT 1 FROM T)
                BEGIN
                    INSERT INTO T VALUES (1);
                END
            """, "IF NOT EXISTS"),

            # Test 8: TRY-CATCH
            ("""
                BEGIN TRY
                    SELECT 1/0;
                END TRY
                BEGIN CATCH
                    SELECT ERROR_MESSAGE();
                END CATCH
            """, "TRY-CATCH"),
        ]

        passed = 0
        failed = 0

        for i, (sql, desc) in enumerate(test_cases, 1):
            print(f"\nTest {i}: {desc}")
            print("-" * 80)

            result = self._parse(sql.strip(), f"test_{i}.sql")

            if result['success']:
                print(f"✅ PASS - {result['parsing_time']:.2f}ms")
                # عرض الشجرة للاختبارات الصغيرة
                self._print_tree_preview(result['tree'], self.SQLParser.ruleNames, indent=1, max_lines=10)
                passed += 1
            else:
                print(f"❌ FAIL - {len(result['errors'])} errors")
                for err in result['errors'][:2]:
                    print(f"   Line {err['line']}: {err['message'][:80]}")
                failed += 1

        print(f"\n{'=' * 80}")
        print(f"Specific Tests Summary: {passed}/{len(test_cases)} passed")
        print(f"{'=' * 80}\n")


def main():
    """الدالة الرئيسية"""
    print("=" * 80)
    print("         COMPREHENSIVE SQL PARSER TEST SUITE")
    print("=" * 80)
    print()

    # إنشاء Test Suite
    suite = ComprehensiveTestSuite()

    # قائمة ملفات الاختبار
    test_files = [
        ('sqlInput.txt', 'Main test file - Complex DDL/DML'),
        ('testing.sql', 'Same as sqlInput - Duplicate test'),
        ('train.sql', 'Training queries - Various SQL patterns'),
        ('train2.sql', 'Advanced training - Constraints & JOINs'),
        ('full_sql_test.sql', 'Full SQL test - All features'),
    ]

    # اختبار كل ملف
    print("🚀 TESTING ALL SQL FILES")
    print("=" * 80)
    print()

    for filepath, description in test_files:
        if Path(filepath).exists():
            suite.test_file(filepath, description)
        else:
            print(f"⚠️  Skipping {filepath} - File not found\n")

    # اختبار استعلامات محددة
    suite.test_specific_queries()

    # طباعة الملخص النهائي
    suite.print_summary()

    # حفظ التقرير
    suite.save_report('parser_test_report.json')

    print("\n✅ All tests completed!")
    print("=" * 80)


if __name__ == '__main__':
    main()
