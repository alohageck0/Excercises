__author__ = 'royalfiish'

arr = []
for i in range(1000, 3001):
    for j in str(i):
        if not int(j) % 2:
            continue
        else:
            arr.append(str(i))
    continue
print(', '.join(arr))
'''
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
