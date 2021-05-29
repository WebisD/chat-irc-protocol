class File:
    def __init__(self, id: str, name: str, content: bytearray) -> None:
        self.id: str = id
        self.name: str = name
        self.content: bytearray = content

    def __str__(self) -> str:
        return f"File({self.id}, {self.name}, {self.content})"
