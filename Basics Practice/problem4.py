# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i^2.

n = int(input())
if (n>=1 & n<=20):
    for i in range(0,n):
        print(i*i)

