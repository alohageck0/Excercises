G = ['7283455864',
     '6731158619',
     '8911111143',
     '3830589324',
     '1311111111',
     '5633845374',
     '6473530293']

P = ['1111',
     '5374',
     '0293']

arr = []


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


testCount = len(P) - 1
count = int
result = "NO"
for i in range(len(G) - len(P)):
    if result == "YES":
        break
    indeciesArrayFirstElem = findIndecies(G[i], P[0])
    if not indeciesArrayFirstElem:
        continue
    else:
        i += 1
        for index in indeciesArrayFirstElem:
            for j in range(1, len(P)):
                testStrin = G[i]
                if testStrin.count(P[j]) > 1:
                    indeciesArrayNextElem = findIndecies(testStrin, P[j])

                else:
