__author__ = 'royalfiish'

levels = int(input())
for i in reversed(range(levels)):
    print(' ' * i + '#' * (levels - i))
