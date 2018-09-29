class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        Time = [int(t[:2])*60+int(t[-2:]) for t in timePoints]
        sort_Time = sorted(Time)
        minimum = 1440
        for i in range(1,len(Time)):
            diff = sort_Time[i] - sort_Time[i-1]
            minimum = min(diff,minimum)
        diff = sort_Time[0] - sort_Time[-1] + 1440
        return min(minimum,diff)