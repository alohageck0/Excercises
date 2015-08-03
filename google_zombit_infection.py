__author__ = 'royalfiish'

population = [[1, 2, 3],
              [2, 3, 4],
              [3, 2, 1],
              [1, 4, 5]]

popul = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
x_max_row = len(population[0])
y_max_col = len(population)


def answer(popul, y, x, strength=None):
    global population
    population = popul

    def next_round(popul, max_iter):
        global population
        population = popul
        for i in range(max_iter):
            for x_row in population:
                for y_col in range(len(x_row)):
                    if x_row[y_col] == -1:
                        neighbors = find_neighbors(population.index(x_row), y_col)
                        for neighbor in neighbors:
                            if population[neighbor[0]][neighbor[1]] <= strength:
                                population[neighbor[0]][neighbor[1]] = -1

    def find_neighbors(x, y):
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

    if population[x][y] <= strength:
        population[x][y] = -1
    else:
        return population
    if x_max_row >= y_max_col:
        next_round(population, x_max_row)
    elif x_max_row < y_max_col:
        next_round(population, y_max_col)

    return population


print(answer(population, 0, 0, 2))
first = answer(popul, 2, 1, 5)
for i in range(len(first)):
    print(first[i])
print([[6, 7, -1, 7, 6], [6, -1, -1, -1, 7], [-1, -1, -1, -1, 10], [8, -1, -1, -1, 9], [8, 7, -1, 9, 9]])
'''
[[1, 2, 3], [2, 3, 4], [3, 2, 1]]

[[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
'''
