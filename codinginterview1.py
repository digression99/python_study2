#기약분수 구하기 문제 파이썬으로 풀기

#숫자 n이 주어지면 0/0 ~ n/n까지 가면서 (0/0은 정상적인 숫자가 아니므로 제외)
#정상적인 숫자이고 기약분수인 수를 찾아야 한다.
#0 이상 1 이하의 수를 찾아야 한다.
# n : 3 -> 0/1 1/1 1/2 1/3 2/1 2/2 2/3 3/1 3/2 3/3
#           X   O   O   O   X   X   O   X   X   X
#

def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

while (True):
    n = int(input())
    if n == 0: break
    nums = 1  # n/n을 넣는다.

    for i in range(1, n + 1):
       for j in range(1, i):
          if gcd(i, j) == 1:
                nums += 1
    print(nums)
