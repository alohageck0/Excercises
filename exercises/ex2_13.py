__author__ = 'royalfiish'

numbers = dict()
for num in range(1, 4):
    numbers[num] = num ** 2
for k, v in numbers.items():
    print(k, '-', v)

'''
Question:
    Define a function which can print a dictionary where the keys are numbers
    between 1 and 3 (both included) and the values are square of keys.

Hints:

    Use dict[key]=value pattern to put entry into a dictionary.
    Use ** operator to get power of a number.
'''
