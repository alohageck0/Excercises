# hour = int(input())
# minutes = int(input())
hour = 5
minutes = 45
words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
         8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
         13: "thirteen", 14: "fourteen", 15: "quarter", 16: "sixteen", 18: "eighteen", 19: "nineteen",
         20: "twenty", 30: "half"}
if minutes == 00:
    print(words[hour] + " o'clock")


elif minutes < 30:
    if str(minutes)[0] == "2":
        print(words[20] + " " + words[int(str(minutes)[1])] + " minutes past " + words[hour])
    elif minutes == 1:
        print(words[minutes] + " minute past " + words[hour])
    elif minutes == 15:
        print(words[minutes] + " past " + words[hour])
    else:
        print(words[minutes] + " minutes past " + words[hour])
elif minutes > 30:
    minutes = 60 - minutes
    if str(minutes)[0] == "2":
        print(words[20] + " " + words[int(str(minutes)[1])] + " minutes to " + words[hour + 1])
    elif minutes == 1:
        print(words[minutes] + " minute to " + words[hour + 1])
    elif minutes == 15:
        print(words[minutes] + " to " + words[hour + 1])
    else:
        print(words[minutes] + " minutes to " + words[hour + 1])
else:
    print(words[minutes] + " past " + words[hour])
