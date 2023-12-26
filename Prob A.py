import math

# Initialize minimum distance as positive infinity
min_dist = float('inf')

# Function to calculate the Euclidean distance between two points
def calculateDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Recursive function to find the closest pair of points in a given set
def ClosestPairPoints(points):
    global min_dist
    n = len(points)
    
    # Base cases
    if n == 2:
        return calculateDistance(points[0], points[1])
    if n == 3:
        return min(
            calculateDistance(points[0], points[1]),
            calculateDistance(points[1], points[2]),
            calculateDistance(points[0], points[2])
        )

    # Divide the set into two halves
    mid = n // 2
    left = points[:mid]
    right = points[mid:]
    
    # Recursive calls on left and right halves
    left_min = ClosestPairPoints(left)
    right_min = ClosestPairPoints(right)
    
    # Update the minimum distance
    min_dist = min(left_min, right_min)

    # Create a strip containing points close to the middle line
    strip = []
    for p in points:
        if abs(p[0] - points[mid][0]) < min_dist:
            strip.append(p)

    # Sort the strip by y-coordinate
    strip = sorted(strip, key=lambda x: x[1])

    # Compare points within the strip to find a closer pair
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            min_dist = min(min_dist, calculateDistance(strip[i], strip[j]))

    return min_dist

# Input the number of points
n = int(input())

# Input the coordinates of each point
points = []
for _ in range(n):
    a, b = input().split(sep=" ")
    points.append([int(a), int(b)])

# Sort points based on x-coordinate
points = sorted(points, key=lambda x: x[0])

# Call the ClosestPairPoints function and print the result
result = ClosestPairPoints(points)
print("{:.3f}".format(result))
