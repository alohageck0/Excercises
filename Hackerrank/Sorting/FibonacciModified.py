arr = [int(x) for x in input().split(' ')]
first = int
sec = int
number = int


def fibon(fir, secon, num):
    global number
    global first
    global sec
    first = fir
    sec = secon
    if number <= num:
        sec = sec ** 2 + first
        first = sec
        number += 1
        return sec, number


print(fibon(first, sec, 3))
