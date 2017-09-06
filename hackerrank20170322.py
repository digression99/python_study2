res = input()
spl = res.split()
n, d = int(spl[0]), int(spl[1])

res = input()
spl = res.split()
l = []
for i in range(n):
    l.append(int(spl[i]))

for j in range(d):
    s = l.pop(0)
    l.append(s)

for k in l:
    print(k, end=' ')