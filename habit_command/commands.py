from habit_command.repository import REPO

class Command:
    """Command base class."""

    def __init__(self, args=""):
        self.args = args


class CreateActivityCommand(Command):
    """Creates a named activity."""

    def execute(self, session):
        name = ' '.join(self.args)
        if not name:
            session.render('I need a name for the activity, please.\n\n')
            return

        REPO.create_activity(name)
        session.render("Created activity %r.\n" % name)

        session.render("Your activities are now:\n\n")
        ListActivitiesCommand().execute(session)


class ListActivitiesCommand(Command):
    """Lists activities."""

    def execute(self, session):
        activities = REPO.get_all_activities()

        if len(activities) == 0:
            session.render("You haven't created any activities.\n" +
                "Create your first activity with `c Take over the world`.\n\n")
            return

        for uid, name in activities:
            session.render("(%d) %s\n" % (uid, name))
        session.render("\n")


class HelpCommand(Command):
    """Prints usage information."""

    usage_text = """\
    l            -- list activities
    t <id>       -- track activity
    c <name>     -- create activity
    s <id>       -- show details for activity
    q            -- quit
    ?            -- this help screen

"""

    def execute(self, session):
        session.render(self.usage_text)


class NotImplementedCommand(Command):
    """Prints a notice that this functionality isn't supported, yet."""

    def execute(self, session):
        session.render('NOT IMPLEMENTED\n\n')
