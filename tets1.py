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
nextIndex = 0

arr = []


def findIndex(elem):
    global nextIndex
    global arr
    global P
    for i in range(len(elem)):
        if elem[i] == P[0][0]:
            if elem.index(P[0]) == i:
                if not arr:
                    arr.append(i)
                    nextIndex = i + len(P[0])
                    break
                else:
                    arr.append(nextIndex + i)
                    nextIndex = arr[-1] + len(P[0])
                    break
    if nextIndex >= len(elem):
        print(arr)
    else:
        return findIndex(elem[nextIndex:])


# smallLen = len(P[0])
# tempIndex = int
# for elem in G:
#     findIndex(elem)
findIndex(G[4])




# todo first find index of first digit - then split from that index by number of small number,
# then look reminder of element for first digit and split - at the end find indecies of large number
