def ask_for_init():
    try:
        result = int(input('please input a number: '))
    except:
        print('That is not a nubmer')
    else:
        print('Yes thank you')
    finally:
        print('end of try/except/finally')

ask_for_init()
