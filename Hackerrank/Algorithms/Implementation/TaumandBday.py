loops = int(input())
for i in range(loops):
    blackwhite = [int(x) for x in input().split(" ")]
    costs = [int(x) for x in input().split(" ")]
    if abs(costs[0] - costs[1]) > costs[2]:
        if costs[0] > costs[1]:
            amount = blackwhite[1] * costs[1] + blackwhite[0] * costs[1] + blackwhite[0] * costs[2]
        else:
            amount = blackwhite[0] * costs[0] + blackwhite[1] * costs[0] + blackwhite[1] * costs[2]
    else:
        amount = blackwhite[0] * costs[0] + blackwhite[1] + costs[1]
    print(amount)
