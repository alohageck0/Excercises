__author__ = 'royalfiish'

import re

emailAddress = input()
pat2 = re.compile("(\w+)@((\w+\.)+(\w))")
r2 = pat2.match(emailAddress)
print(r2.group(1))
# p = re.compile('(a(b)c)d')
# m = p.match('abcd')
# print(m.group(0))
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
