# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return str("[" + str(self.start) + ", " + str(self.end) + "]")

class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        listlen = len(intervals)
        i = 0
        while i < listlen - 1:
            if intervals[i].end >= intervals[i + 1].start:
                if intervals[i].end > intervals[i + 1].end:
                    intervals[i].end = intervals[i + 1].end
                intervals.pop(i + 1)
                listlen -= 1
            else:
                i += 1
        return intervals


l = []
l.append(Interval(1, 3))
l.append(Interval(2, 6))
l.append(Interval(8, 10))
l.append(Interval(15, 18))
Solution().merge(l)

#for dat in l:
#    print(dat)