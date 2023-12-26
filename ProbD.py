T = int(input())
epsilon = 1e-9 
while(T):
    T -= 1
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    if x1 == x2:
        if x3 < x1: 
            if y1 < y2: print("LEFT")
            else: print("RIGHT")
        elif abs(x3 - x1) < epsilon: print("TOUCH")
        else: 
            if y1 < y2: print("RIGHT")
            else: print("LEFT")
    elif x1 != x2: 
        a = (y2 - y1)/(x2 - x1)
        b = y1 - x1 *a 
        f = a*x3 + b
        #print(a,b,f,sep=" ")
        if abs(f - y3) < epsilon: print("TOUCH")
        elif f < y3: 
            if x1 < x2: print("LEFT")
            else: print("RIGHT")
        elif f > y3: 
            if x1 < x2: print("RIGHT")
            else: print("LEFT")
        else: print("TOUCH")
