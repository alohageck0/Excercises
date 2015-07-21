__author__ = 'royalfiish'
import re

while True:
    inp = input("Enter e-mail: ")
    if not inp:
        break
    pattern = re.compile("(\w+)@(\w+\.\w)")
    print(pattern.match(inp).group(1))

'''
Question:

Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the user name of a given email address.
Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john

In case of input data being supplied to the question, it should be assumed to be a console input.
'''
