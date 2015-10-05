cases = int(input())


def addElem(r):
    matrix = []
    for i in range(r):
        matrix.append([int(x) for x in input().split()])
    return matrix


def getMatrix():
    RandC = [int(x) for x in input().split(" ")]
    matrix = addElem(RandC[0])
    return matrix


for i in range(cases):
    G = getMatrix()
    P = getMatrix()
