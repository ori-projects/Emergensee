from app.dal.databases.postgresql_connection import PostgresqlConnection
from app.dal.queries.model_queries import CREATE_MODEL_QUERY, DELETE_MODEL_QUERY, GET_ALL_MODELS_QUERY, GET_MODEL_BY_ID_QUERY, UPDATE_MODEL_QUERY

class ModelProxy:
    """
    Proxy class for interacting with the database through PostgreSQL queries related to models.
    """

    def __init__(self):
        """
        Initializes the ModelProxy instance by obtaining a PostgreSQL database connection instance.
        """
        self.db = PostgresqlConnection.get_instance()

    def create_model(self, name, labeled):
        """
        Creates a new model in the database.

        Args:
        name (str): Name of the model.
        labeled (bool): Whether the model is labeled or not.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(CREATE_MODEL_QUERY, (name, labeled))
            self.db.commit()
            print("Model created successfully")
        except Exception as e:
            print(f"Error creating model: {e}")

    def get_model_by_id(self, model_id):
        """
        Retrieves a model from the database based on model ID.

        Args:
        model_id (int): ID of the model.

        Returns:
        tuple: Model information fetched from the database.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(GET_MODEL_BY_ID_QUERY, (model_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error retrieving model: {e}")

    def update_model(self, model_id, name, labeled):
        """
        Updates the details of an existing model in the database.

        Args:
        model_id (int): ID of the model.
        name (str): New name for the model.
        labeled (bool): Whether the model is labeled or not.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(UPDATE_MODEL_QUERY, (name, labeled, model_id))
            self.db.commit()
            print("Model updated successfully")
        except Exception as e:
            print(f"Error updating model: {e}")

    def delete_model(self, model_id):
        """
        Deletes a model from the database based on model ID.

        Args:
        model_id (int): ID of the model.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(DELETE_MODEL_QUERY, (model_id,))
            self.db.commit()
            print("Model deleted successfully")
        except Exception as e:
            print(f"Error deleting model: {e}")

    def get_all_models(self):
        """
        Retrieves all models stored in the database.

        Returns:
        list: List of tuples, each containing information about a model.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(GET_ALL_MODELS_QUERY)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error retrieving models: {e}")