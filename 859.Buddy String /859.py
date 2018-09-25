class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)!=len(B):
            return False
        fir,sec = [],[]
        for i in range(len(A)):
            if A[i]!=B[i]:
                fir.append(A[i])
                sec.append(B[i])
        if len(fir)==len(sec) and len(fir)==2:
            return fir==sec[::-1]
        elif len(fir)==len(sec) and len(fir)==0:
            d = {}
            for i in range(len(A)):
                if A[i] not in d:
                    d[A[i]] = 1
                else:
                    return True
        return False
                