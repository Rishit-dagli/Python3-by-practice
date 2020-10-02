# # Python Basics
# ''' Multiline Comments '''

# # Basic Calculations
a = 5
b = 10
c = a/b
print("a/b = ",c)

# # User Input
d = int(input("Enter the value of d: "))
print(d)

# # Use of if-else statement
if d%2 == 0:
    print("Number is Even: ",d)
else:
    print("Number is Odd: ",d)

# # tables (for loops)
x = int(input("Enter the number: "))
for i in range(1,11):
    print(i*x)

# list == array (in python)
fruits = ["apple","mango","banana","orange","grapes"]
print(fruits[1])
for i in range(0,4):
    print(fruits[i])
print(type(fruits))

# Tuple
cars = ("creta","swift","kio")
print(type(cars))
print(cars[0])

# set
trees = {"neem", "tulsi","cactus"} 
print(type(trees))
print(trees[0])
#Set doesnot support indexing
#Set is an unordered 

# Dictionary
# Just like JSON data
# car = {"brand": "Ford", "Model": "Mustang", "Year": 1964}
