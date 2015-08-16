__author__ = 'royalfiish'
loops = int(input())

for i in range(loops):
    height_0 = 1
    cycles = int(input())
    if not cycles:
        pass
    else:
        for i in range(cycles):
            if i == 0 or not i % 2:
                height_0 *= 2
            else:
                height_0 += 1
    print(height_0)
