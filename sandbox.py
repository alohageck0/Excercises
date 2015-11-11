arr = [1, 2, 3, 4, 5, 6, 7]
point = int(len(arr) / 2) + 1
down = arr[:point]
up = arr[point:]
i = len(down) - 1
print(down, up)
print(len(down), len(up))
print(i)
