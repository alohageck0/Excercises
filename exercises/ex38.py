__author__ = 'royalfiish'

inp = int(input("Enter n: "))


def foo(n):
    for i in range(0, n + 1):
        if not i % 2:
            yield str(i)


print(",".join(foo(inp)))

'''
Question:

Please write a program using generator to print the even numbers between 0 and n in comma separated form
while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

Hints:
Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.
'''
