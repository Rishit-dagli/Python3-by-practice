def simple_gen():
    for x in range(3):
        yield x


for number in simple_gen():
    print(number)

g = simple_gen()
print(next(g))  # in not hold everything in memory, just generate next value as the time
print(next(g))