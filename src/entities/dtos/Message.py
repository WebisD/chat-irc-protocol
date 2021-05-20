class Message:
    def __init__(self, messageId: str, senderId: str, destinationId: str, content: str, contentType: int) -> None:
        self.messageId: str = messageId
        self.messageSenderId: str = senderId
        self.messageDestinationId: str = destinationId
        self.messageContent: str = content
        self.messageContentType: int = contentType
