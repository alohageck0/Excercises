edges = [(2, 1), (3, 2), (4, 3), (5, 2), (6, 4), (7, 4), (8, 1), (9, 5), (10, 4), (11, 4), (12, 8), (13, 2), (14, 2),
         (15, 8), (16, 10), (17, 1), (18, 17), (19, 18), (20, 4), (21, 15), (22, 20), (23, 2), (24, 12), (25, 21),
         (26, 17), (27, 5), (28, 27), (29, 4), (30, 25)]
arr = [30, 29]


# edges = []
# arr = [int(x) for x in input().split(' ')]
# for i in range(arr[1]):
#     edges.append(tuple([int(x) for x in input().split(' ')]))

# {1: [2, 8, 17], 2: [3, 5, 13, 14, 23], 3: [4], 4: [6, 7, 10, 11, 20, 29], 5: [9, 27], 8: [12, 15], 10: [16], 12: [24],
# 15: [21], 17: [18, 26], 18: [19], 20: [22], 21: [25], 25: [30], 27: [28]}


# {8: [9, 10], 1: [2, 3, 6], 2: [5, 7], 3: [4], 6: [8]}
class Graph:
    def __init__(self, list1, arr1):
        self.arr = arr1
        self.edges = list1
        self.edges_d = dict()
        self.check_key = []
        self.temp = []
        self.children = int
        for edge in self.edges:
            if not edge[1] in self.edges_d.keys():
                self.edges_d[edge[1]] = [edge[0]]
            else:
                self.edges_d.get(edge[1]).append(edge[0])


test = Graph(edges, arr)

children = 0
count = 0


def check_key(node):
    global children
    children = 0
    if node in test.edges_d.keys():
        return test.edges_d.get(node)
    else:
        return test.temp


def foo(list):
    global children
    if not len(list):
        return
    children += len(list)
    footemp = list
    temp = []
    for i in footemp:
        if i in test.edges_d.keys():
            temp.extend(test.edges_d.get(i))
        else:
            continue
    return foo(temp)


for node in range(2, arr[0] + 1):
    children = 0
    temp = check_key(node)
    foo(temp)
    if children % 2 and children != 0:
        count += 1
    else:
        continue
print(count)
