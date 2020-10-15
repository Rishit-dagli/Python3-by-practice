import re

# Term to split on
split_term = '@'

phrase = 'What is the domain name of someone with the email: hello@gmail.com'

# Split the pharse
result = re.split(split_term, phrase)
print(result)
