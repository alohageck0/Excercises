given = [int(x) for x in input().split(" ")]
numbers = [int(x) for x in input().split(" ")]
arr = sorted(numbers)
point = int(len(arr) / 2)
first = arr[:point]
second = arr[point:]


# 43253
