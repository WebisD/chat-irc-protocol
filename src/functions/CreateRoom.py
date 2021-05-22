from entities.Room import Room

class CreateRoom:
    @staticmethod
    def response(user, server, name, maxUser) -> None:
        try:
            if name == '' or maxUser == '':
                raise Exception("Invalid command")
            room = Room(name, int(maxUser))
            server.registeredRooms.append(room)
            user.connectionSkt.send(("Room " + str(name) + " created!\n\n").encode())
        except:
           user.connectionSkt.send(("Error in create room " + str(name) + " \n\n").encode())