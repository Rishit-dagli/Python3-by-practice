import re

# List of patterns to search for
pattern = 'term1'

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

match = re.search(pattern, text)

print(type(match))

print(f'match start at index : {match.start()}')
print(f'match end at index : {match.end()}')
