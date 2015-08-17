import math


# loops = int(input())

testarr = [[3, 4],
           [2, 3],
           [4, 1]]

first = [int(x) for x in input().split(' ')]
count = 1

second = [int(x) for x in input().split(' ')]


def find_power(first, second):
    firstBase = first[0]
    secondBase = second[0]
    if firstBase != secondBase:
        power = math.log(firstBase, secondBase)
    return power


new_power = second[1] / find_power(first, second)
if first[1] > new_power:
    print('first bigger')
else:
    print('second bigger')

# inps = []
# for i in range(loops - 1):
#     arr = [int(x) for x in input().split(' ')]
#     inps.append(arr)
