def convert32bit(num):
    binum = bin(num)[2:]
    if len(binum) < 32:
        binum32 = "0" * (32 - len(binum)) + binum
        return binum32
    else:
        return binum


def flip(strin):
    flipped = str()
    for bit in strin:
        if not int(bit):
            flipped += "1"
        else:
            flipped += "0"
    return flipped


loops = int(input())
for i in range(loops):
    number = int(input())
    print(int(flip(convert32bit(number)), 2))
