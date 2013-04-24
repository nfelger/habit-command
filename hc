#!/usr/bin/env python

import sys

def draw_ui():
  sys.stdout.write('hc> ')

def get_user_input():
  user_choice = raw_input()

def command_from_input(input):
  help_text = """  /l          -- list activities
  /t          -- track activity
  /c          -- create activity
  /s<n>       -- show details for activity
  /list-all   -- list activities (including archived ones)
  /archive<n> -- archive activity number 'n'
  /revive<n>  -- un-archive activity number 'n'
  /h          -- this help screen
"""
  return lambda: help_text

def execute_command(command):
  output = command()
  print output

while True:
  draw_ui()
  user_input = get_user_input()
  command = command_from_input(user_input)
  execute_command(command)
