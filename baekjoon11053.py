n = int(input())
l = list(map(lambda x : int(x), input().split()))

d = [0] * (n + 2)
mx = -1
for i in range(n):
    for j in range(i + 1):
        if l[i] > l[j]:
            d[i] = max(d[i], d[j])
    d[i] += 1
    mx = max(d[i], mx)
print(mx)