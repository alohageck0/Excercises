__author__ = 'royalfiish'

popilation = [[1, 2, 3],
              [2, 3, 4],
              [3, 2, 1],
              [1, 4, 5]]
# popil = [[6, 7, -1, 7, 6], [6, -1, -1, -1, 7], [-1, -1, -1, -1, 10], [8, -1, -1, -1, 9], [8, 7, -1, 9, 9]]
x_max_row = len(popilation[0])
y_max_col = len(popilation)

print(x_max_row)
print(y_max_col)


def find_neighbors(x, y):
    coords = [[] for i in range(4)]
    coords = [[x, y + 1], [x, y - 1], [x - 1, y], [x + 1, y]]

    def clean_arr(arr):
        for i in arr:
            for j in range(len(i)):
                if i[j] < 0 or i[j] > (x_max_row - 1) or i[j] > (y_max_col - 1):
                    arr.remove(i)
                    return clean_arr(arr)

    clean_arr(coords)
    return coords


print(find_neighbors(0, 2))
