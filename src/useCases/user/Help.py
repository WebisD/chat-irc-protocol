from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class Help:
    @staticmethod
    def response(activeUser, server, args) -> None:
        try:
            message = ("\n Available commands" +
                       f"\n → {PrettyPrint.pretty_print('/help', Colors.WARNING)}" +
                       f"\n → {PrettyPrint.pretty_print('/register -name -pass -nick', Colors.WARNING)}" +
                       f"\n → {PrettyPrint.pretty_print('/login  -nick -pass', Colors.WARNING)} " +
                       f"\n → {PrettyPrint.pretty_print('/create -room_name -size', Colors.WARNING)}" +
                       f"\n → {PrettyPrint.pretty_print('/join -room_name', Colors.WARNING)}" +
                       f"\n → {PrettyPrint.pretty_print('/message', Colors.WARNING)}" +
                       #f"\n → {PrettyPrint.pretty_print('//send -path', Colors.WARNING)}" +
                       f"\n → {PrettyPrint.pretty_print('/leave', Colors.WARNING)}" +
                       f"\n → {PrettyPrint.pretty_print('/listroom', Colors.WARNING)}" +
                       #f"\n → {PrettyPrint.pretty_print('/list_files', Colors.WARNING)}" +
                       f"\n → {PrettyPrint.pretty_print('/listusers', Colors.WARNING)}" +
                       f"\n → {PrettyPrint.pretty_print('/quit', Colors.WARNING)}\n\n")

            activeUser.connectionSkt.send(message.encode())
            return activeUser
        except:
            activeUser.connectionSkt.send(
                (PrettyPrint.pretty_print("Error in command help \n\n", Colors.FAIL)).encode())
            return activeUser