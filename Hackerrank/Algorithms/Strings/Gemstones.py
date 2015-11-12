count = dict()
number = 0
arr = []
loops = int(input())
for i in range(loops):
    arr.append(input())
for strin in arr:
    for letter in set(strin):
        if letter not in count.keys():
            count[letter] = 1
        else:
            count[letter] += 1
for value in count.values():
    if value >= loops:
        number += 1
print(number)
