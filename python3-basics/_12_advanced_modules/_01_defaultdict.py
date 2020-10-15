from collections import defaultdict

d = {'k1': 1}
print(d['k1'])
# print(d['k2']) # this line will get KeyError

d = defaultdict(object)
print(d['one'])  # not error

for item in d:
    print(item)

d = defaultdict(lambda: 0)  # return 0 as default value of all keys

print(d['one'])
print(d['two'])
