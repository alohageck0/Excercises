strin = "acxz"


def returnAscii(letter):
    return ord(letter)


# loops = int(input())
# for i in range(loops):
#     strin = input()
revStrin = strin[::-1]
maxIndex = len(strin) - 1
result = "Funny"
for i in range(1, len(strin)):
    if abs(returnAscii(strin[i]) - returnAscii(strin[i - 1])) == abs(
                    returnAscii(revStrin[i]) - returnAscii(revStrin[i - 1])):
        continue
    else:
        result = "Not Funny"
print(result)
