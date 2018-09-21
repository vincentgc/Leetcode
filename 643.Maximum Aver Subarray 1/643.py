class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        _max = sum(nums[:k])
        tmp = _max
        j = 0
        for i in range(k,len(nums)):
            tmp = tmp - nums[j] + nums[i]
            _max = max(_max,tmp)
            j += 1
        return _max / float(k)