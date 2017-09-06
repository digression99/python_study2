#print(ord('z') -ord('a'))
#print(ord('A') - ord('Z'))

n = int(input().strip())
s = list(input().strip())
k = int(input().strip())

diff = ord('z') - ord('a') + 1

for i in range(n):
    t = ord(s[i])
    if ord('a') <= t <= ord('z'):
        t = (t - ord('a') + k) % diff + ord('a')
    elif ord('A') <= t <= ord('Z'):
        t = (t - ord('A') + k) % diff + ord('A')
    s[i] = chr(t)
print(''.join(s))


#
# for i in range(n):
#     if ord('a') <=
#
#
#
#
#
# for i in range(n):
#     t = ord(s[i])
#     if ord('a') <= t <= ord('z'):
#         if t + k >= ord('z'):
#             t += ord('a')
#         t = (t + k) % (ord('z') + 1)
#     elif ord('A') <= t <= ord('Z'):
#         if t + k >= ord('Z'):
#             t += ord('A')
#         t = (t + k) % (ord('Z') + 1)
#     s[i] = chr(t)
# print(''.join(s))
