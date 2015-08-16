import math

__author__ = 'royalfiish'
loops = int(input())

for i in range(loops):
    arr = [int(x) for x in input().split(' ')]
    count = 0
    for num in range(arr[0], arr[1] + 1):
        square = math.sqrt(num)
        if int(square) == square:
            count += 1
        else:
            continue
    print(count)
