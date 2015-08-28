edges = [(2, 1), (3, 1), (4, 3), (5, 2), (6, 1), (7, 2), (8, 6), (9, 8), (10, 8)]
arr = [10, 9]


# # arr = [int(x) for x in input().split(' ')]
# for i in range(arr[1]):
#     edges.append(tuple([int(x) for x in input().split(' ')]))

# {8: [9, 10], 1: [2, 3, 6], 2: [5, 7], 3: [4], 6: [8]}

def make_dic(edges):
    edges_d = dict()
    for edge in edges:
        if not edge[1] in edges_d.keys():
            edges_d[edge[1]] = [edge[0]]
        else:
            edges_d.get(edge[1]).append(edge[0])
    return edges_d


vertices = make_dic(edges)


# print(vertices.get(9))


def count_child(start, dict1):
    count = 0
    if start not in dict1.keys():
        count += 0
    # todo for node in start loop thru keys to add length
    # if
    #     count = 0
    #     # for node in dict1.get(key):
    return count

# print(count_child(8, vertices))
