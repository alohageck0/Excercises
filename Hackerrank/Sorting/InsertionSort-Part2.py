arr = [9, 8, 6, 7, 3, 5, 4, 1, 2]
len = len(arr)
# len = int(input())
# arr = [int(x) for x in input().split(' ')]
for i in range(1, len):
    element = arr[i]
    if element < arr[i - 1]:
        arr[i] = arr[i - 1]
        for j in reversed(range(i)):
            if arr[j - 1] < element:
                arr[j] = element
                break
            else:
                arr[j] = arr[j - 1]
                continue
        print(' '.join([str(x) for x in arr]))

    else:
        print(' '.join([str(x) for x in arr]))
