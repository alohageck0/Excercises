import math

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


def find_max_base(arr):
    maxBase = arr[0][0]
    for i in arr:
        if i[0] >= maxBase:
            maxBase = i[0]
    return maxBase


inps = []
for i in range(loops):
    arr = [int(x) for x in input().split(' ')]
    inps.append(arr)
position = int(input())
base = find_max_base(inps)

for arr in inps:
    if arr[0] != base:
        koef = math.log(base, arr[0])
        arr.append(arr[1] / koef)
    else:
        arr.append(arr[1])

new_list = sorted(inps, key=lambda x: x[2])
print(str(new_list[position - 1][0]) + ' ' + str(new_list[position - 1][1]))
