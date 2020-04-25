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
