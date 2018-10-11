class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n,m = len(A),len(B)
        #intialize
        dp = [[0 for _ in range(m)] for _ in range(n)]
        max_count = 0
        for i in range(m):
            if A[0] == B[i]:
                dp[0][i] = 1
                max_count = 1
        for j in range(n):
            if B[0] == A[j]:
                dp[j][0] = 1
                max_count = 1
        
        for i in range(1,n):
            for j in range(1,m):
                if A[i]==B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_count = max(max_count,dp[i][j])
        #print dp
        return max_count