import random

__author__ = 'royalfiish'

lis = random.sample([x for x in range(1, 1001) if not x % 5 and not x % 7], 5)
print(lis)

'''
Question:

Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 ,
between 1 and 1000 inclusive.



Hints:
Use random.sample() to generate a list of random values.
'''
