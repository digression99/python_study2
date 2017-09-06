# import copy
#
# square = [k * k for k in range(1, 10)]
# print(square)
# squaregen = (k * k for k in range(1, 10))
#
# for i in squaregen:
#     print(i)
# generator & interable -> kinda same use.

# while squaregen:
#     print(squaregen)
#     next(squaregen)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [100, 200, 300]
# print(l3)

#shallow copy
# l1.append(l3)
# l2.append(l3)
#
# #print(l1[3])
#
# l1[3].append(10)
# print(l1)
#print(l2)

#deep copy

# l1.append(l3)
# l2.append(l3[:])
# #l2.append(copy.deepcopy(l3))
# l1[3].append(10)
# print(l1)
# print(l2)

s1 = "abc"
s2 = "def"

def f(x, y):
    return [i + j for i in x for j in y]


#l1 = map(lambda i, j:s[i] + s[j] for s, in s1)
#l = list(map(f, ['abc', 'def', 'ghi'], ['jkl', 'mno', 'pqrs']))
for i in s1:
    for j in s2:
        print(i + j)

def Mulstr(l):
    if len(l) == 1:
        return l[0]

    return [[i for i in l[0]] + j for j in Mulstr(l[1:])]
l = ['abc', 'def', 'ghi']

l = Mulstr(l)
print(l)




    #return [[[i for i in l[0]] for j in l[1]]for k in Mulstr(l[2:])]




