class User:
    def __init__(self, name: str, password: str, nickname: str) -> None:
        self.userName: str = name
        self.userPassword: str = password
        self.userNickname: str = nickname
