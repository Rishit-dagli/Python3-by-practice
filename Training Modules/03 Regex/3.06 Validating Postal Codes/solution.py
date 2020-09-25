regex_integer_in_range = r"_________"
regex_alternating_repetitive_digit_pair = r"_________"
import re
s=input()
print (bool(re.match(r'^[1-9][\d]{5}$',s) and len(re.findall(r'(\d)(?=\d\1)',s))<2 ))
