# coding=utf-8
__author__ = 'royalfiish'
import numpy


def two_dim_list(x, y):
    arr2 = numpy.empty((x, y))
    for x in numpy.nditer(arr2, op_flags=['readwrite']):
        print(x)


two_dim_list(2, 3)

'''
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1, Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0],
 [0, 1, 2, 3, 4],
 [0, 2, 4, 6, 8]]
'''
