__author__ = 'royalfiish'

line = list(input('Enter sentence: '))
d = dict(UPPER=0, LOWER=0)
for ch in line:
    if ch.isupper():
        d['UPPER'] += 1
    elif ch.islower():
        d['LOWER'] += 1
    else:
        pass

print('UPPER ', d['UPPER'])
print('LOWER ', d['LOWER'])


'''
Write a program that accepts a sentence and calculate
the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
