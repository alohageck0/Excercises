import math

__author__ = 'royalfiish'

x = raw_input('Enter sequence of numbers: ')
list_D = x.split(",")
# print list_D
result = []

def sqrt (D):
    d = int(D)
    q = math.sqrt((2 * 50 * d )/ 30)
    return q.__trunc__()

for D in list_D:
    result.append(str(sqrt(D)))
print (",").join(result)

