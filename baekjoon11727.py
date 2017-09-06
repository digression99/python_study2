# d[i] -> 2 * i 직사각형 채우는 방법의 수
# d[i] = 2 * d[i - 2] + d[i - 1]

n = int(input())
d = [0] * (n + 2)
d[1] = 1
d[2] = 3 # n == 1 -> d[2] 가 없다
for i in range(3, n + 1):
    #d[i] = d[i - 2] << 1 + d[i - 1]
    d[i] = 2 * d[i - 2] + d[i - 1]
    #print(i)

print(d[n]% 10007)