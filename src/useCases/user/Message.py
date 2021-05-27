from entities.User import User
from entities.Room import Room

from util.PrettyPrint import PrettyPrint
from util.Colors import Colors

class Message:
    @staticmethod
    def response(user, server, args) -> None:
        try:
            if not user.isLogged or user.statusRoom == 'lobby':
               raise Exception("Invalid command")
            
            message = ""
            for word in args:
                message+= word + " "

            for room in server.registeredRooms:
                if room.name == user.statusRoom:
                    room.broadcast(message, user)
        except:
            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Error in send message '" + str(args) + ". Are you in the lobby?' \n\n", Colors.FAIL)).encode())
            return user