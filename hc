#!/usr/bin/env python

import sys
import re
import sqlite3
from sqlite3 import dbapi2 as sqlite

class CreateActivityCommand:
    '''Creates a named activity.'''
    
    def __init__(self, name, db_cursor):
        self.name = name
        self.db_cursor = db_cursor

    def execute(self, ui):
        statement = "INSERT INTO activities (name) VALUES (:activity_name)"
        db_cursor.execute(statement, (activity_name,))
        db_connection.commit()
        ui.write("Created activity %r. Your activities are now:\n\n" % self.name)
        ListActivitiesCommand(self.db_cursor).execute(ui)

class ListActivitiesCommand:
    '''Lists activities.'''

    def __init__(self, db_cursor):
        self.db_cursor = db_cursor

    def execute(self, ui):
        db_cursor.execute("SELECT * FROM activities")
        activities = db_cursor.fetchall()

        if len(activities) == 0:
            ui.write("You haven't created any activities.\nCreate your first activity with `c Take over the world`.\n\n")
            return

        for id, name in activities:
            ui.write("(%d) %s\n" % (id, name))
        ui.write("\n")


def draw_ui(ui):
    ui.write('hc> ')

def init_db(db_connection):
    try:
        db_connection.cursor().execute('SELECT * FROM activities LIMIT 1')
    except sqlite3.OperationalError, e:
        if not re.match('no such table', e.message):
            raise e
        db_connection.cursor().execute("CREATE TABLE activities (id INTEGER PRIMARY KEY, name VARCHAR(65535))")

try:
    db_connection = sqlite.connect('hc.db')
    init_db(db_connection)
    db_cursor = db_connection.cursor()

    ui = sys.stdout
    draw_ui(ui)

    while True:
        user_input = raw_input()

        if re.match('^\s*\?$' , user_input):
            print """\
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
        elif re.match('^\s*l$' , user_input):
            ListActivitiesCommand(db_cursor).execute(ui)
        elif re.match('^\s*c( .*)?$' , user_input):
            activity_name = user_input[2:]
            if activity_name == '' or activity_name == ' ':
                print 'I need a name for the activity, please.'
            else:
                CreateActivityCommand(activity_name, db_cursor).execute(ui)
        elif re.match('^\s*(t|s|a|r|q).*' , user_input):
            print 'NOT IMPLEMENTED'
        else:
            print "Huh? What is it you want? (try ? for help)\n"

        draw_ui(ui)

except EOFError, e:
    print "\n"
    pass # CTRL-d to exit

except Exception, e:
    print "Oops, something went wrong.", e

db_connection.close()