#!/usr/bin/env python3
# TODO: Add docstrings

from pyfucc.tokens import Token, TokenType

class ScannerError(Exception):
    """Base-class for scanner errors"""
    def __init__(self, msg: str, line: int):
        super().__init__(msg)
        self.msg = msg
        self.line = line



class Scanner:
    """Converts source string into tokens"""

    def __init__(self):
        # Each significant token in BrainFuck is only one character, 
        #   so we don't need to track a "start" pointer for tokens
        self.current_char = None
        self.line = 1

    def scan_tokens(self, source: str) -> list[Token]:
        self.tokens = []
        self.source = iter(source)
        try:
            while True:
                self.scan_token()
        except StopIteration:
            pass
        self.tokens.append(Token(TokenType.EOF, "", self.line))
        return self.tokens

    def add_token(self, type: TokenType):
        self.tokens.append(Token(type, self.current_char, self.line))

    def scan_token(self):
        self.current_char = next(self.source)
        match self.current_char:
            case ">": self.add_token(TokenType.RPOINTER)
            case "<": self.add_token(TokenType.LPOINTER)
            case "+": self.add_token(TokenType.INCREMENT)
            case "-": self.add_token(TokenType.DECREMENT)
            case ".": self.add_token(TokenType.OUTPUT)
            case ",": self.add_token(TokenType.INPUT)
            case "[": self.add_token(TokenType.JUMP_ZERO)
            case "]": self.add_token(TokenType.JUMP_NONZERO)
            case "$": self.add_token(TokenType.DEBUG)
            # Whitespace
            case "\n":
                self.line += 1
                self.add_token(TokenType.NEWLINE)
            case _:
                # Anything else is ignored by the interpreter
                pass
        return