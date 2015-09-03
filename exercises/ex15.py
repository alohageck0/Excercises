__author__ = 'royalfiish'

num = int(input('Enter number: '))


def count(num, digit):
    summ = 0
    for number in range(1, digit + 1):
        summ += int("%s" % str(num) * number)
    print(summ)


children(num, 4)

'''
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''
