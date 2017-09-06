class StringIterator:
    def __init__(self, compressedString):
        self.orgStr = compressedString
        self.orgPtr = 0
        self.rest = 0
        self.nowc = ' '
        self.ln = len(compressedString)

        """
        :type compressedString: str
        """

    def next(self):
        if self.rest > 0:
            self.rest -= 1
        else:
            if self.hasNext():
                self.nowc = self.orgStr[self.orgPtr]
                self.orgPtr += 1
                self.rest = self.getNum() - 1
            else:
                self.nowc = ' '
        return self.nowc

        # if self.unStr:
        #     return self.unStr.pop(0)
        #
        # if not self.unStr and self.hasNext():
        #     nowc = self.orgStr[self.orgPtr]
        #     self.orgPtr += 1
        #
        #     rep = self.getNum()
        #     self.unStr += [nowc] * (rep - 1)
        #     return nowc
        # elif not self.unStr and not self.hasNext():
        #     return ' '
        # """
        # :rtype: str
        # """

    def getNum(self):
        start = self.orgPtr
        end = start

        while end < self.ln and '0' <= self.orgStr[end] <= '9':
            end += 1

        self.orgPtr = end

        return int(self.orgStr[start:end])

    def hasNext(self):
        if self.orgPtr < self.ln:
            return True
        else:
            return False



        # Your StringIterator object will be instantiated and called as such:
        # obj = StringIterator(compressedString)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()

l = "L10e2t1C1o1d1e11"
l2 = "x6"
l3 = "a1234567890b1234567890"

iterator = StringIterator(l3)

test = ["next","next","next","hasNext","next","next","next","next","next","next","next","hasNext","next","next","next","next","next","hasNext","next","next","next","next","next","hasNext","next","next","next","next","hasNext","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","next","hasNext","next","hasNext","next","next","next","next","next","next","hasNext","next","next","next","next","next","next","next","next","next","next","next","next","next","next","hasNext","next","next","next","hasNext","next","next","hasNext","next","next","next","next","next"]
test2 = ["next","next","next","next","next","next","hasNext","next","hasNext"]


for t in test:
    if t == "next":
        print(iterator.next())
    else:
        print(iterator.hasNext())


# print(iterator.next()) #// return 'L'
# print(iterator.next()) #// return 'e'
# print(iterator.next()) #// return 'e'
# print(iterator.next()) #// return 't'
# print(iterator.next()) #// return 'C'
# print(iterator.next()) #// return 'o'
# print(iterator.next()) #// return 'd'
# print(iterator.hasNext()) #// return true
# print(iterator.next()) #// return 'e'
# print(iterator.hasNext()) #// return false
# print(iterator.next()) #// return ' '
