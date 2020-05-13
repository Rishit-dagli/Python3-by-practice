N = int(input())
stud_dict = dict()

for i in range(N):
    tmp = input().split(' ')
    name = tmp[0]
    stud_dict[name] = (float(tmp[1]), float(tmp[2]), float(tmp[3]))
    
name = input()
print('%.2f' % (sum(stud_dict[name]) / 3.0))
