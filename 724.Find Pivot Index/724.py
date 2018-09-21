class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
		#转化为计算左右和的比较
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        total = sum(nums)
        left = nums[0]
        if sum(nums[1:]) == 0:
            return 0
        for i in range(1,len(nums)):
            if total-left-nums[i]==left:
                return i
            else:
                left += nums[i]
        return -1