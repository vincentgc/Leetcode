class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        total = sum(A) + sum(B)
        final = total / 2
        diff = final - sum(A)
        res = []
        _B = set(B)
		#用set会省很多时间，不然会超时
        for i in A:
            b = i + diff
            if b in _B:
                res.append(i)
                res.append(b)
                break
        return res