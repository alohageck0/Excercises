numbers = int(input())
arr = [int(x) for x in input().split(' ')]
# arr = [1, 1, 1, 1, 2, 3, 3, 3, 2, 2, 4, 4, 2, 2, 9]
result = dict()
for elem in arr:
    if elem not in result.keys():
        result[elem] = 1
    else:
        result[elem] += 1
reverse = {v: k for k, v in result.items()}
print(reverse.get(1))
