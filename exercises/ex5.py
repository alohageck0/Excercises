__author__ = 'royalfiish'


class Func():
    def __init__(self):
        self.x = ""

    def getstring(self):
        self.x = input('Enter string: ')

    def toupper(self):
        print(self.x.upper())


y = Func()
y.getstring()
y.toupper()

'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
