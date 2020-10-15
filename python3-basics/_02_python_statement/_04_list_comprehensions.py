# beginner do
my_string = 'hello'
my_list = []
for letter in my_string:
    my_list.append(letter)
print(my_list)

# advance
my_list_adv = [letter for letter in my_string]
print(my_list_adv)

# create list of range number
list_number = [number for number in range(0, 10)]
print(list_number)

# create list of range number square
list_number = [number ** 2 for number in range(0, 10)]
print(list_number)

# with if statement
list_number = [number for number in range(0, 10) if number % 2 == 0]
print(list_number)

# celcius to fahrenheit
c = [0, 10, 20, 34.5]
f = [((9 / 5) * temp + 32) for temp in c]
print(f)
