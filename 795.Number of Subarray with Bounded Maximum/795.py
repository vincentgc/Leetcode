class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        dp = 0
        prev = -1
        for i in range(len(A)):
            if A[i] < L:
                res += dp
            elif A[i] > R:
                dp = 0
                prev = i
            else:
                dp = i - prev
                res += dp
        return res