class Dog:

    # Class Object Attribute
    # Same for any instance of a class
    species = 'mammal'

    def __init__(self, name,spots):
        self.name = name
        # True/False
        self.spots = spots

    # OPERATIONS/Actions --> method
    def print_details(self):
        print(self.name + ' ' + str(self.spots))

    def bark(self,number): # connect bark method to use self keyword
        for i in range(0,number):
            print('wolf!')

my_dog = Dog(name='Jojo',spots=True)
my_dog.print_details()
my_dog.bark(4)