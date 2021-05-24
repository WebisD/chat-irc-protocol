from Interface.Colors import Colors


class PrettyPrint:
    @staticmethod
    def pretty_print(text, color):
        return f"{color}{text}{Colors.ENDC}"
