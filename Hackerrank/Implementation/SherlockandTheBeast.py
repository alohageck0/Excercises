__author__ = 'royalfiish'

loops = int(input())
for i in range(loops):
    number = int(input())
lis = []


def checkNumber(num):
    check = True
    numStr = str(num)
    for k in range(len(numStr)):
        if not numStr[k] in ['3', '5']:
            check = False
    return check


for j in range(10 ** (number - 1), 10 ** (number)):
    if checkNumber(j):
        lis.append(j)

        # print(lis)
