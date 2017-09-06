memo = []

def fibonacci(n):
    if n <= 1:
        return n
    else:
        if memo[n] > 0:
            return memo[n]

        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]

#bottom up
d = [0] * 100
def fibonacci2(n):
    d[0] = 1
    d[1] = 1
    for i in range(2, n):
        d[i] = d[i - 1] + d[i - 2]
    return d[n]





# int fibonacci(int n) {
#     if (n <= 1) {
#         return n;
#     } else {
#         memo[n] = fibonacci(n-1) + fibonacci(n-2);
#         return memo[n];
# } }