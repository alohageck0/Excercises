__author__ = 'royalfiish'


class Generator:
    def __init__(self):
        self.n = int
        self.d = int

    def generate(self, range, divisible):
        self.n = range
        self.d = divisible
        gen = 0
        while gen <= self.n:
            if not gen % self.d:
                yield gen
            else:
                pass
            gen += 1


test_lis = Generator()

for x in test_lis.generate(100000, 7):
    print(x)

'''
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield
'''
