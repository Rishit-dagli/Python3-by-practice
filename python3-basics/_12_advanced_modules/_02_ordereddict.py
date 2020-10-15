from collections import OrderedDict
print('Normal dictionary')

d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['e'] = 'E'

for k, v in d.items():
	print(k, v)

print('Ordered dictionary')
d = OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['e'] = 'E'
for k, v in d.items():
	print(k, v)


d1 = {}
d1['a'] = 1
d1['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print( d1 == d2)  # True

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print( d1 == d2)  # False



