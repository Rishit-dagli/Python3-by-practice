from collections import namedtuple

t = (1, 2, 3)
print(t[0])

Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2, breed='Lab', name='Sammy')
print(sam.age)
print(sam[0])  # can do this because it's tuple

Cat = namedtuple('Cat', 'fur claws name')
c = Cat(fur='Fuzzy', claws=False, name='Kitty')
print(c.name)
print(c[2])
