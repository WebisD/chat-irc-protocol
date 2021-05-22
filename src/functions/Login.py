class Login:
    @staticmethod
    def response(user, server, nick, password) -> None:
        try:
            if nick == '' or password == '':
                raise Exception("Invalid command")
            for userRegistered in server.registeredUsers:
              if userRegistered.nick == nick and userRegistered.password == password and not userRegistered.isLogged:
                userRegistered.toggleLog()
                userRegistered.setSocket(user.connectionSkt)
                user.connectionSkt.send( ( "Client " + str(nick) + " successfully log\n\n").encode())
                return userRegistered
            user.connectionSkt.send( ( "Client " + str(nick) + " not found or already logged\n\n").encode())
            return user
        except:
            user.connectionSkt.send(("Error in login client " + str(nick) + " \n\n").encode())