loops = int(input())
for i in range(loops):
    blackwhite = [int(x) for x in input().split(" ")]
    costs = [int(x) for x in input().split(" ")]
    if abs(costs[0] - costs[1]) > costs[2]:
    # write
    else:
        amount = blackwhite[0] * costs[0] + blackwhite[1] + costs[1]
    print(amount)
