# hour = int(input())
# minutes = [int(x) for x in input().split(" ")]
hour = 12
minutes = 00
words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
         8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
         13: "thirteen", 14: "fourteen", 15: "quarter", 16: "sixteen", 18: "eighteen", 19: "nineteen",
         20: "twenty", 30: "half"}
if minutes == 00:
    print(words[hour] + " o'clock")
