from typing import List
from repositories.RepositoryInterface import RepositoryInterface
from entities.dtos.User import User


class UserRepository(RepositoryInterface):
    def __init__(self, dbName: str = "concord.db") -> None:
        super().__init__(dbName)
        self.tableName: str = 'user'

    def findById(self, id: str) -> List[User]:
        self.databaseHandler.runQueryWithArgs(
            f'''
                SELECT * from {self.tableName} where nickname = :nickname
            ''',
            {"nickname": id}
        )

        result = self.databaseHandler.fetchLastQuery()
        userList: List[User] = []

        for rows in result:
            userList.append(User(*rows))

        return userList

    def updateById(self, id: str, newData: User) -> any:
        self.databaseHandler.runQueryWithArgs(
            query=f'''
                UPDATE user
                SET nickname = :nickname, name = :name, password = :password
                WHERE nickname = :userId;
            ''',
            args={"userId": id, "nickname": newData.nickname, "name": newData.name, "password": newData.password}
        )

        self.databaseHandler.connection.commit()
