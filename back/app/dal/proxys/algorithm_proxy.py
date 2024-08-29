from app.dal.databases.postgresql_connection import PostgresqlConnection
from app.dal.queries.algorithm_queries import (
    CREATE_ALGORITHM_QUERY, DELETE_ALGORITHM_QUERY, GET_ALGORITHM_BY_ID_QUERY,
    GET_ALGORITHMS, GET_STATS_QUERY, UPDATE_ALGORITHM_QUERY
)

class AlgorithmProxy:
    """
    Proxy class for interacting with the database through PostgreSQL queries related to algorithms.
    """

    def __init__(self):
        """
        Initializes the AlgorithmProxy instance by obtaining a PostgreSQL database connection instance.
        """
        self.db = PostgresqlConnection.get_instance()

    def create_algorithm(self, algorithm_name, success_rank, num_uses):
        """
        Creates a new algorithm in the database.

        Args:
        algorithm_name (str): Name of the algorithm.
        success_rank (float): Success rank of the algorithm.
        num_uses (int): Number of times the algorithm has been used.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(CREATE_ALGORITHM_QUERY, (algorithm_name, success_rank, num_uses))
            self.db.commit()
            print("Algorithm created successfully")
        except Exception as e:
            print(f"Error creating algorithm: {e}")

    def get_algorithm_by_id(self, algorithm_id):
        """
        Retrieves an algorithm from the database based on algorithm ID.

        Args:
        algorithm_id (int): ID of the algorithm.

        Returns:
        tuple: Algorithm information fetched from the database.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(GET_ALGORITHM_BY_ID_QUERY, (algorithm_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error retrieving algorithm: {e}")

    def update_algorithm(self, algorithm_id, algorithm_name, success_rank, num_uses):
        """
        Updates an existing algorithm in the database.

        Args:
        algorithm_id (int): ID of the algorithm.
        algorithm_name (str): Name of the algorithm.
        success_rank (float): Success rank of the algorithm.
        num_uses (int): Number of times the algorithm has been used.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(UPDATE_ALGORITHM_QUERY, (algorithm_name, success_rank, num_uses, algorithm_id))
            self.db.commit()
            print("Algorithm updated successfully")
        except Exception as e:
            print(f"Error updating algorithm: {e}")

    def delete_algorithm(self, algorithm_id):
        """
        Deletes an algorithm from the database based on algorithm ID.

        Args:
        algorithm_id (int): ID of the algorithm.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(DELETE_ALGORITHM_QUERY, (algorithm_id,))
            self.db.commit()
            print("Algorithm deleted successfully")
        except Exception as e:
            print(f"Error deleting algorithm: {e}")

    def get_algorithms(self):
        """
        Retrieves all algorithms from the database.

        Returns:
        list: List of algorithms fetched from the database.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(GET_ALGORITHMS)
            algorithms = cursor.fetchall()
            return algorithms
        except Exception as e:
            print(f"Error retrieving algorithms: {e}")

    def get_statistics(self):
        """
        Retrieves statistics related to algorithms from the database.

        Returns:
        tuple: Statistics fetched from the database.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(GET_STATS_QUERY)
            stats = cursor.fetchone()
            return stats
        except Exception as e:
            print(f"Error retrieving statistics: {e}")