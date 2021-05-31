from typing import List, Tuple
from repositories import *
from dtos.dto_user import User

__all__ = ['UserRepository']


class UserRepository(RepositoryInterface):
    """A class that manipulates the user table"""

    def __init__(self, db_name: str = "concord.db") -> None:
        """Responsible for initializing the UserRepository

        :param db_name: the database name
        :returns: None
        """
        super().__init__(db_name)
        self.table_name: str = 'user'

    def get_all_users(self) -> Tuple[User or None, bool]:
        """Finds all Participants containing the user_id

        :returns: A tuple containing containing all users and whether the operation was successful or not
        """
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
        """Finds all Users containing the user_id

        :param user_id: the user's unique identification code
        :returns: A tuple containing containing the list of users and whether the operation was successful or not
        """
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
        """Finds one Users containing the user_id

        :param user_id: the user's unique identification code
        :returns: A tuple containing containing one user and whether the operation was successful or not
        """
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
        """Updates one Users containing the user_id

        :param user_id: the user's unique identification code
        :param new_data: the user's new data
        :returns: A boolean representing whether the operation was successful or not
        """
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
        """Deletes one Users containing the user_id

        :param user_id: the user's unique identification code
        :returns: A boolean representing whether the operation was successful or not
        """
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
        """Puts one Users containing the user_id

        :param user: the user to be stored in the database
        :returns: A boolean representing whether the operation was successful or not
        """
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
