class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2 # this can be self.pi Circle.pi


my_circle = Circle()
result = my_circle.get_circumference()
print(result)