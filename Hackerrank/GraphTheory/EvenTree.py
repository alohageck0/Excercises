# edges = [(2, 1), (3, 1), (4, 3), (5, 2), (6, 1), (7, 2), (8, 6), (9, 8), (10, 8)]
# arr = [10, 9]

edges = []
arr = [int(x) for x in input().split(' ')]
for i in range(arr[1]):
    edges.append(tuple([int(x) for x in input().split(' ')]))


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
    if not children % 2 and children != 0:
        count += 1
    else:
        continue
print(count)
