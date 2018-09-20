class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        count = 1
        _max = 0
        while i < len(nums):
            if i<len(nums)-1 and nums[i] < nums[i+1]:
                count += 1
            elif i>=len(nums)-1 or nums[i] >= nums[i+1]:
                _max = max(count,_max)
                count = 1
            i += 1
        return _max