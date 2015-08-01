__author__ = 'royalfiish'


def summa_ostatka(n):
    summa = 0
    for x in range(0, n):
        summa += 3 ** x
    return summa


print(summa_ostatka(1))
