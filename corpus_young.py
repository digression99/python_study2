import re

f = open('robinson_young_lines.txt', 'r')
#save = open('robinson_young_lines.txt', 'w')

magic = 10

st = []
totlen = 0
totWordCnt = 0

for l in f:
    if re.search('[a-zA-z0-9, \'!\.;?-]+', l):
        if len(l) < magic: continue
    if re.search('CHAPTER', l) : continue
    if re.search('Robinson Crusoe\n', l): continue
    if re.search('[0-9]+ of [0-9]+', l): continue
    if l == '\n': continue

    t = re.search('\.|\;', l)

    if t:
        str1 = l[:t.span(0)[1]]
        str2 = l[t.span(0)[1]:-1]
        converted = ' '.join(st) + str1 + '\n'

        cnt = converted.split(' ')
        totWordCnt += len(cnt)
        totlen += 1
        st.clear()
        st.append(str2)
    else:
        st.append(l[:-1])

print(totWordCnt / totlen)