class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        for j in d:
            if d[j] > 1:
                res.append(j)
        return res