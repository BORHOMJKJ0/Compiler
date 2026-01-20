from antlr4 import InputStream
from BaseLexer import BaseLexer as GeneratedLexer
import re


class BaseLexer:

    def __init__(self, input_text: str):
        self.original_text = input_text
        self.processed_text = self._preprocess_comments(input_text)
        self.input_stream = InputStream(self.processed_text)
        self.lexer = GeneratedLexer(self.input_stream)
        self._tokens = None

    def _preprocess_comments(self, text: str) -> str:
        result = list(text)
        i = 0
        n = len(text)
        while i < n:
            if text[i:i+2] == '/*':
                start = i
                depth = 1
                i += 2
                while i < n - 1 and depth > 0:
                    if text[i:i+2] == '/*':
                        depth += 1
                        i += 2
                    elif text[i:i+2] == '*/':
                        depth -= 1
                        i += 2
                    else:
                        i += 1

                for j in range(start, min(i, n)):
                    if result[j] not in ('\n', '\r'):
                        result[j] = ' '
            else:
                i += 1
        return "".join(result)

    def tokenize(self):
        if self._tokens is None:
            self._tokens = self.lexer.getAllTokens()
            self.lexer.reset()
        return self._tokens

    def get_token_list(self):
        tokens = self.tokenize()
        return [
            (t.line, t.column, self.get_token_type_name(t.type), t.text)
            for t in tokens
        ]

    def get_token_type_name(self, token_type: int) -> str:
        if 0 <= token_type < len(self.lexer.symbolicNames):
            return self.lexer.symbolicNames[token_type]
        return "UNKNOWN"

    def reset(self):
        self._tokens = None
        self.lexer.reset()
