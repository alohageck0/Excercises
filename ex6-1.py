import math

__author__ = 'royalfiish'
result = []
items = [x for x in (raw_input('Enter sequence of numbers: ').split(','))]
for d in items:
    result.append(str(int(math.sqrt((2 * 50 * float(d) )/ 30))))
print (",").join(result)
