class Dog():
    def __init__(self, name,spots):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.name = name
        # Expect boolean True/False
        self.spots = spots

my_dog = Dog(name='Jojo',spots=True)