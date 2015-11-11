# given = [int(x) for x in input().split(" ")]
# numbers = [int(x) for x in input().split(" ")]
# arr = sorted(numbers)
given = [5, 2]
arr = [1, 2, 3, 4, 5]
point = int(len(arr) / 2)
diff = given[1]
down = arr[:point]
up = arr[point:]
print(down, up)
count = 0
i = len(down) - 1
j = 0
while j < len(up):
    while abs(down[i] - up[j]) > diff and i > 0:
        i -= 1
    if abs(down[i] - up[j]) == diff:
        count += 1
    j += 1
print(count)
# todo loop through elements in arrays
# 43253
