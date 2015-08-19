__author__ = 'royalfiish'

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

foo = map(lambda x: x ** 2, lis)
for num in foo:
    print(num)

'''
Question:
    Write a program which can map() to make a list whose
    elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints:

    Use map() to generate a list.
    Use lambda to define anonymous functions.
'''
