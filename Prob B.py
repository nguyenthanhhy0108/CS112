k = int(input())
coins = list(map(int, input().split()))
m = int(input())

# let f(x) be the number of ways to choose the coins
# we have:
# f(x) = 0 if x < 0
# f(x) = 1 if x = 0
# f(x) = sum(f(x) - a) for a in values
# we need to find f(m)
target = [0 for i in range(m + 1)]
target[0] = 1
for i in range(m + 1):
    for c in coins:
        target[i] += (0 if i - c < 0 else target[i - c])
print(target[m])