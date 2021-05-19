class Login:
    @staticmethod
    def response(user, server, nick, password) -> None:
        try:
            for userRegistered in server.registeredUsers:
              if userRegistered.nick == nick and userRegistered.password == password:
                userRegistered.toggleLog()
                user.connectionSkt.send( ( "Client " + str(nick) + " successfully log\n\n").encode())
                print(server.registeredUsers)
                return
            user.connectionSkt.send( ( "Client " + str(nick) + " not found\n\n").encode())
        except:
            user.connectionSkt.send(("Error in login client " + str(nick) + " \n\n").encode())