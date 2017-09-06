d = {5 : 1, 7 : 2, 1 : 3}


d = sorted(d, key=lambda x : d[x])
print(d)
