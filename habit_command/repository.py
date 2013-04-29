import re
from sqlite3 import OperationalError
from sqlite3 import dbapi2 as sqlite

class Repository:
    def __init__(self, db_name):
        self.db_name = db_name

    def init_connection(self):
        self.connection = sqlite.connect(db_name)
        self._set_up_tables()

    def close_connection(self):
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
            self.connection.cursor().execute("CREATE TABLE activities (id INTEGER PRIMARY KEY, name VARCHAR(65535))")
            self.connection.commit()
        except OperationalError, e:
            # Bubble up any unexpected exceptions.
            if not re.match('table activities already exists', e.message):
                raise e



db_name = 'hc.db'
repo = Repository(db_name)


def init_connection():
    repo.init_connection()

def close_connection():
    repo.close_connection()

def create_activity(name):
    repo.create_activity(name)

def get_all_activities():
    return repo.get_all_activities()
