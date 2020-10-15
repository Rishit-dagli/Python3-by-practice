def hello():
    return 'Hi Jose!'


def other(some_def_func):  # try pass function as parameter
    print('Other code runs here!')
    print(some_def_func())


other(hello)
