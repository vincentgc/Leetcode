class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        _max = 0
        v = sorted(d.keys())
        for p in range(len(v)-1):
            if v[p+1] - v[p] == 1:
                _max = max(_max,d[v[p]]+d[v[p+1]])
        return _max