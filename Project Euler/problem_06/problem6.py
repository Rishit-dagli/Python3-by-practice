import math

def nsum(n):
    s = (n * (n + 1)) / 2
    ss = math.pow(s,2)
    return ss

def ssum(n):
    x = (n * (n + 1) * ((2 * n) + 1)) / 6
    return x

def dif(a,b):
    d = a - b
    print(d)

num = 100

dif(nsum(num),ssum(num))

