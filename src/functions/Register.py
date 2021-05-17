from entities.User import User

class Register:
    @staticmethod
    def response(connectionSocket, server, name, nick, password) -> None:
        try:
            user = User(name, nick, password, connectionSocket)
            server.activeUser.append(user)
            print("Client " + str(name) + " successfully registered ")
        except:
            print("Errot in register client " + str(name))
