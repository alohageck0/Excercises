__author__ = 'royalfiish'

line = input('Enter sentence: ')
clean_list = []
symbols = '!@#$%^&*()_ +{}|:\";\'<>?,./'
for letter in line:
    for i in range(0, len(symbols)):
        line = line.replace(symbols[i], "")
        if len(letter) > 0:
            clean_list.append(letter)

# print(line)
letters = 0
digits = 0
for ch in line:
    try:
        int(ch)
        digits += 1
    except:
        letters += 1

print('LETTERS ', letters, '\n', 'DIGITS ', digits)

'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
