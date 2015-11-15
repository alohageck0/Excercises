given = [int(x) for x in input().split(" ")]
arr = [int(x) for x in input().split(" ")]
result = [1 for i in arr if i + given[1] in arr]
print(len(result))
