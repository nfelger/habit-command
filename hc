#!/usr/bin/env python

import sys
import habit_command
from habit_command import parser
from sqlite3 import dbapi2 as sqlite


def draw_ui(ui):
    ui.write('hc> ')

try:
    db_connection = sqlite.connect('hc.db')

    ui = sys.stdout

    while True:
        draw_ui(ui)
        user_input = raw_input()

        command = parser.match(user_input, db_connection)
        if command is None:
            ui.write("Huh? What is it you want? (try ? for help)\n\n")
            continue

        command.execute(ui)

except EOFError, e:
    print "\n"
    pass # CTRL-d to exit

except Exception, e:
    print "Oops, something went wrong: %r" % e

db_connection.close()