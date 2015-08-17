__author__ = 'royalfiish'

loops = int(input())

testarr = [[3, 4],
           [2, 3],
           [4, 1]]


def find_index(arr, num):
    """

    :param arr - list of inputs:
    :param num - number to find index:
    :return index of element:
    """
    for i in arr:
        if i[0] == num:
            return arr.index(i)


def find_max_base(arr):
    maxBase = arr[0][0]
    for i in arr:
        if i[0] >= maxBase:
            maxBase = i[0]
    return maxBase


inps = []
for i in range(loops - 1):
    arr = [int(x) for x in input().split(' ')]
    inps.append(arr)
