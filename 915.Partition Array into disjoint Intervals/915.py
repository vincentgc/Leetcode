class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        part = 0
        v = A[part]
        _max = v
        for i in range(len(A)):
            _max = max(_max,A[i])
            if A[i] < v:
                part = i
                v = _max
        return part+1