__author__ = 'royalfiish'
import ex21


def print_doc(func):
    print(func.__doc__)


print_doc(abs)
print_doc(int)
print_doc(input)
print_doc(ex21.change_coords)

'''
Question:
    Python has many built-in functions, and if you do not know how to use it,
    you can read document online or find some books.
    But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function

Hints:
    The built-in document method is __doc__
'''
