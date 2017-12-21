import re

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

# When we create copies of the submitted reports, we will use the following
# file name template.
new_report_fname_template = '%s, %s, report%s'

# Marksheets have the following file name template.
marksheet_fname_template = '%s, %s, marksheet.docx'
# And here's the regex.
marksheet_fname_pattern = re.compile(r'([^,]*), ([^,]*), marksheet.docx')
