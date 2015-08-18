arr = [1, 4, 3, 5, 6, 2]
len = len(arr)
# len = int(input())
# arr = [int(x) for x in input().split(' ')]
while True:
    count = 0
    for i in range(1, len):
        if arr[i - 1] > arr[i]:
            tempor = arr[i - 1]
            arr[i - 1] = arr[i]
            arr[i] = tempor
            break
        else:
            count += 1
    if count == len - 1:
        break
    print(' '.join([str(x) for x in arr]))
