cases = int(input())


def addElem(r):
    matrix = []
    for i in range(r):
        matrix.append(input())
    return matrix


def getMatrix():
    RandC = [int(x) for x in input().split(" ")]
    matrix = addElem(RandC[0])
    return matrix


# G = ['7283455864', '6731158619', '8988242643',
#      '3830589324', '2229505813', '5633845374', '6473530293',
#      '7053106601', '0834282956', '4607924137']
#
# P = ['9505', '3845', '3530']
for i in range(cases):
    G = getMatrix()
    P = getMatrix()
    # print(P)
    # print(G)
    for i in range(len(G)):
        if P[0] not in G[i]:
            if i <= len(G):
                continue
            else:
                print("NO")
                break
        else:
            row = i
            first = G[i].index(P[0])
            break

    if len(P) - 2 > len(G) - row:
        print("NO")
    else:
        i = 1
        while i < len(P):
            if P[i] in G[row + i]:
                if G[row + i].index(P[i]) != first:
                    print("NO")
                    break
                else:
                    if i == len(P) - 1:
                        print("YES")
                        break
                    i += 1
            else:
                print("NO")
                break
