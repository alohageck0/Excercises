__author__ = 'royalfiish'

popilation = [[1, 2, 3],
              [2, 3, 4],
              [3, 2, 1]]


def answer(population, x, y, strength=None):
    popilation[x][y] = -1
    for x_col in popilation:
        for y_row in x_col:
            if popilation[x_col][y_row] == -1:





'''
[[1, 2, 3], [2, 3, 4], [3, 2, 1]]

[[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
'''
