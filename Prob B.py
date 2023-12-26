# Determine direction between two vectors
def clockwise(x1, y1, x2, y2):
    # 1: clockwise, -1: counterclockwise, 0: colinear
    d = x1 * y2 - x2 * y1
    return 0 if d == 0 else 1 if d < 0 else -1

# Check if two line segments intersect or not
def is_intersecting(x1, y1, x2, y2, x3, y3, x4, y4):
    cw1 = clockwise(x3 - x1, y3 - y1, x4 - x1, y4 - y1) 
    cw2 = clockwise(x3 - x2, y3 - y2, x4 - x2, y4 - y2)
    cw3 = clockwise(x1 - x3, y1 - y3, x2 - x3, y2 - y3) 
    cw4 = clockwise(x1 - x4, y1 - y4, x2 - x4, y2 - y4)

    if cw1 * cw2 == 0 and cw3 * cw4 == 0:
        if (cw1 + cw2 != 0):
            return True
        else:
            minx1, maxx1 = (x1, x2) if x1 < x2 else (x2, x1)
            miny1, maxy1 = (y1, y2) if y1 < y2 else (y2, y1)
            minx2, maxx2 = (x3, x4) if x3 < x4 else (x4, x3)
            miny2, maxy2 = (y3, y4) if y3 < y4 else (y4, y3)
            return maxx1 >= minx2 and maxx2 >= minx1 and maxy1 >= miny2 and maxy2 >= miny1
    if cw1 * cw2 <= 0 and cw3 * cw4 <= 0:
        return True
    return False    
    

t = int(input())
for _ in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    print('YES' if is_intersecting(x1, y1, x2, y2, x3, y3, x4, y4) else 'NO')