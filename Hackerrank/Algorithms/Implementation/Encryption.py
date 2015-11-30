import math
# message = input()
message = "if man was meant to stay on the ground god would have given us roots"
newMess = message.replace(" ", "")
# rows = round(math.sqrt(len(input().replace(" ", ""))))
rows = round(math.sqrt(len(message.replace(" ", ""))))
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
for elem in Matrix:
    strin = ""
    for i in range(rows + 1):
        strin += elem[i]
    arr.append(strin)
print(arr)
