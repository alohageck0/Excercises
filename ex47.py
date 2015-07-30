import random

__author__ = 'royalfiish'

lis = random.sample([x for x in range(100, 201) if not x % 2], 5)
print(lis)

'''
Question:

Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.



Hints:
Use random.sample() to generate a list of random values.
'''
