__author__ = 'royalfiish'


def get_indecies(weight):
    global left
    global right
    global left_arr
    global right_arr
    global summ
    global index_dict
    index_dict = dict()
    left = weight
    right = 0
    summ = 0
    index_arr = [i for i in range(100)]
    left_arr = []
    right_arr = []
    while True:
        if left > right:
            for item in index_arr:
                summ += right
                right += 3 ** item
                right_arr.append(item)
                print('R')
                if (left + summ) > right:
                    right = 0
                    right_arr = []
                    continue
                elif (left + summ) == right:
                    left_arr = right_arr
                    right_arr = [item]
                else:
                    break

        # elif left < right:
        #     for item in index_arr:
        #         left += 3 ** item
        #         left_arr[item] = 'L'
        #         print('L')
        #         if (right - left) >= 3 ** index_arr[item + 1]:
        #             continue
        #         else:
        #             break
        elif left == right:
            break

    print(right_arr)


x = get_indecies(3)
print(x)
