class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def help(n):
            res = [0 for _ in range(len(n))]
            res[0] = n[0]
            res[1] = max(n[0],n[1])
            for i in range(2,len(n)):
                res[i] = max(res[i-1],res[i-2]+n[i])
            return res[-1]
        if len(nums) == 0:
            return 0
        if len(nums) < 2:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        return max(help(nums[1:]),help(nums[:-1]))