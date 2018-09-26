class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [-1 for _ in nums]
        for i in range(len(nums))*2:
            while stack and nums[i]>nums[stack[-1]]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res