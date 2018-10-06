class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(10001)]
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        for j in sorted(d):
            if j>1:
                dp[j] = max(dp[:j-1]) + d[j]*j
            else:
                dp[j] = d[j]*j
        return max(dp)