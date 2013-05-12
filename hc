#!/usr/bin/env python

from sys import argv
from habit_command import session

if len(argv) > 1:
    # Process individual command.
    one_time_session = session.Session()
    one_time_session.start()
    session.process_single_command(one_time_session, ' '.join(argv[1:]))
    one_time_session.terminate()
else:
    # Start interactive session.
    session.start_loop()

