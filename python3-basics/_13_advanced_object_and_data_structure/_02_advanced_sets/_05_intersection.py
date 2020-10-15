s = {1,2,3}
s2 = {1,2,4}

print(s.intersection(s2)) # {1, 2}
print(s) # {1, 2, 3}

s.intersection_update(s2)
print(s) # {1, 2}