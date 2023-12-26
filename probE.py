def find_password(arr):
    n = len(arr)
    if n == 1:
        return 1
    arr = sorted(arr)
    cases = []
    #delete first element
    case1 = arr[1] + arr[-1]
    cases.append(case1)
    #delete last element
    case2 = arr[-2] + arr[0]
    cases.append(case2)
    #delete any middle element
    case3 = arr[0] + arr[-1]
    cases.append(case3)
    cases = sorted(cases)
    #iterate each case above
    for case in cases:
        #two pointer
        left, right = 0, n - 1
        rem, skip = 0, 0
        while left < right:
            #if sum of left element and right element < case => the left element might be the redundant element 
            if arr[left] + arr[right] < case:
                skip += 1
                rem = left
                left += 1
            #if sum of left element and right element > case => the right element might be the redundant element 
            elif arr[left] + arr[right] > case:
                skip += 1
                rem = right
                right -= 1
            #otherwise, there is no redundant element => just skip
            else:
                left += 1
                right -= 1
        #after iterate all element in 1 case, if there is less than 1 redundant element
        if skip <= 1:
            #if there is no redundant element, then the redundant element is the middle element itself, so result = case - middle
            if skip == 0 and case - arr[left] > 0:
                #print("skip 0")
                return case - arr[left]
            #if there is 1 redundant element, result = case - redundant element
            elif case - arr[rem] > 0:
                #print("skip 1", arr[rem], case, arr[left])
                return case - arr[rem]
    #otherwise, there is no answer
    return -1


T = int(input())  # Number of test cases

for i in range(T):
    N = int(input())  # Size of the array
    arr = list(map(int, input().split()))  # Array of 2N - 1 positive integers
    result = find_password(arr)
    if result <= 0:
        result = -1
    print(f"Case #{i + 1}: {result}")
