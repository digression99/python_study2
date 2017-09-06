def checkList(l):
    if len(l) > 10:
        return

    l.append(10)
    checkList(l)



l1 = [10, 20, 30]
l2 = l1 + [40]
l1.append(50)

print(l1)
print("\n")
print(l2)
