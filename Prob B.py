# Function to find the maximum sum of a subarray crossing the midpoint
def maxmidSum(arr, mid):
    sumall = 0
    left_sum = float('-inf')
    
    # Calculate the maximum sum for the left subarray
    for i in range(mid - 1, -1, -1):
        sumall += arr[i]
        left_sum = max(left_sum, sumall)
    
    # Reset sum for the right subarray
    sumall = 0
    right_sum = float('-inf')
    
    # Calculate the maximum sum for the right subarray
    for i in range(mid, len(arr)):
        sumall += arr[i]
        right_sum = max(sumall, right_sum)
    
    # Return the sum of the left and right subarrays
    return left_sum + right_sum

# Recursive function to find the maximum sum of a subarray
def maxSum(arr):
    n = len(arr)
    
    # Base case: return the only element for an array of length 1
    if n == 1:
        return arr[0]
    
    # Base case: return 0 for an empty array
    if not arr:
        return 0
    
    # Find the midpoint of the array
    mid = n // 2
    
    # Recursive calls on left and right subarrays
    left_sum = maxSum(arr[:mid])
    right_sum = maxSum(arr[mid:])
    
    # Call the function to find the maximum sum crossing the midpoint
    mid_sum = maxmidSum(arr, mid)
    
    # Return the maximum of the three sums
    return max(left_sum, right_sum, mid_sum)

# Input the number of elements in the array
n = int(input())

# Input the array elements
arr = input().split(sep=" ")
arr = [int(i) for i in arr]

# Call the maxSum function and print the result
print(maxSum(arr))
