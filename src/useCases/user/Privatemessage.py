from entities.User import User
from entities.Room import Room

from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class Privatemessage:

    @staticmethod
    def response(user, server, args) -> None:
        try:
            if not user.isLogged:
                raise Exception("You have to be logged in to send private messages.\n\n")
            if len(args) < 2:
                raise Exception("Command error. Review your  arguments\n\n")

            receiver_nick = args[0]
            message = " ".join(args[1:])

            receiver_user = None

            for userRegistered in server.registeredUsers:
                if userRegistered.nick == receiver_nick:
                    receiver_user = userRegistered

            if not receiver_user:
                raise Exception(f"There is no one called '{args[0]}' on Concord\n\n")



            print(receiver_nick)
            print(message)

            return user

        except Exception as e:
            if e:
                user.connectionSkt.send(
                    (PrettyPrint.pretty_print(e, Colors.FAIL)).encode())
            else:
                message = " ".join(args[1:])
                user.connectionSkt.send(
                    (PrettyPrint.pretty_print("Error in send message to" + args[0] + "\n\n",
                                              Colors.FAIL)).encode())
            return user
