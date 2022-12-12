import argparse
from pathlib import Path
from datetime import datetime
import io
import sys
from array import array

from pyfucc.tokens import Token
from pyfucc.scanner import Scanner, ScannerError
from pyfucc.interpreter import Interpreter, InvalidInput, NegativeIndex
from pyfucc.termcolors import TermColorer, Colors

# TODO: Make it so you can get previous command using "Up arrow"
clr = TermColorer()

class PyFucc:
    """Delagates tasks and operations to the Scanner and Interpreter"""

    def __init__(self):
        self.name = "🧠 BrainFuck 🤯"
        self.version = "v0.1.0"
        self.had_error = True
        self.prev_line = None

    def scan(self, source: str, scanner: Scanner) -> list[Token]:
        try:
            tokens = scanner.scan_tokens(source)
        except ScannerError as e:
            self.error(e.line, e.msg)
        return tokens

    def interpret(self, tokens: list[Token], interpreter: Interpreter):
        try:
            interpreter.execute_all(tokens)
        except InvalidInput as e:
            self.error(e.msg, e.line)
        except NegativeIndex as e:
            self.error(e.msg, e.line)
        return

    def show_help(self):
        print("REPL commands:")
        repl_commands = {
            ":help": "Help",
            ":exit": "Exit REPL",
            ":about": "More information about BrainFuck",
            ":reset": "Reset program state",
            ":undo": "Undo the last operation"
        }
        for command, description in repl_commands.items():
            print(f"\t{command}\t{description}")

    def show_about(self):
        print("This is a BrainFuck interpreter. Learn more about BrainFuck:")
        resources = [
            "https://www.youtube.com/watch?v=hdHjjBS4cs8",
            "https://en.wikipedia.org/wiki/Brainfuck",
            "https://openprocessing.org/sketch/516467/"
        ]
        for resource in resources:
            print(f"\t{resource}")

    def match_repl_command(self, line: str, interpreter: Interpreter):
        match line:
            case ":help": self.show_help()
            case ":exit": self.end()
            case ":about": self.show_about()
            case ":reset": interpreter.reset()
            case ":undo": interpreter.undo()
            case _:
                pass
        return

    def run_prompt(self) -> None:
        print(f"{self.name} {self.version} ({datetime.today().ctime()})")
        print("Type \":help\" or \":about\" for more information")
        exec_number = 0
        scanner = Scanner()
        interpreter = Interpreter()
        while True:
            print(clr.print(f"In [{exec_number}]:", Colors.OK_GREEN), end=" ")
            try:
                line = input()
                self.match_repl_command(line, interpreter)
            except EOFError: # Ctrl-Z on Windows, Ctrl-D on Linux/Mac
                break
            else:
                # Scan a line, then pass the tokens to the interpreter to update
                tokens = self.scan(line, scanner)
                self.interpret(tokens, interpreter)
                if interpreter.out != "":
                    print(clr.print(f"Out[{exec_number}]: {interpreter.out}", Colors.HEADER_PURPLE))
                    print()
                # Interpreter should keep going, even after error
                self.had_error = False
                # Clear output
                interpreter.clear_out()
                exec_number += 1
        return

    def run_file(self, filepath: Path) -> None:
        with io.open(filepath, mode="r") as f:
            source = f.read()
        scanner = Scanner()
        tokens = self.scan(source, scanner)
        interpreter = Interpreter()
        self.interpret(tokens, interpreter)
        print(interpreter.out)
        if self.had_error:
            sys.exit(65)

    def report(self, message: str, where: str, line: int) -> None:
        report_line = f"[line {line}]" 
        report_error = clr.print("Mental Breakdown", Colors.FAIL_RED)
        report_where = f"({where})" if where != "" else ""
        print(f"{report_error} {report_line}{report_where}: {message}")
        self.had_error = True

    def error(self, message: str, line: int) -> None:
        self.report(message, "", line)

    def end(self):
        sys.exit(64)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", "-s", type=str, help="Source file")
    args = parser.parse_args()

    pyfucc = PyFucc()

    if args.src:
        pyfucc.run_file(Path(args.src))
    else:
        pyfucc.run_prompt()


