__author__ = 'royalfiish'
import zlib

strin = b"hello world!hello world!hello world!hello world!"
comp = zlib.compress(strin)
print(comp)
decomp = zlib.decompress(comp)
print(decomp)
'''
Question:

Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".



Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
'''
