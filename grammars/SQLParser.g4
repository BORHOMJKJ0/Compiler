parser grammar SQLParser;
options { tokenVocab=BaseLexer; }
import StatementParser;

// القاعدة الرئيسية
parse: sqlScript EOF;
