# N = int(input())
# sticks = [int(x) for x in input().split(" ")]

N = 8
sticks = [1, 13, 3, 8, 14, 9, 4, 4]
cutted = 0
while N != cutted:
    cut = min(filter(lambda x: x > 0, sticks))
    print(N - cutted)
    cutted = 0
    for i in range(len(sticks)):
        sticks[i] = sticks[i] - cut
        if sticks[i] <= 0:
            cutted += 1
