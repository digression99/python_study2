l = [1, 2, 3, 4, 5]
l2 = [5, 6, 7, 8, 9]
l3 = [11, 12, 13, 14, 15]
f = lambda x : x * x
y = lambda x, y, z : x * y * z




newl = map(y, l, l2, l3)




#print(list(newl))


testl = [-1, -8, 3, -4, 2, 5, -7]
testl.sort(key=lambda x: x*x, reverse=True)
print(testl)