from entities.User import User
from entities.Room import Room

class LeaveRoom:
    @staticmethod
    def response(user, server) -> None:
        for room in server.registeredRooms:
            if room.name == user.statusRoom:
                if room.remove(user):
                    user.statusRoom = 'lobby'
                    return user
        user.connectionSkt.send(("Error in left room " + str(room.name) + " \n\n").encode())       
        return user   