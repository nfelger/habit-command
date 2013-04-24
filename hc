#!/usr/bin/env python

import sys
import re

def draw_ui():
    sys.stdout.write('hc> ')

draw_ui()

while True:
    user_input = raw_input()

    if re.match('^/(h|\?)$' , user_input):
        print """\
  /l          -- list activities
  /t          -- track activity
  /c          -- create activity
  /s<n>       -- show details for activity
  /list-all   -- list activities (including archived ones)
  /archive<n> -- archive activity number 'n'
  /revive<n>  -- un-archive activity number 'n'
  /h, /?      -- this help screen
"""
    elif re.match('^/(l|t|c|s|a|r|q).*' , user_input):
        print 'NOT IMPLEMENTED'
    else:
        print "No idea what you want from me (try /h for help)"

    draw_ui()
