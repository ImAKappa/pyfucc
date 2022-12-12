# from pyfucc.interpreter import Interpreter

class Debugger:

    def __init__(self):
        pass

    def debug(self, interpreter):
        self.interpreter = interpreter
        self.show_cells()
        self.show_pointer()
        return

    def show_cells(self):
        cells = self.interpreter.cells
        print(cells)
        return

    def __mark(self, pos: int, marker: str):
        cells = self.interpreter.cells
        marker_debug = [marker if i == pos else f"{' '*len(str(cells[i]))}  " for i in range(len(cells))]
        print("".join([" ", *marker_debug, " "]))

    def show_pointer(self):
        pointer = self.interpreter.pointer
        self.__mark(pointer, "^")
        return