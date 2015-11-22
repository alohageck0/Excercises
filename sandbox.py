# hour = int(input())
# minutes = int(input())
hour = 7
minutes = 31
words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
         8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
         13: "thirteen", 14: "fourteen", 15: "quarter", 16: "sixteen", 18: "eighteen", 19: "nineteen",
         20: "twenty", 30: "half"}


def vars(p44, p55):
    global p2, p3, p4, p5
    # p2, p3, p4, p5 = str()
    p2 = ""
    p3 = ""
    p4 = p44
    p5 = p55


def twenty(min):
    global p1
    p1 = str()
    if str(min)[0] == "2":
        p1 = words[20]
    else:
        p1 = words[min]


if minutes == 00:
    p1 = words[hour]
    vars(" o' clock", "")
    # p2 = ""
    # p3 = ""
    # p4 = " o' clock"
    # p5 = ""


elif minutes < 30:
    twenty(minutes)
    vars(" minutes past ", words[hour])
    # p2 = ""
    # p3 = ""
    # p4 = " minutes past "
    # p5 = words[hour]
    if str(minutes)[0] == "2":
        p1 = words[20]
        p2 = " "
        p3 = words[int(str(minutes)[1])]
    elif minutes == 1:
        p4 = " minute past "
    elif minutes == 15:
        p4 = " past "
    else:
        pass
elif minutes > 30:
    minutes = 60 - minutes
    twenty(minutes)
    vars(" minutes to ", words[hour + 1])
    # p2 = ""
    # p3 = ""
    # p4 = " minutes to "
    # p5 = words[hour + 1]
    if str(minutes)[0] == "2":
        p1 = words[20]
        p2 = " "
        p3 = words[int(str(minutes)[1])]
    elif minutes == 1:
        p4 = " minute to "
    elif minutes == 15:
        p4 = " to "
    else:
        pass
else:
    p1 = words[minutes]
    vars(" past ", words[hour])
    # p2 = ""
    # p3 = ""
    # p4 = " past "
    # p5 = words[hour]
print(p1 + p2 + p3 + p4 + p5)
