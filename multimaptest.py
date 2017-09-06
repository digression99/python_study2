class MultiMap:
    _MapType = dict

    def __init__(self):
        self._map = self._MapType()
        self._n = 0

    def __iter__(self):
        for k, sec in self._map.items():
            for v in sec:
                yield(k, v)

    def add(self, k, v):
        container = self._map.setdefault(k, [])
        container.append(v)
        self._n += 1

    def pop(self, k):
        sec = self._map[k]
        v = sec.pop()
        if len(sec) == 0:
            del self._map[k]
        self._n -= 1
        return k, v

    def find(self, k):
        sec = self._map[k]
        return k, sec[0]

    def find_all(self, k):
        sec = self._map.get(k, [])
        for v in sec:
            yield (k, v)

a = MultiMap()
a.add('seoul', 10)
a.add('japan', 20)
a.add('new york', 100)
a.add('seoul', 300)

for k, v in a:
    print(k, v)