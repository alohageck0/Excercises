act3 = 0
act5 = 0


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
            print("act3 = ", act3)
            print("act5 = ", act5)
            return True
        else:
            return False
    else:
        return False


print(check35(333))
