__author__ = 'royalfiish'
import timeit


def test():
    return 1 + 1


t = timeit.Timer()

print(t.timeit(test()))
