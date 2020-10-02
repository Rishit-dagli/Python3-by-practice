n1= input()
n2 = input()
j = 1
for i in range(1,n1+1):
    j = i*j
k = j%n2
print(k)
print("\n")