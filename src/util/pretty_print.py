from util.colors import *
import textwrap

__all__ = ['PrettyPrint']


class PrettyPrint:
    """Class of PrettyPrint console"""

    @staticmethod
    def pretty_print(text, color) -> str:
        """Return the text with the specific color 
        
        :param text: text to be colored 
        :param color: color of text 
        
        :returns: Text with color
        """
        return f"{color}{text}{Colors.ENDC}"

    @staticmethod
    def wrap(s, w) -> str:
        """
        Return a parsed string
        :param s: string to be parsed
        :param w: place where the string should be split
        :return: string divided equally
        """
        return textwrap.fill(s, w)
