# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        merge_interval = intervals + [newInterval]
        sort_i = sorted(merge_interval,key=lambda i:i.start)
        res = [sort_i[0]]
        for i in sort_i[1:]:
            if res[-1].end >= i.start:
                res[-1].start, res[-1].end = min(res[-1].start,i.start),max(res[-1].end,i.end)
            else:
                res.append(i)
        return res