G = ['7283455864',
     '6731158619',
     '8988242643',
     '3830589324',
     '131111111111112',
     '5633845374',
     '6473530293']

P = ['111',
     '5374',
     '0293']

arr = []


def findNewIndex(elem):
    global arr
    if P[0] in elem:
        ind = elem.index(P[0])
        if not arr:
            arr.append(ind)
        else:
            arr.append(arr[-1] + ind)
    elem = elem[ind:]
    if P[0] not in elem:
        print(arr)
    else:
        return findNewIndex(elem)


def findNewIndexNew(elem):
    global arr
    if P[0] in elem:
        for i in range(len(elem)):

            ind = elem.index(P[0])
            if i == ind:
                arr.append(i)
    print(arr)


def find_characters(word, character):
    found = []
    last_index = -1
    while True:
        try:
            last_index = word.index(character, last_index + 1)
        except ValueError:
            break
        else:
            found.append(last_index)
    return found
