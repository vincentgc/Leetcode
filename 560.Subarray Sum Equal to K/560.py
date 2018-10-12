class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        tmp = 0
        d = {0:1}
        for i in nums:
            tmp += i
            res += d.get(tmp-k,0)
            d[tmp] = d.get(tmp,0)+1
            
        return res