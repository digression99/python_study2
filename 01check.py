s = '00000111110000011111011'
count = 1

for i in s:
    if i == '1':
        count += 1
    else:
        count -= 1
print(count)
