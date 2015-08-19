__author__ = 'royalfiish'


def sum_array(n):
    s = sum(n)
    print(s)


inp1 = input()
inp = input()
arr = inp.split(' ')
arr_digit = [int(x) for x in arr]
sum_array(arr_digit)
