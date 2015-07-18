__author__ = 'royalfiish'

coords = [0, 0]


def change_coords(tup):
    global coords
    tup0 = tup[0].lower()
    tup1 = int(tup[1])
    if tup0 == 'up':
        coords[1] += tup1
    elif tup0 == 'down':
        coords[1] -= tup1
    elif tup0 == 'right':
        coords[0] += tup1
    elif tup0 == 'left':
        coords[0] -= tup1
    else:
        print("Enter 'UP, DOWN, RIGHT or LEFT': ")
        return False


test = ['DOWN', 4]
test1 = ['UP', 5]
tes = change_coords(test)
tes = change_coords(test1)
print(coords)
'''
while True:
    put = input("Enter 'direction, steps': ")
    if not put:
        break
    acc = tuple(put.split(' '))

print(acc)
'''
'''
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2

The numbers after the direction are steps.
Please write a program to compute the distance from current position after a sequence of
movement and original point. If the distance is a float, then just print the nearest integer.

Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
