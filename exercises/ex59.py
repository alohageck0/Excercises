__author__ = 'royalfiish'

lis = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
lis_set = set(lis)
lis1 = []
for x in lis:
    if x in lis_set:
        lis1.append(x)
        lis_set.remove(x)
print(lis1)

'''
With a given list [12,24,35,24,88,120,155,88,120,155],
write a program to print this list after removing all duplicate values with original order reserved.

Hints:
Use set() to store a number of values without duplicate.
'''
