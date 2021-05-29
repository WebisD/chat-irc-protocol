__all__ = ['Room']

import uuid


class Room:
    def __init__(self, room_id: str = uuid.uuid4().__str__(), name: str = None, max_participants: int = None) -> None:
        self.id: str = room_id
        self.name: str = name
        self.max_participants: int = max_participants

    def __str__(self) -> str:
        return f"Room({self.id}, {self.name}, {self.max_participants})"
