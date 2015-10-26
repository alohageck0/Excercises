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


def splitElem(strin, num):
    arr = []
    while strin:
        arr.append(strin[:num])
        strin = strin[num:]
    return arr


def findIndecies(strin, pattern):
    """
    Returns array of indexes of first row of pattern
    :param strin:
    :param pattern:
    :return:
    """
    found = []
    last_index = -1
    if pattern in strin:
        while True:
            try:
                last_index = strin.index(pattern, last_index + 1)
            except ValueError:
                break
            else:
                found.append(last_index)
        return found
    else:
        return False


for i in range(cases):
    G = getMatrix()
    P = getMatrix()
    testCount = len(P) - 1
    count = 0
    result = "NO"
    for i in range((len(G) - len(P)) + 1):
        if result == "YES":
            break
        indeciesArrayFirstElem = findIndecies(G[i], P[0])
        if not indeciesArrayFirstElem:
            continue
        else:
            i += 1
            for elem in range(i, i + len(P) - 1):
                for index in indeciesArrayFirstElem:
                    for j in range(1, len(P)):
                        testStrin = G[elem]
                        if testStrin.count(P[j]) >= 1:
                            indeciesArrayNextElem = findIndecies(testStrin, P[j])
                            if index in indeciesArrayNextElem:
                                count += 1
    if testCount == count:
        result = "YES"
    print(result)
