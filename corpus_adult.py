import re

f = open('testcorpus.txt', 'r')
save = open('testsave.txt', 'w')


st = []
totlen = 0
totWordCnt = 0

for l in f:

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

        save.writelines(converted)
        st.clear()
        st.append(str2)
    else:
        st.append(l[:-1])

print(totWordCnt / totlen)