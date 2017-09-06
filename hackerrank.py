seqList = []
lastAns = 0

resp = input()
spl = resp.split()
n, q = int(spl[0]), int(spl[1])

for i in range(n):
    seqList.append([])

for j in range(q):
    resp = input()
    spl = resp.split()
    base, x, y = int(spl[0]), int(spl[1]), int(spl[2])

    if base == 1:
        seqList[(x^lastAns) % n].append(y)
    elif base == 2:
        size = len(seqList[(x^lastAns) % n])
        lastAns = seqList[(x^lastAns) % n][y % size]
        print(lastAns)