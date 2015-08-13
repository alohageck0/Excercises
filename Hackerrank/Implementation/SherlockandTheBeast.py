__author__ = 'royalfiish'

loops = int(input())
for i in range(loops):
    number = int(input())
lis = []
newlis = []


# todo try generator
def checkNumber(num):
    check = True
    numStr = str(num)
    for k in range(len(numStr)):
        if not numStr[k] in ['3', '5']:
            check = False
    return check


def check35(num):
    numStr = str(num)
    act3 = 0
    act5 = 0
    for k in numStr:
        if k == '3':
            act3 += 1
        elif k == '5':
            act5 += 1
    if act3 >= 5 or act5 >= 3 or (act3 >= 5 and act5 >= 3):
        if (not act3 % 5 and act5 == 0) or (not act5 % 3 and act3 == 0) or not act3 % 5 or not act5 % 3:
            # print("act3 = ", act3)
            # print("act5 = ", act5)
            return True
        else:
            return False
    else:
        return False


for j in range(10 ** (number - 1), 10 ** (number)):
    if checkNumber(j):
        lis.append(j)

for item in lis:
    if check35(item):
        newlis.append(item)
if len(newlis) == 0:
    print(-1)
else:
    print(max(newlis))
