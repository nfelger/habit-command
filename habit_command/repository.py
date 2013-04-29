import re
from sqlite3 import OperationalError
from sqlite3 import dbapi2 as sqlite

class Repository:
    """Encapsulates DB access."""

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def init_connection(self):
        """Set up DB connection, create DB & tables if necessary."""

        self.connection = sqlite.connect(self.db_name)
        self._set_up_tables()

    def close_connection(self):
        """Close DB connection."""
        self.connection.close()

    def create_activity(self, name):
        """Creates an activity named `name` in the DB."""

        db_cursor = self.connection.cursor()
        statement = "INSERT INTO activities (name) VALUES (:activity_name)"
        db_cursor.execute(statement, (name,))
        self.connection.commit()

    def get_all_activities(self):
        """Retrieves all activity records from the DB."""

        db_cursor = self.connection.cursor()
        db_cursor.execute("SELECT * FROM activities")
        activities = db_cursor.fetchall()
        return activities

    def _set_up_tables(self):
        try:
            # QQQ: Is there a better way to test for table existence?
            statement = """CREATE TABLE activities (
                    id INTEGER PRIMARY KEY, name VARCHAR(65535)
                )"""
            self.connection.cursor().execute(statement)
            self.connection.commit()
        except OperationalError, e:
            # Bubble up any unexpected exceptions.
            if not re.match('table activities already exists', e.message):
                raise e


REPO = Repository('hc.db')