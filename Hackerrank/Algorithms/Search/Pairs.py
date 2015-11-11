given = [int(x) for x in input().split(" ")]
numbers = [int(x) for x in input().split(" ")]
arr = sorted(numbers)
point = int(len(arr) / 2)
diff = given[1]
down = arr[:point]
up = arr[point:]
count = 0
i = len(down)
j = 0
while j < len(up):
    tryDiff = abs(down[i] - up[j])
    if tryDiff == diff and i > 0:
        count += 1
    else:
        if tryDiff > diff:
            i -= 1
        else:
            j += 1
print(count)

# 43253
