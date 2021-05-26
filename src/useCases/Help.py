from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class Help:
    @staticmethod
    def response(activeUser) -> None:
        message = ("\n Available commands" +
                   f"\n → {PrettyPrint.pretty_print('/help', Colors.WARNING)}" +
                   f"\n → {PrettyPrint.pretty_print('/register -name -pass -nick', Colors.WARNING)}" +
                   f"\n → {PrettyPrint.pretty_print('/login  -nick -pass', Colors.WARNING)} " +
                   f"\n → {PrettyPrint.pretty_print('/create -room_name -size', Colors.WARNING)}" +
                   f"\n → {PrettyPrint.pretty_print('/join -room_name', Colors.WARNING)}" +
                   f"\n → {PrettyPrint.pretty_print('/m or /message', Colors.WARNING)}" +
                   #f"\n → {PrettyPrint.pretty_print('//send -path', Colors.WARNING)}" +
                   f"\n → {PrettyPrint.pretty_print('/leave', Colors.WARNING)}" +
                   f"\n → {PrettyPrint.pretty_print('/listrooms', Colors.WARNING)}" +
                   #f"\n → {PrettyPrint.pretty_print('/list_files', Colors.WARNING)}" +
                   f"\n → {PrettyPrint.pretty_print('/list_users', Colors.WARNING)}" +
                   f"\n → {PrettyPrint.pretty_print('/quit', Colors.WARNING)}\n\n")

        activeUser.connectionSkt.send(message.encode())
# /register wever webis 1234
# /login webis 1234
