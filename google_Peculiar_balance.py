__author__ = 'royalfiish'


def answer(x):
    def summa_ostatka(n):
        summa = 0
        for x in range(0, n):
            summa += 3 ** x
        return summa

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
    max_ind_arr = [x for x in range(max_ind)]
    right = 3 ** max_ind
    index_dict[max_ind] = 'R'
    for _ in reversed(max_ind_arr):
        if left == right:
            break
        elif (left + summa_ostatka(_)) < right:
            left += 3 ** _
            index_dict[_] = "L"
            continue
        elif (left + summa_ostatka(_)) > right:
            right += 3 ** _
            index_dict[_] = 'R'
            continue
        elif (left + 3 ** _) > (right + summa_ostatka(_)):
            index_dict[_] = "-"
            continue
    print(index_dict)


answer(22)
