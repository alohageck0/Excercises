__author__ = 'royalfiish'
loops = int(input())

for i in range(loops):
    number = input()
    children = 0
    for letter in number:
        divisor = int(letter)
        if not divisor:
            continue
        elif not int(number) % divisor:
            children += 1
        else:
            continue
    print(children)
