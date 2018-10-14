class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        _max = max(nums)
        _min1 = _max
        _min2 = _max
        for i in range(len(nums)):
            if nums[i] < _min1:
                _min1 = nums[i]
            if nums[i] > _min1 and nums[i] < _min2:
                _min2 = nums[i]
            if nums[i] > _min2:
                return True
        return False
                