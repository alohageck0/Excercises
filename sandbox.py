# given = [int(x) for x in input().split(" ")]
# numbers = [int(x) for x in input().split(" ")]
# arr = sorted(numbers)

given = [5, 2]
arr = [1, 2, 3, 4, 5]
result = [1 for i in arr if i + given[1] in arr]
print(len(result))
