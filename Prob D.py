n, k = 0, 0
arr = []

# calculate how many ops are needed to increase arr[ind] to target
# if not possible, return inf
def increase_op(ind, target):
    if ind == n:
        return float('inf')
    if arr[ind] >= target:
        return 0
    return increase_op(ind + 1, target - 1) + target - arr[ind]
    
# calculate how many ops are needed to increase any element to target
# if not possible, return inf
def calculate_min_ops(target):
    min_ops = float('inf')
    for i in range(n):
        min_ops = min(min_ops, increase_op(i, target))
    return min_ops
    
# find maximum possible target
def binary_search(left, right):
    if left == right:
        return left
    mid = (left + right) // 2 + 1
    if calculate_min_ops(mid) > k:
        return binary_search(left, mid - 1)       
    else:
        return binary_search(mid, right)
        
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(binary_search(0, 1000010000))