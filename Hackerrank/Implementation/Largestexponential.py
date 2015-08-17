__author__ = 'royalfiish'

loops = int(input())


def find_index(arr, num):
    """

    :param arr - list of inputs:
    :param num - number to find index:
    :return index of element:
    """
    for i in arr:
        if i[0] == num:
            return arr.index(i)


indexes = []
for i in range(loops):
    arr = [int(x) for x in input().split(' ')]
    indexes.append(arr)
