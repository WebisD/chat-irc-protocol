from entities.User import User

class JoinRoom:
    @staticmethod
    def response(connectionSocket, server, roomname) -> None:
        try:
            user = User("Pedrinh", "pp", "1111", connectionSocket)

            for rooms in server.activeRooms:
                if rooms.name == roomname:
                    rooms.add(user)
        except:
            print("Errot in join client ")

        