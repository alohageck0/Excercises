__author__ = 'royalfiish'

total = 0
while True:
    put = input('Enter: ')
    if not put:
        break
    acc = put.split(' ')
    if acc[0] is 'D':
        total += int(acc[1])
    elif acc[0] is 'W':
        total -= int(acc[1])
    else:
        pass
print(total)

'''
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200
¡­
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''
