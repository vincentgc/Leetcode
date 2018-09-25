class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k == 0:
            pass
        else:
            nums[:k],nums[k:] = nums[-k:],nums[:-k]