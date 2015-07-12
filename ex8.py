__author__ = 'royalfiish'

words = input('Enter words separated by comma: ')
words_list = words.split(',')
print(', '.join(sorted(words_list)))

'''
Question:
Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''
