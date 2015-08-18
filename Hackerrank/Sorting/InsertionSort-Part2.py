arr = [1, 4, 3, 5, 6, 2]
len = len(arr)
# len = int(input())
# arr = [int(x) for x in input().split(' ')]
maxnum = 0
while True:
    for i in range(1, len - 1):
        if arr[i - 1] > arr[i]:
            tempor = arr[i - 1]
            arr[i] = arr[i - 1]
            arr[i - 1] = tempor
            if maxnum < tempor:
                maxnum = tempor
        else:
            continue
    if arr[-1] == maxnum:
        break
# todo break wile loop
print(' '.join([str(x) for x in arr]))
