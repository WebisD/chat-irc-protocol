class Participants:
    def __init__(self, nickname: str, room_id: str) -> None:
        self.user_nickname: str = nickname
        self.room_id: str = room_id

    def __str__(self) -> str:
        return f"Participants({self.user_nickname}, {self.room_id})"
