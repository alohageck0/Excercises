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
    print(P)
    print(G)
    # for elem in G:
    #    if P[0] in elem:
    #        print('Yes')
