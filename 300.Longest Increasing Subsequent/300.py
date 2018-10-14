class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
		#O(n2)—可优化成O(nlogn)
        if len(nums) == 0:
            return 0
        dp = [1 for _ in range(len(nums))]
        #dp[0] = 1
        for i in range(1,len(nums)):
            for j in range(i,-1,-1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        #print dp
        return max(dp)