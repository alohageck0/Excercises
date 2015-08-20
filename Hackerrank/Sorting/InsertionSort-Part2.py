arr = [1, 4, 3, 5, 6, 2]
len = len(arr)
# len = int(input())
# arr = [int(x) for x in input().split(' ')]
for i in range(len - 1):
    element = arr[i + 1]
    newlen = i + 1
    if element < arr[i]:
        arr[i + 1] = arr[i]
        for j in reversed(range(newlen)):
            if arr[j - 1] < element:
                arr[j] = element
                break
            else:
                arr[j] = arr[j - 1]
                continue
        print(' '.join([str(x) for x in arr]))

    else:
        print(' '.join([str(x) for x in arr]))