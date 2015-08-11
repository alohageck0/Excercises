__author__ = 'royalfiish'

total = int(input())
strin = input()
arr = strin.split(' ')
pos = 0
neg = 0
zero = 0
for i in map(int, arr):
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zero += 1
print(round((pos / total), 3))
print(round((neg / total), 3))
print(round((zero / total), 3))
