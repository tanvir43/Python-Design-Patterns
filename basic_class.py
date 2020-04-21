import math

class Circle:

    def __init__(self, radius):
        """
        Object Initialization with "radius" parameter
        """
        self.radius = int(radius)

    def get_area(self):
        """
        method to calculate area
        """
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        """
        method to calculate perimeter
        """
        return 2 * math.pi * self.radius

# Creating object from "Circle" class
circle = Circle("5")

print(f"Circle radius {circle.radius}")

#Call "get_area()" method from "circle" object
print(f"Area of the circle is {circle.get_area():.2f}")

#Call "get_perimeter" method from "circle" object
print(f"Perimeter of the circle is {circle.get_perimeter():.2f}")
