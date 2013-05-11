import sys

import habit_command.parser as parser
from habit_command.repository import REPO

def start_loop():
    """Start interactive habit-command CLI session."""

    try:
        REPO.init_connection()
        ui = sys.stdout

        while True:
            ui.write('hc> ')
            user_input = raw_input()

            command = parser.match(user_input)
            if command is None:
                ui.write("Huh? What is it you want? (try ? for help)\n\n")
                continue

            command.execute(ui)

    except EOFError, e:
        print "\n"
        pass # CTRL-d to exit

    except Exception, e:
        print "Oops, something went wrong: %r" % e

    # QQQ: Is there a Python equivalent of ensure/finally?
    REPO.close_connection()
