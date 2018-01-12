import re
import os

# These are the UG grades. These probably won't change.
grades = '''
1EXC 
1HIGH 1MID 1LOW 
21HIGH 21MID 21LOW 
22HIGH 22MID 22LOW 
3HIGH 3MID 3LOW 
FMARG FMID FLOW 
ZERO
'''.strip().split()

# These could easily change from year to year.
labgroups = [str(i+1) + ' SH' for i in range(6)] +\
            [str(i+1) + ' CRI' for i in range(6, 10)] +\
            ['11 SOC']

# This is the regular expression for a filename submitted to a NOW dropbox . 
submitted_report_filename_pattern\
    = re.compile(r'([0-9]{5,6}-[0-9]{5}) - ([NT]0[0-9]{6}) - (.*[a-z])- ([^-]*) - (.*)')

# The template document for the marksheets
this_dir = os.path.dirname(os.path.abspath(__file__))
marksheet_template_fname\
        = os.path.abspath(os.path.join(this_dir,
            'marksheet_templates/psyc20255_marksheet_template_v0.docx')
            )


# When we create copies of the submitted reports, we will use the following
# file name template.
new_report_fname_template = '%s__%s__%s__report%s'

# Marksheets have the following file name template.
marksheet_fname_template = '%s__%s__%s__marksheet.docx'
# And here's the regex.
marksheet_fname_pattern = re.compile(r'(.*)__(.*)__(.*)__marksheet.docx')
