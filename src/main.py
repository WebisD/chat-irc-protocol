from entities.Server import startServer
from repositories.MessageRepository import MessageRepository
from repositories.RoomRepository import RoomRepository
from repositories.UserRepository import UserRepository
from src.entities.dtos.User import User
from src.entities.dtos.Room import Room
from src.entities.dtos.Message import Message


def main() -> None:
    """ Calls the function that instantiates a server

    :return: None

    """
    startServer()


if __name__ == "__main__":
    main()
