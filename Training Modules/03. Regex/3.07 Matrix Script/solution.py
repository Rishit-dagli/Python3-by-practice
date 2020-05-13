#!/bin/python3

import math
import os
import random
import re
import sys

p = re.compile(r'(?<=\w)([\$\#\%\s]+)(?=\w)')
dem = sys.stdin.readline().split();
r = int(dem[0])
c = int(dem[1])
rows = [l for l in sys.stdin]
text = "";
for i in range(c):
    for j in range(r):
        text = text+rows[j][i]
print(p.sub(' ',text))


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
