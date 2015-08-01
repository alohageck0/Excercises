__author__ = 'royalfiish'

arr1 = ["I", "You"]
arr2 = ["Play", "Love"]
arr3 = ["Hockey", "Football"]

for i in range(len(arr1)):
    for j in range(len(arr2)):
        for k in range(len(arr3)):
            print(arr1[i] + ' ' + arr2[j] + ' ' + arr3[k])

'''
Please write a program to generate all sentences where subject is in
["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list.
'''
