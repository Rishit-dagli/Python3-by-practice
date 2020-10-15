my_list = [1,2,3]

my_list = [5,4,3,2,1,0]

print(my_list)

print(my_list[0])
print(my_list[2:])
print(my_list[:2])

my_list.append('four')

print(my_list)
# remove last index
my_list.pop()
print(my_list)

# remove first index
my_list.pop(0)
print(my_list)

my_list.sort()
print(my_list)

# replace value in list
my_list[0] = 'zero'
print(my_list)