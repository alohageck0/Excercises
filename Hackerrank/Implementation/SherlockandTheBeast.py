__author__ = 'royalfiish'

loops = int(input())


def count(num):
    if num <= 5:
        if num == 3:
            return '555'
        elif num == 5:
            return '33333'
        else:
            return -1
    arr = dict()
    threes = 0
    while True:
        ost = (num - threes * 5)
        if ost < 0:
            return -1
        if not ost % 3:
            arr['fives'] = ost // 3
            arr['threes'] = threes
            return arr
            break
        else:
            threes += 1
            continue


for i in range(loops):
    numberdigits = int(input())
    dic = count(numberdigits)
    if type(dic) == dict:
        print('555' * dic['fives'] + '33333' * dic['threes'])
    else:
        print(dic)
