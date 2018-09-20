class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        _max = 0
        for p in d.keys():
            if d[p] > _max:
                temp = [p]
                _max = d[p]
            elif d[p] == _max:
                temp.append(p)
        t = {}
        for i,v in enumerate(nums):
            if v in temp:
                if v not in t:
                    t[v] = [i,i]
                else:
                    t[v][1] = i
        _min = len(nums)
        for p in t.keys():
            if t[p][1] - t[p][0] + 1< _min:
                _min = t[p][1] - t[p][0] + 1
        return _min