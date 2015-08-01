__author__ = 'royalfiish'


def get_indecies(weight):
    summ = 0
    left = weight
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
    print(max_ind)


get_indecies(13)
