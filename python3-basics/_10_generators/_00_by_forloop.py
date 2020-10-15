def create_cube(n):  # this function return [ ] of x ** 3
    result = []
    for x in range(n):
        result.append(x ** 3)
    return result


for x in create_cube(10):
    print(x)
