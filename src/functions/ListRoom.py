from entities.User import User
from entities.Room import Room

class ListRoom:
    @staticmethod
    def response(user, server) -> None:
        if user.statusRoom == 'lobby':
            user.connectionSkt.send(("As salas são: \n\n").encode())       
            for room in server.registeredRooms:
                user.connectionSkt.send((str(room.name) + " \n\n").encode())   
