import sys
from entities.ent_user import *
from util import *

__all__ = ['Privatemessage']


class Privatemessage:

    @staticmethod
    def response(user, server, args) -> User:
        try:
            if not user.is_logged:
                raise Exception("You have to be logged in to send private messages.\n\n")
            if len(args) < 2:
                raise Exception("Command error. Review your  arguments\n\n")

            receiver_nick = args[0]
            message = " ".join(args[1:])

            receiver_user = None

            for userRegistered in server.registered_users:
                if userRegistered.nickname == receiver_nick:
                    receiver_user = userRegistered

            if not receiver_user:
                raise Exception(f"There is no one called '{args[0]}' on Concord\n\n")

            print(receiver_nick)
            print(message)

            return user

        except Exception as exp:
            print(exp.with_traceback(sys.exc_info()[2]))

            if exp:
                user.connection_socket.send(
                    (PrettyPrint.pretty_print(exp, Colors.FAIL)).encode()
                )

            else:
                message = " ".join(args[1:])
                user.connection_socket.send(
                    (PrettyPrint.pretty_print(
                        "Error in send message to" + args[0] + "\n\n", Colors.FAIL
                    )).encode()
                )

        return user
