#!/bin/python3

import sys

arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 9, 2, -4, -4, 0],
       [0, 0, 0, -2, 0, 0],
       [0, 0, -1, -2, -4, 0]]


# arr = []
# for arr_i in range(6):
#     arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#     arr.append(arr_t)


def count_hourglass(start):
    summ = arr[start][start] + arr[start][start + 1] + arr[start][start + 2] + arr[start + 1][start + 1] + \
           arr[start + 2][start] + arr[start + 2][start + 1] + arr[start + 2][start + 2]
    return summ


num1 = 0
num2 = 0
result = 0
for i in range(4):
    for j in range(4):
        test = count_hourglass(j)
        if test > result:
            result = test
print(result)
