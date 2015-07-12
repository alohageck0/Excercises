__author__ = 'royalfiish'


def check_every_digit(num):
    marker = int
    for n in str(num):
        if int(n) % 2:
            marker = 1
            break
        else:
            marker = 2
    if not marker % 2:
        return True
    else:
        return False


arr = []
for i in range(1000, 3001):
    if check_every_digit(i):
        arr.append(str(i))
print(', '.join(arr))

'''
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
