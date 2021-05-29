__all__ = ['RoomMessages']


class RoomMessages:
    def __init__(self, message_id: str, room_id: str) -> None:
        self.message_id: str = message_id
        self.room_id: str = room_id

    def __str__(self) -> str:
        return f"RoomMessages({self.message_id}, {self.room_id})"
