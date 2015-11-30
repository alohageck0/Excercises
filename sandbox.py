import math
# message = input()
message = "chillout"
newMess = message.replace(" ", "")
# rows = round(math.sqrt(len(input().replace(" ", ""))))
rows = round(math.sqrt(len(newMess)))
print(rows)
arr = []
Matrix = [["" for x in range(rows + 1)] for x in range(rows)]
for elem in Matrix:
    for i in range(len(elem)):
        try:
            elem[i] = newMess[i]
        except IndexError:
            pass
    newMess = newMess[rows + 1:]
print(Matrix)
for i in range(rows + 1):
    word = ""
    for elem in Matrix:
        word += elem[i]
    arr.append(word)
print(" ".join(arr))
