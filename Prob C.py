t = int(input())
for i in range(t):
    n = int(input())
    hordes = list(map(int, input().split()))
    hordes.sort()
    left = 0
    right = n - 1
    x = 0
    answer = 0
    while left <= right:
        if left == right: # 1 horde left
            if hordes[left] < 2: # use first type
                answer += hordes[left]
            else: # use first type until second type available
                answer += (hordes[left] - x + 3) // 2
            break
        first_type = min(hordes[left], hordes[right] - x) # use second type if killing left horde exceeds right horde, otherwise use first type
        answer += first_type
        hordes[left] -= first_type # update left horde
        x += first_type # update x
        if hordes[left] <= 0: # no more in left horde
            left += 1
        if hordes[right] <= x: # no more in right horde
            answer += 1 # for using second type
            right -= 1 
            x = 0
    print(answer)
