class JoinRoom:
    @staticmethod
    def response(connectionSocket, server, roomname) -> None:
        
        for rooms in server.activeRooms:
            if rooms.name == roomname:
                rooms.add(connectionSocket)