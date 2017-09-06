
req = input()
pieces = req.split()
n, m = int(pieces[0]), int(pieces[1])
dat = []

req = input()
pieces = req.split()
mx = 0

for i in range(n):
    if int(pieces[i]) > mx:
        mx = int(pieces[i])
    dat.append(int(pieces[i]))

def getres(dat, h, m):
    t = 0
    for i in range(len(dat)):
        t += (dat[i] - h if dat[i] - h >= 0 else 0)
    return t >= m

mn = 1
ans = 0

while mn <= mx:
    mid = (mx + mn) // 2
    if getres(dat, mid, m):
        if ans < mid:
            ans = mid
        mn = mid + 1
    else:
        mx = mid - 1
print(ans)




