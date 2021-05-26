class Message:
    def __init__(self, message_id: str, sender_id: str, destination_id: str, content: str, content_type: int) -> None:
        self.id: str = message_id
        self.sender_id: str = sender_id
        self.destination_id: str = destination_id
        self.content: str = content
        self.content_type: int = content_type

    def __str__(self) -> str:
        return f"Message({self.id}, {self.sender_id}, {self.destination_id}, {self.content}, {self.content_type})"
