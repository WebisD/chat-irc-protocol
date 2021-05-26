from entities.User import User

class Register:
    @staticmethod
    def response(user, server, name, nick, password) -> None:
        try:
            if name == '' or nick == '' or password == '':
                raise Exception("Invalid command")
            user = User(name, nick, password, user.connectionSkt)
            for userRegistered in server.registeredUsers:
              if userRegistered.nick == nick:
                user.connectionSkt.send( ("Client " + str(name) + " already registered \n\n").encode())
                raise Exception("Invalid command")
            server.registeredUsers.append(user)
            user.connectionSkt.send( ("Client " + str(name) + " successfully registered \n\n").encode())
        except:
            user.connectionSkt.send( ("Error in register client " + str(name) + " \n\n").encode() )
