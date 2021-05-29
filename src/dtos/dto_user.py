class User:
    def __init__(self, nickname: str, name: str, password: str) -> None:
        self.nickname: str = nickname
        self.name: str = name
        self.password: str = password

    def __str__(self) -> str:
        return f"User({self.nickname}, {self.name}, {self.password})"
