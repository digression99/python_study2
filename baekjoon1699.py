# 어떤 자연수는 그보다 작은 제곱수들의 합으로 나타낼 수 있다.
# 11 = 3^2 + 1^2 + 1^2 or 11 = 2^2 + 2^2 + 1^2 + 1^2 + 1^2
# 이때 제곱수 항의 최소 개수는 3개
# N 의 제곱수 항의 최소개수를 구하라

import math

def dp(d, n):
    if d[n]:
        return d[n]
    if n == 0:
        return 1
    mn = 9999
    end = int(math.sqrt(n))
    for i in range(1, end + 1):
        mn = min(mn, dp(d, n - i**2) + d[i**2 % n])
    d[n] = mn
    return d[n]

n = int(input())

d = [0] * (n + 2)
d[0], d[1] = 0, 1

print(dp(d, n))




