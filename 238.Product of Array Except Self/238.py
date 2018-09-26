class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1 for i in nums]
        right = [1 for i in nums]
        tmp = 1
        for i in range(len(nums)):
            left[i] = tmp
            tmp = tmp * nums[i]
        tmp = 1
        for j in range(len(nums)-1,-1,-1):
            right[j] = tmp
            tmp = tmp * nums[j]
        res = [1 for i in nums]
        for i in range(len(res)):
            res[i] = left[i] * right[i]
        return res
        