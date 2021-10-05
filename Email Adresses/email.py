import re


regexp = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @ # @ symbol
    (\w)+ # domain name
    (\.[a-zA-Z]{2,4}) # dot-something
    )''', re.VERBOSE)
