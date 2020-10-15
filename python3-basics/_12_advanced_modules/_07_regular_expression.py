import re

# List of patterns to search for
patterns = ['term1', 'term2']

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print(f'Searching for {pattern} in...')
    print(text)
    # Check for match
    if re.search(pattern, text):
        print('Match was found')
    else:
        print('No match was found.')
    print('=======')
