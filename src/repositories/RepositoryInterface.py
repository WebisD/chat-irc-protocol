from handler.HandlerDatabase import DatabaseHandler


class RepositoryInterface:
    def __init__(self, dbName: str = 'concord.db') -> None:
        self.databaseHandler: DatabaseHandler = DatabaseHandler(dbName)

    def findById(self, id: str) -> any:
        pass

    def updateById(self, id: str) -> any:
        pass

    def deleteById(self, id: str) -> any:
        pass

    def create(self, object: any) -> any:
        pass