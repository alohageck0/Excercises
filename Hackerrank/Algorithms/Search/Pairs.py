given = [int(x) for x in input().split(" ")]
numbers = [int(x) for x in input().split(" ")]
arr = sorted(numbers)
count = 0
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if arr[j] - arr[i] == given[1]:
            count += 1
            break
print(count)


# 43253
