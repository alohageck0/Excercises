__author__ = 'royalfiish'


class Calc:
    def __init__(self):
        self.val = int

    def square(self, value):
        self.val = value ** 2
        return self.val


num = int(input("Enter number to calculate square value: "))
number = Calc()
print('Square number of', num, 'is', number.square(num))

'''
Question:
    Write a method which can calculate square value of number

Hints:
    Using the ** operator
'''
