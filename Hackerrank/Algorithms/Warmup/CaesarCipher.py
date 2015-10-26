import string

length = int(input())
strin = input()
k = int(input())
lower = string.ascii_lowercase
upper = string.ascii_uppercase
strin1 = []
for letter in strin:
    if letter in lower:
        k_ = lower.index(letter) + k
        if k_ < len(lower):
            strin1.append(lower[k_])
        else:
            strin1.append(lower[k_ % len(lower)])
    elif letter in upper:
        k_ = upper.index(letter) + k
        if k_ < len(lower):
            strin1.append(upper[k_])
        else:
            strin1.append(upper[k_ % len(lower)])
    else:
        strin1.append(letter)
print(''.join(strin1))
