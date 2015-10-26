bags = int(input())
arr = [int(x) for x in input().split(' ')]
total = 0


# def apples(arr):
#     global total
#     if not sum(arr) % 3:
#         return sum(arr)
#     while (sum(arr) - total) % 3:
#         for bag in arr:
#             if not bag:
#                 arr.remove(bag)
#                 continue
#             bag -= 1
#             total += 1
#         if


print(total)
print(not total % 3)
