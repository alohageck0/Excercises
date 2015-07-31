__author__ = 'royalfiish'


def get_indecies(weight):
    global left
    global right
    left = weight
    right = 0
    indecies_arr = [x for x in range(100)]
    indecies_dict = dict()
    while not left == right:
        if (left - right) == 1:
            right += 1
            indecies_dict[0] = 'R'
            continue
        elif (right - left) == 1:
            left += 1
            indecies_dict[0] = 'L'
            continue
        elif (left - right) == 3:
            right += 3
            indecies_dict[1] = 'R'
            continue
        elif (right - left) == 3:
            left += 3
            indecies_dict[1] = 'L'
            continue

    return indecies_dict


x = get_indecies(3)
print(x)
