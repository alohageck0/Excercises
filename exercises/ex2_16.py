__author__ = 'royalfiish'

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
list_even = []
for num in tup:
    if not num % 2:
        list_even.append(num)
print(tuple(list_even))

# Question:
#     Write a program to generate and print another tuple whose values
#     are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
# 
# Hints:
# 
#     Use "for" to iterate the tuple
#     Use tuple() to generate a tuple from a list.
