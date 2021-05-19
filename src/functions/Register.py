from entities.User import User

class Register:
    @staticmethod
    def response(user, server, name, nick, password) -> None:
        try:
            user = User(name, nick, password, user.connectionSkt)
            server.registeredUsers.append(user)
            user.connectionSkt.send( ("Client " + str(name) + " successfully registered \n\n").encode())
        except:
            user.connectionSkt.send( ("Error in register client " + str(name) + " \n\n").encode() )
