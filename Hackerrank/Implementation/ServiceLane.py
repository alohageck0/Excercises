arr = [int(x) for x in input().split(" ")]
width = [int(x) for x in input().split(" ")]
for i in range(arr[1]):
    case = [int(x) for x in input().split(" ")]
    segments = width[case[0]:case[1] + 1]
    print(min(segments))
