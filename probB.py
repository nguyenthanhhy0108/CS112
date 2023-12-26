n = int(input())
arr = list(map(int, input().split()))

'''dp = [(last + presum, presum, memo)]
left, right = first, last element of subarray
last[right]: sum of the last subarray if we had cut the previous elements optimally
presum[right]: the sum of elements from 0 to i
memo[right]: the optimal solution for arr[0] to arr[right]
        memo[right] = max(memo[right], memo[left] + 1)'''
dp = [(0, 0, 0)]

presum, result = 0, 0
right, left = 0, 0
'''To make the array non-decreasing, we need:
        presum[right] - presum[left] >= last[left]
'''
while right < n:
    presum += arr[right]
    left = min(left, len(dp) - 1)
    #looking for 'left' where last[left] + presum[left] <= presum[right]
    while left + 1 < len(dp) and presum >= dp[left + 1][0]:
        left += 1
    (val, pre_pre, pre_dp) = dp[left] #get value of dp[left]
    result = curr_dp = pre_dp + 1 #update the memo array

    last = presum - pre_pre #update the last array
    #pop all the less optimal memo result
    while len(dp) > 0 and dp[-1][0] >= last + presum:
        dp.pop()
    #append the optimal result
    dp.append((last + presum, presum, curr_dp))
    right += 1
    
print(result)