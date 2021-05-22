from entities.User import User

class JoinRoom:
    @staticmethod
    def response(user, server, roomname) -> None:
        try:
            if roomname == '':
                raise Exception("Invalid command")
            for room in server.activeRooms:
                if room.name == roomname:
                    if room.add(user):
                        user.statusRoom = roomname
                        return user
            user.connectionSkt.send(("Error in join to room " + str(roomname) + " \n\n").encode())       
            return user
        except:
            print("Error in join client ")

        