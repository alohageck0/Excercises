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


def check35(num):
    numStr = str(num)
    for k in range(len(numStr)):
        act3 = 0
        act5 = 0
        if k == 3:
            act3 += 1
            print(act3)
        elif k == 5:
            act5 += 1
            print(act5)
        if not act3 % 5 and not act5 % 3:
            return True
        else:
            return False

for j in range(10 ** (number - 1), 10 ** (number)):
    if checkNumber(j):
        lis.append(j)

# for item in lis:
#     if check35(item):
#         pass
#     else:
#         lis.remove(item)
print(lis)
