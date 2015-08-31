edges = [(2, 1), (3, 1), (4, 3), (5, 2), (6, 1), (7, 2), (8, 6), (9, 8), (10, 8)]
arr = [10, 9]


# # arr = [int(x) for x in input().split(' ')]
# for i in range(arr[1]):
#     edges.append(tuple([int(x) for x in input().split(' ')]))

# {8: [9, 10], 1: [2, 3, 6], 2: [5, 7], 3: [4], 6: [8]}
class Graph:
    def __init__(self, list1):
        self.edges = list1
        self.edges_d = dict()
        self.final = []
        for edge in self.edges:
            if not edge[1] in self.edges_d.keys():
                self.edges_d[edge[1]] = [edge[0]]
            else:
                self.edges_d.get(edge[1]).append(edge[0])

    def children_of_node(self, node):
        """
            returns list of values of 'node' key
            :param node:
            :return:
            """
        temp = self.edges_d.get(node)
        for i in temp:
            self.final.append(i)


# todo try store dict in class variable and create method which returns amount of childs of any node
test = Graph(edges)
print(test.edges_d)


def count_child(node, dict1):
    count = []
    if node not in dict1.keys():
        count += 0


    # if
    #     count = 0
    #     # for node in dict1.get(key):
    return count

# print(count_child(8, vertices))
