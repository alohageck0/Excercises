__author__ = 'royalfiish'


def get_indecies(weight):
    global left
    global right
    global index_dict
    global right_arr
    global left_arr
    global summ
    summ = 0
    left = weight
    right = 0
    index_arr = [i for i in range(100)]
    index_dict = dict()
    left_arr = []
    right_arr = []
    while True:
        if left > right:
            for item in index_arr:
                right += 3 ** item
                summ = right
                right_arr.append(item)
                print('R')
                if (left + summ) > 3 ** item:
                    right = 0
                    right_arr.remove(item)
                    continue
                elif left > right:
                    continue
                elif left < right:
                    break

        elif left < right:
            for item in index_arr:
                left += 3 ** item
                left_arr.append(item)
                print('L')
                if left < right:
                    continue
                elif left > right:
                    break
        elif left == right:
            break
    return index_dict


x = get_indecies(3)
print(x)
