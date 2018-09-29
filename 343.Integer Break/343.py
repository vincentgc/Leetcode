class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] + [1 for i in range(n)]
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(dp[j]*dp[i-j],dp[i],dp[j]*(i-j),j*dp[i-j],j*(i-j))
        return dp[-1]