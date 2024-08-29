from app.dal.databases.postgresql_connection import PostgresqlConnection
from app.dal.queries.dataset_queries import CREATE_DATASET, DELETE_DATASET, SELECT_DATASET_BY_ID, UPDATE_DATASET_DESCRIPTION

class DatasetProxy:
    """
    Proxy class for interacting with the database through PostgreSQL queries related to datasets.
    """

    def __init__(self):
        """
        Initializes the DatasetProxy instance by obtaining a PostgreSQL database connection instance.
        """
        self.connection = PostgresqlConnection.get_instance()

    def create_dataset(self, name, description):
        """
        Creates a new dataset in the database.

        Args:
        name (str): Name of the dataset.
        description (str): Description of the dataset.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(CREATE_DATASET, (name, description))
                self.connection.commit()
                print("Dataset created successfully")
        except Exception as e:
            print(f"Error creating dataset: {e}")

    def get_dataset_by_id(self, dataset_id):
        """
        Retrieves a dataset from the database based on dataset ID.

        Args:
        dataset_id (int): ID of the dataset.

        Returns:
        tuple: Dataset information fetched from the database.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(SELECT_DATASET_BY_ID, (dataset_id,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Error retrieving dataset: {e}")

    def update_dataset_description(self, dataset_id, new_description):
        """
        Updates the description of an existing dataset in the database.

        Args:
        dataset_id (int): ID of the dataset.
        new_description (str): New description to be updated for the dataset.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(UPDATE_DATASET_DESCRIPTION, (new_description, dataset_id))
                self.connection.commit()
                print("Dataset description updated successfully")
        except Exception as e:
            print(f"Error updating dataset description: {e}")

    def delete_dataset(self, dataset_id):
        """
        Deletes a dataset from the database based on dataset ID.

        Args:
        dataset_id (int): ID of the dataset.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(DELETE_DATASET, (dataset_id,))
                self.connection.commit()
                print("Dataset deleted successfully")
        except Exception as e:
            print(f"Error deleting dataset: {e}")