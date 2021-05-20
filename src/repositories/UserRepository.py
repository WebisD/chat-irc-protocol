from RepositoryInterface import RepositoryInterface
from entities.dtos.User import User


class UserRepository(RepositoryInterface):
    def __init__(self, tableName: str = 'user') -> None:
        super().__init__()
        self.tableName: str = tableName

    def findById(self, id: str) -> User:
        self.databaseHandler.runQueryWithArgs(
            '''
                SELECT * from :tableName where user_id = :userId
            ''',
            {"tableName": self.tableName, "userId": id}
        )

        return self.databaseHandler.fetchLastQuery()
