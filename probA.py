n, m = map(int, input().split())
'''
sumL[i]: satisfactions from 1 to i 
sumR[i]:  satisfaction from i to m
'''
sumL, sumR = [0] * (m + 1) , [0] * (m + 1)
result = 0

for _ in range(n):
    l, r, s = map(int, input().split())
    sumL[r] += s
    sumR[l] += s


for i in range(1, m + 1):
    sumL[i] += sumL[i - 1]

#rint(sumR[m+1])
for i in range(m - 1, 0, -1):
    #print(sumR[i])
    sumR[i] += sumR[i + 1]

result = 0
#leave the i-th dish, then the ans will be sumL[i - 1] + sumR[i + 1]
for i in range(1, m):
    result = max(result, sumL[i - 1] + sumR[i + 1])

print(result)
