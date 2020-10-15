# format 0
try:
    result = 10+10
except:
    print('program is error!')
else:
    print(result)
finally:
    print('======== end program')

# format 1
try:
    result = 10+10
    print(result)
except:
    print('program is error!')
finally:
    print('======== end program')
