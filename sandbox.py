strin = "BBBBB"
deletions = 0
letter = strin[0]
for i in range(1, len(strin)):
    if strin[i] == letter:
        deletions += 1
    else:
        letter = strin[i]
print(deletions)
