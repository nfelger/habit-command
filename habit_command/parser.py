# encoding: utf-8

import re

from habit_command.commands import (
    CreateActivityCommand,
    ListActivitiesCommand,
    HelpCommand,
    NotImplementedCommand)

COMMAND_REGEXES = {
    'help':    (r'^\s*\?$',           HelpCommand),
    'list':    (r'^\s*l$',            ListActivitiesCommand),
    'create':  (r'^\s*c( .*)?$',      CreateActivityCommand),
    'notimpl': (r'^\s*(t|s|a|r|q).*', NotImplementedCommand)
}

def match(user_input):
    """Parse user supplied command string into an executable command."""

    for key in COMMAND_REGEXES:
        regexp, command_class = COMMAND_REGEXES[key]
        if re.match(regexp, user_input):
            args = user_input.split()[1:]
            return command_class(args)

    return None
