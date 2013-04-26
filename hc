#!/usr/bin/env python

import sys
import re
import sqlite3
from sqlite3 import dbapi2 as sqlite

class Command:
    '''Abstract base command class.'''

    def __init__(self):
        if(self.__class__ == Command):
            raise Exception("I'm not really a thing. More of a concept. Maybe try subclassing me?")

    def execute(self, ui):
        raise Exception('IMPLEMENT ME')

class CreateActivityCommand(Command):
    '''Creates a named activity.'''
    
    def __init__(self, name):
        self.name = name

    # def execute(self, ui):
    #     ui.write("I'M NOT EVEN DOING ANYTGHIN!!\n")

class ListActivitiesCommand(Command):
    '''Lists all currently active activities (i.e. ones that haven't been archived).'''

    # def execute(self, ui):
    #     ui.write( "I'M NOT EVEN DOING ANYTGHIN!!\n")

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
        elif re.match('^\s*c( .*)?$' , user_input):
            activity_name = user_input[2:]
            if activity_name == '' or activity_name == ' ':
                print 'I need a name for the activity, please.'
            else:
                command = CreateActivityCommand(activity_name, db_cursor)
                command.execute(ui)
                ListActivitiesCommand().execute(ui)
        elif re.match('^\s*(l|t|s|a|r|q).*' , user_input):
            print 'NOT IMPLEMENTED'
        else:
            print "No idea what you want from me (try ? for help)"

        draw_ui(ui)
except Exception, e:
    print "Oops, something went wrong.", e
db_connection.close()