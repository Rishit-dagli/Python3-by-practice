
#Print the string of number without using string function

n = int(input("Enter the number: "))
r = range(1,n+1)
print(*r,sep="")