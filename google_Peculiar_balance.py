__author__ = 'royalfiish'


def get_indecies(weight):
    global left
    global right
    left = weight
    right = 0
    index_arr = [i for i in range(100)]
    index_dict = dict()
    while True:
        if left == right:
            return index_dict
            break
        elif left > right:
            if (left - right) == 1:
                right += 1
                index_dict[0] = 'R'
                continue
            elif (left - right) == 3:
                right += 3
                index_dict[1] = 'R'
                continue
            for item in index_arr:
                right += 3 ** item
                index_dict[item] = 'R'
                if









        elif (right - left) == 1:
            left += 1
            index_dict[0] = 'L'
            continue
        elif (left - right) == 3:
            right += 3
            index_dict[1] = 'R'
            continue
        elif (right - left) == 3:
            left += 3
            index_dict[1] = 'L'
            continue

    return index_dict


x = get_indecies(3)
print(x)
