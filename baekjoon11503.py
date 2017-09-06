t = int(input())

def delete(s1, s2):
    stack = []
    pass

def insert(s1, s2, label):
    pass

def relabel(s1, s2, label):
    pass



def levMake(s1, s2, pos, ln):
    i = pos
    stack = []

    while i < ln:
        if s1[i] == '(':


            pass
        elif s1[i] == ')':
            pass
        else:
            if s1[i] != s2[i]:
                if checkNode(s1, i + 1):
                    pass
            pass
        i += 1

for i in range(t):
    s1 = input()
    s2 = input()
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        else:

