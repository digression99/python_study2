n = int(input())
l = []
for i in range(n):
    l.append(input())
q = int(input())
for j in range(q):
    s = input()
    cnt = 0
    for k in range(n):
        if s == l[k]:
            cnt += 1
    print(cnt)