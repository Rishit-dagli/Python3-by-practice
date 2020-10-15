# pass
x = [1,2,3]
for i in x:
    # comment use pass to avoid syntax error
    pass

# continue
my_string = 'sammy'
for i in my_string:
    if i == 'a':
        continue
    print(f'letter : {i}')

# break
y = [1,2,3,4,5]
for i in y:
    if i == 3:
        break
    print(f'print {i} before break')
