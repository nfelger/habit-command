import re
from sqlite3 import OperationalError
from sqlite3 import dbapi2 as sqlite

def _init_db(db_connection):
    try:
        # QQQ: Is there a better way to test for table existence?
        db_connection.cursor().execute('SELECT * FROM activities LIMIT 1')
    except OperationalError, e:
        # Bubble up any unexpected exceptions.
        if not re.match('no such table', e.message):
            raise e

        db_connection.cursor().execute("CREATE TABLE activities (id INTEGER PRIMARY KEY, name VARCHAR(65535))")
        db_connection.commit()

_db_connection = sqlite.connect('hc.db')
_init_db(_db_connection)
