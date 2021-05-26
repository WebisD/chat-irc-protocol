from entities.User import User
from entities.Room import Room

class ListUsersRoom:
    @staticmethod
    def response(user, server) -> None:
        for room in server.registeredRooms:
            if room.name == user.statusRoom:
                user.connectionSkt.send(("Os usuários na sala " + room.name + "são: \n\n").encode())       
                for users in room.list_of_clients:
                    user.connectionSkt.send((str(users.nick) + " \n\n").encode())   
                return    
        user.connectionSkt.send(("Você não está em nenhuma sala \n\n").encode())       
