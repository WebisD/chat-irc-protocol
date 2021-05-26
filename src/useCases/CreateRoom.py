from entities.Room import Room
from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class CreateRoom:
    @staticmethod
    def response(user, server, name, maxUser) -> None:
        try:
            if name == '' or maxUser == '':
                raise Exception("Invalid command")
            room = Room(name, int(maxUser))
            server.registeredRooms.append(room)
            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Room '" + str(name) + "' created!\n\n", Colors.OKGREEN)).encode())
        except:
           user.connectionSkt.send(("Error in create room " + str(name) + " \n\n").encode())