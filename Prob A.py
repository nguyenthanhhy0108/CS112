a, b = map(int, input().split())
rect = []
for i in range(b):
    rect.append(list(map(int, input().split())))

# Find the maximum area of a rectangle under a given histogram
def find_histogram_max_rect(histogram):
    l = len(histogram)
    max_rect = 0
    incr_seq = [] # a stack to store an increasing sequence
    for ind in range(len(histogram)):
        while incr_seq and histogram[ind] < histogram[incr_seq[-1]]:
            # If the current bar is smaller than the bar at the top of the stack,
            # pop the bar from the stack and calculate the area of the largest rectangle
            chosen_bar = incr_seq.pop(-1)
            if not incr_seq:      
                max_rect = max(max_rect, histogram[chosen_bar] * ind)
            else:
                max_rect = max(max_rect, histogram[chosen_bar] * (ind - incr_seq[-1] - 1))
        incr_seq.append(ind)
    while incr_seq:
        # if there are still bars left in the stack,
        # these bars have heights greater than or equal to all the bars that follow them.
        chosen_bar = incr_seq.pop(-1)
        if not incr_seq:
            max_rect = max(max_rect, histogram[chosen_bar] * l)
        else:
            max_rect = max(max_rect, histogram[chosen_bar] * (l - incr_seq[-1] - 1))
    return max_rect

# Create a histogram by iterate through each row of the matrix
# and find the maximum area  
dp_array = rect[0].copy()
max_rect = find_histogram_max_rect(dp_array)
for i in range(1, b):
    for j in range(a):
        if rect[i][j]:
            dp_array[j] += 1
        else:
            dp_array[j] = 0
    max_rect = max(max_rect, find_histogram_max_rect(dp_array))
print(max_rect)