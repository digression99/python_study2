def checkPrime(p):
    if p == 1:
        return True
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

def threePrime(k, cnt):
    if cnt == 3:
        if k == 0:
            return 0
        else:
            return -1
    else:
        if k == 0:
            return -1
        for i in range(k, -1, -1):
            if checkPrime(i):
                if threePrime(k - i, cnt + 1) == 0:
                    print(i, end=' ')
                    return 0
    return -1

t = int(input())
for i in range(t):
    k = int(input())
    threePrime(k, 0)