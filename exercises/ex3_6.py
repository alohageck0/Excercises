__author__ = 'royalfiish'

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

foo_square = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, lis))
for num in foo_square:
    print(num)

'''
Question:
    Write a program which can map() and filter() to make a list whose
    elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints:

    Use map() to generate a list.
    Use filter() to filter elements of a list.
    Use lambda to define anonymous functions.
'''
