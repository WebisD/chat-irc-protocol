from typing import List, Tuple
from repositories import *
from dtos.dto_user import User

__all__ = ['UserRepository']


class UserRepository(RepositoryInterface):
    def __init__(self, db_name: str = "concord.db") -> None:
        super().__init__(db_name)
        self.table_name: str = 'user'

    def get_all_users(self) -> Tuple[User or None, bool]:
        try:
            self.controller_database.run_query(
                f'''
                    SELECT * from {self.table_name}
                '''
            )

            result: List[Tuple] = self.controller_database.fetch_all_results_from_last_query()
            if result:

                users = [User(*u) for u in result]
                return users, True

        except Exception as exp:
            print(f"Could not select all users")
            print(repr(exp))

        return None, False

    def find_all_by_id(self, user_id: str) -> Tuple[List[User], bool]:
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where nickname = :nickname
                ''',
                {"nickname": user_id}
            )

            result = self.controller_database.fetch_all_results_from_last_query()
            user_list: List[User] = []

            for rows in result:
                user_list.append(User(*rows))

            return user_list, True

        except Exception as exp:
            print(f"Could not find users with id {user_id}")
            print(repr(exp))

        return [], False

    def find_by_id(self, user_id: str) -> Tuple[User or None, bool]:
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where nickname = :nickname
                ''',
                {"nickname": user_id}
            )

            result = self.controller_database.fetch_one_result_from_last_query()

            if result:
                user = User(*result)
                return user, True

        except Exception as exp:
            print(f"Could not find user with id {user_id}")
            print(repr(exp))

        return None, False

    def update_by_id(self, user_id: str, new_data: User) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    UPDATE {self.table_name}
                    SET nickname = :nickname, name = :name, password = :password
                    WHERE nickname = :userId;
                ''',
                args={"userId": user_id, "nickname": new_data.nickname, "name": new_data.name,
                      "password": new_data.password}
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not update user with id {user_id}")
            print(repr(exp))

            return False

        return True

    def delete_by_id(self, user_id: str) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    DELETE FROM {self.table_name}
                    WHERE nickname = :nickname 
                ''',
                args={"nickname": user_id}
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not delete user with id {user_id}")
            print(repr(exp))

            return False

        return True

    def put(self, user: User) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                        INSERT INTO {self.table_name}(nickname,name,password) 
                        VALUES (:nickname,:name,:password)
                ''',
                args={"nickname": user.nickname, "name": user.name, "password": user.password}
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not create user {user.__str__()}")
            print(repr(exp))

            return False

        return True
