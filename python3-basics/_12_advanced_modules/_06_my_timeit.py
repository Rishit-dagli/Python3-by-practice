import timeit

# For loop
fl = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'For loop 10000 time(s) : {fl}')

# List comprehension
lc = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(f'List comprehension 10000 time(s) : {lc}')

# Map()
m = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(f'Map 10000 time(s) : {m}')

# Great! We see a significant time difference by using map()! This is good to know and we should keep this in mind.
