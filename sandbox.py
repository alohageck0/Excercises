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
    summ = 0
    summ += arr[start][start]
    a = arr[start][start]
    summ += arr[start][start + 1]
    a = arr[start][start + 1]
    summ += arr[start][start + 2]
    a = arr[start][start + 2]
    summ += arr[start + 1][start + 1]
    a = arr[start + 1][start + 1]
    summ += arr[start + 2][start]
    a = arr[start + 2][start]
    summ += arr[start + 2][start + 1]
    a = arr[start + 2][start + 1]
    summ += arr[start + 2][start + 2]
    a = arr[start + 2][start + 2]
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
