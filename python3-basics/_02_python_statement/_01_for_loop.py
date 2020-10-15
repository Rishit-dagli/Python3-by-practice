list_string = ['Hello',' ','World']
for i in list_string:
    print(i)


list_number = [1,2,3,4,5,6,7,8,9,10]
for i in list_number:
    if i%2==0:
        print(f'found even number {i}')
    else:
        print(f'found odd number {i}')

print('list_number len is ',len(list_number))


my_dict = {'k1':1,'k2':2,'k3':3}

print('=== loop dictionary')
for k,v in my_dict.items():
    print(v)
