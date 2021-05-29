__all__ = ['Words']


class Words:
    def __init__(self, id: str, content: str) -> None:
        self.id: str = id
        self.content: str = content

    def __str__(self) -> str:
        return f"Words({self.id}, {self.content})"
