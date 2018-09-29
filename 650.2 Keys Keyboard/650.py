class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        else:
            dp = [0] + [i+1 for i in range(n)]
            for i in range(2,n+1):
                for j in range(i-1,1,-1):
                    if i%j==0:
                        dp[i] = min(dp[i],dp[j]+(i/j))
            return dp[n]