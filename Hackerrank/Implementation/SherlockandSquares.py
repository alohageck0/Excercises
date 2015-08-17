import math

loops = int(input())


def findFirstSquare(first, last):
    while first < last + 1:
        square = math.sqrt(first)
        if int(square) == square:
            return int(square)
        first += 1
    return 0


for i in range(loops):
    count = 0
    arr = [int(x) for x in input().split(' ')]
    if findFirstSquare(arr[0], arr[1]):
        first = findFirstSquare(arr[0], arr[1])
    else:
        print(count)
        continue
    while first ** 2 <= arr[1]:
        first += 1
        count += 1
    print(count)
