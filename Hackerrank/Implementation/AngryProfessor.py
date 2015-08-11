__author__ = 'royalfiish'

loops = int(input())
for i in range(loops):
    early = 0
    cond = [10, 4]
    students = [-93, -86, 49, -62, -90, -63, 40, 72, 11, 67]
    for _ in students:
        if _ <= 0:
            early += 1
    if early < cond[1]:
        print("YES")
    else:
        print("NO")
