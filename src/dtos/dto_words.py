__all__ = ['Words']


class Words:
    def __init__(self, words_id: str, content: str) -> None:
        self.id: str = words_id
        self.content: str = content

    def __str__(self) -> str:
        return f"Words({self.id}, {self.content})"
