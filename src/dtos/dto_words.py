__all__ = ['Words']


class Words:
    def __init__(self, words_id: str, content: str) -> None:
        """ Responsible for initializing the class Words

        :param words_id: the words' unique identification code
        :param content: the words' content
        :returns: None

        """
        self.id: str = words_id
        self.content: str = content

    def __str__(self) -> str:
        """Responsible for representing the class in a string format"""

        return f"Words({self.id}, {self.content})"
