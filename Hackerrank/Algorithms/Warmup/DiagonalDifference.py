__author__ = 'royalfiish'

array = [[11, 2, 4],
         [4, 5, 6],
         [10, 8, -12]]

array1 = []
inp = int(input())
for i in range(inp):
    inp = input()
    digits = inp.split(' ')
    array1.append([int(x) for x in digits])


def foo(arr):
    d1 = 0
    d2 = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i + j == (len(arr) - 1):
                d1 += arr[i][j]
            if i == j:
                d2 += arr[i][j]
    print(abs(d1 - d2))


foo(array1)
