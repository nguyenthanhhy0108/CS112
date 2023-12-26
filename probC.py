n = int(input())
coins = list(map(int, input().split()))
target = int(input())

#array use to store minimum number of coins of value i
dp = [float('inf')] * (target + 1)
dp[0] = 0

for curr in range(1, target + 1):
    for coin in coins:
        #check if the current value is bigger than the value of current coin AND check if the number of coins at (the current value minus the value of current coin) is already has in the memo array
        if coin <= curr and dp[curr - coin] + 1 < dp[curr]:
            #update the memo array = the previous value + 1
            dp[curr] = dp[curr - coin] + 1

#print the result != inf
print(dp[target] if dp[target] != float('inf') else -1)