class CreateActivityCommand:
    '''Creates a named activity.'''

    def __init__(self, name, db_connection):
        self.name = name
        self.db_connection = db_connection
        self.db_cursor = db_connection.cursor()

    def execute(self, ui):
        if not self.name:
            ui.write('I need a name for the activity, please.\n\n')
            return

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


class HelpCommand:
    """Prints usage information."""

    usage_text = """\
    l            -- list activities
    t <id>       -- track activity
    c <name>     -- create activity
    s <id>       -- show details for activity
    list-all     -- list all activities (including archived ones)
    archive <id> -- archive activity number 'n'
    revive <id>  -- un-archive activity number 'n'
    q            -- quit
    ?            -- this help screen

"""

    def execute(self, ui):
        ui.write(self.usage_text)


class NotImplementedCommand:
    """Prints a notice that this functionality isn't supported, yet."""

    def execute(self, ui):
        ui.write('NOT IMPLEMENTED\n\n')
