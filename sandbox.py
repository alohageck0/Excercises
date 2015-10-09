G = ['7283455864',
     '6731158619',
     '8988242643',
     '3830589324',
     '2229505813',
     '5633845374',
     '6473530293']

P = ['9505',
     '3845',
     '3530']

for i in range(len(G)):
    if P[0] not in G[i]:
        if i <= len(G):
            continue
        else:
            print("NO")
            break
    else:
        row = i
        first = G[i].index(P[0])
        break
        # todo iterate trhough remaining elems in G, if another elems from P have index as first elemhhhjkjkkj

# print(row, first)

if len(P) - 1 >= len(G) - row:
    print("NO")
else:
    i = 1
    while i < len(P):
        if P[i] in G[row + i]:
            if G[row + i].index(P[i]) != first:
                print("NO")
                break
            else:
                if i == len(P) - 1:
                    print("YES")
                    break
                i += 1
        else:
            print("NO")
            break
