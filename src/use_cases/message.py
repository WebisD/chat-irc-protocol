__all__ = ['Message']


class Message:
    @staticmethod
    def response(user, server, message) -> None:
        for room in server.registered_rooms:
            if room.name == user.status_room:
                room.broadcast(message, user)
