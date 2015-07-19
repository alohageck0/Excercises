__author__ = 'royalfiish'


def get_dict(n):
    numbers = dict()
    for num in range(1, n + 1):
        numbers[num] = num ** 2
    for k, v in numbers.items():
        print(k, '-', v)


get_dict(20)
'''
Question:
    Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
    and the values are square of keys.

Hints:

    Use dict[key]=value pattern to put entry into a dictionary.
    Use ** operator to get power of a number.
    Use range() for loops.
'''
