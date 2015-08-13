__author__ = 'royalfiish'

loops = int(input())
for i in range(loops):
    numberdigits = int(input())
    fives = numberdigits // 3
    threes = numberdigits - fives * 3

    if not threes % 5:
        print('555' * fives + '33333' * threes)
        # print(threes)
    elif not numberdigits % 5:
        threes = numberdigits // 5
        print('33333' * threes)
    else:
        print(-1)
