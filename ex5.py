__author__ = 'royalfiish'


class Func():

    def __init__(self):
        self.x = ""

    def getstring(self):
        self.x = raw_input('Enter string: ')

    def toupper(self):
        print self.x.upper()

y = Func()
y.getstring()
y.toupper()

