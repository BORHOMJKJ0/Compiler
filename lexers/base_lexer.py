from antlr4 import InputStream
from BaseLexer import BaseLexer as GeneratedLexer


class BaseLexer:
    """Wrapper class for the generated ANTLR lexer"""

    def __init__(self, input_text: str):
        self.input_stream = InputStream(input_text)
        self.lexer = GeneratedLexer(self.input_stream)
        self._tokens = None

    def tokenize(self):
        """Tokenize the input and return all tokens"""
        if self._tokens is None:
            self._tokens = self.lexer.getAllTokens()
            self.lexer.reset()
        return self._tokens

    def get_token_list(self):
        """Get tokens as a list of tuples (line, column, type, text)"""
        tokens = self.tokenize()
        return [
            (t.line, t.column, self.get_token_type_name(t.type), t.text)
            for t in tokens
        ]

    def get_token_type_name(self, token_type: int) -> str:
        """Get the symbolic name of a token type"""
        if 0 <= token_type < len(self.lexer.symbolicNames):
            return self.lexer.symbolicNames[token_type]
        return "UNKNOWN"

    def reset(self):
        """Reset the lexer"""
        self._tokens = None
        self.lexer.reset()