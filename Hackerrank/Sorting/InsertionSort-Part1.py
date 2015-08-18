# arr = [2, 4, 5, 6, 7, 8, 3]
len = int(input())
arr = [int(x) for x in input().split(' ')]
num = arr[-1]
for i in reversed(range(len)):
    if arr[i - 1] < num:
        arr[i] = num
        break
    else:
        arr[i] = arr[i - 1]
        print(' '.join([str(x) for x in arr]))
print(' '.join([str(x) for x in arr]))
