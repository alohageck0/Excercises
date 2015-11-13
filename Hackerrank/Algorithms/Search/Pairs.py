# given = [int(x) for x in input().split(" ")]
# numbers = [int(x) for x in input().split(" ")]
# arr = sorted(numbers)
def pointer(point):
    global count
    down = arr[:point]
    up = arr[point:]
    i = len(down) - 1
    j = 0
    while j < len(up):
        while abs(down[i] - up[j]) > diff and i > 0:
            i -= 1
        if abs(down[i] - up[j]) == diff:
            count += 1
        j += 1


given = [5, 2]
arr = [1, 2, 3, 4, 5]
count = 0
diff = given[1]

point = int(len(arr) / 2)
for i in range(1, len(arr) - 1):
    pointer(i)
print(count)
