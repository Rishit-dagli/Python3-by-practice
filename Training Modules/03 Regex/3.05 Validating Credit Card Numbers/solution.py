import sys
import re

def credit_card(s):
    if not s[0] in "456": return False
    if not re.match("[0-9-]+", s): return False
    if sum([1 if "0" <= _ and _ <= "9" else 0 for _ in s]) != 16: return False
    if not (len(s) == 16 or len(s) == 19 and s[4] == "-" and s[9] == "-" and s[14] == "-"): return False
    s = s.replace("-", "")
    for i in range(len(s)-3):
        if s[i] == s[i+1] and s[i] == s[i+2] and s[i] == s[i+3]: return False
    return True

stdin = sys.stdin
t = int(stdin.readline())

for z in range(t):
    line = stdin.readline().rstrip()
    if(credit_card(line)):
        print("Valid")
    else:
        print("Invalid")
