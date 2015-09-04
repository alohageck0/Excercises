edges = [(2, 1), (3, 1), (4, 3), (5, 2), (6, 1), (7, 2), (8, 6), (9, 8), (10, 8)]
arr = [10, 9]


# # arr = [int(x) for x in input().split(' ')]
# for i in range(arr[1]):
#     edges.append(tuple([int(x) for x in input().split(' ')]))

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

    def add_to_list(self, list):
        self.final.extend(list)
        for i in self.final:
            self.add_to_list(self.edges_d.get(i))

    def children_of_node(self, parent):
        count = 0
        if parent in self.edges_d.keys():
            count += self.count_nodes(parent)
        else:
            return count
        temp = self.get_children_list(parent)

        for i in temp:
            count += self.count_nodes(i)
            temp

    def get_children_list(self, node):
        if node in self.edges_d.keys():
            return self.edges_d.get(node)

    def count_nodes(self, node):
        if node in self.edges_d.keys():
            return len(self.edges_d.get(node))
        else:
            return 0

    def check_key(self, node):
        self.check_key = []
        self.children = 0
        self.temp = []
        if node in self.edges_d.keys():
            return self.edges_d.get(node)
        else:
            return self.check_key

    def foo(self, list):
        if not len(list):
            return
        self.children += len(self.temp)
        footemp = list
        self.temp = []
        for i in footemp:
            if i in test.edges_d.keys():
                self.temp.extend(test.edges_d.get(i))
            else:
                continue
        return foo(self.temp)

        # def get_list_of_nodes(graph, x):


# test

# def count_child(graph, node):
#     count = 0
#     if node in graph.edges_d.keys():
#         count += len(graph.edges_d.get(node))
#     temp = graph.edges_d.get(node)
#     print(temp, count)
#
#     # for child in temp:
#     #     count += graph.count_nodes(child)
#     #     return count_child(graph, child)
#     # return count
#
#     # if
#     #     count = 0
#     #     # for node in dict1.get(key):
#     # return count


test = Graph(edges, arr)
# test.check_key(1)

print(test.children)
children = 0
count = 0


def check_key(node):
    arr = []
    if node in test.edges_d.keys():
        return test.edges_d.get(node)
    else:
        return arr


temp = check_key(5)


def foo(list):
    global temp
    global children
    if not len(list):
        return
    children += len(temp)
    footemp = list
    temp = []
    for i in footemp:
        if i in test.edges_d.keys():
            temp.extend(test.edges_d.get(i))
        else:
            continue
    return foo(temp)


foo(temp)
print(children)
# # print(count_child(8, vertices))
# for node in range(arr[0]):
#     count = int
#     children = foo()
#     if not children % 2:
#         count += 1
#     else:
#         continue
# print(count)
