import re

from habit_command.commands import (
    CreateActivityCommand,
    ListActivitiesCommand,
    HelpCommand,
    NotImplementedCommand)


command_regexes = {
    'help':    '^\s*\?$',
    'list':    '^\s*l$',
    'create':  '^\s*c( .*)?$',
    'notimpl': '^\s*(t|s|a|r|q).*'
}

def match(user_input, db_connection):
    if re.match(command_regexes['help'] , user_input):
        return HelpCommand()

    elif re.match(command_regexes['list'] , user_input):
        return ListActivitiesCommand(db_connection)

    elif re.match(command_regexes['create'], user_input):
        activity_name = user_input[2:].strip()
        return CreateActivityCommand(activity_name, db_connection)

    elif re.match(command_regexes['notimpl'], user_input):
        return NotImplementedCommand()

    else:
        return None
