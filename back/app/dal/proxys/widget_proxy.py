from app.dal.databases.postgresql_connection import PostgresqlConnection
from app.dal.queries.widget_queries import GET_WIDGETS_QUERY

class WidgetProxy:
    """
    Proxy class for interacting with the database through PostgreSQL queries related to widgets.
    """

    def __init__(self):
        """
        Initializes the WidgetProxy instance by obtaining a PostgreSQL database connection instance.
        """
        self.db = PostgresqlConnection.get_instance()

    def get_widgets(self):
        """
        Retrieves widgets from the database.

        Returns:
        tuple: Widget information fetched from the database.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(GET_WIDGETS_QUERY)
            return cursor.fetchone()
        except Exception as e:
            print(f"Error retrieving widgets: {e}")