n = input()
stones = list(map(int, input().split()))

l = stones[-1] + 1
river = [False for i in range(l)]
for i in stones:
    river[i] = True
jump = [[False for i in range(l)] for j in range(l)]
jump[0][0] = True

# check if a certain position and step size can be reached or not
def check(pos, step):
    if pos < 0 or step < 0 or step > l - 1:
        return False
    return jump[pos][step]

# for each pair of position and step size, determine if it can be reached or not
# using the information from the previous step             
for pos in range(l):
    for step in range(l):
        jump[pos][step] = (check(pos - step, step - 1) \
                    or check(pos - step, step) \
                    or check(pos - step, step + 1)) \
                    and river[pos]

# check if the final position can be reached or not
flag = False
for i in range(l):
    if jump[-1][i]:
        flag = True
        break
print(flag)