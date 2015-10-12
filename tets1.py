G = ['7283455864',
     '6731158619',
     '8988242643',
     '3830589324',
     '9509505813',
     '5633845374',
     '6473530293']

P = ['950',
     '384',
     '353']


def splitElem(strin, num):
    arr = []
    while strin:
        arr.append(strin[:num])
        strin = strin[num:]
    return arr


arr = splitElem(G[0], len(P[0]))
print(arr)
