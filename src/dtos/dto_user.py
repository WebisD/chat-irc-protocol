__all__ = ['User']


class User:
    def __init__(self, nickname: str, name: str, password: str) -> None:
        """ Responsible for initializing the class User

        :param nickname: the user's unique identification code
        :param name: the user's name
        :param password: the user's password
        :returns: None

        """
        self.nickname: str = nickname
        self.name: str = name
        self.password: str = password

    def __str__(self) -> str:
        """Responsible for representing the class in a string format"""

        return f"User({self.nickname}, {self.name}, {self.password})"
