import re

from habit_command.commands import (
    CreateActivityCommand,
    ListActivitiesCommand,
    HelpCommand,
    NotImplementedCommand)

COMMAND_REGEXES = {
    'help':    r'^\s*\?$',
    'list':    r'^\s*l$',
    'create':  r'^\s*c( .*)?$',
    'notimpl': r'^\s*(t|s|a|r|q).*'
}

def match(user_input):
    """Parse user supplied command string into an executable command."""

    if re.match(COMMAND_REGEXES['help'], user_input):
        return HelpCommand()

    elif re.match(COMMAND_REGEXES['list'], user_input):
        return ListActivitiesCommand()

    elif re.match(COMMAND_REGEXES['create'], user_input):
        activity_name = user_input[2:].strip()
        return CreateActivityCommand(activity_name)

    elif re.match(COMMAND_REGEXES['notimpl'], user_input):
        return NotImplementedCommand()

    else:
        return None
