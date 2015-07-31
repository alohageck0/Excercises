__author__ = 'royalfiish'


def get_indecies(weight):
    global left
    global right
    global index_dict
    left = weight
    right = 0
    index_arr = [i for i in range(100)]
    index_dict = dict()
    while True:
        if left > right:
            for item in index_arr:
                right += 3 ** item
                index_dict[item] = 'R'
                print('R')
                if (left - right) >= 3 ** index_arr[item + 1]:
                    right = 0
                    continue
                else:
                    break

        elif left < right:
            for item in index_arr:
                left += 3 ** item
                index_dict[item] = 'L'
                print('L')
                if (right - left) >= 3 ** index_arr[item + 1]:
                    continue
                else:
                    break
        elif left == right:
            break
    return index_dict


x = get_indecies(3)
print(x)
