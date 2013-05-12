import sys

import habit_command.parser as parser
from habit_command.repository import REPO

class Session:
    def __init__(self):
        self.ui = sys.stdout

    def start(self):
        REPO.init_connection()

    def terminate(self):
        REPO.close_connection()

    def render(self, text):
        self.ui.write(text)


def start_loop():
    """Start interactive habit-command CLI session."""

    session = Session()

    try:
        session.start()

        while True:
            session.render('hc> ')
            user_input = raw_input()

            process_single_command(session, user_input)

    except EOFError, e:
        session.render("\n")
        pass # CTRL-d to exit

    except Exception, e:
        print "Oops, something went wrong: %r" % e

    # QQQ: Is there a Python equivalent of ensure/finally?
    session.terminate()

def process_single_command(session, user_input):
    command = parser.match(user_input)
    if command is None:
        session.render("Huh? What is it you want? (try ? for help)\n\n")
        return

    command.execute(session)