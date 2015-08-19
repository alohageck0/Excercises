__author__ = 'royalfiish'
x = [1, 3, 6, 78, 35, 55]
y = [12, 24, 35, 24, 88, 120, 155]
x = set(x)
y = set(y)
x.intersection_update(y)
print(x)

'''
Question:

With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
write a program to make a list whose elements are intersection of the above given lists.

Hints:
Use set() and "&=" to do set intersection operation.
'''
