__author__ = 'royalfiish'


class American:
    @staticmethod
    def printNationality(val=None):
        print(val)

    def __init__(self):
        self.nat


class NewYorker(American):
    def __init__(self):
        self.nat = 'New Yorker'


man = NewYorker()
American.printNationality()
American.printNationality("American")
NewYorker.printNationality(man.nat)

'''
Question:
Define a class named American and its subclass NewYorker.

Hints:

Use class Subclass(ParentClass) to define a subclass.
'''
