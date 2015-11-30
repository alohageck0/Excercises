import math

message = input()
newMess = message.replace(" ", "")
rows = round(math.sqrt(len(message.replace(" ", ""))))
columns = rows
while columns * rows < len(newMess):
    columns += 1
arr = []
Matrix = [["" for x in range(columns)] for x in range(rows)]
for elem in Matrix:
    for i in range(len(elem)):
        try:
            elem[i] = newMess[i]
        except IndexError:
            pass
    newMess = newMess[columns:]
for i in range(columns):
    word = ""
    for elem in Matrix:
        word += elem[i]
    arr.append(word)
print(" ".join(arr))
