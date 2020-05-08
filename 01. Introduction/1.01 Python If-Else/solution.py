n = int(input().strip())
if n%2 == 1:
    print("Weird")
elif n>1 and n<6:
    print("Not Weird")
elif n>5 and n<21:
    print("Weird")
else:
    print("Not Weird")
