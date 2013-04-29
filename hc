#!/usr/bin/env python

import sys
import re
import habit_command
from habit_command.commands import (
    CreateActivityCommand, 
    ListActivitiesCommand)
from sqlite3 import dbapi2 as sqlite

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

def draw_ui(ui):
    ui.write('hc> ')

try:
    db_connection = sqlite.connect('hc.db')

    ui = sys.stdout

    while True:
        draw_ui(ui)
        user_input = raw_input()

        if re.match('^\s*\?$' , user_input):
            print usage_text

        elif re.match('^\s*l$' , user_input):
            ListActivitiesCommand(db_connection).execute(ui)

        elif re.match('^\s*c( .*)?$' , user_input):
            activity_name = user_input[2:].strip()
            if not activity_name:
                print 'I need a name for the activity, please.\n'
                continue
            CreateActivityCommand(activity_name, db_connection).execute(ui)

        elif re.match('^\s*(t|s|a|r|q).*' , user_input):
            print 'NOT IMPLEMENTED'

        else:
            print "Huh? What is it you want? (try ? for help)\n"

except EOFError, e:
    print "\n"
    pass # CTRL-d to exit

except Exception, e:
    print "Oops, something went wrong: %r" % e

db_connection.close()