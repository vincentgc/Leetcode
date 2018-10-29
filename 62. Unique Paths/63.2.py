class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break
        for j in range(m):
            if obstacleGrid[j][0] == 0:
                dp[j][0] = 1
            else:
                break
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]
                    