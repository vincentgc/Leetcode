class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
		#典型双指针
        i,j = 0,0
        while i < len(nums):
            if nums[i]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
            i += 1