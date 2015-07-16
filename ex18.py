import string

__author__ = 'royalfiish'

passwords = input("Enter passwords: ").split(',')


def check_len(password):
    if 6 <= len(password) <= 12:
        return True
    else:
        return False


def check_symbol(list1, list2):
    Check_sym = False
    for letter in list1:
        if letter in list2:
            Check_sym = True
    return Check_sym


lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
number = list(string.digits)
special = ['$', '#', '@']
valid = []

for password in passwords:
    if not check_len(password):
        continue
    else:
        pass
    if not check_symbol(password, lower):
        continue
    elif not check_symbol(password, upper):
        continue
    elif not check_symbol(password, number):
        continue
    elif not check_symbol(password, special):
        continue
    else:
        pass
    valid.append(password)

print(','.join(valid))

'''
Question:
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
