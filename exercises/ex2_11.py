__author__ = 'royalfiish'

arr = []
for strin in range(2):
    arr.append(input("Enter string: "))
len1 = len(arr[0])
len2 = len(arr[1])
if len1 > len2:
    print(arr[0])
elif len1 == len2:
    for strin in arr:
        print(strin)
else:
    print(arr[1])

'''
Question:
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string
'''
