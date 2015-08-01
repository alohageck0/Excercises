__author__ = 'royalfiish'


def answer(x):
    summ = 0
    left = x
    right = 0
    index_arr = [i for i in range(100)]
    index_dict = dict()
    left_arr = []
    right_arr = []
    max_ind = int
    for i in index_arr:
        summ = right
        right += 3 ** i
        if (left + summ) >= 3 ** i:
            max_ind = i
            right_arr.append(max_ind)
    max_ind_arr = [x for x in range(max_ind)]
    for _ in reversed(max_ind_arr):
        if (left + 3 ** _) >
