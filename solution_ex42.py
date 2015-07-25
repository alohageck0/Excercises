__author__ = 'royalfiish'

import math

steps = 0


def bin_search(li, element):
    global steps
    bottom = 0
    top = len(li) - 1
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top + bottom) / 2.0))
        if li[mid] == element:
            index = mid
        elif li[mid] > element:
            top = mid - 1
        else:
            bottom = mid + 1
        steps += 1
    return index


li = range(1, 100000)
print(bin_search(li, 1))
print(steps)
