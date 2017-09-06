n = int(input())
d = [0] * (n + 1)
d[1] = 1
d[2] = 2

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2] # 이 규칙을 찾는게 관건

print(d[n] % 10007)
# 피보나치이므로 어레이 필요 없다
# top down으로 다시 짜보기