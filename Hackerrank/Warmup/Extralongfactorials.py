__author__ = 'royalfiish'

number = int(input())
fact = number


def factorial(num):
    if num > 1:
        global fact
        fact *= num - 1
        return factorial(num - 1)
    else:
        return fact


print(factorial(number))
