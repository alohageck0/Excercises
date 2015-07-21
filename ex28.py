__author__ = 'royalfiish'


def foo(numerator, denominator):
    global a
    a = numerator
    print(a / denominator)


try:
    foo(5, 0)
except ZeroDivisionError:
    print(a, "can not divide by zero")
finally:
    print("Settings restored")

'''
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions.
'''
