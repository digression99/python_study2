# d = {}
#
# #d.setdefault(10, 0)
#
# #d[10] += 1
#
# d[10] = 2
# #d[10] += 1
#
# # if d[11]:
# #     print("exist")
# # else:
# #     print("not exist")
#
# d.setdefault(10, 0)
# d[10] += 1
#
# d.setdefault(10, 0)
# d[10] += 1
#
#
# print(d)
#
#

# d = {}
#
# d["b"] = 20
# d["abc"] = 40
# d["a"] = 1
#
# #print(d.keys())
#
#
# #print(sorted(d.keys()))
# print(sorted(d.items(), key=lambda x : x[1]))
# d = sorted(d.items(), key=lambda x: x[1])
# print(d[0][1])

l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']

k = zip(*l2)

for i in k:
    print(i)


# for x in enumerate(zip(*l2)):
#     print(x)
