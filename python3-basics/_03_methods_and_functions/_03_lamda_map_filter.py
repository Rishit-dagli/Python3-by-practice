# Map
def square(number):
    return number**2
my_list_number = [1,2,3,4,5]
for item in map(square,my_list_number): # map(function,parameter)
    print(item)

# Filter
def check_even(number):
    return number%2 == 0

my_list_number1 = [1,2,3,4,5,6]

for n in filter(check_even,my_list_number1): #filter(function,parameter)
    print(n)

# lambda Expression
# function that use one time
# no method's name
my_list_number2 = [9,2,3,4,5,6]

for item in map(lambda num:num**2,my_list_number2):
    print(item)
