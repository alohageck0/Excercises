__author__ = 'royalfiish'

legs = int
for i in range(1, 36):
    i_ = 35 - i
    if 2 * i + i_ * 4 == 94:
        print('Chicken:', i, "Rabbits:", i_)
    else:
        continue

'''
Question:

Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.
'''
