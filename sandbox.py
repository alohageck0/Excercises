import math


# loops = int(input())

def findFirstSquare(first, last):
    while first < last + 1:
        square = math.sqrt(first)
        if int(square) == square:
            return int(square)
        first += 1
    return 0


print(findFirstSquare(3, 9))
