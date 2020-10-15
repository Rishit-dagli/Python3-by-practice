s = 'hello'
# next(s) → this line will error not support iterable
s_iter = iter(s)
h = next(s_iter)
print(h)