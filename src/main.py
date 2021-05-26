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
    # startServer()

    user_repository: UserRepository = UserRepository()
    user: User = User("runtimeUser", "runtimeName", "runtimePassword")
    print(f"user: {user}")

    # 1: add to db
    user_repository.create(user)

    # 2: find user
    result,_ = user_repository.find_by_id(user.nickname)
    print(f"result: {result.__str__()}")

    # 3: update user
    user.name = "updated at runtime"
    user_repository.update_by_id(user.nickname, user)

    result, _ = user_repository.find_by_id(user.nickname)
    print(f"result: {result.__str__()}")

    # 4: delete user
    # user_repository.delete_by_id(user.nickname)

    # ----------------------------------------------
    room_repository: RoomRepository = RoomRepository()
    room: Room = Room("runtimeRoom", "runtimeName", 10)
    print(f"room: {room}")

    # 1: add to db
    room_repository.create(room)

    # 2: find user
    result, _ = room_repository.find_by_id(room.id)
    print(f"result: {result.__str__()}")

    # 3: update user
    room.name = "updated at runtime"
    room_repository.update_by_id(room.id, room)

    result, _ = room_repository.find_by_id(room.id)
    print(f"result: {result.__str__()}")

    # 4: delete user
    # room_repository.delete_by_id(room.id)"

    # ----------------------------------------------
    message_repository: MessageRepository = MessageRepository()
    message: Message = Message(
        "MSG_2a1s3d12a3ssfhjas",
        "antuniooh",
        "margaritas",
        "WORD_1a23sd23asd4fsfad",
        1,
        "2021-05-25 12:30:27"
    )
    print(f"message: {message}")

    # 1: add to db
    message_repository.create(message)

    # 2: find user
    result, _ = message_repository.find_by_message_id(message.id)
    print(f"result: {result.__str__()}")

    # 3: update user
    message.date = "2021-05-26 01:30:31"
    message_repository.update_by_message_id(message.id, message)

    result, _ = message_repository.find_by_message_id(message.id)
    print(f"result: {result.__str__()}")

    # 4: delete user
    # message_repository.delete_by_id(message.id)



if __name__ == "__main__":
    main()
