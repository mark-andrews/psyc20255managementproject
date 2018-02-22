""" Utilities for processing submitted lab reports.

"""
#=============================================================================
# Standard library imports
#=============================================================================
import os
import datetime
import shutil
from collections import defaultdict

#=============================================================================
# Imports of homespun packages
#=============================================================================
from ernst import esys

#=============================================================================
# Local imports
#=============================================================================
from .. import conf

#================================ End Imports ================================


def get_submitted_reports_list(reports_directory):

    '''
    Return a list of all submitted reports.
    Keep only the most recent submitted version when there are more than one
    submissions.

    '''

    def get_timestamp(timestamp_str):
        '''Parse a timestamp string
        
        In particular, this is to parse the one in the submitted report filename.
        '''

        return datetime.datetime.strptime(timestamp_str, "%d %B, %Y %I%M %p")


    def get_most_recent_submission(multiple_submissions):
        '''
        Return the most recent submission from a list of submissions, each of
        which contain a submission timestamp.

        '''
        return sorted(multiple_submissions, 
                      key = lambda submission: submission['timestamp']).pop()

    submissions = defaultdict(list)
    for fname in os.listdir(reports_directory):
        match = conf.submitted_report_filename_pattern.match(fname)
        if not match:
            print('Did not match file "%s".' % fname)
        else:
            _, student_id, student_name, date_string, doc_name = match.groups()
            timestamp = get_timestamp(date_string)

            filepath = os.path.join(reports_directory, fname)
            _, extension = os.path.splitext(filepath)

            assert extension[0] == '.', 'expecting a dot at start of %s' % extension

            submissions[student_id].append(
                dict(filename = fname,
                     filepath = filepath,
                     student_name = student_name,
                     student_id = student_id,
                     extension = extension,
                     checksum = esys.checksum(filepath),
                     timestamp = timestamp)
            )
            
    return {key:get_most_recent_submission(submissions[key]) 
            for key in submissions}


def copy_report(submission_info, new_directory='tmpdir'):

    '''
    Copy the report whose details are listed in `submission_info` into a new
    directory that is relative to the current working directory.

    The name of the new file is determined by the new_report_fname_template
    that is found in conf.py. 

    '''
    
    new_filename = conf.new_report_fname_template % (submission_info['student_name'].replace(' ', '_'), 
                                                     submission_info['student_id'],
                                                     submission_info['extension'])
    
    new_path = os.path.join(new_directory, new_filename)
    
    shutil.copy2(submission_info['filepath'], new_path)
    
    assert esys.checksum(new_path) == submission_info['checksum']
    
    return new_filename # Return new name just in case we need it
