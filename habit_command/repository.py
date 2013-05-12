import re
import psycopg2

class Repository:
    """Encapsulates DB access."""

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def init_connection(self):
        """Set up DB connection, create DB & tables if necessary."""

        self.connection = psycopg2.connect(database=self.db_name)
        self._set_up_tables()

    def close_connection(self):
        """Close DB connection."""
        self.connection.close()

    def create_activity(self, name):
        """Creates an activity named `name` in the DB."""

        db_cursor = self.connection.cursor()
        statement = 'INSERT INTO activities (name) VALUES (%(activity_name)s)'
        db_cursor.execute(statement, {'activity_name': name})
        self.connection.commit()

    def get_all_activities(self):
        """Retrieves all activity records from the DB."""

        db_cursor = self.connection.cursor()
        db_cursor.execute("SELECT * FROM activities")
        activities = db_cursor.fetchall()
        return activities

    def _set_up_tables(self):
        statements = [
            """CREATE TABLE IF NOT EXISTS activities (
                id   bigserial    primary key,
                name varchar(255))""",
            """CREATE TABLE IF NOT EXISTS log_entries (
                id          bigserial   primary key,
                activity_id int         not null references activities,
                date        date        not null,
                multiplier  int         not null default 1)"""
        ]

        for statement in statements:
            self.connection.cursor().execute(statement)
        self.connection.commit()

REPO = Repository('habit-command')
