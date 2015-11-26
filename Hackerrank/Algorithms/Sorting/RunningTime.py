arr = [2, 1, 3, 1, 2]
len = len(arr)
# len = int(input())
# arr = [int(x) for x in input().split(' ')]
count = 0
for i in range(1, len):
    element = arr[i]
    if element < arr[i - 1]:
        arr[i] = arr[i - 1]
        for j in reversed(range(i)):
            if arr[j - 1] < element:
                arr[j] = element
                count += 1
                break
            else:
                if j == 0:
                    arr[j] = element
                    count += 1
                else:
                    arr[j] = arr[j - 1]
                    count += 1
                if arr[j - 1] == element:
                    break
                else:
                    continue
    else:
        pass
print(count)
