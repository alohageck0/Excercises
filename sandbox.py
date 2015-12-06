# given = int(input())
# numbers = [int(x) for x in input().split(" ")]
# numbers = [1, 2, 3]
test = []
for i in range(len(numbers)):
    test.append(str(numbers[len(numbers) - i - 1]))
print(" ".join(test))
