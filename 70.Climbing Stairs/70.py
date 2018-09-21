class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n > 2:
            d = [1,2] + [[0] for _ in range(2,n)]
            for i in range(2,n):
                d[i] = d[i-2]+d[i-1]
            return d[n-1]