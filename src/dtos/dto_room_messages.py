__all__ = ['RoomMessages']


class RoomMessages:
    def __init__(self, message_id: str, room_id: str) -> None:
        """ Responsible for initializing the class RoomMessages

        :param message_id: the id of the message sent in the room
        :param room_id: the id of the room the message was sent in
        :returns: None

        """

        self.message_id: str = message_id
        self.room_id: str = room_id

    def __str__(self) -> str:
        """Responsible for representing the class in a string format"""

        return f"RoomMessages({self.message_id}, {self.room_id})"
