from util.colors import *

__all__ = ['PrettyPrint']


class PrettyPrint:
    @staticmethod
    def pretty_print(text, color):
        return f"{color}{text}{Colors.ENDC}"
