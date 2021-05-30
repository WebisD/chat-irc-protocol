from util.colors import *

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
