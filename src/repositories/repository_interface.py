from controllers import *

__all__ = ['RepositoryInterface']


class RepositoryInterface:
    """A generic class for manipulating the database"""
    def __init__(self, db_name: str = 'concord.db') -> None:
        """Responsible for initializing the RepositoryInterface

        :param db_name: the database name
        :returns: None
        """

        self.controller_database: ControllerDatabase = ControllerDatabase(db_name)

    def find_all_by_id(self, subject_id) -> any:
        """Finds all objects containing the subject_id and returns them

        :param subject_id: the subject identification code
        :returns: any
        """
        pass

    def find_by_id(self, subject_id: str) -> any:
        """Finds an object containing the subject_id and returns it

        :param subject_id: the subject identification code
        :returns: any
        """
        pass

    def update_by_id(self, subject_id: str, new_subject_data: any) -> any:
        """Updates an object containing the subject_id and returns it

        :param subject_id: the subject identification code
        :param new_subject_data: the new subject data
        :returns: any
        """
        pass

    def delete_by_id(self, subject_id: str) -> any:
        """Deletes an object containing the subject_id and returns whether the operation was successful or not

        :param subject_id: the subject identification code
        :returns: any
        """
        pass

    def put(self, subject: any) -> any:
        """Puts an object on the database

        :param subject: the subject to be stored on the database
        :returns: any
        """
        pass
