from entities.User import User
from Interface.PrettyPrint import PrettyPrint
from Interface.Colors import Colors


class Register:
    @staticmethod
    def response(user, server, name, nick, password) -> None:
        try:
            if name == '' or nick == '' or password == '':
                raise Exception("Invalid command")
            user = User(name, nick, password, user.connectionSkt)
            for userRegistered in server.registeredUsers:
                if userRegistered.nick == nick:
                    user.connectionSkt.send(
                        (PrettyPrint.pretty_print("Client '" + str(name) + "' already registered \n\n",
                                                  Colors.FAIL)).encode())
                    return

            server.registeredUsers.append(user)
            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Client " + str(name) + " successfully registered \n\n", Colors.OKGREEN)).encode())

        except:
            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Error in register client '" + str(name) + "'\n\n", Colors.FAIL)).encode())
