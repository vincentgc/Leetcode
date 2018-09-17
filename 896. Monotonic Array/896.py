class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)==1:
            return True
        state = 's'
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                pass
            elif state in ['s','inc'] and A[i] < A[i+1]:
                state = 'inc'
            elif state in ['s','dec'] and A[i] > A[i+1]:
                state = 'dec'
            else:
                return False
        return True
