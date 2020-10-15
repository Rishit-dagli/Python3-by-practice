import re


def multi_re_find(patterns, phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print(f'Searching the phrase using the re check: {pattern}')
        print(re.findall(pattern, phrase))

