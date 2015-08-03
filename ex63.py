__author__ = 'royalfiish'

legs = int
for i in range(1, 36):
    if 2 * i + (35 - i) * 4 == 94:
        print('Chicken:', i, "Rabbits", 35 - i)
    else:
        continue
'''
Question:

Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.
'''
