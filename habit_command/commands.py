class CreateActivityCommand:
    '''Creates a named activity.'''

    def __init__(self, name, db_connection):
        self.name = name
        self.db_connection = db_connection
        self.db_cursor = db_connection.cursor()

    def execute(self, ui):
        statement = "INSERT INTO activities (name) VALUES (:activity_name)"
        self.db_cursor.execute(statement, (self.name,))
        self.db_connection.commit()
        ui.write("Created activity %r.\n" % self.name)
        ui.write("Your activities are now:\n\n")
        ListActivitiesCommand(self.db_connection).execute(ui)

class ListActivitiesCommand:
    '''Lists activities.'''

    def __init__(self, db_connection):
        self.db_cursor = db_connection.cursor()

    def execute(self, ui):
        self.db_cursor.execute("SELECT * FROM activities")
        activities = self.db_cursor.fetchall()

        if len(activities) == 0:
            ui.write("You haven't created any activities.\nCreate your first activity with `c Take over the world`.\n\n")
            return

        for id, name in activities:
            ui.write("(%d) %s\n" % (id, name))
        ui.write("\n")
