import sys

import habit_command.parser as parser
from habit_command.repository import REPO

class Session:
    """An interactive habit-command CLI session."""

    def draw_ui(self, ui):
        ui.write('hc> ')

    def start_loop(self):
        try:
            REPO.init_connection()
            ui = sys.stdout

            while True:
                self.draw_ui(ui)
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
