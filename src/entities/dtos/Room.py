class Room:
    def __init__(self, id: str, name: str, numOfParticipants: int, maxParticipants: int) -> None:
        self.roomId: str = id
        self.roomName: str = name
        self.roomNumOfParticipants: int = numOfParticipants
        self.roomMaxParticipants: int = maxParticipants
