arr = [0, 1, 5]
# arr = [int(x) for x in input().split(' ')]
number = 2
num = arr[2]
fibo = [arr[0], arr[1]]


def fibon(arr):
    global number
    global num
    global fibo
    if number <= num:
        sec = arr[-1] ** 2 + arr[-2]
        number += 1
        fibo.append(sec)
        return fibon(fibo)


fibon(fibo)
print(fibo[num - 1])
