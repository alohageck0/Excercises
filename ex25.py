__author__ = 'royalfiish'


class Testclass:
    classparam = 'CLASS'

    def __init__(self, instparam=None):
        self.inst = instparam


test = Testclass('INSTANCE')
print('%s is class parameter and %s is instance parameter' % (test.classparam, test.inst))

test = Testclass()
test.inst = 'INSTANCE'
print('%s is class parameter and %s is instance parameter' % (test.classparam, test.inst))



'''
Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
'''
