__author__ = 'royalfiish'

lis = range(1, 4000, 1)
index = 0
step = 0


def find(elem, arr):
    global index
    global step
    step += 1
    denom = len(arr) // 2
    arr_elem = arr[denom]
    if denom == 1:
        return index
    if elem == arr_elem:
        index += denom
        return index
    elif elem < arr_elem:
        arr = arr[:denom + 1]
        return find(elem, arr)
    elif elem > arr_elem:
        arr = arr[denom:]
        index += denom
        return find(elem, arr)


print("Index is", find(1453, lis))
print("Steps", step)
'''
Question:

Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.


Hints:
Use if/elif to deal with conditions.
'''
