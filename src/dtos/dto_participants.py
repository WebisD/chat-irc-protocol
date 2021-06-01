__all__ = ['Participants']


class Participants:
    def __init__(self, nickname: str, room_id: str) -> None:
        """ Responsible for initializing the class Participants

        :param nickname: the user id of the participant
        :param room_id: the id of the room joined by the user
        :returns: None

        """
        self.user_nickname: str = nickname
        self.room_id: str = room_id

    def __str__(self) -> str:
        """Responsible for representing the class in a string format"""

        return f"Participants({self.user_nickname}, {self.room_id})"
