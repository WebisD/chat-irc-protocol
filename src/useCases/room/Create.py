from entities.Room import Room
from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class Create:
    @staticmethod
    def response(user, server, args) -> None:
        try:
            if user.statusRoom != 'lobby':
                user.connectionSkt.send(
                 (PrettyPrint.pretty_print("Você já está em uma sala \n\n", Colors.FAIL)).encode())
                return user
            if not user.isLogged:
                user.connectionSkt.send(
                 (PrettyPrint.pretty_print("Você deve estar logado \n\n", Colors.FAIL)).encode())
                return user

            name =args[0] 
            maxUser = args[1]
            room = Room(name, int(maxUser))

            for roomRegistered in server.registeredRooms:
                if roomRegistered.name == room.name:
                    user.connectionSkt.send(
                        (PrettyPrint.pretty_print("Room '" + str(name) + "' already created!\n\n", Colors.OKGREEN)).encode())
                    return user
                    
            server.registeredRooms.append(room)
            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Room '" + str(name) + "' created!\n\n", Colors.OKGREEN)).encode())
            return user
        except:
            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Error in create room '" + str(name) + "' \n\n", Colors.FAIL)).encode())
            return user
