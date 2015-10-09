G = ['7283455864',
     '6731158619',
     '8988242643',
     '3830589324',
     '2229505813',
     '5633845374',
     '6473530293',
     '7053106601',
     '0834282956',
     '4607924137']

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

print(row, first)
# for i in range(1, len(P) - 1):
#     if G[row + 1].index(P[i]) == first:
#         row += 1
#         continue
#     else:
#         print("NO")
#         break
#     print("YES")
