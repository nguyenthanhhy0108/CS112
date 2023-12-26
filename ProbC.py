n = int(input())
price = list(map(int, input().split()))

dp = {}

def DP(i, times, hold):
    global n, price, dp
    if i == n or times == 0:
        return 0
    
    if (i, times, hold) in dp:
        return dp[(i, times, hold)]
    
    nothing = DP(i + 1, times, hold)
    if hold:
        sell = price[i] + DP(i + 1, times - 1, False)
    else:
        buy = -price[i] + DP(i + 1, times, True)
        not_buy = DP(i + 1, times, False) 
        sell = max(buy, not_buy)
       
    
    dp[(i, times, hold)] = max(nothing, sell)
    return dp[(i, times, hold)]

result = DP(0, 2, False)
print(result)
