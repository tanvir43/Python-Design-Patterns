import math

# Rectangle and Circle class have some common attribute and method

class OldRectangle:
    def __init__(self, color, filled, width, length):
        self.color = color
        self.filled = filled
        self.width = width
        self.length = length

        def get_color(self):
            return self.color
        def set_color(self, color):
            self.color = color
            return self.color
        def get_filled(self):
            return self.filled
        def sef_filled(self, filled):
            self.filled = filled
            return self.filled
        def is_filled(self):
            return self.filled
        def get_area(self):
            return self.width * self.length

class OldCircle:
    def __init__(self, color, filled, radius):
        self.color = color
        self.filled = filled
        self.radius = radius

        def get_color(self):
            return self.color
        def set_color(self, color):
            self.color = color
            return self.color
        def get_filled(self):
            return self.filled
        def sef_filled(self, filled):
            self.filled = filled
            return self.filled
        def is_filled(self):
            return self.filled
        def get_area(self):
            return math.pi * self.__radius ** 2

# Remove common attributes and methods from "Rectangle" and "Circle" class
# and add a parent class 'Shape' having that common attributes and methods

class Shape:
    def __init__(self, color="red", filled=True):
        self.color = color
        self.filled = filled

    def get_color(self):
            return self.color
    def set_color(self, color):
        self.color = color
        return self.color
    def get_filled(self):
        return self.filled
    def sef_filled(self, filled):
        self.filled = filled
        return self.filled
    def is_filled(self):
        return self.filled

# 'Rectangle' class inherits the 'Shape' class

class Rectangle(Shape):
    def __init__(self, width, length):

        # super() method for calling parent class method,
        # this time its calling __init__() method.

        super().__init__()
        self.width = width
        self.height = length

    def get_area(self):
        return self.width * self.length

# 'Circle' class inherits the 'Shape' class

class Circle(Shape):
    def __init__(self, radius):

        # again calling __init__() from parent method

        super().__init__()
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

rectange = Rectangle(2,3) 

# remove super().__init__() from the class, it will raise an error

print("Rectangle color is ", rectange.get_color()) # we are accessing parent class method

circle = Circle(7)

# remove super().__init__() from the class, it will raise an error

print("Set circle color as ", circle.set_color('blue')) # we are accessing parent class method
print("Cirlce color is ", circle.get_color()) # again we are accessing parent class method

