import math

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

rectangle = Rectangle(5,7)

print("Area of the rectangle is {:.2f}".format(rectangle.get_area()))
