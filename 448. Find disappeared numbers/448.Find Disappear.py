class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            n = nums[i]
            while n!=-1:
                tmp = nums[n-1]
                nums[n-1]=-1
                n = tmp
        for j in range(len(nums)):
            if nums[j]!=-1:
                res.append(j+1)
        return res