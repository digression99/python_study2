l = [3, 1, 2]

print(sorted(l))

b = [4, 3, 2, 1]

b.sort()

print(b)

print(list(map(lambda a : a * 2, [1, 2, 3, 4])))

mul = lambda a, b : a * b

print(mul(10, 20))

for i, name in enumerate(['kbs', 'mbc', 'sbs']):
    print(i, name)

import calendar

print(calendar.calendar(2015))