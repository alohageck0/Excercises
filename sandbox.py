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


print(convert32bit(1))
print(flip("00000000000000000000000000000001"))
print(int("11111111111111111111111111111110", 2))

print(int(flip(convert32bit(1)), 2))
