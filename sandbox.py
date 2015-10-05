G = ['7283455864', '6731158619', '8988242643',
     '3830589324', '2229505813', '5633845374', '6473530293',
     '7053106601', '0834282956', '4607924137']

P = ['9505', '3845', '3530']

for elem in G:
    if P[0] in elem:
        # print('Yes')
        row = G.index(elem)
        first = elem.index(P[0])

        if len(G) - G.index(elem) < len(P) - 1:
            print("NO")
            break
        print(row, first)
    else:
        print("NO")
        # todo iterate trhough remaining elems in G, if another elems from P have index as first elem
