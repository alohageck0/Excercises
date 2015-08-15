__author__ = 'royalfiish'

loops = int(input())


def count(num):
    if num < 5:
        if num == 3:
            return '555'
        else:
            return -1
    arr = dict()
    fives = num // 3
    threes = 0
    while True:
        if (fives * 3 + threes * 5) > num:
            fives -= 1
            continue
        if (fives * 3 + threes * 5) == num:
            arr['fives'] = fives
            arr['threes'] = threes
            return arr
            break
        elif threes * 5 == num:
            arr['fives'] = 0
            arr['threes'] = threes
            return arr
            break
        elif fives < 0:
            return -1
            break
        else:
            fives -= 1
            threes += 1
            continue


for i in range(loops):
    numberdigits = int(input())
    dic = count(numberdigits)
    if type(dic) == dict:
        print('555' * dic['fives'] + '33333' * dic['threes'])
    else:
        print(dic)
