try:
    # f = open('testfile','w')
    f = open('testfile','r')
    f.write('example : line one')
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error")
finally:
    print('=== end program')
