name = 'this is global string'

def greet():
    # name = 'Jojo'
    def hello():
        name = 'IM A LOCAL'
        print('Hello '+name)
    hello()
greet()

x = 50
def func(x):
    x = 200
    print(f'x is {x}')

func(x)
