from entities.User import User
from entities.Room import Room
from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class Listroom:
    @staticmethod
    def response(user, server, args) -> None:
        try:
            if user.statusRoom != 'lobby':
                user.connectionSkt.send(
                (PrettyPrint.pretty_print("Você já está em uma sala \n\n", Colors.WARNING)).encode())
                return user
                
            if len(server.registeredRooms) == 0:
                user.connectionSkt.send("There are no rooms here. But you can create one running "
                                        f"{PrettyPrint.pretty_print('/create -room_name -size', Colors.WARNING)} \n\n".encode())
                return user
    
            user.connectionSkt.send("The rooms are: \n".encode())
            for room in server.registeredRooms:
                user.connectionSkt.send((" # " + PrettyPrint.pretty_print(str(room.name), Colors.OKCYAN) + "\n").encode())
            user.connectionSkt.send('\n'.encode())
            return user
        except:
            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Error in command list \n\n", Colors.FAIL)).encode())
            return user
