
# 자동 소트


class Simple(object):
    def __init__(self):
        self.kDict = {}
        self.max = 1
        self.min = 1
        self.vDict = {}  # value dict
        #self.vDict[1] = []

    # def hashFunc(self, n):
    #     return (n + 100) % 20001
    #
    # def insertHash(self, n, key): # 이거는 넣을때.. 지울때는??
    #     if n not in self.vDict:
    #         self.vDict[n] = key
    #     else:
    #         h = self.hashFunc(n)
    #         while True:
    #             if h in self.vDict:
    #                 continue
    #             else:
    #                 self.vDict[h] = key
    #                 self.vDict[self.hashFunc(h)] = -1 # 한번 더 가서 -1 # 지우기 위해
    #                 break
    # 지우는 거는 그냥 in operator로 찾으면 되지 않나?

    def setValDict(self, old, new, key): # old == new 이면 없던거이므로 넣는다
        #insert, delete를 여기서 다 해야 한다.
        if old == new:
            # if len(self.vDict[old]) < 1:
            #     self.vDict[old] = []
            # if type(self.vDict[old]) == list:
            #     self.vDict[old].append(key)
            #     return
            # else:
            #     self.vDict[old] = []
            self.vDict.setdefault(old, [])
            self.vDict[old].append(key)
        else:
            for k, l in self.vDict.items():
                if key in l: # 어떤 리스트에 key, 즉 스트링이 있다면 지운다.
                    l.pop(l.index(key))
                    if len(l) == 0:
                        self.vDict.pop(k) # 아예 리스트를 없앤다.
                    break
            self.setValDict(new, new, key)
            #self.vDict[new].append(key)




    def inc(self, key):
        # if there is no key

        # if ther is a key
        if key in self.kDict:
            self.kDict[key] += 1
            self.setValDict(self.kDict[key] - 1, self.kDict[key], key)

            # if key in self.vDict.values(): # key는 유일한 값이라 생각.
            #
            #     # delete the item
            #     for k, v in self.vDict.items():
            #         if v == key:
            #             self.vDict.pop(k)
            #             break
            #
            #     #self.vDict.values().index(key)
            # # if self.kDict[key] in self.vDict:
            # #     self.vDict.pop(self.kDict[key])
            # self.kDict[key] += 1
            # if self.max < self.kDict[key]:
            #     self.max = self.kDict[key]
        else:
            self.kDict[key] = 1
            self.setValDict(1, 1, key)
            # if not self.findHash(self.kDict[key]):
            #     self.vDict[self.kDict[key]] = 1
            # else:

        # if self.kDict[key] not in self.vDict:
        #     self.vDict[self.kDict[key]] = key

    def dec(self, key):
        if key in self.kDict:
            if self.kDict[key] == 1: # 여기에 걸렸다면 self.min 이 이미 1이다
                self.kDict.pop(key)
                #idx = self.vDict[1].index(key)
                self.vDict[1].remove(key)
                #self.vDict[1].remove(self.vDict[1].index(key))
                return

            self.kDict[key] -= 1
            self.setValDict(self.kDict[key] + 1, self.kDict[key], key)

            #
            #
            # if key in self.vDict.values(): # key는 유일한 값이라 생각.
            #     # delete the item
            #     for k, v in self.vDict.items():
            #         if v == key:
            #             self.vDict.pop(k)
            #             break

            # if self.kDict[key] in self.vDict:
            #     self.vDict.pop(self.kDict[key])
             # 이건 반드시 있어야 함.
                # # 여전히 이게 빠져나가면 어떻게 그 다음 min을 찾지?
                # for i in self.vDict.keys():
                #     self.min = i
                #     break
                #self.min = self.vDict.keys()
            # elif self.kDict[key] > 1: # 줄어들면 max변경해야
            #     self.kDict[key] -= 1

            #self.insertHash(self.kDict[key], key)
            #self.vDict[self.kDict[key]] = key
    def getMaxKey(self):
        if len(self.kDict) > 0:
            return self.vDict[sorted(self.vDict.keys(), reverse=True)[0]][0]

            # l = sorted(self.vDict.items(), reverse=True)
            # for i in range(0, len(l)):
            #     if l[i] !=
            #         return i
            #sorted(self.vDict.items(), reverse=True)

            #for k in sorted(self.vDict.keys(), reverse=True):





            #return sorted(self.vDict.items(), reverse=True)

            #
            # for i in sorted(self.vDict.keys(), reverse=True):
            #     if len(self.vDict[i]) > 0:
            #         return i



            #l = sorted(self.vDict.keys(), reverse=True)
            #if len(l) > 0:
            #    return self.vDict[l[0]]
            # for i in reversed(self.vDict.keys()):
            #     return i
            #
            # # if self.max in self.vDict: # 이 코드가 있어야 된다는 게 말이 안됨. 항상 있어야 함.
            # #     return self.vDict[self.max]
            # # return self.vDict[self.max]
        return ""
        #
        # if self.vDict[self.max] in self.vDict:
        #     return self.vDict[self.max]
        # else:
        #     return ""
    def getMinKey(self):
        if len(self.kDict) > 0:
            return self.vDict[sorted(self.vDict.keys())[0]][0]
            # for k, v in self.vDict.items():
            #     print(k, v)
                #return v[0]
            #return sorted(self.vDict.items())
            # for i in sorted(self.vDict.keys()):
            #     if len(self.vDict[i]) > 0:
            #         return i

            #l = sorted(self.vDict.keys())
            #if len(l) > 0:
            #    return self.vDict[l[0]]
            # for i in self.vDict.keys():
            #     return i
            #return self.vDict[self.max]
        return ""


obj = Simple()

obj.inc('allone')
for i in range(0, 5):
    obj.inc('inc')

obj.dec('inc')
obj.dec('inc')
obj.dec('inc')
obj.dec('inc')
#obj.dec('inc')
#
print(obj.getMinKey())
print(obj.getMaxKey())





# obj.inc('str')
# print(obj.kDict)
# print(obj.vDict)
# print(obj.getMaxKey())
# print(obj.getMinKey())

