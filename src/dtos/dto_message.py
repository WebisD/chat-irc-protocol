class Message:
    def __init__(self, message_id: str, sender_id: str, destination_id: str, content: str, content_type: int,
                 date: str) -> None:
        self.id: str = message_id
        self.sender_id: str = sender_id
        self.receiver_id: str = destination_id
        self.content_id: str = content
        self.type: int = content_type
        self.date: str = date

    def __str__(self) -> str:
        return f"Message({self.id}, {self.sender_id}, {self.receiver_id}, {self.content_id}, {self.type}, {self.date})"
