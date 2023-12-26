l1, r1, l2, r2 = map(int, input().split())
dictt = [[l1,r1], [l2,r2]]
dictt = sorted(dictt, key=lambda x:x[0])
if dictt[0][1] >= dictt[1][0]:
    if dictt[1][1] < dictt[0][1]:
        print(dictt[1][1] - dictt[1][0])
    else:
        print(dictt[0][1] - dictt[1][0])
else:
    print(0)