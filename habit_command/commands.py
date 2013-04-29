import repository

class CreateActivityCommand:
    """Creates a named activity."""

    def __init__(self, name):
        self.name = name

    def execute(self, ui):
        if not self.name:
            ui.write('I need a name for the activity, please.\n\n')
            return

        repository.create_activity(self.name)
        ui.write("Created activity %r.\n" % self.name)

        ui.write("Your activities are now:\n\n")
        ListActivitiesCommand().execute(ui)


class ListActivitiesCommand:
    """Lists activities."""

    def execute(self, ui):
        activities = repository.get_all_activities()
        
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
