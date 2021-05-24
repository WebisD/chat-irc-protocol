from entities.User import User
from entities.Room import Room


class Message:
    @staticmethod
    def response(user, server, message) -> None:
        for room in server.registeredRooms:
            if room.name == user.statusRoom:
                room.broadcast(message, user)