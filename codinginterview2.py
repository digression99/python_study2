# is는 object를 아마 비교하는 거 같고
# ==는 값을 비교하는 듯 하다
# object identity 는 is not을 쓴다

def share(l, m):
    cnt = 0
    kp = cp = 0

    while True:
        if kp < 4 and l[kp] >= m:
            kp += 1
            continue
        if cp < 4 and l[cp] <= m:
            cp += 1
            continue

        if kp == cp == 4:
            return cnt

        srt = m - l[kp]
        res = l[cp] - m

        if srt <= res:
            l[kp] += srt
            l[cp] -= srt
        elif srt > res:
            l[kp] += res
            l[cp] -= res

        cnt += 1

while True:
    n = int(input())
    if n == 0:
        break
    l = []
    s = 0
    nw = 0

    for i in range(0, n):
        nw = int(input())
        s += nw
        l.append(nw)

    if not(s % n == 0):
        print(-1)
    else:
        print(share(l, s / n))









