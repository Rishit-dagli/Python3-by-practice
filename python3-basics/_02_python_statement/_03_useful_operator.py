from random import shuffle
from random import randint

for i in range(10):  # range (start, stop, step)
    print(f'i is {i}')

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

word = 'abcde'
for index, letter in enumerate(word):
    print(index, letter)
    print('\n')

my_list = [0, 1, 2]
my_list1 = ['a', 'b', 'c']
for item in zip(my_list, my_list1):
    print(item)

# in keywords operator
print(f'0 is in my_list : {0 in my_list}')

# min max function
print(f'min of my_list is {min(my_list)}')
print(f'min of my_list is {max(my_list)}')

# shuffle reference function
shuffle(my_list)
print(f'shuffle my_list : {my_list}')

# random
print(f'random 0 to 100 : {randint(0,100)}')

# input
result = input('What is your name?')
print(result)
