# temp = 5.0
# org = temp
# org += 1
# print("org : ", org, "temp : ", temp)
#
# temp2 = float(3.0)
# org2 = temp2
# org2 += 1
#
# print("org2 :", org2, "temp2 :", temp2)
#
# response = "hiiyihi"
# let = response[3]
# #response[3] = "k"
#
# print(let)
#
# print(response.lower())
# print(response.lower().startswith('y'))
# response += "k"
# print(response)
#
# test1 = "hikiki"
# test2 = test1
#
#
# if test1 is not test2:
#     print("no")
# else:
#     print("yes")
#
# test2 += "wawa"
# test1 += "wawa"
#
# if test1 is not test2:
#     print("no")
# else:
#     print("yes")
#
# print("""hi, my name is kim
# i'm preparing to teach
# data structure""")

# s1 = set('hello')
# s2 = set('mynameis')
# s3 = s1.intersection(s2)
# print(s3)
#
# s4 = s1.difference(s2)
# print(s4)
# s5 = s2.difference(s1)
# print(s5)
# s6 = s1.union(s2)
# print(s6)
#
# print(s6.issuperset(s1))
# print(s6.isdisjoint(s5))
#
# s7 = {'a', 'b', 'c'}
# s8 = {'a', 'b', 'c'}
# print(s7.issubset(s8))
# print(s8.issubset(s7))
#
# if s7.issubset(s8) and s8.issubset(s7):
#     print("same")
# else:
#     print("diff")
#
# a = -10
#
# s = a > 0 and min(20, 30)
# print(s)
#
#
#
# c = 10 if a > 0 else 20
#
# print(c)

# n = 13
# m = 20
# q = n // m
# r = n % m
# c = q * m + r
# print(n, m, q, r, c)
#
# print(0^0^1^1^2)
# print(0^0^2)
# print(0^2)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# l4 = reversed(l2)
# l1.reverse()
# l3 = l1 + l2
#print(l3)
#
# for i in l4:
#     print(i)
#
# for j in l2:
#     print(j)
#     if j == 5:
#         del j
# print(l2)

# for k in range(len(l2)):
#     if l2[k] == 5:
#         del l2[k]
#         break
# print(l2)
#
# str1 = list('hello')
# str2 = list('zoo')
#
# print("hello is big" if str1 > str2 else "zoo is big")

#
# if str1 < str2:
#     print("zoo is big")
# else:
#     print("hello is big")

# s1 = {4, 5, 6}
# s2 = {1, 2, 3, 4}
# s3 = s1 | s2
# s4 = s1 & s2
# s5 = s1 - s2
# s6 = s1 ^ s2
#
# print(s3)
# print(s4)
# print(s5)
# print(s6)
#
# tempset = set()
# alphabet = set("abcdefghijklmnopqrstuvwxyz")
# s = ""
# while s != "exit":
#     s = input("enter string :")
#     for i in s:
#         tempset.add(i)
# print("tempset : ", tempset)
# ans = alphabet - tempset
# s2 = ""
# while ans:
#     s2 += ans.pop()
# print(s2)


# alpha = [1, 2, 3]
# beta = alpha
# beta += [4, 5]
# beta = beta + [6, 7]
# print(alpha)

#print(2 << 4)

l = [1, 2, 3, 4, 5, 6]
i = 0

# print(sum(l))
# print(max(l))

l2 = ['a', 'b', 'c' ,'d']
#print(sum(l2))
# print(max(l2))

# def modify(a, b):
#     a += 1
#     b += 2
#     return
#
# def listmodify(l):
#     l.append(20)
#     return
#
# def listcopy(l, t=(1, 2)):
#     l2 = l[:]
#     l2.append(20)
#     return
#
# a = 10
# b = 20
# modify(a, b)
# print(a, b)
#
# l = [1, 2, 3, 4]
# #listmodify(l)
# listcopy(l)
# print(l)

# def keywordfunc(a=10, b=20, c=30):
#     return a*b+c
#
# print(keywordfunc(c=40))
#
# a = 20
# c = -35
# print(max(a, c, key=abs))
# print(round(1.4))
# print(round(1.6))

# reply = input("x, y, z :")
# pieces = reply.split()
# x = float(pieces[0])
# y = float(pieces[1])
# z = float(pieces[2])
# print(x, y)
#
# ltest1 = [1, 2, 3, 4]
# it = iter(ltest1)

# print(it)
# print(next(it))
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))

# while it:
#     print(next(it))

def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k

# def gen():
#     for i in range(10):
#         yield i ** 3
#
# for i in gen():
#     print(i)
#
# for factor in factors(100):
#     print(factor)

n = 10
squares = []
for k in range(1, n + 1):
    squares.append(k * k)

print(squares)

squares.clear()

squares = [k * k for k in range(1, n + 1) if k > 0]

print(squares)

factors2 = [k for k in range(1, n + 1) if n % k == 0]

print(factors2)

total = sum(k * k for k in range(1, n + 1))

print(total)

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

print(sum(i for i in fibonacci(10)))

import array
import collections
import heapq











