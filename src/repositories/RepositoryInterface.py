from handler.HandlerDatabase import DatabaseHandler


class RepositoryInterface:
    def __init__(self, db_name: str = 'concord.db') -> None:
        self.database_handler: DatabaseHandler = DatabaseHandler(db_name)

    def find_all_by_id(self, subject_id) -> any:
        pass

    def find_by_id(self, subject_id: str) -> any:
        pass

    def update_by_id(self, subject_id: str, new_subject_data: any) -> any:
        pass

    def delete_by_id(self, subject_id: str) -> any:
        pass

    def create(self, subject: any) -> any:
        pass
