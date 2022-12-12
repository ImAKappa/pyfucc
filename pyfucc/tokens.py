import token
from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    RPOINTER = token.GREATER
    LPOINTER = token.LESS
    INCREMENT = token.PLUS
    DECREMENT = token.MINUS
    OUTPUT = token.DOT
    INPUT = token.COMMA
    JUMP_ZERO = token.LSQB
    JUMP_NONZERO = token.RSQB
    DEBUG = token.COMMENT
    NEWLINE = token.NEWLINE
    EOF = token.ENDMARKER

@dataclass
class Token:
    type: TokenType
    lexeme: str
    # There are no literals in BrainFuck, at least not in source code
    line: int

    def __str__(self):
        return f"{self.type} {self.lexeme}"