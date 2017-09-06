l = []
d = {}
d2 = {}

str1 = "eat"
str2 = "tea"

for i in range(len(str1)):
    d.setdefault(str1[i], 0)
    d[str1[i]] += 1
for j in range(len(str2)):
    d2.setdefault(str2[j], 0)
    d2[str2[j]] += 1


l.append(d)
l.append(d2)

if set(l[0].items()) == set(l[1].items()):
    print("t")
else:
    print("f")

# if d == d2:
#     print("t")
# else:
#     print("f")






# s = {1, 2, 3}
#
# s2 = {3, 4, 5}
#
# d[s] = 1
# d[s2] = 2
#
# # l.append(s)
# # l.append(s2)
#
# if s in d:
#     print("t")
# else:
#     print("f")





# if s in l and l.index(s):
#     print("t")
# else:
#     print("f")
#
# if s in {4, 5, 6} and l.index({4, 5, 6}):
#     print("t")
# else:
#     print("f")