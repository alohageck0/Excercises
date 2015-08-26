edges = [(2, 1), (3, 1), (4, 3), (5, 2), (6, 1), (7, 2), (8, 6), (9, 8), (10, 8)]
arr = [10, 9]


# # arr = [int(x) for x in input().split(' ')]
# for i in range(arr[1]):
#     edges.append(tuple([int(x) for x in input().split(' ')]))


def make_dic(edges):
    edges_d = dict()
    for edge in edges:
        if not edge[1] in edges_d.keys():
            edges_d[edge[1]] = [edge[0]]
        else:
            edges_d.get(edge[1]).append(edge[0])
    return edges_d


print(make_dic(edges))
edges = [(3, 1), (4, 3), (5, 2), (6, 1), (7, 2), (8, 6), (9, 8), (10, 8)]
print(sorted(make_dic(edges)))
