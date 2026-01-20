parser grammar SQLParser;
options { tokenVocab=BaseLexer; }
import StatementParser;

parse: sqlScript EOF;
