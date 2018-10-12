# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals,key = lambda x:x.start)
        stack = [intervals[0]]
        res = 0
        #print stack[-1].end
        for i in intervals[1:]:
            if i.start < stack[-1].end:
                stack[-1].start,stack[-1].end = max(i.start,stack[-1].start),min(i.end,stack[-1].end)
                res += 1
            else:
                stack.append(i)
        return res