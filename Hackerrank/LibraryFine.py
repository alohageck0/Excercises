__author__ = 'royalfiish'

actual = input()
arr_act = actual.split(' ')
expected = input()
arr_exp = expected.split(' ')
total = 0
if actual == expected or (
                    int(arr_act[0]) < int(arr_exp[0]) and int(arr_act[1]) == int(arr_exp[1]) and int(arr_act[2]) == int(
            arr_exp[2])) or int(arr_act[1]) < int(arr_exp[1]) or int(arr_act[2]) < int(arr_exp[2]):
    print(0)
else:
    if not int(arr_act[0]) == int(arr_exp[0]):
        razn1 = int(arr_act[0]) - int(arr_exp[0])
        total = razn1 * 15
    if not int(arr_act[1]) == int(arr_exp[1]):
        razn1 = int(arr_act[1]) - int(arr_exp[1])
        total = razn1 * 500
    if not int(arr_act[2]) == int(arr_exp[2]):
        total = 10000
print(total)
