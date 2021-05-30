from datetime import datetime
import uuid

__all__ = ['Message']


class Message:
    def __init__(self, message_id: str = uuid.uuid4().__str__(), sender_id: str = None, receiver_id: str = None,
                 content_id: str = None, content_type: int = None,
                 date: str = datetime.now().strftime("%y-%m-%d %H:%M:%S")) -> None:
        self.id: str = message_id
        self.sender_id: str = sender_id
        self.receiver_id: str = receiver_id
        self.content_id: str = content_id
        self.type: int = content_type
        self.date: str = date

    def __str__(self) -> str:
        return f"Message({self.id}, {self.sender_id}, {self.receiver_id}, {self.content_id}, {self.type}, {self.date})"
