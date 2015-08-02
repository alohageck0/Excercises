__author__ = 'royalfiish'

popilation = [[1, 2, 3],
              [2, 3, 4],
              [3, 2, 1],
              [1, 4, 5]]

x_max_row = len(popilation[0])
y_max_col = len(popilation)


def open_near(y, x):
    coords = [[] for i in range(4)]
    coords = [[x, y + 1], [x, y - 1], [x - 1, y], [x + 1, y]]

    def clean_arr(arr):
        for i in arr:
            for j in range(len(i)):
                if i[j] < 0:
                    arr.remove(i)
                    return clean_arr(arr)

    clean_arr(coords)
    return coords


print(open_near(0, 0))

# def answer(population, x, y, strength=None):
#     popilation[x][y] = -1
#     for x_col in popilation:
#         for y_row in x_col:
#             if popilation[x_col][y_row] == -1:
#                 for x in range(1, 5):


'''
[[1, 2, 3], [2, 3, 4], [3, 2, 1]]

[[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
'''
