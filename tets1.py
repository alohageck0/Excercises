G = ['7283455864',
     '6731158619',
     '8911111143',
     '3830589324',
     '1311111112',
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


# todo develop logic for searhcing every element
result = "NO"
for i in range(len(G) - len(P)):
    x = findIndecies(G[i], P[0])
    if not x:
        print(result)
