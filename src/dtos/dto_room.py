__all__ = ['Room']

import uuid


class Room:
    def __init__(self, room_id: str = uuid.uuid4().__str__(), name: str = None, max_participants: int = None) -> None:
        """ Responsible for initializing the class Room

        :param room_id: the room's unique identification code
        :param name: the room name
        :param max_participants: the maximum number of people that can fit in a room
        :returns: None

        """

        self.id: str = room_id
        self.name: str = name
        self.max_participants: int = max_participants

    def __str__(self) -> str:
        """Responsible for representing the class in a string format"""

        return f"Room({self.id}, {self.name}, {self.max_participants})"
