def tCheck(s):
    cnt = 0
    d = {}
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return 0
        d.setdefault(s[i], 1)
    if len(d) > 2:
        return 0
    return len(s)


def backtrack(s, l):
    if len(l) == 2:
        return tCheck(s)
    mx = 0
    i = 0
    while i < len(l):
        





        i += 1





    #l = ht.keys()[:]

    # while i < len(l):
    #     while l[i] in s:
    #         s.remove(l[i])
    #     ht.pop(l[i])
    #     d2 = ht.copy()
    #     nexts = s[:]
    #     mx = max(mx, backtrack(nexts, d2))
    # return mx
    # while k in ht.keys():
    #     while k in s:
    #         s.remove(k)
    #     ht.pop(k)
    #     d2 = ht.copy()
    #     nexts = s[:]
    #     mx = max(mx, backtrack(nexts, d2))

    # for k in ht.keys():
    #     # s에서 뺀다면 무조건 앞에서부터 빼기 때문에 오류가 있을 수도 있다.
    #     while k in s:
    #         s.remove(k)
    #     ht.pop(k)
    #     d2 = ht.copy()
    #     nexts = s[:]
    #     mx = max(mx, backtrack(nexts, d2))

    # for i in range(len(ht)):
    #     d2 = ht.copy()
    #     nexts = s[:]
    #     while d2[i] in nexts:
    #         nexts.remove(d2[i])
    #     del d2[i]
    #     mx = max(mx, backtrack(s, n + 1, d2))
    #return mx


s_len = int(input().strip())
s = input().strip()
s = list(s)
#d = {}
d = []
for i in range(len(s)):
    if s[i] not in d:
        d.append(s[i])

# for i in range(len(s)):
#     d.setdefault(s[i], 1)

print(backtrack(s, d))

#375
#uyetuppelecblwipdsqabzsvyfaezeqhpnalahnpkdbhzjglcuqfjnzpmbwprelbayyzovkhacgrglrdpmvaexkgertilnfooeazvulykxypsxicofnbyivkthovpjzhpohdhuebazlukfhaavfsssuupbyjqdxwwqlicbjirirspqhxomjdzswtsogugmbnslcalcfaxqmionsxdgpkotffycphsewyqvhqcwlufekxwoiudxjixchfqlavjwhaennkmfsdhigyeifnoskjbzgzggsmshdhzagpznkbahixqgrdnmlzogprctjggsujmqzqknvcuvdinesbwpirfasnvfjqceyrkknyvdritcfyowsgfrevzon