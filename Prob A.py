home = {} # count occurances of each home color
away = [] # away color of each team
n = int(input())
for i in range(n):
    h, a = map(int, input().split())
    if h in home.keys():
        home[h] += 1
    else:
        home[h] = 1
    away.append(a)
for i in away:
    if i in home.keys():
        print(f'{n - 1 + home[i]} {n - 1 - home[i]}')      
    else:
        print(f'{n - 1} {n - 1}')
