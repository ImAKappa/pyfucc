
from pyfucc.tokens import TokenType, Token
from pyfucc.scanner import Scanner

scanner = Scanner()

class TestScanner:

    def test_scanner(self):
        test_in = "><[].$"
        test_out = [
            Token(TokenType.RPOINTER, ">", 1),
            Token(TokenType.LPOINTER, "<", 1),
            Token(TokenType.JUMP_ZERO, "[", 1),
            Token(TokenType.JUMP_NONZERO, "]", 1),
            Token(TokenType.OUTPUT, ".", 1),
            Token(TokenType.DEBUG, "$", 1),
            Token(TokenType.EOF, "", 1),
        ]
        assert scanner.scan_tokens(test_in) == test_out
