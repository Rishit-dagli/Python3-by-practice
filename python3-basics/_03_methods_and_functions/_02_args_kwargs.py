# args return tuple
# kwargs return dictionary

def myfunc(a,b,c=0,d=0):
    # Returns 5% of the sum of a and b
    return sum((a,b,c,d))*0.05
result = myfunc(40,60)
print(result)

# this line will error myfunc(40,40,40,40,40)

def myfunc1(*args): # args can be a word you want such as vals
    # Returns 5% of the sum of a and b
    return sum((args))*0.05
result1 = myfunc1(40,60,40)
print(result1)

def myfunc2(*args):
    for item in args:
        print(item)
myfunc2(1,2,3,4,5)

def myfunc3(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}.'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
myfunc3(fruit='apple')
