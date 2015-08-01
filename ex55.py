__author__ = 'royalfiish'

lis = [12, 24, 35, 70, 88, 120, 155]
print([x for x in lis if not x % 5 and not x % 7])

'''
Question:

By using list comprehension, please write a program to print the list after removing
delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

Hints:[12,24,35,70,88,120,155]
Use list comprehension to delete a bunch of element from a list.
'''
