# Inheritance
print('======= Inheritance')


class Animal:

    def __init__(self,name):
        self.name = name
        print('from animal class')

    def speak(self):
        print('I am '+self.name+'.')


class Rabbit(Animal):

    def __init__(self,name):
        self.name = name
        print('creating a rabbit object')


my_rabbit = Rabbit('Rabito')
my_rabbit.speak()

# Polymorphism
print('======= Polymorphism')


class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " wolf!"


class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " meow!"


def pet_speak(pet):
    print(pet.speak())


dog = Dog('Dogy')
pet_speak(dog)

cat = Cat('Caty')
pet_speak(cat)

# Abstract class design for base class only


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Method speak did not implement!')


class Dog(Animal):
    def speak(self):
        return self.name + " wolf!"


dogy = Dog('Dogy')
print(dogy.speak())
