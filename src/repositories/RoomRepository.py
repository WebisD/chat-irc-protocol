from typing import List, Tuple
from repositories.RepositoryInterface import RepositoryInterface
from entities.dtos.Room import Room


class RoomRepository(RepositoryInterface):
    def __init__(self, db_name: str = "concord.db") -> None:
        super().__init__(db_name)
        self.table_name: str = 'room'

    def find_all_by_id(self, room_id: str) -> Tuple[List[Room], bool]:
        try:
            self.database_handler.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where id = :id
                ''',
                {"id": room_id}
            )

            result = self.database_handler.fetch_all_results_from_last_query()
            user_list: List[Room] = []

            for rows in result:
                user_list.append(Room(*rows))

            return user_list, True

        except Exception as exp:
            print(f"Could not find users with id {room_id}")
            print(repr(exp))

        return [], False

    def find_by_id(self, room_id: str) -> Tuple[Room or None, bool]:
        try:
            self.database_handler.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where id = :id
                ''',
                {"id": room_id}
            )

            result = self.database_handler.fetch_one_result_from_last_query()

            if result:
                room = Room(*result)
                return room, True

        except Exception as exp:
            print(f"Could not find room with id {room_id}")
            print(repr(exp))

        return None, False

    def update_by_id(self, room_id: str, new_data: Room) -> bool:
        try:
            self.database_handler.run_query_with_args(
                query=f'''
                    UPDATE {self.table_name}
                    SET 
                        id = :id,
                        name = :name,
                        max_number_of_participants = :max_number_of_participants
                    WHERE id = :userId;
                ''',
                args={"userId": room_id, 
                      "id": new_data.id,
                      "name": new_data.name,
                      "max_number_of_participants": new_data.max_participants}
            )

            self.database_handler.save_changes()

        except Exception as exp:
            print(f"Could not update room with id {room_id}")
            print(repr(exp))

            return False

        return True

    def delete_by_id(self, room_id: str) -> bool:
        try:
            self.database_handler.run_query_with_args(
                query=f'''
                    DELETE FROM {self.table_name}
                    WHERE id = :id 
                ''',
                args={"id": room_id}
            )

            self.database_handler.save_changes()

        except Exception as exp:
            print(f"Could not delete room with id {room_id}")
            print(repr(exp))

            return False

        return True

    def create(self, room: Room) -> bool:
        try:
            self.database_handler.run_query_with_args(
                query=f'''
                        INSERT INTO {self.table_name}(id,name,max_number_of_participants) 
                        VALUES (:id,:name,:max_number_of_participants)
                ''',
                args={
                    "id": room.id,
                    "name": room.name,
                    "max_number_of_participants": room.max_participants
                }
            )

            self.database_handler.save_changes()

        except Exception as exp:
            print(f"Could not create room {room.__str__()}")
            print(repr(exp))

            return False

        return True
