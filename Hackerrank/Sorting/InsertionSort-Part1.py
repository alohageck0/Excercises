arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
len = len(arr)
# len = int(input())
# arr = [int(x) for x in input().split(' ')]
num = arr[-1]
for i in range(len):
    if arr[i] > arr[i + 1]:
        arr[i + 1] = arr[i]
        print(' '.join([str(x) for x in arr]))
    else:
        continue
print(' '.join([str(x) for x in arr]))
