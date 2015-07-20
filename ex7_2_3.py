import math

__author__ = 'royalfiish'


class Circle:
    def __init__(self, radius):
        self.rad = radius

    def area(self):
        return round(math.pi * self.rad ** 2)


test = Circle(50)
print(test.area())

'''
Question:
Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.

'''
