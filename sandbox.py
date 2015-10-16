G = ['7283455864',
     '6731158619',
     '8988242643',
     '3830589324',
     '1239503950',
     '5633845374',
     '6473530293']

P = ['3950',
     '5374',
     '0293']

smallLen = len(P[0])

arr = []


def findNewIndex(elem):
    '''
    create array with indecies of P[0]
    :param elem:
    :return:
    '''
    global arr
    if P[0] in elem:
        ind = elem.index(P[0])
        if not arr:
            arr.append(elem.index(P[0]))
        else:
            arr.append(arr[-1] + len(P[0]) + ind)
        elem = elem[len(P[0]) + ind:]
    if P[0] not in elem:
        return
    else:
        return findNewIndex(elem)


for elem in G:
    if not arr:
        findNewIndex(elem)
    else:
        break
# todo create function if found match with first element, but not found pattern and reminder rows in G more than rows in pattern -
# todo loop findNewIndex() again until rows G < rows P
if not arr:
    print("NO")
else:
    i = 1
    for inde in arr:
        while i < len(P):
            if P[i] in G[row + i]:
                if G[row + i].index(P[i]) != inde:
                    prints.append("NO")
                    break
                else:
                    if i == len(P) - 1:
                        prints.append("YES")
                        break
                    i += 1
            else:
                prints.append("NO")
                break
                # print(prints)
    if "YES" in prints:
        print("YES")
    else:
        print("NO")
