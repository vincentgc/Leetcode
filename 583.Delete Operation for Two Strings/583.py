class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
		#判断两个字符串的交集
        m,n = len(word1),len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j],dp[i][j]+(word1[i]==word2[j]))
        return m+n-2*dp[m][n]
        