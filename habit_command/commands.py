from habit_command.repository import REPO

class Command:
    """Command base class."""

    def __init__(self, args=""):
        self.args = args


class CreateActivityCommand(Command):
    """Creates a named activity."""

    def execute(self, ui):
        name = ' '.join(self.args)
        if not name:
            ui.write('I need a name for the activity, please.\n\n')
            return

        REPO.create_activity(name)
        ui.write("Created activity %r.\n" % name)

        ui.write("Your activities are now:\n\n")
        ListActivitiesCommand().execute(ui)


class ListActivitiesCommand(Command):
    """Lists activities."""

    def execute(self, ui):
        activities = REPO.get_all_activities()

        if len(activities) == 0:
            ui.write("You haven't created any activities.\n" +
                "Create your first activity with `c Take over the world`.\n\n")
            return

        for uid, name in activities:
            ui.write("(%d) %s\n" % (uid, name))
        ui.write("\n")


class HelpCommand(Command):
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


class NotImplementedCommand(Command):
    """Prints a notice that this functionality isn't supported, yet."""

    def execute(self, ui):
        ui.write('NOT IMPLEMENTED\n\n')
