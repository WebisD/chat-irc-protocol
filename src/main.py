from entities.Server import startServer
from repositories.UserRepository import UserRepository


def main() -> None:
    """ Calls the function that instantiates a server

    :return: None

    """
    # startServer()

    userRepository: UserRepository = UserRepository()
    result = userRepository.findById("dragonslayer69")
    print(*result)

    result[0].password = "mudei a senha"

    userRepository.updateById("dragonslayer69", result[0])

    result = userRepository.findById("dragonslayer69")
    print(*result)


if __name__ == "__main__":
    main()
