# arr = [int(x) for x in input().split(' ')]
number = 0
num = 5
fibo = []


def fibon(fir, secon):
    global number
    global num
    global fibo
    if number <= num:
        sec = secon ** 2 + fir
        number += 1
        fibo.append(sec)
        fir = secon
        return fibon(fir, sec)


fibon(0, 1)
print(fibo)
