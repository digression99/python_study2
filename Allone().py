class AllOne(object):
    def __init__(self):
        self.kDict = {}
        self.max = 1
        self.min = 1
        self.vDict = {}  # value dict

    def inc(self, key):
        if key in self.kDict:
            self.kDict[key] += 1
            if self.max < self.kDict[key]:
                self.max = self.kDict[key]
                self.vDict[self.kDict[key]] = key
        else:
            self.kDict[key] = 1
            if len(self.kDict.keys()) == 1:
                self.maxKey = key
                self.vDict[self.maxKey] = key

    def dec(self, key):
        if key in self.kDict:
            if self.kDict[key] == 1:  # this is the smallest value
                # this is the biggest problem.
                for i in range(self.min + 1, self.max):
                    if i in self.vDict:  # if there is a key with the min value
                        self.max = i
                        break
            else:
                self.kDict[key] -= 1
                if self.min > self.kDict[key]:
                    self.min = self.kDict[key]
                    self.vDict[self.kDict[key]] = key

    def getMaxKey(self):
        return self.vDict[self.max]

    def getMinKey(self):
        return self.vDict[self.min]

obj = Allone()