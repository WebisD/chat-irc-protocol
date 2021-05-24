from entities.User import User
from entities.Room import Room
from Interface.PrettyPrint import PrettyPrint
from Interface.Colors import Colors


class ListRoom:
    @staticmethod
    def response(user, server) -> None:
        if user.statusRoom == 'lobby':
            if len(server.registeredRooms) == 0:
                user.connectionSkt.send("There are no rooms here. But you can create one running "
                                        f"{PrettyPrint.pretty_print('/create -room_name -size', Colors.WARNING)} \n\n".encode())
                return

            user.connectionSkt.send("The rooms are: \n".encode())
            for room in server.registeredRooms:
                user.connectionSkt.send((" # " + PrettyPrint.pretty_print(str(room.name), Colors.OKCYAN) + "\n").encode())
            user.connectionSkt.send('\n'.encode())
            return    
        user.connectionSkt.send("Você já está em uma sala \n\n".encode())

