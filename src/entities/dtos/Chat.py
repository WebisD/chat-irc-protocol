class Chat:
    def __init__(self, message_id: str, room_id: str) -> None:
        self.message_id = message_id
        self.room_id = room_id

    def __str__(self) -> str:
        return f"Chat({self.message_id}, {self.room_id})"
