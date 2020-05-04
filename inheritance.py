import math

# Rectangle and Circle class have some common attribute and method

class Rectangle:
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

class Circle:
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
            return math.pi * self.__radius ** 2
