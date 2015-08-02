__author__ = 'royalfiish'

popilation = [[1, 2, 3],
              [2, 3, 4],
              [3, 2, 1],
              [1, 4, 5]]

x_max_row = len(popilation[0])
y_max_col = len(popilation)


def find_neighbors(y, x):
    coords = [[] for i in range(4)]
    coords = [[x, y + 1], [x, y - 1], [x - 1, y], [x + 1, y]]

    def clean_arr(arr):
        for i in arr:
            for j in range(len(i)):
                if i[j] < 0 or i[j] > x_max_row or i[j] > y_max_col:
                    arr.remove(i)
                    return clean_arr(arr)

    clean_arr(coords)
    return coords


x = enumerate(popilation)
for i in x:
    print(i)
