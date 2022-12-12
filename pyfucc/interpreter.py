from pyfucc.tokens import Token, TokenType
from pyfucc.debugger import Debugger
# TODO: Add docstrings
# TODO: Add shebang

class InterpreterError(Exception):
    """Base-class for Interpreter Errors"""
    def __init__(self, msg: str, line: int):
        super().__init__(msg)
        self.msg = msg
        self.line = line

class NegativeIndex(InterpreterError):
    """Pointer is at negative index"""

class InvalidInput(InterpreterError):
    """Invalid input"""

class Interpreter:
    """Runs BrainFuck commands"""

    def __init__(self):
        self.init()

    def init(self):
        # Persistent state
        self.cells = [0]
        self.pointer = 0
        self.ops: list[Token]
        self.jump: int
        self.debugger = Debugger()
        self.out = ""
        self.current_op = 0
        self.line = 1

    def reset(self):
        self.init()
        print("reset")
        self.debug()
        return

    def undo(self):
        print("'undo' feature coming soon")
        return NotImplemented

    def execute_all(self, ops: list[Token]):
        """Executes a list of operations (op)"""
        # Temporary state
        self.ops = ops
        self.current_op = 0
        self.jump = None
        while not self.is_at_end():
            self.execute_op()
        return

    def is_at_end(self):
        return self.current_op >= len(self.ops)

    def advance(self):
        op = self.ops[self.current_op]
        self.current_op += 1
        return op

    def execute_op(self):
        token = self.advance()
        match token.type:
            case TokenType.RPOINTER: self.move_right()
            case TokenType.LPOINTER: self.move_left()
            case TokenType.INCREMENT: self.increment()
            case TokenType.DECREMENT: self.decrement()
            case TokenType.OUTPUT: self.output()
            case TokenType.INPUT: self.input()
            case TokenType.JUMP_ZERO: self.jump_zero()
            case TokenType.JUMP_NONZERO: self.jump_nonzero()
            case TokenType.DEBUG: self.debug()
            case TokenType.NEWLINE: 
                self.line += 1
                # TODO: Figure out how to link line with source file line; currently incorrect
            case TokenType.EOF:
                pass
        return

    def move_right(self):
        self.pointer += 1
        if self.pointer == len(self.cells):
            self.cells.append(0)

    def move_left(self):
        self.pointer -= 1
        if self.pointer < 0:
            self.pointer = 0
            raise NegativeIndex(f"Pointer at negative index {self.pointer}", self.line)

    def increment(self):
        self.cells[self.pointer] += 1

    def decrement(self):
        self.cells[self.pointer] -= 1

    def output(self):
        self.out += chr(self.cells[self.pointer])

    def clear_out(self):
        self.out = ""

    def input(self):
        input_val = input()
        try:
            val = int(input_val)
        except ValueError as e:
            raise InvalidInput(f"Invalid non-integer input '{input_val}'", self.line)
        self.cells[self.pointer] = val

    def jump_zero(self):
        """["""
        if self.cells[self.pointer] == 0:
            # Look for next "]"
            while not self.is_at_end():
                token = self.advance()
                if token.type == TokenType.JUMP_NONZERO:
                    self.jump_nonzero()
                    break
        else:
            self.jump = self.current_op
        
    def jump_nonzero(self):
        """]"""
        if self.cells[self.pointer] != 0:
            self.current_op = self.jump

    def debug(self):
        self.debugger.debug(self)