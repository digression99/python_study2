
code = list(map(int, list(input())))

#inp = str(input()).split()
#code = list(map(int, str(inp).split()))


d = [0] * 5001 # d[1] 1
res = 1
cl = 0 # chunk length

d[0] = 1
d[1] = 1
d[2] = 2

for i in range(1, len(code) + 1):
    d[i] = d[i - 2] + d[i - 1]

for i in range(len(code)): # 1 2 9
    if code[i] == 1 or code[i] == 2:
        cl += 1
    elif code[i] == 0:
        res *= d[cl - 1]
        cl = 0
    elif 7 <= code[i] <= 9:
        if i - 1 >= 0 and code[i - 1] == 1:
            res *= d[cl + 1]
        elif i - 1 >= 0 and code[i - 1] == 2:
            res *= d[cl]
        cl = 0
    else: # 3 4 5 6
        res *= d[cl + 1]
        cl = 0
else:
    res *= d[cl]
# 1 1 1 1 1 1


print(res % 1000000)

