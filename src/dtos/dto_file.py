__all__ = ['File']


class File:
    """ Class responsible for representing the File to be stored in the database"""

    def __init__(self, file_id: str, name: str, content: bytearray) -> None:
        """ Responsible for initializing the class File

        :param file_id: the file unique identification code
        :param name: the file name
        :param content: the file content in a bytearray format
        :returns: None
        """

        self.id: str = file_id
        self.name: str = name
        self.content: bytearray = content

    def __str__(self) -> str:
        """Responsible for representing the class in a string format"""

        return f"File({self.id}, {self.name}, {self.content})"
