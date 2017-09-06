class Solution:
    def findDuplicate(self, paths):
        import re
        d1 = {}
        d2 = {}
        res = []

        for i in range(len(paths)):
            spl = paths[i].split(' ')

            for i in range(1, len(spl)):
                name = (re.search('[a-z0-9]*.txt', spl[i])).group(0)
                cont = (re.search('\([a-z0-9]*\)', spl[i])).group(0)

                #idx = d2.setdefault(cont, len(res) - 1)
                if d1.get(cont) != None:
                    d1[cont].append(spl[0] + '/' + name)
                    #idx = d2.setdefault(d2[cont], len(res) - 1)
                    #res[idx].append(spl[0] + '/' + name)
                else:
                    d1.setdefault(cont, [])
                    d1[cont].append(spl[0] + '/' + name)
                    #d1[cont] = spl[0] + '/' + name
                    #res.append([d1[cont]])
                    #d2[cont] = len(res) - 1
        for k, v in d1.items():
            if len(v) > 1:
                res.append(v)
        return res

tc1= ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
tc2 = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]
print(Solution().findDuplicate(tc1))
