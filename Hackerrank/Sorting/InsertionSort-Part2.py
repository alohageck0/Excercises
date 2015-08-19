arr = [1, 4, 3, 5, 6, 2]
len = len(arr)
# len = int(input())
# arr = [int(x) for x in input().split(' ')]
num = arr[-1]
for i in reversed(range(len)):
    if arr[i - 1] <= num or i == 0:
        arr[i] = num
        break
    else:
        arr[i] = arr[i - 1]
        print(' '.join([str(x) for x in arr]))
print(' '.join([str(x) for x in arr]))
