__author__ = 'royalfiish'

strin = 'abcdefgabc'
children = dict()

for letter in strin:
    if not children.get(letter):
        children[letter] = 1
    else:
        children[letter] += 1

for k in sorted(children.keys()):
    print(str(k) + ',' + str(children[k]))

'''
Question:

Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.
'''
