s1 = {1, 2}
s2 = {1, 2, 4}

print(s1.symmetric_difference(s2))  # {4}
print(s1) # {1, 2}
s1.symmetric_difference_update(s2)
print(s1) # {4}