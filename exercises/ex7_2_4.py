__author__ = 'royalfiish'


class Rectangle:
    def __init__(self, length, width):
        self.len = length
        self.width = width

    def area(self):
        return self.len * self.width


test = Rectangle(3, 5)
print(test.area())
'''
    Define a class named Rectangle which can be constructed by a length and width.
    The Rectangle class has a method which can compute the area.

Hints:

    Use def methodName(self) to define a method.
'''
