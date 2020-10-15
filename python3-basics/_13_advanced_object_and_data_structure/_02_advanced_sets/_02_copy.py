s = {1, 2, 3}
print(type(s))

sc = s.copy()
print(sc)
sc.add(4)

print(s) # {1, 2, 3}
print(sc) # {1, 2, 3, 4}