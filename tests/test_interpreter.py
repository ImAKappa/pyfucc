from pyfucc.tokens import Token, TokenType
from pyfucc.interpreter import Interpreter

interpreter = Interpreter()

class TestInterpreter:

    def test_interpreter(self):
        test_in = [
            Token(TokenType.RPOINTER, ">", 1),
            Token(TokenType.INCREMENT, "+", 1), 
            Token(TokenType.RPOINTER, ">", 1),
            Token(TokenType.INCREMENT, "+", 1), 
            Token(TokenType.JUMP_ZERO, "[", 1),
            Token(TokenType.INCREMENT, "+", 1),
            Token(TokenType.INCREMENT, "+", 1),
            Token(TokenType.INCREMENT, "+", 1),
            Token(TokenType.LPOINTER, "<", 1),
            Token(TokenType.DECREMENT, "-", 1),
            Token(TokenType.JUMP_NONZERO, "]", 1),
            Token(TokenType.RPOINTER, ">", 1),
            Token(TokenType.OUTPUT, ".", 1),
            Token(TokenType.EOF, "", 1),
        ]
        interpreter.execute_all(test_in)
        test_out = interpreter.cells
        assert [0, 0, 4] == test_out