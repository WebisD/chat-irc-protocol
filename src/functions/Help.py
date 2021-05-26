class Help:
    @staticmethod
    def response(activeUser) -> None:
        message = ("\nAvailable commands\n" +
                "\n/help" +
                "\n/register -name -pass -nick" +
                "\n/login  -nick -pass " +
                "\n/create -room_name -size" +
                "\n/join -room_name" +
                "\n//m //-m || //message // -message" +
                "\n//send -path" +
                "\n/leave" +
                "\n/list" +
                "\n/list_files" +
                "\n/list_users" + 
                "\n/quit\n\n")

        activeUser.connectionSkt.send(message.encode())