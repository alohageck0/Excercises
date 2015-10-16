G = ['7283455864',
     '6731158619',
     '8988242643',
     '3830589324',
     '139502395055395022',
     '5633845374',
     '6473530293']

P = ['3950',
     '5374',
     '0293']

arr = []


def findNewIndex(elem):
    global arr
    if P[0] in elem:
        ind = elem.index(P[0])
        if not arr:
            arr.append(elem.index(P[0]))
        else:
            arr.append(arr[-1] + len(P[0]) + ind)
    elem = elem[len(P[0]) + ind:]
    if P[0] not in elem:
        print(arr)
    else:
        return findNewIndex(elem)


findNewIndex(G[4])
