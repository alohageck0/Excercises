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

arr = []
for elem in G:
    for i in range(len(elem)):
        if elem[i] == P[0][0]:
            if elem[i] == P[0]:
                arr.append(i)

print(arr)
# todo first find index of first digit - then split from that index by number of small number,
# then look reminder of element for first digit and split - at the end find indecies of large number
