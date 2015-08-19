__author__ = 'royalfiish'

num = int(input("Enter number to check: "))


def check_even(number):
    if not number % 2:
        print("It is an even number")
    else:
        print("It is an odd number")


check_even(num)

'''
Question:
    Define a function that can accept an integer number as input and print the
    "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

    Use % operator to check if a number is even or odd.
'''
