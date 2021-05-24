from entities.Room import Room

class CreateRoom:
    @staticmethod
    def response(connectionSocket, server, name, maxUser) -> None:
        room = Room(name)
        server.activeRooms.append(room)
        