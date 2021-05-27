from entities.User import User
from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class Register:
    @staticmethod
    def response(user, server, args) -> None:
        try:
            print(args)
            if user.isLogged:
               raise Exception("Already logged")
            name = args[0] 
            nick = args[1] 
            password = args[2]

            if name == '' or nick == '' or password == '':
                raise Exception("Invalid command")
            userToRegister = User(name, nick, password, user.connectionSkt)
            for userRegistered in server.registeredUsers:
                if userRegistered.nick == nick:
                    user.connectionSkt.send(
                        (PrettyPrint.pretty_print("Client '" + str(name) + "' already registered \n\n",
                                                  Colors.FAIL)).encode())
                    return user

            server.registeredUsers.append(userToRegister)
            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Client " + str(name) + " successfully registered \n\n", Colors.OKGREEN)).encode())
            return user
        except:
            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Error in register client '" + str(name) + "'\n\n", Colors.FAIL)).encode())
            return user
