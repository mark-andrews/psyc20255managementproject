#!/usr/bin/env python

"""psyc20255admin: A tool for admin of the NTU psyc20255 module

Usage:
  psyc20255admin database (create|initialize|populate|update)
  psyc20255admin submissions (validate|create_marking_assignments) <submissions_dropbox_zip> 
  psyc20255admin completions (validate|process) <completed_marking_directory>
  psyc20255admin data new <corpus_name> [--data-type=<data_type>] <text_file> <vocab_file>
  psyc20255admin (-h | --help)
  psyc20255admin --version

Options:
  initialize                    Initialize the database, and fill it.
  -h --help                     Show this screen.
  --version                     Show version.

"""

from docopt import docopt
from sqlalchemy import create_engine
import psyc20255management

from psyc20255management.models import Base
from psyc20255management.utils import marksheets

from ernst import esys

ROOT = esys.thisDir(psyc20255management.__file__)

db_name = 'foobar'


if __name__ == '__main__':

    arguments = docopt(__doc__, version='psyc20255 0.0.0')
    print(arguments)

    if arguments['completions']:

        completed_marking_directory\
                = arguments['<completed_marking_directory>']

        if arguments['validate']:
            ## For now, just go through the process and see if we get errors.
            ## But in the future, we probably want to do
            ## 1) See if each marksheet has a grade 
            ## 2) (As already done) see if the names and IDs match
            ## 3) Check if each student is in the database
            ## 4) Check if their report has been reported, and if so, check if
            ##    anything has changed.
            ## 5) etc
            marksheets.process_completed_marksheets(completed_marking_directory)

        elif arguments['process']:
            completed_marksheets\
                    = marksheets.process_completed_marksheets(
                            completed_marking_directory
                    )

            print('\n'.join([','.join(completed_marksheet) 
                             for completed_marksheet in completed_marksheets])
                             )


    elif arguments['database']:

        if arguments['create']:

            engine = create_engine('sqlite:///%s.db' % db_name)
            Base.metadata.create_all(engine)

        elif arguments['initialize']:
            # Use all config info to fill database
            pass
