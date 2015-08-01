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
            right_arr.append(max_ind)
    max_ind_arr = [x for x in range(max_ind)]
    right = 3 ** max_ind
    for _ in reversed(max_ind_arr):
        if left == right:
            break
        elif (left + summa_ostatka(_)) <= right:
            left += 3 ** _
            left_arr.append(_)
            continue
        elif (left + summa_ostatka(_)) > right:
            continue
        elif (left + 3 ** _) > (right + summa_ostatka(_)):
            right += 3 ** _
            right_arr.append(_)
            continue
    print(right_arr)
    print(left_arr)


answer(2)
