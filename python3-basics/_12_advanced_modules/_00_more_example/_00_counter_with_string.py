from collections import Counter

print('=== with string')
print(Counter('aabsbsbsbhshhbbsbs'))

s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

print('=== with sentence')
print(Counter(words))