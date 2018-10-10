class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        dp = [0 for _ in range(target+1)]
        for i in range(1,target+1):
            for num in nums:
                if num>i:break
                if num==i:dp[i]+=1
                if num<i:dp[i] += dp[i-num]
        return dp[target]