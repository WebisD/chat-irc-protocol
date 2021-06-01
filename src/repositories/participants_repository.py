from typing import List, Tuple
from repositories import *
from dtos.dto_participants import Participants

__all__ = ['ParticipantsRepository']


class ParticipantsRepository(RepositoryInterface):
    """A class that manipulates the participants table"""

    def __init__(self, db_name: str = "concord.db") -> None:
        """Responsible for initializing the ParticipantsRepository

        :param db_name: the database name
        :returns: None
        """
        super().__init__(db_name)
        self.table_name: str = 'participants'

    def find_all_by_user_id(self, user_id: str) -> Tuple[List[Participants], bool]:
        """Finds all Participants containing the user_id

        :param user_id: the participant's user id
        :returns: A tuple containing containing the list of participants and whether the operation was successful or not
        """
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where user_id = :id
                ''',
                {"id": user_id}
            )

            result = self.controller_database.fetch_all_results_from_last_query()
            message_list: List[Participants] = []

            for rows in result:
                message_list.append(Participants(*rows))

            return message_list, True

        except Exception as exp:
            print(f"Could not find participants with user_id {user_id}")
            print(repr(exp))

        return [], False

    def find_all_by_room_id(self, room_id: str) -> Tuple[List[Participants], bool]:
        """Finds all Participants containing the room_id

        :param room_id: the participant's room id
        :returns: A tuple containing containing the list of participants and whether the operation was successful or not
        """
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where room_id = :id
                ''',
                {"id": room_id}
            )

            result = self.controller_database.fetch_all_results_from_last_query()
            message_list: List[Participants] = []

            for rows in result:
                message_list.append(Participants(*rows))

            return message_list, True

        except Exception as exp:
            print(f"Could not find participants with room_id {room_id}")
            print(repr(exp))

        return [], False

    def find_one_by_user_id(self, user_id: str) -> Tuple[Participants or None, bool]:
        """Finds one Participants containing the user_id

        :param user_id: the participant's user_id
        :returns: A tuple containing containing one participant and whether the operation was successful or not
        """
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where user_id = :id
                ''',
                {"id": user_id}
            )

            result = self.controller_database.fetch_one_result_from_last_query()

            if result:
                message = Participants(*result)
                return message, True

        except Exception as exp:
            print(f"Could not find participant with room_id {user_id}")
            print(repr(exp))

        return None, False

    def find_one_by_room_id(self, room_id: str) -> Tuple[Participants or None, bool]:
        """Finds one Participants containing the room_id

        :param room_id: the participant's room_id
        :returns: A tuple containing containing one participant and whether the operation was successful or not
        """
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where room_id = :id
                ''',
                {"id": room_id}
            )

            result = self.controller_database.fetch_one_result_from_last_query()

            if result:
                message = Participants(*result)
                return message, True

        except Exception as exp:
            print(f"Could not find participant with room_id {room_id}")
            print(repr(exp))

        return None, False

    def find_one_by_user_id_and_room_id(self, user_id: str, room_id: str) -> Tuple[Participants or None, bool]:
        """Finds one Participants containing both the given user_id and room_id

        :param user_id: the participant's user_id
        :param room_id: the participant's room_id
        :returns: A tuple containing containing one participant and whether the operation was successful or not
        """
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name}
                    WHERE user_id = :user_id AND room_id = :room_id
                ''',
                {"user_id": user_id, "room_id": room_id}
            )

            result = self.controller_database.fetch_one_result_from_last_query()

            if result:
                message = Participants(*result)
                return message, True

        except Exception as exp:
            print(f"Could not find participant with user_id {user_id} and room_id {room_id}")
            print(repr(exp))

        return None, False

    def update_by_user_id(self, user_id: str, new_data: Participants) -> bool:
        """Finds one Participants containing the user_id

        :param user_id: the participant's user_id
        :param new_data: the participant's new data
        :returns: A tuple containing containing one participant and whether the operation was successful or not
        """
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    UPDATE {self.table_name}
                    SET 
                        user_id = :user_id,
                        room_id = :room_id
                        
                    WHERE user_id = :search_user_id;
                ''',
                args={
                    "search_user_id": user_id,
                    "user_id": new_data.user_nickname,
                    "room_id": new_data.room_id
                }
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not update participants with room_id {user_id}")
            print(repr(exp))

            return False

        return True

    def update_by_room_id(self, room_id: str, new_data: Participants) -> bool:
        """Finds one Participants containing the room_id

        :param room_id: the participant's room_id
        :param new_data: the participant's new data
        :returns: A tuple containing containing one participant and whether the operation was successful or not
        """
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    UPDATE {self.table_name}
                    SET 
                        user_id = :user_id,
                        room_id = :room_id

                    WHERE room_id = :search_room_id;
                ''',
                args={
                    "search_room_id": room_id,
                    "user_id": new_data.user_nickname,
                    "room_id": new_data.room_id
                }
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not update participant with room_id {room_id}")
            print(repr(exp))

            return False

        return True

    def delete_by_user_id(self, user_id: str) -> bool:
        """Deletes all Participants containing the user_id

        :param user_id: the participant's user_id
        :returns: A boolean representing whether the operation was successful or not
        """
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    DELETE FROM {self.table_name}
                    WHERE user_id = :user_id 
                ''',
                args={"user_id": user_id}
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not delete participant with user_id {user_id}")
            print(repr(exp))

            return False

        return True

    def delete_by_room_id(self, room_id: str) -> bool:
        """Deletes all Participants containing the room_id

        :param room_id: the participant's room_id
        :returns: A boolean representing whether the operation was successful or not
        """
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    DELETE FROM {self.table_name}
                    WHERE room_id = :room_id 
                ''',
                args={"room_id": room_id}
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not delete participant with room_id {room_id}")
            print(repr(exp))

            return False

        return True

    def put(self, participant: Participants) -> bool:
        """Deletes all Participants containing the user_id

        :param participant: A participant to be stored in the database
        :returns: A boolean representing whether the operation was successful or not
        """
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                        INSERT INTO {self.table_name}(user_id, room_id) 
                        VALUES (:user_id,:room_id);
                ''',
                args={
                    "user_id": participant.user_nickname,
                    "room_id": participant.room_id,
                }
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not create participant {participant.__str__()}")
            print(repr(exp))

            return False

        return True
