count = dict()

loops = int(input())
for i in range(loops):
    strin = input()
    for letter in strin:
        if letter not in count.keys():
            count[letter] = 1
        else:
            count[letter] += 1
print(count)
