n=[]
r=[]
for i in range(int(input())):
    n.append(input())
    r.append(float(input()))
m=min(r)
re=[]
for i in range(len(r)):
    if r[i]==m :r[i]=1000
m=min(r)
for i in range(len(r)):
    if r[i]==m:re.append(n[i]) 
re.sort()
for i in re :print(i)
