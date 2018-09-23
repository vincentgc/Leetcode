class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def issquare(n):
            return int(n**0.5)**2 == n
        for i in range(int(c**0.5)+1):
            tmp = c - i**2
            if issquare(tmp):
                return True
        return False