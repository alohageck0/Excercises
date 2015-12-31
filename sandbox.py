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


def count_hourglass(first, second):
    summ = 0
    summ += arr[first][second]
    summ += arr[first][second + 1]
    summ += arr[first][second + 2]
    summ += arr[first + 1][second + 1]
    summ += arr[first + 2][second]
    summ += arr[first + 2][second + 1]
    summ += arr[first + 2][second + 2]
    return summ


result = 0
for i in range(4):
    for j in range(4):
        test = count_hourglass(i, j)
        if test > result:
            result = test
print(result)
