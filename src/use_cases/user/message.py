import sys
import uuid
from entities.ent_user import *
from dtos.dto_words import Words
from dtos.dto_message import Message as dtoMessage
from dtos.dto_message import Message as dtoMessage
from util import *

__all__ = ['Message']


class Message:
    """Class to send a message of the user in the room"""

    @staticmethod
    def response(user, server, args) -> User:
        """Performs the broadcast in the rooms, basically send the message of the user to anothers in the room 
        
        :param server: IP where the server will be allocated 
        :param args: args to send the message 
        
        :returns: user obj with the changes
        """
        try:
            if not user.is_logged or user.status_room == 'lobby':
                raise Exception("Invalid command")

            message = " ".join(args)

            for room in server.registered_rooms:
                if room.name == user.status_room:
                    room.broadcast(message, user)
                    words: Words = Words(
                        words_id=uuid.uuid4().__str__(),
                        content=message
                    )
                    server.words_repository.put(words)

                    msg: dtoMessage = dtoMessage(
                        message_id=uuid.uuid4().__str__(),
                        sender_id=user.nickname,
                        receiver_id="BROADCAST",
                        content_id=words.id,
                        content_type=0,
                    )

                    print(msg)

                    server.message_repository.put(msg)

                    return user

        except Exception as exp:
            print(exp.with_traceback(sys.exc_info()[2]))

            message = " ".join(args)

            user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in sending message '" + message + "'. Are you logged?' \n\n",
                                          Colors.FAIL)).encode())

        return user
