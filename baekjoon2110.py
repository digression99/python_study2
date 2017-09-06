req = input()
pieces = req.split()
n, c = int(pieces[0]), int(pieces[1])
dat = []

for i in range(n):
    dat.append(int(input()))

dat.sort()
print(dat)


# dat = sorted(dat) # sorting

def check(dat, m, c):
    cnt = c
    start = dat[0]
    for i in range(1, len(dat)):
        if dat[i] - start >= m:  # not sorted -> sort -> without abs
            cnt -= 1
            start = dat[i]
    return cnt <= 0


mn = 1
mx = dat[len(dat) - 1] - dat[0]

ans = 0
while mn <= mx:
    mid = (mn + mx) // 2
    if check(dat, mid, c):
        if ans < mid:
            ans = mid
        mn = mid + 1
    else:
        mx = mid - 1
print(ans)








