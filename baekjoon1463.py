n = int(input())

d = [0] * (n + 1)
#top down
d[1] = 0
d[2] = 1
for i in range(3, n + 1):
    min = 123456789
    if i % 3 == 0:
        min = d[i // 3] + 1
    if i % 2 == 0:
        min = min if min < d[i // 2] + 1 else d[i // 2] + 1
    d[i] = min if min < d[i - 1] + 1 else d[i - 1] + 1

print(d[n])

# top down, bottom up 으로 다시 풀어보기!