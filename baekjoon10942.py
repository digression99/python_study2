def check(d, l, left, right): # d is map array. -> how to check map array?
    if right < left:
        return 1
    if d[left][right] >= 0:
        return d[left][right]
    if l[left - 1] != l[right - 1]:
        return 0
    else:
        d[left][right] = check(d, l, left + 1, right - 1)
        return d[left][right]

def dp(d, l, n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if l[j - 1] != l[i - 1]:
                d[j][i] = 0
            else:
                d[j][i] = check(d, l, j + 1, i - 1)
n = int(input())
l = list(map(int, input().split()))
d = [[-1] * (n + 1) for i in range(n + 1)]

#l2 = [1, 2, 1, 3, 1, 2, 1]

for i in range(1, n + 1):
    d[i][i] = 1 # every palindrome in length 1 is true
dp(d, l, n)

q = int(input())
#inp = [[1, 3], [2, 5], [3, 3], [5, 7]]

for i in range(q):
    inp = list(map(int, input().split()))
    print(d[inp[0]][inp[1]])