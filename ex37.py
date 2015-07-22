__author__ = 'royalfiish'

inp = int(input("Enter n: "))


def comp(n):
    if n > 1:
        return comp(n - 1) + comp(n - 2)
    elif n == 1:
        return 1
    elif n == 0:
        return 0


lis = [str(comp(inp)) for inp in range(0, inp + 1)]
print(', '.join(lis))

'''
Question:

    The Fibonacci Sequence is computed based on the following formula:


    f(n)=0 if n=0
    f(n)=1 if n=1
    f(n)=f(n-1)+f(n-2) if n>1

    Please write a program using list comprehension to print the Fibonacci Sequence
    in comma separated form with a given n input by console.

Example:
    If the following n is given as input to the program:

    7

    Then, the output of the program should be:

    0,1,1,2,3,5,8,13


Hints:
    We can define recursive function in Python.
    Use list comprehension to generate a list from an existing list.
    Use string.join() to join a list of strings.

In case of input data being supplied to the question, it should be assumed to be a console input.
'''
