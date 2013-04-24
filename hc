#!/usr/bin/env python

import sys

RESPONSES = {
    '/h' : """  /l          -- list activities
  /t          -- track activity
  /c          -- create activity
  /s<n>       -- show details for activity
  /list-all   -- list activities (including archived ones)
  /archive<n> -- archive activity number 'n'
  /revive<n>  -- un-archive activity number 'n'
  /h          -- this help screen
""",
    '' : ''
}

def draw_ui():
    sys.stdout.write('hc> ')


def response_for_input(input_string):
    if input_string in RESPONSES:
        return RESPONSES[input_string]
    else:
        return "No idea what you want from me (try /h for help)"


draw_ui()

while True:
    user_input = raw_input()
    print response_for_input(user_input)
    draw_ui()
