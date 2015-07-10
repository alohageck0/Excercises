fn = int(raw_input('Enter number: '))
i = 1
fact = fn
while i <= (fn - 1):
    fact = fact * (fn - i)
    i += 1
print fact

'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''
