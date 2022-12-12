class Colors:
    """ANSI escape sequences for terminal colors"""
    HEADER_PURPLE = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING_YELLOW = '\033[93m'
    FAIL_RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class TermColorer:

    def __init__(self):
        pass

    def print(self, msg: str, color: Colors):
        return f"{color}{msg}{Colors.ENDC}"

    def bold(self, msg: str, color: Colors):
        return f"{Colors.BOLD}{color}{msg}{Colors.ENDC}"

    def underline(self, msg: str, color: Colors):
        return f"{Colors.UNDERLINE}{color}{msg}{Colors.ENDC}"