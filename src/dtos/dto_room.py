class Room:
    def __init__(self, id: str, name: str, max_participants: int) -> None:
        self.id: str = id
        self.name: str = name
        self.max_participants: int = max_participants

    def __str__(self) -> str:
        return f"Room({self.id}, {self.name}, {self.max_participants})"
