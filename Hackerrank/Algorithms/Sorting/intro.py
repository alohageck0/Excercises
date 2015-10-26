arr = [1, 4, 5, 7, 9, 12]
len = len(arr)
number = 4
# number = int(input())
# len = int(input())
# arr = [int(x) for x in input().split(' ')]
for i in range(len):
    if arr[i] == number:
        print(i)
        break
