import psycopg2
from psycopg2 import OperationalError
from app.entities.configs.postgresql import Postgresql

class PostgresqlConnection:
    """
    Singleton class for managing PostgreSQL database connections using psycopg2.
    """

    _instance = None

    @classmethod
    def get_instance(cls):
        """
        Singleton method to get or create an instance of the PostgreSQL connection.

        Returns:
        psycopg2.connection: An instance of the PostgreSQL database connection.
        """
        if cls._instance is None:
            cls._instance = cls._create_connection()
        return cls._instance

    @classmethod
    def _create_connection(cls):
        """
        Private method to create a new PostgreSQL database connection.

        Returns:
        psycopg2.connection: A new instance of the PostgreSQL database connection.
        """
        try:
            connection = psycopg2.connect(
                dbname=Postgresql.DBNAME,
                user=Postgresql.USER,
                password=Postgresql.PASSWORD,
                host=Postgresql.HOST,
                port=Postgresql.PORT)
            return connection
        except OperationalError as e:
            print(f"Error: {e}")
            return None

    def get_connection(self):
        """
        Method to return the existing PostgreSQL database connection instance.

        Returns:
        psycopg2.connection: The existing instance of the PostgreSQL database connection.
        """
        return self._instance