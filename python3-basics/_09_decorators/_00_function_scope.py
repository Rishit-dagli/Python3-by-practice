# normal function
def my_func():
    print(1)


# function in scope of local function
def hello(name='Jose'):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is welcome() inside hello'

    print(greet())
    print(welcome())
    print('This is the end of the hello function!')


hello()