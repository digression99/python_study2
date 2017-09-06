class sda(object):
    # not a binary dynamic array
    # copying the array to a new variable?
    def __init__(self, length=0):
        self._data = [] * length
        self._length = len(self._data)
        self._data.append('$') # dollar should be the very front.

    def search(self, val):
        pos = self.binarySearch(val, 0, len(self._data) - 1, 0)
        if self._data[pos] != val:
            return False
        return True

    def insert(self, val):
        # pos = self.search(val)
        # if pos:
        #     self._data.append(0)
        #     for i in range(len(self._data) -1, pos + 1, -1):
        #         self._data[i] = self._data[i - 1]
        #     self._data[pos + 1] = val
        pos = self.binarySearch(val, 0, len(self._data) - 1, 0)
        self._data.append(-1) # last index : len(self._data) - 1

        for i in range(len(self._data) - 1, pos + 1, -1):
            self._data[i] = self._data[i - 1]
        self._data[pos + 1] = val

    def delete(self, val):
        pos = self.binarySearch(val, 0, len(self._data) - 1, 0)
        if self._data[pos] != val:
            return False
        del self._data[pos]
        return True

    def binarySearch(self, tgt, l, h, bef):
        # finds index.
        if l > h:
            return bef
        else:
            mid = (l + h) // 2
            if self._data[mid] == '$':
                return mid
            if tgt == self._data[mid]:
                return mid
            elif tgt < self._data[mid]:
                return self.binarySearch(tgt, l, mid - 1, h)
            else:
                return self.binarySearch(tgt, mid + 1, h, l)

    def __str__(self):
        return str(self._data)
        #return [i for i in range(0, len(self._data))]

if __name__ == "__main__":
    import sys
    import array
    # print(sys.getsizeof(1))
    # print(sys.getsizeof('a'))
    # print(sys.getsizeof('abcde'))
    # l1 = [4, 8]
    # print(sys.getsizeof(l1))
    #primes = array('i',[2, 3, 4, 5])
    #print(sys.getsizeof(array('i', [1, 2, 3, 4, 5])))

    obj = sda()
    #

    # obj.insert(30)
    # obj.insert(20)
    # obj.insert(10)
    #
    # obj.insert(40)
    # obj.insert(90)
    # obj.insert(1)
    # obj.insert(-1)
    #
    # print(obj)
    #
    # obj.delete(-1)
    # print(obj)
    # obj.delete(2)
    # obj.delete(30)
    # print(obj)
    # print(obj.search(40))


