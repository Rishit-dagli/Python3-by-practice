import re

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

print(re.findall('[^!.? ]+',test_phrase))