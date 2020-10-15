s1 = {1,2,3}
s2 = {3,4,5}

print(s1.union(s2)) # {1, 2, 3, 4, 5}

print(s1) # {1, 2, 3}

s1.update(s2)
print(s1) # {1, 2, 3, 4, 5}