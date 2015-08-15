__author__ = 'royalfiish'

loops = int(input())


def count(num):
    arr = dict()
    fives = num // 3
    threes = 0
    while True:
        if (fives * 3 + threes * 5) == num:
            arr['fives'] = fives
            arr['threes'] = threes
            break
        else:
            fives -= 1
            threes += 1
            continue
    return arr


for i in range(loops):
    numberdigits = int(input())
    dic = count(numberdigits)
    print('555' * dic['fives'] + '33333' * dic['threes'])
