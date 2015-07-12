__author__ = 'royalfiish'


def to_decimal(binary):
    return int(binary, 2)


words = input('Enter words separated by space: ').split(',')
divisible = []
for num in words:
    if not to_decimal(num) % 5:
        divisible.append(num)
print(','.join(divisible))

'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers
as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''
