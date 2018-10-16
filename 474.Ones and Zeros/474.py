class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        #knapsack prolbem
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for s in strs:
            zero,one = s.count('0'),s.count('1')
            for i in range(n,one-1,-1):
                for j in range(m,zero-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-one][j-zero]+1)
        return dp[n][m]