#!/usr/bin/env python

import sys
import re

def draw_ui():
    sys.stdout.write('hc> ')

draw_ui()

while True:
    user_input = raw_input()

    if re.match('^\?$' , user_input):
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
    elif re.match('^(l|t|c|s|a|r|q).*' , user_input):
        print 'NOT IMPLEMENTED'
    else:
        print "No idea what you want from me (try ? for help)"

    draw_ui()
