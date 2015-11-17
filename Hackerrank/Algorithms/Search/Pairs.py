given = [int(x) for x in input().split(" ")]
numbers = [int(x) for x in input().split(" ")]
result = dict()
for i in numbers:
    if i not in result.keys():
        result[i] = 1
result1 = [1 for i in result.keys() if i + given[1] in result.keys()]
print(len(result1))
